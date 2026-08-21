import cv2
print(cv2.getBuildInformation())
#  cap = cv2.VideoCapture('autovideosrc ! videoconvert ! appsink', cv2.CAP_GSTREAMER)
#  if not cap.isOpened():
#      print('Could not open source')
#      exit()

#  while True:
#      ret, frame = cap.read()
#      if not ret:
#          print("Error reading frame")
#          break

#      cv2.imshow("Frame", frame)
#      if cv2.waitKey(1) == ord('q'):
#          break

#  cap.release()
#  cap.destroyAllWindows()
