# Overview
This section contains preliminary familiarisation steps with the core libraries of the project. It is also designed to complement (and satisfy) the performance requirements of the preliminary assessment.

## Required performance demonstration

You must demonstrate your ability at:

- Determining an organisation’s technology, development tools, and UI platform
- Enabling interprocess communication in Python while using third-party libraries and referencing third-party documentation


## Instructions

1. Complete the knowledge section (Word document) available via Blackboard
2. Fork this repository
3. Clone the repository to your local computer
4. Install `uv` and check that it is running with `uv --version`
5. Obtain a video that can be used to test the functionality and place in the `resources/` folder - your instructor will provide you with one
6. Follow the steps in the remainder of the guide insuring your commit to git whenever prompted
7. Submit a `zip` of this repository along with the `.git` folder. **Do not include your `venv/`**. Ensure your submission includes the assessment Word document with all of the questions in it attempted.


## Steps
Complete the steps below and fill in the `> block` sections
> If you see a section like this, fill it in!


### Installing and running OpenCV

1. Examine the `pyproject.toml` what dependencies does it currently identify?
> There is currently nothing in the dependencies because this is a brand new project.
>
2. Create a `.venv` in this folder using `uv venv`
3. Activate the `venv` as instructed by `uv`
4. In order to complete the project, we need to install OpenCV. Fill in the following:
  - What role does OpenCV have in this project?
  > OpenCV is used for splitting a video into individual frames that can be saved as an image.
  - What is the `uv pip` command to install OpenCV?
  > `uv pip install opencv-python`
  - What is the URL of this library's git repo?
  > [https://github.com/opencv/opencv-python](https://github.com/opencv/opencv-python)
5. Add OpenCV to your project using the `uv add` command:
  > `uv add opencv-python`

6. Have the dependencies in the `pyproject.toml` changed? If so, how?
  > The dependencies now require the latest version of opencv for python which is 4.12.0.88
  > 
  > This is the line that was added in: `"opencv-python>=4.12.0.88",` 
7. Why did we use `uv add` over `uv pip`?
  > We use `uv add` because it adds OpenCV to the pyproject.toml dependencies. 
  > Additionally, this states the version required to run the project. 
  >
8. The `numpy` library is required for OpenCV. Should you add an explicit requirement for it? Why/Why not?
  > It should be added to ensure that the version of OpenCV can run and interpret numpy's ndarrays as intended.
  >
9. Commit the changes so far to git. Use the message `chore: add OpenCV dependency`
10. Go to `preliminary/library_basics.py` and complete the required functionality.
11. Commit your changes with `feat: save video frames`


### Installing and running Tesseract

[Tesseract OCR](https://github.com/tesseract-ocr/tesseract) provides optical character recognition (OCR) functionality needed for the project.

Tesseract consists of both an OCR Engine and a command line program. It is predominantly written in C++.

1. Examine the [Readme](https://github.com/tesseract-ocr/tesseract?tab=readme-ov-file) and find a list of Python wrappers.

2. What is the URL that lists Python wrappers for Tesseract?
  > https://tesseract-ocr.github.io/tessdoc/AddOns.html#tesseract-wrappers

3. Select a Python wrapper. What wrapper did you choose and why? Ensure you address each element below in your answer
> - name of the python library - pytesseract
> 
> 
> - how long ago was a commit made to the library - 8 months ago
> 
> 
> - does it have external dependencies
> - * Pillow>=8.0.0
>   * packaging>=21.3
>   * python_requires>=3.9
>   
> 
> - how does it suite the project requirements
>   * It  supports all image types of Pillow libraries, as well as being able to run it as a standalone script.
>     It also prints the recognised text, instead of writing a new file, making debugging easier.

4. Use UV to add the dependency to your project and your `pyproject.toml`

5. If your library has additional requirements (e.g. installing tesseract binaries), note it in your README.md

6. Commit the new dependency `chore: add tesseract dependency`

7. Add a new method in `library_basics.py` that returns the text of a given frame/time/image (you decide!)

8. Commit the changes as `feat: OCR an image


### Install and run FastAPI

FastAPI will allow us to enable communication with our OCR service from other processes on the current machine or across a network.

1. Add the requirement for FastAPI using UV. FastAPI has optional requirements so the command is a little different:
`uv add fastapi --extra standard`
2. Commit the new dependency `chore: add FastAPI dependency`
3. Run in development mode using:
`uv run fastapi dev preliminary/simple_api.py`
4. Run the following curl command (may require git bash on Windows):
`curl 127.0.0.1:8000/video`
5. Confirm that a list of videos and URLs is returned by copying the output below:
> ```sh
>   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
>                                  Dload  Upload   Total   Spent    Left  Speed
> 100   140  100   140    0     0   7057      0 --:--:-- --:--:-- --:--:--  7368{"count":1,"videos":[{"id":"demo","path":"..\\resources\\oop.mp4","_links":{"self":"/video/demo","frame_example":"/video/demo/frame/1.0"}}]}
> ```

6. What are the names of the two processes that just communicated?
> - Uvicorn
> - FastAPI
>
> When the session shell uses the curl command, it requests data from our app's ASGI server Uvicorn. FastAPI responds to these API requests by returning a success message and a list of any videos and frames/
6. Modify the simple_api.py so that it works correctly with your implementation and complete any TODO markers
>```sh
>   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
>                                  Dload  Upload   Total   Spent    Left  Speed
> 100    83  100    83    0     0    406      0 --:--:-- --:--:-- --:--:--   406"I finally saw The Matrix today.\nIt was the best documentary\nI've ever seen.\n\n"
>```
8. Demonstrate the use of at least two other end points below:
> > ### Endpoint 1 (video/{vid}):
> > $ curl http://127.0.0.1:8000/video/demo/frame/42 --output resources/output.png
> > ```sh
> >   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
> >                                  Dload  Upload   Total   Spent    Left  Speed
> > 100    83  100    83    0     0   5007      0 --:--:-- --:--:-- --:--:--  5187{"fps":23.976023976023978,"frame_count":15152,"duration_seconds":631.9646666666666}
>> ```
> 
> > ### Endpoint 2: (video/{vid}/frame/{t})
> > ```sh
> > $ curl http://127.0.0.1:8000/video/demo/frame/42 --output resources/output.png
> >  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
> >                                  Dload  Upload   Total   Spent    Left  Speed
> > 100  3
> > ```
> > 
> > **Output File:**
> >
> > ![output.png](../resources/output.png)
