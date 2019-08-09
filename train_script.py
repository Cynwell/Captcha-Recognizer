import os
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
from model import Net as Net
from captchaDataset import captchaDataset as captchaDataset

IMAGE_PATH_TRAIN = "./split/train"
IMAGE_PATH_TEST = "./split/test"
MODEL_PATH = "./model"

n_epochs = 50
batch_size_train = 50
batch_size_test = 300
learning_rate = 0.01
momentum = 0.9
log_interval = 10

network = Net()
if torch.cuda.is_available():
    network = network.cuda()

optimizer = optim.Adam(network.parameters(), lr=learning_rate)

try:
    with open(os.path.join(os.path.abspath(MODEL_PATH), "model.syn"), 'rb') as file:
        network.load_state_dict(torch.load(file))
    with open(os.path.join(os.path.abspath(MODEL_PATH), "optimizer.syn"), 'rb') as file:
        optimizer.load_state_dict(torch.load(file))
    print("Loaded network and optimizer files.")
except:
    print("Network and optimizer files not found.")
    if not os.path.exists(MODEL_PATH):
        os.makedirs(os.path.abspath(MODEL_PATH))

dataset = captchaDataset(IMAGE_PATH_TRAIN)
testset = captchaDataset(IMAGE_PATH_TEST)
train_loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size_train, shuffle=True)
test_loader = torch.utils.data.DataLoader(testset, batch_size=batch_size_test, shuffle=True)

train_losses = []
train_counter = []
test_losses = []

criterion = nn.CrossEntropyLoss()


def five_cat_loss(output, target):
    loss = 0
    for i in range(output.shape[0]):
        loss += criterion(output[i], target[i])
    return loss


def train(epoch):
    network.train()
    for batch_index, (data, target) in enumerate(train_loader):
        output = network(data)
        loss = five_cat_loss(output, target)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if batch_index % log_interval == 0:
            print("Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}".format(
                epoch, batch_index * len(data), len(train_loader.dataset),
                100. * batch_index * len(data) / len(train_loader.dataset), loss.item()))

    # Log
    train_losses.append(loss.item())
    train_counter.append((batch_index*batch_size_train) + epoch*len(train_loader.dataset))
    torch.save(network.state_dict(), os.path.join(os.path.abspath(MODEL_PATH), "model.syn"))
    torch.save(optimizer.state_dict(), os.path.join(os.path.abspath(MODEL_PATH), "optimizer.syn"))


def test():
    network.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            output = network(data)
            test_loss += five_cat_loss(output, target)

            # Code below is for extracting the prediction from the network output and compare with true answers
            pred = output.data.max(2, keepdim=True)[1]
            for i in range(pred.shape[0]):
                all_correct_guess = pred[i].eq(target[i].data.view_as(pred[i])).sum()
                if all_correct_guess == 5:
                    correct += 1
            correct_characters = pred.eq(target.data.view_as(pred)).sum()

            # visualization
            # for i in range(data.shape[0]):
            #     visualize(data[i].cpu(), "{}: Predicted: {}".format(i, argmax_to_string(pred[i].squeeze().cpu())))

        # Log
        test_loss /= len(test_loader.dataset)
        test_losses.append(test_loss)
        print('\nTest set: Avg. loss: {:.4f}, Accuracy on characters: {}/{} ({:.0f}%), Whole images: {}/{} ({:.0f}%)\n'.format(
            test_loss, correct_characters, len(test_loader.dataset) * 5,
            100. * correct_characters / (len(test_loader.dataset) * 5),
            correct, len(test_loader.dataset),
            100. * correct / len(test_loader.dataset)))


try:
    train_losses = []
    train_counter = []
    test_losses = []

    # If only testing, enable this:
    # test()

    # If training + testing, enable this:
    for epoch in range(1, n_epochs + 1):
        train(epoch)
        test()
finally:
    print("Finished Training.")

    # Plot graph
    fig = plt.figure()
    ax = fig.add_subplot(211)
    ax.plot(train_counter, train_losses)
    ax.set_xlabel("Training Samples")
    ax.set_ylabel("Loss")

    bx = fig.add_subplot(212)
    bx.plot(train_counter, test_losses)
    bx.set_xlabel("Testing Samples")
    bx.set_ylabel("Loss")
    plt.tight_layout()
    plt.show()
    input("Press Enter to close the window...")
