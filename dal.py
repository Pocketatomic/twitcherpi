from pymongo import MongoClient
import base64
from io import BytesIO
from datetime import datetime

client = MongoClient('mongodb://10.1.1.214')
db = client.twitcherpi

class ImageDocument():
    __image = BytesIO
    __captured_date = ""

    def __init__(self):
        now = datetime.now()
        self.__captured_date = now.isoformat

    def save_image(self, image):
        self.__image =image
        db.images.insert_one({"date":self.__captured_date, "image":base64.b64encode(image.getbuffer())})