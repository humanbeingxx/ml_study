# coding: utf-8

import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        self.conv1 = torch.nn.Conv2d(in_channels=1, out_channels=5, kernel_size=5)
        self.conv2 = torch.nn.Conv2d(in_channels=5, out_channels=15, kernel_size=5)

        self.fc1 = nn.Linear(in_features=15*5*5, out_features=100)
        self.fc2 = nn.Linear(in_features=100, out_features=70)
        self.fc3 = nn.Linear(in_features=70, out_features=10)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)

        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)

        return x

    def num_flat_features(self, x):
        size = x.size()[1:]     # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features

if __name__ == "__main__":
    input = torch.randn(1, 1, 32, 32)
    net = Net()
    out = net(input)
    print(out)
    parameters = list(net.parameters())
    print(len(parameters))
    for i in range(0, len(parameters)):
        print(parameters[i].size())