# Overview

Include a brief overview of the project, include:

- How do you deploy and run the project?
- What are its core dependencies?
- Who is it for and why?

## Project Setup on Windows
> ### Install UV
> - `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
>
> ### Create virtual environment
> - `uv venv`
> - Activate venv as instructed by UV
> 
> ### Install Core Dependencies
> - Install Pillow 
> `uv add pillow`
>
> - Install Tesseract 
> `uv add pytesseract`
> 
> - Install OpenCV
> `uv add opencv-python`
> 
> - Install FastAPI 
> `uv add fastapi --extra standard`
> 
> ### Install Tesseract Wrapper
> - Python wrappers can be found here:https://github.com/UB-Mannheim/tesseract/wiki
> - The version currently used: https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe
> 
> ### Run FastAPI (development mode)
> - In your preferred shell: `uv run fastapi dev preliminary/simple_api.py`
> 
> ### Test Operations
> - Open a shell session and enter: `curl 127.0.0.1:8000/video`
> - If there's an output, you're ready to go! You can check other possible API commands at http://127.0.0.1:8000/docs.

## Who needs this?
> This is intended, but not limited to use for assisting impaired people log video changes, specifically code examples usually not said verbally.

## Why use this?
> It allows the user to upload a video of their choice and have it log text displayed on screen, and when at what time it was recorded.   