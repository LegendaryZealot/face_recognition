import cv2.cv2 as cv
import dlib
import face_recognition
import os

def real_time_face_recognition():
    cp=cv.VideoCapture(0)
    success,frame=cp.read()
    while success:
        #cv.imshow("real_time_face_recognition",frame)
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
        cv.imshow("real_time_face_recognition_result",frame)
        cv.waitKey(1)
        success,frame=cp.read()
    cp.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    real_time_face_recognition()
else:
    print("dd")