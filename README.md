# Object Detection using OpenCV
![Cocoapods](https://img.shields.io/cocoapods/l/AFNetworking) ![Twitter Follow](https://img.shields.io/twitter/follow/manankohlii?label=manankohlii&logo=Twitter&style=social) 

## About the Project
### Principle
* [OpenCV](https://opencv.org/) (Open Source Computer Vision Library) is an open source computer vision and machine learning software library.
* The Program uses the WebCam to capture video until interrupted
* First Frame of the video is taken as reference and any movement after that is treated as an object
* Times of object entering and leaving the frame is stored and can be viewd later from a csv file
* Changes can be made in terms of video used for observation, extent of contouring for objects etc.
### Dependencies 
* Python 3.8.6
* OpenCV 4.4.0
* Pandas 1.1.5

## Saving files
### Using Git
* Open Terminal
* Traverse to the directory where you want to save project files
* Type `git clone https://github.com/manankohlii/object-detection-opencv.git`

### Download from GitHub
* Go to **Code** in the Repository
* Download ZIP
* Unzip and save files 

## Setting up Virtual Environment
### With Conda
* Open Terminal 
* Traverse to the directory where files were saved
* Use `conda create --name <env> --file requirements.txt` 
## Executing the Project
### Running the Program
* Open terminal and move to the directory where program files are stored
* Enter `python capture.py`
* Four windows appear with different tasks
* Press `q` after observation is complete 
### Viewing Results
* A **Times.csv** file has been created in the directory where program files are saved
* Open a the file in a Text Editor or MS Excel to view the results
