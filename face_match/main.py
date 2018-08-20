import face_recognition
import cv2.cv2 as cv

def face_match():
    gaici_img=cv.imread("./Gaici.jpg")
    cook_img=cv.imread("./Cook.jpg")
    master_img=cv.imread("./Master.jpg")
    unknown_img=cv.imread("./UnKnown.jpg")
    gaici_face_encoding=face_recognition.face_encodings(gaici_img)[0]
    cook_face_encoding=face_recognition.face_encodings(cook_img)[0]
    master_face_encoding=face_recognition.face_encodings(master_img)[0]
    unknown_face_encoding=face_recognition.face_encodings(unknown_img)[0]
    print("begin matching...")
    results = face_recognition.compare_faces([gaici_face_encoding, cook_face_encoding,master_face_encoding], unknown_face_encoding )
    labels = ['gaici', 'master','master']
    print(results)
    hasResult=False
    for i in range(0, len(results)):
        if results[i] == True:
            print('The person is:'+labels[i])
            hasResult=True
    if not hasResult:
        print("not matched")

if __name__ == "__main__":
    face_match()
else:
    print("dd")