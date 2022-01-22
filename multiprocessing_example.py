from multiprocessing import Process
from PIL import Image
import numpy as np
import multiprocessing as mp
import time

# list_of_pixels = [560, 570, 580, 590, 610, 620, 630, 640, 650, 660, 670, 680, 690]
list_of_pixels = [630]
def compressImage(name):
    # time.sleep(2)
    for size in list_of_pixels:
        re_name = f"{name}.png"
        image_path = "D:\\Coding\\NFT\\HashLipsTutorial\\hashlips_art_engine-1.0.6_update\\build\\images\\"
        save_path = f"D:\\Coding\\NFT\\HashLipsTutorial\\hashlips_art_engine-1.0.6_update\\build\\{size}x{size}_compressed_images\\"
        new_image = Image.open(f"{image_path}{re_name}")
        new_image = new_image.resize((size, size), Image.ANTIALIAS)
        new_image.save(f"{save_path}{re_name}", optimize=True, quality=100)
    print(f"Completed: {name}.png")

if __name__ == "__main__":
    start_time = time.time()
    pool = mp.Pool(mp.cpu_count())
    names = np.arange(1, 2501)
    results = [pool.apply_async(compressImage(row)) for row in names]
    pool.close()
    print(f"Executed in: {(time.time() - start_time).__round__(3)} seconds")
