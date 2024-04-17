from PIL import Image
import os

# Path to the directory with images
directory = "/home/kevincai/zzzholder/cs180/proj6/final_output/wave_home_run"

# List and sort the image files
images = sorted([f for f in os.listdir(directory) if f.endswith('.jpg') or f.endswith('.png')],
                key=lambda x: int(x.split('/')[-1].split('.')[0]))

# Create an image list for the GIF
image_list = []
for file in images:
    file_path = os.path.join(directory, file)
    image_list.append(Image.open(file_path))

# Save the images as a GIF
image_list[0].save('wave_home.gif', save_all=True, append_images=image_list[1:], optimize=False, duration=200, loop=0)