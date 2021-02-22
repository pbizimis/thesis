from PIL import Image
import operator
import os

input_path = "/mnt/c/Users/bizim/Downloads/ScreenshotsThesis6rgb"
output_path_good = "/mnt/c/Users/bizim/Desktop/ThesisTesting/dataset2"
output_path_error = "/mnt/c/Users/bizim/Desktop/ThesisTesting/not_good2"

def save_img(output_path):
    image_output_path = os.path.join(output_path, image_path)
    im.save(image_output_path)

for image_path in os.listdir(input_path):
    image_input_path = os.path.join(input_path, image_path)
    im = Image.open(image_input_path)
    image_dict = {}

    for pixel in im.getdata():
        try:
            image_dict[pixel] += 1
        except:
            image_dict[pixel] = 1

        
    max_key = max(image_dict, key=lambda key: image_dict[key])

    highest_percentage = image_dict[max_key] / 4194304

    if highest_percentage > 0.85:
        save_img(output_path_error)
        print("NOT GOOD", image_path)
        continue
    save_img(output_path_good)
    print("GOOD", image_path)

# duplicates
# integrate into rgb
# train classifier to find cookie windows
# if pixel have a 90% stake, delete