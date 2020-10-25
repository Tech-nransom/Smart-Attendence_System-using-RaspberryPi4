import cv2
import face_recognition
import numpy as np
import picamera
import os
from datetime import datetime

try:
    
    file = open("Attendence.csv",'r+')
    file.close()
except:
    file = open("Attendence.csv",'a')
    file.write("Name,Date,Time\n")
    file.close()


def markAttendance(name):
    now = datetime.now()
    dtString = now.strftime('%H:%M:%S')
    Date = now.strftime("%d:%m:%y")
    with open('Attendence.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        dateList = []
        for line in myDataList:
            entry = line.split(',')
            if len(entry)==3 and entry[0] != '\n':
                
                nameList.append(entry[0])
                dateList.append(entry[1])
        if (name not in nameList) or ( Date != dateList[len(nameList) - 1 - nameList[::-1].index(name)]):
            f.writelines(f'\n{name},{Date},{dtString}')
            print("Attendence Is Marked")

camera = picamera.PiCamera()
camera.resolution = (512, 512)
camera.vflip = True


known_face_dir = 'Known_faces'

print("loading know faces",end="")
known_faces,known_names = [],[]
for name in os.listdir(known_face_dir):
    print("..",end='')
    
    for filename in os.listdir(known_face_dir+'/'+name):
        image = face_recognition.load_image_file(known_face_dir+'/'+name+'/'+filename)
        encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(name)
print()
while True:

    camera.capture('video_sample.jpg')
    frame = cv2.imread('video_sample.jpg')
    
    try:
        face_locations = face_recognition.face_locations(frame)
    except:
        face_locations = face_recognition.face_locations(face_recognition.load_image_file(frame))
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        
        matches = face_recognition.compare_faces(known_faces,face_encoding,0.5)
        name = "Unknown"
        color = (0,0,255)
        face_distances = face_recognition.face_distance(known_faces,face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            color = (0,255,0)
            name = known_names[best_match_index]
        
            markAttendance(name)
        cv2.rectangle(frame,(left,top),(right,bottom),color,2)
        cv2.putText(frame,name,(left + 6, bottom - 5),cv2.FONT_HERSHEY_COMPLEX,0.5,(200,200,200),2)
        
    cv2.imshow('FEED',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

camera.close()
try:os.remove("video_sample.jpg")
except:pass