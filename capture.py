# to capture the images from the pi
# 27/07/2023

from datetime import datetime
from picamera import PiCamera
from dal2 import ImageDocument
from io import BytesIO

image_docuement = ImageDocument()

camera = PiCamera()
camera.resolution = (1024, 768)

def take_picture():
    image = BytesIO
    camera.capture('test2.jpg')
    # camera.capture(image, 'jpeg')
    
    return image

def save_image(image):

    image_docuement.__captured_date = str(datetime.now().isoformat)
    image_docuement.__author = "Andrew Butler"
    image_docuement.save_image(image)

img = take_picture()
save_image(img)