"""A basic introduction to Open CV

Instructions
------------

Implement the functions below based on their docstrings.

Notice some docstrings include references to third-party documentation
Some docstrings **require** you to add references to third-party documentation.

Make sure you read the docstrings C.A.R.E.F.U.L.Y (yes, I took the L to check that you are awake!)
"""

# imports - add all required imports here
from pathlib import Path
from PIL import Image
import cv2
import numpy as np
import pytesseract

ROOT_PATH = Path(__file__).parents[1]
OUT_PATH = ROOT_PATH / Path("resources")
VID_PATH = OUT_PATH / Path("oop.mp4")

# Path to tesseract wrapper for Python
pytesseract.pytesseract.tesseract_cmd = 'C:/Users/admin/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
output_image = 'output.png'

class CodingVideo:
    capture: cv2.VideoCapture


    def __init__(self, video: Path | str):
        self.capture = cv2.VideoCapture(video) # You complete me!
        if not self.capture.isOpened():
            raise ValueError(f"Cannot open {video}")

        self.fps = self.capture.get(cv2.CAP_PROP_FPS)
        self.frame_count = self.capture.get(cv2.CAP_PROP_FRAME_COUNT)
        self.duration = self.frame_count / self.fps


    def __str__(self) -> str:
        """Displays key metadata from the video

        Specifically, the following information is shown:
            FPS - Number of frames per second rounded to two decimal points
            FRAME COUNT - The total number of frames in the video
            DURATION (minutes) - Calculated total duration of the video given FPS and FRAME COUNT

        Reference
        ----------
        https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
        """
        video_info = (f'FPS: {self.fps:.2f},\n'
                      f'Frames: {self.frame_count},\n'
                      f'Duration (min): {self.duration/60:.2f}\n')

        return video_info

    def get_frame_number_at_time(self, seconds: int) -> int:
        """Given a time in seconds, returns the value of the nearest frame"""
        return int(seconds*self.fps)


    def get_frame_rgb_array(self, frame_number: int) -> np.ndarray:
        """Returns a numpy N-dimensional array (ndarray)

        The array represents the RGB values of each pixel in a given frame

        Note: cv2 defaults to BGR format, so this function converts the color space to RGB

        Reference
        ---------
        # TODO: Find a tutorial on OpenCV that demonstrates color space conversion
        https://opencv.org/blog/color-spaces-in-opencv/

        """
        self.capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number - 1)
        ok, frame = self.capture.read()
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    def get_image_as_bytes(self, seconds: int) -> bytes:
        self.capture.set(cv2.CAP_PROP_POS_FRAMES, self.get_frame_number_at_time(seconds))
        ok, frame = self.capture.read()
        if not ok or frame is None:
            raise ValueError("Invalid frame in target location")
        ok, buf = cv2.imencode(".png", frame)
        if not ok:
            raise ValueError("Failed to encode frame")
        return buf.tobytes()

    def save_as_image(self, seconds: int, output_path: Path | str = output_image) -> None:
        """Saves the given frame as a png image using Pillow

        Reference
        ---------
        # TODO: Requires a third-party library to convert ndarray to png
        # TODO: Identify the library and add a reference to its documentation
        Pillow repo - https://github.com/python-pillow/Pillow
        Pillow docs - https://pillow.readthedocs.io/en/stable/
        """
        if type(output_path) is str:
            output_path = OUT_PATH / output_path

        frame = self.get_frame_number_at_time(seconds)
        frame = self.get_frame_rgb_array(frame)
        image = Image.fromarray(frame)
        image.save(output_path)

    # TODO (personal): Add arg 'boost_contrast: bool' which enables grayscale and black-white.
    def get_frame_text(self, frame_number: int) -> str:
        """Capture text from specified frame using pytesseract OCR

        Tesseract performs best with clean, high-quality images. Improve the input quality by resizing, converting to
        grayscale, and applying thresholding or binarization to reduce noise and enhance contrast. This preprocessing
        can significantly improve recognition rates.

        Reference
        ----------
        https://www.nutrient.io/blog/how-to-use-tesseract-ocr-in-python/
        https://www.geeksforgeeks.org/python/reading-text-from-the-image-using-tesseract/
        """
        frame = self.get_frame_rgb_array(frame_number)

        # Convert frame to grayscale
        frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        # Convert grayscale frame to black and white
        (thresh, frame_black_white) = cv2.threshold(frame_grayscale, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        return pytesseract.image_to_string(frame_black_white, lang='eng')


# TODO (personal): Should receive image bytes (not a path), then return its text.
# TODO (personal): Bad method placement, move to a class.
def get_image_text(file: str = output_image):
    """Capture text from image using pytesseract OCR

    Tesseract performs best with clean, high-quality images. Improve the input quality by resizing, converting to
    grayscale, and applying thresholding or binarization to reduce noise and enhance contrast. This preprocessing
    can significantly improve recognition rates.

    Reference
    ----------
    https://www.nutrient.io/blog/how-to-use-tesseract-ocr-in-python/
    https://www.geeksforgeeks.org/python/reading-text-from-the-image-using-tesseract/
    """
    output_path = OUT_PATH / file
    if not output_path.exists():
        return 'file not found'

    # Load image into memory as NumPy ndarray
    image = cv2.imread(output_path)

    # Convert image to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Convert grayscale image to black and white
    (thresh, image_black_white) = cv2.threshold(grayscale, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Save image
    # image = Image.fromarray(image_black_white)
    # filename, file_extension = file.split('.')
    # image.save(OUT_PATH / f'{filename}-sanitised.{file_extension}')

    return pytesseract.image_to_string(image_black_white, lang='eng')

def test():
    """Try out your class here"""
    oop = CodingVideo(VID_PATH)
    print(oop)
    oop.save_as_image(42)
    print(oop.get_frame_text(1006))

if __name__ == '__main__':
    test()
