# Face_based_attendace_system
Marks attendance based on Face recognition and detection

## Objective
This desktop application aims to simplify the process of Attendance Management of students and faculty using Face Recognition and user-friendly GUI. The management of data and marking of attendance is carried out in Excel files.

## About the project
This python based app uses OpenCV libraries: face detection using Haar feature-based cascade classifier and face recognition using Local Binary Patterns Histograms (LBPH) and pandas library to manage excel sheet through python scripts. GUI features are implemented using tkinter library.

Database development, face detection, face recognition, and attendance updating are the four steps of this system.

## About the Application
The app has two main Panels: Registrations and Manage Attendance.

![GUI-new](https://user-images.githubusercontent.com/41962976/130661445-b0c850ff-1983-4fcb-9947-23dbf98c9a96.png)

## Directory structure

![Directories-mine](https://user-images.githubusercontent.com/41962976/130661649-0128a914-654f-48e3-bb15-f27de1dd17b5.png)

 **./TrainingImage** : contains the training data images and unrecognized student’s directory.  
**./StudentDetails** : contains the Student details such as ID and name with serial numbers.  
**./Attendance** : contains the Attendance css files sorted as per the date.   
**./TrainingImageLabel** : contains the Recognizer model and Files contains admin password and emails.  
**./Attendance Excel** : contains the Student’s attendance excel sheets sorted as per the date.  
**./src** : contains the images and fonts that are used in the project.  
**./main.py** : python code of the project.  
**./haarcascade frontalface default.xml** : Haar Cascade classifiers are an ef- fective way for object detection.  

## Flow of the Project

![FRAS FD](https://user-images.githubusercontent.com/41962976/130662207-ac1aa2c6-2fd7-45cf-b427-46b504be84ad.jpg)

**Four phases** :  
  
**1. Database Creation** : We take images of a person during the enrollment process, as well as his/her ID and Name. Database is created by the images from live video stream of users.  
**1. Face detection** : Face detection is performed by Haar Cascades and recognition is performed using Local Binary Pattern Histogram (LBPH) algorithm, during enrolling of a user, we  take multiple images of a user along with his/her id and name also.   
**1. Face recognition** : Each student’s/employee’s presence will be updated in the database. The last step is to find the person in our database of known people who has closest measurements of the test image.  
**1. Attendance updation** : After the completion of the whole process the if the detected face is found in the database, user is recorded in the excel sheet and displayed on the GUI with timestamp. Attendance sheet will be mailed to administrator of that particular day on clicking the button.  
