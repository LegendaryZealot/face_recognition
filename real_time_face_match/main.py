import face_recognition
import cv2.cv2 as cv
import os

def real_time_face_match():
    target_img=cv.imread("./target.JPG")
    target_encoding=face_recognition.face_encodings(target_img)[0]
    cp=cv.VideoCapture(0)
    success,frame=cp.read()
    while success:
        face_locations = face_recognition.face_locations(frame)
        faceNum = len(face_locations)
        for i in range(0, faceNum):
            top =  face_locations[i][0]
            right =  face_locations[i][1]
            bottom = face_locations[i][2]
            left = face_locations[i][3]
            start = (left, top)
            end = (right, bottom)
            color = (55,255,155)
            thickness = 3
            cv.rectangle(frame, start, end, color, thickness)
            face=frame[top:left,bottom:right]
            face_encodings=face_recognition.face_encodings(face)
            if 0!=len(face_encodings):
                face_encoding=face_encodings[0]
                result=face_recognition.compare_faces([target_encoding],face_encoding)
                result_lables=["target"]
                for i in range(len(result)):
                    if result[i] == True:
                        font = cv.FONT_HERSHEY_SIMPLEX
                        cv.putText(frame,result_lables[i], (top, left), font, 1.2, (255, 255, 255), 2)
        cv.imshow("real_time_face_match",frame)
        cv.waitKey(1)
        success,frame=cp.read()

if __name__ == "__main__":
    real_time_face_match()
else:
    print("dd")