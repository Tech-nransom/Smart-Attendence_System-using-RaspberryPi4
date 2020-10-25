# Smart-Attendence_System-using-RaspberryPi4
 
This is the Project For Smart Attendence System and Uses Facial Recognition

## Installation
You Need opencv and face_recognition and numpy packages Installed on Raspberry pi

To install face_recognition visit:
[Facial Recognition](https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65)

To install opencv :

```bash
sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-100
sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo pip3 install opencv-contrib-python
```

To install numpy :
```bash

sudo apt install libatlas3-base
sudo apt-get install python3-numpy

```

## Directory setup

```bash

Base -->Known_faces
			|
			-->Person1Name
					|
					-->person_image1.jpg
					-->person_image2.jpg
			-->Person2Name
					|
					-->person_image1.jpg
					-->person_image2.jpg
			   .
			   .
			   .

```

## Running Program

First check if all The packages are been downloaded,Once that is checked

Run:

```bash
python3 Attendence_System.py
```

## Result
It Generates Attendence.csv file in Base Directory
The Attendence list is saved in Attendence.csv file

Enjoy 😁