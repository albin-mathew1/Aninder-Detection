import cv2
output_filename = 'ANINDER_CAM_001.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
fps = 10
frame_width = 640 
frame_height = 480 
video_writer = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))
webcam = cv2.VideoCapture(0)
if not webcam.isOpened():
    print("Error opening webcam")
    exit()
while True:
    ret, frame = webcam.read()

    if not ret:
        print("Error reading frame from webcam")
        break
    cv2.imshow('Webcam', frame)
    video_writer.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
webcam.release()
video_writer.release()
cv2.destroyAllWindows()

