from PIL import Image
import os
import random
import time

# add rarity and weihts to randomization
# make nft


def main(run_count):
    start_time = time.time()
    count = 0
    while count < run_count:
        background = Image.open("layers/Outline/Untitled_Artwork-1.png")
        eyes = Image.open(f"layers/Pupils/{random.choice(os.listdir('layers/Pupils/'))}")
        eyebrows = Image.open(f"layers/Eyebrows/{random.choice(os.listdir('layers/Eyebrows/'))}")
        eye_outline = Image.open(f"layers/Eyes/{random.choice(os.listdir('layers/Eyes/'))}")
        mouth = Image.open(f"layers/Mouth/{random.choice(os.listdir('layers/Mouth/'))}")
        nose = Image.open(f"layers/Nose/{random.choice(os.listdir('layers/Nose/'))}")

        image_list = [background, eyes, eyebrows, eye_outline, mouth, nose]

        for i in image_list:
            i = i.convert("RGBA")

        background.paste(eyes, (0, 0), mask=eyes)
        for x in image_list:
            background.paste(x, (0, 0), mask=x)
        background.save(f"output/auto-gen-{count + 1}.png", "PNG")
        count += 1
    print(f"Completed. {run_count} images generated.")
    print(f"Executed in: {(time.time() - start_time).__round__(3)} seconds")


def create_weights(location):
    weights = []
    # print(os.listdir(location))
    for file in os.listdir(location):
        # print(((file.split("-"))[1].split("."))[0])
        weights.append(int(((file.split("-"))[1].split("."))[0]))
    return weights


if __name__ == "__main__":
    main(15)
    # weight = create_weights("layers/Eyebrows/")
    # print(weight)

