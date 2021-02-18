from PIL import Image
import os

input_path = "/mnt/c/Users/bizim/Downloads/ScreenshotsThesis6"
output_path = "/mnt/c/Users/bizim/Downloads/ScreenshotsThesis6rgb"

for image_path in os.listdir(input_path):
    image_input_path = os.path.join(input_path, image_path)
    im = Image.open(image_input_path)
    out = im.convert("RGB")
    image_output_path = os.path.join(output_path, image_path)
    out.save(image_output_path)