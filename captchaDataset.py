import numpy as np
from PIL import Image
import torch
from torch.utils.data import Dataset
import os
import cv2
from utilities import preprocess, to_argmax, argmax_to_string, visualize


# First preprocess all, then store in memory and reduce __getitem__ time
class captchaDataset(Dataset):
    def __init__(self, image_path, transform=None):
        self.dataset = np.array([])
        self.label = []
        self.transform = transform

        # Initialize and read data in the specified path
        self._init_dataset(os.path.abspath(image_path))

        # Preprocess data
        self.dataset = preprocess(self.dataset)

        # For data augmentation
        if self.transform is not None:
            for i in range(len(self.dataset)):
                self.dataset[i] = self.transform(Image.fromarray(self.dataset[i]))
        else:
            self.dataset = torch.FloatTensor(self.dataset)  # a tensor of shape (n, 36, 128)
        self.label = torch.LongTensor(self.label).squeeze()  # a tensor of shape (n, 5)

        if torch.cuda.is_available():
            self.dataset = self.dataset.cuda()
            self.label = self.label.cuda()

    def __len__(self):
        return self.dataset.shape[0]

    def __getitem__(self, index):
        return self.dataset[index], self.label[index]

    def _init_dataset(self, image_abs_path):
        for (_, _, filelist) in os.walk(image_abs_path):
            self.dataset = np.array([[cv2.imread(os.path.join(image_abs_path, filename), 1)] for filename in filelist])
            self.label = np.array([to_argmax(filename[:5]) for filename in filelist])


if __name__ == "__main__":
    IMAGE_PATH = "./split/test"
    dataset = captchaDataset(IMAGE_PATH)
    print("Length of dataset:", len(dataset))   # for verifying whether all data has benn loaded
    (images, labels) = dataset[0:2]
    print(images.shape)

    for image, label in zip(images, labels):
        visualize(image.cpu(), to_argmax(argmax_to_string(label.cpu())))

    # Or show in this way:
    # img = np.array(image[0].cpu())
    # cv2.imshow("The first image", img)
    # cv2.waitKey(0)
