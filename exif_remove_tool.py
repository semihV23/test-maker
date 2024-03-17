import os
from PIL import Image
from tqdm import tqdm

files = [f for f in os.listdir("exif_remove")
         if os.path.isfile("exif_remove/"+f) and f.lower().endswith((".jpg", ".png"))]
print("Images:", files)

for file in tqdm(files, desc="Processing", unit="file"):
    image = Image.open("exif_remove/"+file)
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)

    image_without_exif.save(
        "exif_remove/safe/"+file, optimize=True)
