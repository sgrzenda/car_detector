from picamera import PiCamera
from skimage.measure import compare_ssim as ssim
import cv2
import sys
from time import sleep
import io
import numpy as np


base_image = None
# car_detected = False


def compare_images(img_a, img_b):
  return ssim(img_a, img_b)


old_img = None
new_img = None
stream = io.BytesIO()

cam = PiCamera()
cam.resolution = (1024, 768)
cam.start_preview()
sleep(2)


while True:
  cam.capture(stream, format='jpeg')
  data = np.fromstring(stream.getvalue(), dtype=np.uint8)
  # "Decode" the image from the array, preserving colour
  new_image = cv2.imdecode(data, 1)
  new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
  if not old_img:
    old_img = new_img
    sleep(10)
    continue
  else:
    print('Original vs new: %f' % compare_images(old_image, new_image))
    sleep(10)
