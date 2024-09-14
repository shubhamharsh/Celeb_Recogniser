import numpy as np
import cv2
import matplotlib.pyplot as plt
import base64

def get_cv2_image_from_base64_string(b64str):
    print(b64str[:50])  # To print the first 50 characters for debugging
    encoded_data = b64str.split(',')[1]  # This assumes the base64 string is prefixed with data type information
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

# Read the base64 string from the file
with open(r'server\artifacts\b64.txt', 'r') as file:
    b64str = file.read()

img = get_cv2_image_from_base64_string(b64str)
print(img)

# Optionally display the image using OpenCV or Matplotlib
if img is not None:
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image could not be decoded")
