import io
import pyperclip
from google.cloud import vision
from google.cloud.vision import types
from PIL import ImageGrab, Image

# getting image from clipboard
im = ImageGrab.grabclipboard()
if isinstance(im, Image.Image):
    
    # google vision client
    client = vision.ImageAnnotatorClient()
    
    # loading clipboard to byte array
    imgByteArr = io.BytesIO()
    im.save(imgByteArr, "JPEG")
    
    # passing image to Goole Vision
    image = types.Image(content=imgByteArr.getvalue())
    response = client.text_detection(image=image)
    
    # retrieving response
    texts = response.text_annotations
    if texts:
    	# coping regonized text back to clipboard
        pyperclip.copy(texts[0].description)