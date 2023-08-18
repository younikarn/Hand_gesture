import cv2
import mediapipe as mp
import winsound
#cv2: This is the OpenCV library used for video capture, image processing, and visualization.
#mediapipe: This is the Mediapipe library that provides tools for various computer vision tasks, including hand tracking.
#winsound: This is a library used to play sound signals, which will be used to trigger an auditory alarm when a gesture is detected.



# Initialize Mediapipe
#mp_hands: This initializes the hand tracking module of the Mediapipe library.
#hands: This creates an instance of the hand tracking module.

#mp_drawing: This provides utility functions for drawing landmarks and connections on frames.


mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
#This line initializes the webcam for capturing video frames. The 0 represents the default camera device.
cap = cv2.VideoCapture(0)

#This loop continuously captures frames from the webcam until it's closed.
#  It checks if the capture was successful (ret) and reads the captured frame.

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break


# Convert frame to RGB
#This converts the captured BGR frame (used by OpenCV) to RGB format (used by Mediapipe).
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Detect hand landmarks
#This line processes the RGB frame using the hands object created earlier, which detects hand landmarks.
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Draw landmarks on the frame
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            #if hand landmarks are detected in the frame, the loop iterates through each detected hand and
            #  draws the landmarks on the frame using mp_drawing.draw_landmarks().

            # Implement gesture detection logic
            thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_finger_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            # Implement gesture detection logic
            #These lines extract the coordinates of the thumb tip and index finger tip landmarks from the detected landmarks.





            
        # Calculate distance between thumb tip and index finger tip
            #This calculates the Euclidean distance between the thumb tip and index finger tip landmarks.
            distance = ((thumb_tip.x - index_finger_tip.x) ** 2 + (thumb_tip.y - index_finger_tip.y) ** 2) ** 0.5


            
            # Define a threshold distance for the "rock" gesture
            threshold_distance = 0.1
            
            # If the distance between thumb tip and index finger tip is below the threshold, play a beep sound
            if distance < threshold_distance:
                winsound.Beep(1000, 300)  # Play a beep sound for 300 ms






    cv2.imshow('Rock Gesture Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
