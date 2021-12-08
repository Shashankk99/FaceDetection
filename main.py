from cvzone.FaceDetectionModule import FaceDetector
import cv2

cap = cv2.VideoCapture(0)
detector = FaceDetector()

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img)

    if bboxs:
        cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()