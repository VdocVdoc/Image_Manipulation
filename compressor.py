from PIL import Image
import os
import random
import time

def main():
    print("Running")
    start_time = time.time()
    name = "1"
    file_format = ".png"
    path = "D:\\Coding\\NFT\\HashLipsTutorial\\hashlips_art_engine-1.0.6_update\\build\\images\\"
    new_image = Image.open(f"{path}{name}{file_format}")
    new_image.save(f"{path}save\\{name}\\original_{name}{file_format}")
    new_image = new_image.resize((800, 800), Image.ANTIALIAS)
    new_image.save(f"{path}save\\{name}\\resized_{name}{file_format}", quality=100)
    new_image.save(f"{path}save\\{name}\\optimized_resized_{name}{file_format}", optimize=True, quality=100)
    print(f"Executed in: {(time.time() - start_time).__round__(3)} seconds")
# main()


def compressAllImages():
    print("Running")
    start_time = time.time()
    file_format = ".png"
    image_path = "D:\\Coding\\NFT\\HashLipsTutorial\\hashlips_art_engine-1.0.6_update\\build\\images\\"
    save_path = "D:\\Coding\\NFT\\HashLipsTutorial\\hashlips_art_engine-1.0.6_update\\build\\compressed_images\\"
    image_name = 1
    # for image_name in range(1, 1001, 1):
    while image_name <= 1000:
        new_image = Image.open(f"{image_path}{image_name}{file_format}")
        new_image = new_image.resize((700, 700), Image.ANTIALIAS)
        new_image.save(f"{save_path}{image_name}{file_format}", optimize=True, quality=100)
        print(f"Completed: {image_name}")
        image_name += 1

    print(f"Executed in: {(time.time() - start_time).__round__(3)} seconds")


compressAllImages()

