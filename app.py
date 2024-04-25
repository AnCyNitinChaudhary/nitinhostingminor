import cv2
video_capture = cv2.VideoCapture(0)
ret,frame=video_capture.read()

face_names = ['9921103118']
output_json = {"face_name": face_names}
print(output_json, flush=True)  # Print JSON object to stdout
