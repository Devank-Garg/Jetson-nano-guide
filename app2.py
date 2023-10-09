import sys
import cv2
import imutils
import imageio
from yoloDet import YoloTRT

# use path for library and engine file
model = YoloTRT(library="yolov5/build/libmyplugins.so", engine="yolov5/build2/last.engine", conf=0.5,yolo_ver="v5")

cap = cv2.VideoCapture(0)

# Create an imageio FFmpegWriter object
output_path = 'output.mp4'
writer = imageio.get_writer(output_path, fps=12)  # Adjust the frame rate as needed

while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=600)
    detections, t = model.Inference(frame)
    for obj in detections:
        print(obj['class'], obj['conf'], obj['box'])
    print("FPS: {} sec".format(1/t))
    cv2.imshow("Output", frame)

    # Convert the frame from BGR to RGB before writing to the video
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    writer.append_data(rgb_frame)  # Write the frame to the video file

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
writer.close()  # Close the video writer
cv2.destroyAllWindows()

