
import cv2 


camerafile = "video.avi"

cap2 = cv2.VideoCapture(camerafile)

for i in range(500):
    ret, frame = cap2.read()
    # frame = cv2.resize(frame, (640, 420))
    # # Show raw camera image
    cv2.imshow("modeld", frame)
    # Clean plot for next frame

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
