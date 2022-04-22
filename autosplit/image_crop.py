import os
import cv2
import random
import time

SPATULA_PATH = "autosplit/learner/dataset/data/spatula"

WIDTH = 640
W_WIDTH = round(WIDTH/6)
W_MIN = 275
W_MAX = 325

HEIGHT = 480
H_WIDTH = round(HEIGHT/6)
H_MIN = 10
H_MAX = 50

for label in os.listdir(SPATULA_PATH):
    print(f"Processing label = '{label}'")
    if not os.path.isdir(f"{SPATULA_PATH}/{label}/new"):
        continue
    for filename in os.listdir(f"{SPATULA_PATH}/{label}/new"):
        full_frame = cv2.imread(f"{SPATULA_PATH}/{label}/new/{filename}", 3)
        gray_frame = cv2.cvtColor(full_frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f"{SPATULA_PATH}/{label}/{filename}", gray_frame)
        os.remove(f"{SPATULA_PATH}/{label}/new/{filename}")
    os.rmdir(f"{SPATULA_PATH}/{label}/new")
    time.sleep(3)



# for label in os.listdir(SPATULA_PATH):
#     print(f"Processing label = '{label}'")
#     image_count = 0
#     for filename in os.listdir(f"{SPATULA_PATH}/{label}"):
#         if not filename.endswith(".jpg"):
#             continue
#         image_path = f"{SPATULA_PATH}/{label}/{filename}"
#         full_frame = cv2.imread(image_path, 3)
#         gray_frame = cv2.cvtColor(full_frame, cv2.COLOR_BGR2GRAY)
#         os.remove(image_path)

#         for width in range(W_MIN, W_MAX + 1):
#             for height in range(H_MIN, H_MAX + 1):
#                 if random.randint(1, 1000) < 20:
#                     cropped_image = gray_frame[height : height + H_WIDTH, width : width + W_WIDTH]
#                     cv2.imwrite(f"{SPATULA_PATH}/{label}/spatula_{label}_{image_count}.jpg", cropped_image)
#                     image_count += 1
#     time.sleep(3)
