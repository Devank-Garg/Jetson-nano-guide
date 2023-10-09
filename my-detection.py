import jetson_inference
import jetson_utils

net = jetson_inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

camera = jetson_utils.gstCamera(1280, 720, "/dev/video0")
display = jetson_utils.glDisplay()
output_path = '/home/labuser/Downloads/camera_output.mp4'  # Corrected the output path
output = jetson_utils.videoOutput(output_path, camera.GetWidth(), camera.GetHeight())  # Specify width and height

while True:
    img, width, height = camera.CaptureRGBA()
    detections = net.Detect(img, width, height)
    output.Render(img)
    display.RenderOnce(img, width, height)
    display.SetTitle("First Time Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

output.Close()
print('done')

