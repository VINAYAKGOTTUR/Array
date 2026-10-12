import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hand module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Capture webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)  # Mirror image
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
            
            # Get coordinates of fingertips
            finger_tips = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky
            thumb_tip = 4
            h, w, c = frame.shape
            
            finger_status = []
            for tip in finger_tips:
                x_tip = int(handLms.landmark[tip].x * w)
                y_tip = int(handLms.landmark[tip].y * h)
                x_mcp = int(handLms.landmark[tip - 2].x * w)
                y_mcp = int(handLms.landmark[tip - 2].y * h)
                
                if y_tip < y_mcp:  # Finger is up
                    finger_status.append(1)
                else:
                    finger_status.append(0)
            
            # Thumb
            x_thumb_tip = int(handLms.landmark[thumb_tip].x * w)
            x_thumb_ip = int(handLms.landmark[thumb_tip - 2].x * w)
            if x_thumb_tip > x_thumb_ip:
                thumb_status = 1
            else:
                thumb_status = 0
            
            # Gesture controls
            # Play/Pause: Index finger up, others down
            if finger_status == [1,0,0,0]:
                pyautogui.press('space')  # Play/pause
            # Volume Up: Thumb up
            elif thumb_status == 1 and sum(finger_status) == 0:
                pyautogui.press('volumeup')
            # Volume Down: Thumb down
            elif thumb_status == 0 and sum(finger_status) == 0:
                pyautogui.press('volumedown')
    
    cv2.imshow("Gesture Control", frame)
    
    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
