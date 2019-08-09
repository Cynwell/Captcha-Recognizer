import os
import random

SOURCE_FOLDER = "./download"
TRAIN_FOLDER = "./split/train"
TEST_FOLDER = "./split/test"
TEST_COUNT = 2

if not os.path.exists(SOURCE_FOLDER):
    print("Unable to reach source folder!")
    exit()
if not os.path.exists(TRAIN_FOLDER):
    os.makedirs(TRAIN_FOLDER)
if not os.path.exists(TEST_FOLDER):
    os.makedirs(TEST_FOLDER)

for (dirpath, _, filelist) in os.walk(SOURCE_FOLDER):
    if TEST_COUNT > len(filelist):
        print("Not enough images in source folder! Please lower TEST_COUNT and re-try.")
        exit()
    selection = random.sample(range(len(filelist)), TEST_COUNT)
    # Move randomly selected files to test folder
    for i in selection:
        os.rename(os.path.join(dirpath, filelist[i]), os.path.join(os.path.abspath(TEST_FOLDER), filelist[i]))

# Move remained files to train folder
for (dirpath, _, filelist) in os.walk(SOURCE_FOLDER):
    for filename in filelist:
        os.rename(os.path.join(dirpath, filename), os.path.join(os.path.abspath(TRAIN_FOLDER), filename))
print("Finished separation. Results have been saved to:")
print("TRAIN_FOLDER:", os.path.abspath(TRAIN_FOLDER))
print("TEST_FOLDER:", os.path.abspath(TEST_FOLDER))
