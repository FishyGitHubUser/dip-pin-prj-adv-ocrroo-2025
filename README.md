# Overview

This app is designed to extracting text from any point of a given video, and translating it into screen reader friendly plain text.

## Project Setup on Windows
> ### Install UV
> - `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
>
> ### Create virtual environment
> - `uv venv`
> - Activate venv as instructed by UV
> 
> ### Install Core Dependencies
> - Install Pillow: 
> `uv add pillow`
>
> - Install Tesseract: 
> `uv add pytesseract`
> 
> - Install OpenCV:
> `uv add opencv-python`
> 
> - Install FastAPI: 
> `uv add fastapi --extra standard`
> 
> ### Install Tesseract's Python Wrapper
> - Python wrappers can be found here:https://github.com/UB-Mannheim/tesseract/wiki
> - The version currently used: https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe
> 
> ### Run FastAPI (development mode)
> - In your preferred shell: `uv run fastapi dev preliminary/simple_api.py`
> 
> NOTE: This command runs as a script or wrapper ONLY for direct API route testing, so there is no ASGI server running!
> 
> ### Run ASGI server Uvicorn
> - In your preferred shell: `uvicorn preliminary.simple_api:app --reload --host 127.0.0.1 --port 8000`
> 
> NOTE: Specifying the host and port is not necessary, but it is suggested to reduce potential API communication issues.
> 
> ### Test Operations
> - Open a shell session and enter: `curl 127.0.0.1:8000/video`
> - If there's an output, you're ready to go! You can check other possible API commands at http://127.0.0.1:8000/docs.

## Who needs this?
> This is intended, but not limited to use for assisting impaired people log video changes, specifically code examples usually not said verbally.

## Why use this?
> It allows the user to upload a video of their choice and have it log text displayed on screen, and when at what time it was recorded.   