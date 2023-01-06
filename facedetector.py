import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('haarcascade_eye.xml')
# Read the input image
img = cv2.imread('img/magetan.jpg')
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#     for (ex, ey, ew, eh) in eye:
#         cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh)(0, 255, 0), 2)
font = cv2.FONT_HERSHEY_SIMPLEX
jumlah = 0
for (x, y, w, h) in faces:
    jumlah = jumlah + 1
    # cv2.putText(img, "found", (x, y-10), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    detection_eye = eye.detectMultiScale(roi_gray)
    # for (ex, ey, ew, eh) in detection_eye:
    #     cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 255, 0), 2)

# Display the output
cv2.putText(img, "Jumlah wajah ada " + str(jumlah), (100, 100),
            font, 2, (0, 100, 255), 2, cv2.LINE_AA)
cv2.imshow('Facedetector', img)
cv2.waitKey()
