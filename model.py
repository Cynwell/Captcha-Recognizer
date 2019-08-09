import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # Input (n, 1, 32, 128)
        self.conv1 = nn.Conv2d(1, 12, 3, 1, 1)   # Output (n, 12, 32, 128)
        self.bn1 = nn.BatchNorm2d(12)
        self.conv2 = nn.Conv2d(12, 20, 3, 1, 1)  # Output (n, 20, 32, 128) then (n, 20, 16, 64)
        self.bn2 = nn.BatchNorm2d(20)
        self.conv3 = nn.Conv2d(20, 20, 3, 1, 1)  # Output (n, 20, 16, 64)
        self.bn3 = nn.BatchNorm2d(20)
        self.conv4 = nn.Conv2d(20, 24, 3, 1, 1)  # Output (n, 24, 16, 64) then (n, 24, 8, 32)
        self.bn4 = nn.BatchNorm2d(24)
        self.conv5 = nn.Conv2d(24, 28, 3, 1, 1)  # Output (n, 28, 8, 32)
        self.bn5 = nn.BatchNorm2d(28)
        self.conv6 = nn.Conv2d(28, 32, 3, 1, 1)  # Output (n, 32, 8, 32) then (n, 32, 4, 16)
        self.bn6 = nn.BatchNorm2d(32)
        self.conv7 = nn.Conv2d(32, 24, 3, 1, 1)  # Output (n, 24, 4, 16)
        self.bn7 = nn.BatchNorm2d(24)
        self.conv8 = nn.Conv2d(24, 24, 3, 1, 1)  # Output (n, 24, 4, 16) then (n, 24, 2, 8)
        self.bn8 = nn.BatchNorm2d(24)
        self.conv9 = nn.Conv2d(24, 28, 4, 1, 1)  # Output (n, 28, 1, 7)
        self.bn9 = nn.BatchNorm2d(28)
        self.fc1 = nn.Linear(196, 115)

    def forward(self, x):
        x = F.relu(self.bn1(self.conv1(x)))
        x = F.relu(F.max_pool2d(self.bn2(self.conv2(x)), 2))
        x = F.relu(self.bn3(self.conv3(x)))
        x = F.relu(F.max_pool2d(self.bn4(self.conv4(x)), 2))
        x = F.relu(self.bn5(self.conv5(x)))
        x = F.relu(F.max_pool2d(self.bn6(self.conv6(x)), 2))
        x = F.relu(self.bn7(self.conv7(x)))
        x = F.relu(F.max_pool2d(self.bn8(self.conv8(x)), 2))
        x = F.relu(self.bn9(self.conv9(x)))
        x = x.view(-1, 196)
        x = self.fc1(x)
        return x.reshape(-1, 5, 23)
