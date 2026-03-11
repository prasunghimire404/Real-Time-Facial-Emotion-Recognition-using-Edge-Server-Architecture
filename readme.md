# Emotion Detection Streaming System

## Project Overview

This project is a **distributed real-time emotion detection system** that uses a **Raspberry Pi camera for video capture** and a **laptop for AI processing**. The Raspberry Pi sends live camera frames to the laptop over the network. The laptop runs a deep learning model to detect faces and classify emotions. After processing, the laptop sends the annotated video frames back to the Raspberry Pi, where they are displayed on a connected LCD screen.

This approach allows the system to perform computationally heavy AI tasks on a more powerful device (the laptop) while keeping the Raspberry Pi responsible for camera capture and display.

---

# System Architecture

The system is built using a **client–server architecture with bidirectional video streaming**.

### Components

**1. Raspberry Pi (Edge Device)**
Responsibilities:

* Capture video from the Pi camera or USB webcam.
* Send raw video frames to the laptop.
* Receive processed frames from the laptop.
* Display the results on a connected LCD screen.

The Raspberry Pi acts as the **data source and display node**.

---

**2. Laptop (Processing Server)**
Responsibilities:

* Receive raw frames from the Raspberry Pi.
* Perform face detection.
* Run a trained deep learning model to classify emotions.
* Draw bounding boxes and emotion labels on detected faces.
* Send the processed frames back to the Raspberry Pi.

The laptop acts as the **AI inference server**.

---

# Data Flow

The system operates in a continuous loop:

1. The **Raspberry Pi camera captures a video frame**.
2. The frame is **sent over the network to the laptop**.
3. The laptop performs:

   * Face detection
   * Emotion classification using a trained CNN model.
4. The laptop **annotates the frame** with:

   * Face bounding boxes
   * Predicted emotion labels.
5. The **processed frame is sent back to the Raspberry Pi**.
6. The Raspberry Pi **displays the processed frame on its LCD screen**.
7. The cycle repeats for the next frame.

This creates a **near real-time emotion recognition system**.

---

# Communication Architecture

The project uses a **two-channel streaming communication model**.

| Channel   | Direction             | Purpose                |
| --------- | --------------------- | ---------------------- |
| Channel 1 | Raspberry Pi → Laptop | Send raw camera frames |
| Channel 2 | Laptop → Raspberry Pi | Send processed frames  |

This allows **simultaneous sending and receiving of video streams**.

---

# Key Technologies

**Computer Vision**

* Face detection using Haar Cascade classifiers.

**Deep Learning**

* Convolutional Neural Network (CNN) trained for emotion classification.

**Networking**

* Image streaming over TCP using a lightweight message-based system.

**Multithreading**

* Allows the Raspberry Pi to send frames and receive processed results at the same time.

---

# Supported Emotion Classes

The model detects the following facial expressions:

* Angry
* Happy
* Neutral
* Sad
* Surprise

---

# Advantages of This Architecture

**1. Efficient computation**
Heavy AI processing runs on the laptop instead of the Raspberry Pi.

**2. Real-time processing**
Streaming allows continuous emotion detection.

**3. Modular design**
Camera, processing, and display are separated into different roles.

**4. Scalability**
Multiple Raspberry Pi devices could send streams to the same processing server.

---

# Example Use Cases

* Human emotion monitoring systems
* Smart classroom engagement analysis
* Interactive robots
* Smart mirrors
* Behavioral research tools

---

# Summary

This project demonstrates how **edge devices and powerful processing machines can collaborate** to build real-time AI systems. The Raspberry Pi handles sensor input and display, while the laptop performs deep learning inference. By streaming frames over the network, the system achieves efficient and scalable real-time emotion detection.
