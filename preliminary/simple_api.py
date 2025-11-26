"""Provides a simple API for your basic OCR client

Drive the API to complete "interprocess communication"

Requirements
"""
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi import UploadFile, File
from fastapi import Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
from preliminary.library_basics import CodingVideo, get_image_text
import datetime


app = FastAPI()

# Allowing front-end URI root URI to access the backend - This Bypasses CORS errors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Specify origins to allow access (e.g. http://localhost:5173)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# We'll create a lightweight "database" for our videos
# You can add uploads later (not required for assessment)
# For now, we will just hardcode are samples
ROOT_PATH = Path(__file__).parents[1]
VIDEOS: dict[str, Path] = {
    "demo": ROOT_PATH / Path("resources/oop.mp4")
}

# Recursive delete folder temp files - https://csatlas.com/python-remove-directory/\
TEMP_PATH = ROOT_PATH / 'resources/uploads'
if (Path(TEMP_PATH).exists()):
    import shutil
    mydir = TEMP_PATH
    shutil.rmtree(mydir)

class VideoMetaData(BaseModel):
    fps: float
    frame_count: int
    duration_seconds: float
    _links: dict | None = None

# Response structure (viewable in DOM)
@app.get("/video")
def list_videos():
    """List all available videos with HATEOAS-style links."""
    return {
        "count": len(VIDEOS),
        "videos": [
            {
                "id": vid,
                "path": str(path), # Not standard for debug only
                "_links": {
                    "self": f"/video/{vid}",
                    "frame_example": f"/video/{vid}/frame/1.0"
                }
            }
            for vid, path in VIDEOS.items()
        ]
    }

def _open_vid_or_404(vid: str) -> CodingVideo:
    path = VIDEOS.get(vid)
    if not path or not path.is_file():
        raise HTTPException(status_code=404, detail="Video not found")
    try:
        return CodingVideo(path)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Could not open video {e}")

def _meta(video: CodingVideo) -> VideoMetaData:
    return VideoMetaData(
            fps=video.fps,
            frame_count=video.frame_count,
            duration_seconds=video.duration
    )

@app.post("/video/upload/{vid}")
async def upload_video(file: UploadFile = File()):
    """
    Receives a video from the client and saves it temporarily.
    Returns an ID to access it later.
    """
    temp_path = ROOT_PATH / f"resources/uploads/{file.filename}"
    temp_path.parent.mkdir(parents=True, exist_ok=True)

    # Save file to disk
    with temp_path.open("wb") as f:
        content = await file.read()
        f.write(content)

    # Add to your video dict for demo purposes
    VIDEOS[file.filename] = temp_path

    return {"id": file.filename, "message": "Video uploaded successfully"}

@app.get("/video/{vid}", response_model=VideoMetaData)
def video(vid: str):
    video = _open_vid_or_404(vid)
    try:
            meta = _meta(video)
            meta._links = {
                "self": f"/video/{vid}",
                "frames": f"/video/{vid}/frame/{{seconds}}"
            }
            return meta
    finally:
        video.capture.release()

# GET requests
@app.get("/video/{vid}/frame/{t}", response_class=Response)
def video_frame(vid: str, t: float):
    try:
        video = _open_vid_or_404(vid)
        return Response(content=video.get_image_as_bytes(t), media_type="image/png")
    finally:
      video.capture.release()

@app.get("/video/{vid}/frame/{t}/ocr", response_class=Response)
# Queries are automatically split from the url if an arg matches (e.g. "?high_contrast=true" == high_contrast).
def time_ocr(vid: str, t: float, high_contrast: bool = False):
    try:
        video = _open_vid_or_404(vid)
        # Seconds to datetime - https://stackoverflow.com/questions/775049/how-do-i-convert-seconds-to-hours-minutes-and-seconds

        timestamp = str(datetime.timedelta(seconds=t)).split('.')[0]
        captured_text = video.get_frame_text(video.get_frame_number_at_time(t), high_contrast)

        if not captured_text:
            captured_text = 'No text was captured'

        formatted_text = (f'[{timestamp}]\n' +
                          f'{captured_text}').strip()

        return Response(content=formatted_text + '\n'*3, media_type="text/plain")
    finally:
        video.capture.release()

# TODO: add endpoint to get ocr e.g. /video/{vid}/frame/{t}/ocr
@app.get('/video/{vid}/frame/{num}/ocr')
def frame_ocr(vid: str, num: int):
    video = _open_vid_or_404(vid)
    try:
        return video.get_frame_text(num)
    finally:
        video.capture.release()

@app.get('/img/{img}/ocr')
def image_ocr(img: str):
    return Response(content=get_image_text(img), media_type="text/plain")


# POST requests
@app.post("/video/upload")
# UploadFile stores files in memory up to 1MB. If a file exceed this, it is saved as a temporary file to disk.
async def upload_video(file: UploadFile = File()):
    """Save a user uploaded video file.

    Users can upload a video file which is saved resources/uploads. The video path is stored in server memory.

    Reference
    ---------
    https://fastapi.tiangolo.com/tutorial/request-files/#file-parameters-with-uploadfile
    https://fastapi.tiangolo.com/reference/uploadfile/#fastapi.UploadFile.write
    https://betterstack.com/community/guides/scaling-python/uploading-files-using-fastapi/

    """
    temp_path = ROOT_PATH / f"resources/uploads/{file.filename}"
    # Must create the directory first
    temp_path.parent.mkdir(parents=True, exist_ok=True)
    with temp_path.open("wb") as f:
        # Writes like a normal file
        f.write(await file.read())
    # Saves in memory - Disappears when server restarts
    VIDEOS[file.filename] = temp_path
    return {"id": file.filename, "message": "Video uploaded successfully"}

if __name__ == '__main__':
    print(frame_ocr('demo', 1006))