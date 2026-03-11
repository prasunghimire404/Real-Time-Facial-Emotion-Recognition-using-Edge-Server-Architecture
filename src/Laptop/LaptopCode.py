import cv2
import imagezmq
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array

# ===============================
# Network Configuration
# ===============================
PI_IP = ""   # Raspberry Pi IP

# Hub receives raw from Pi (5555)
image_hub = imagezmq.ImageHub(open_port='tcp://*:5555')

# Sender sends processed frames back to Pi (5556)
sender_back = imagezmq.ImageSender(connect_to=f'tcp://{PI_IP}:5556')


# ===============================
# Load Models
# ===============================
face_classifier = cv2.CascadeClassifier('face.xml')
classifier = load_model('model.h5')

emotion_labels = ['Angry','Happy','Neutral','Sad','Surprise']

print("Laptop Hub Active. Receiving Pi Camera...")

while True:

    # Receive frame from Pi
    rpi_name, frame = image_hub.recv_image()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        roi_gray = gray[y:y+h,x:x+w]
        roi_gray = cv2.resize(roi_gray,(48,48))

        roi = roi_gray.astype('float')/255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)

        prediction = classifier.predict(roi)[0]
        label = emotion_labels[prediction.argmax()]

        cv2.putText(frame, label, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Laptop Processing Monitor", frame)
    cv2.waitKey(1)

    # Send processed frame back to Pi
    sender_back.send_image("Processed", frame)

    image_hub.send_reply(b'OK')
