import socket
import threading

import cv2
import imagezmq

# ===============================
# Network Configuration
# ===============================
LAPTOP_IP = ""  # Laptop IP

# ===============================
# Sender Thread
# ===============================
def send_raw_frames():

    sender = imagezmq.ImageSender(connect_to=f'tcp://{LAPTOP_IP}:5555')

    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

    while True:

        ret, frame = cap.read()

        if ret:
            sender.send_image(socket.gethostname(), frame)


# ===============================
# Receiver Thread
# ===============================
def receive_processed_frames():

    image_hub = imagezmq.ImageHub(open_port='tcp://*:5556')

    window_name = "Pi Emotion Display"

    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:

        name, processed_frame = image_hub.recv_image()

        cv2.imshow(window_name, processed_frame)
        cv2.waitKey(1)

        image_hub.send_reply(b'OK')


# ===============================
# Main
# ===============================
if __name__ == "__main__":

    t = threading.Thread(target=send_raw_frames, daemon=True)
    t.start()

    receive_processed_frames()
