import numpy as np
import torch
from torch import nn, Tensor
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader


class Generator(nn.Module):
    def __init__(self, input_size, output_size):
        super(Generator, self).__init__()

        def block(in_size, out_size):
            layers = [nn.Linear(in_size, out_size),
                      nn.BatchNorm1d(out_size, 0.8),
                      nn.LeakyReLU(0.2, inplace=True)]
            return layers

        self.model = nn.Sequential(
            *block(input_size, 128),
            *block(128, 256),
            *block(256, 512),
            *block(512, 1024),
            nn.Linear(1024, output_size),
            nn.Tanh()
        )

    def forward(self, z):
        url = self.model(z)
        return url


class Discriminator(nn.Module):
    def __init__(self, input_size, output_size):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_size, 128),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(128, 256),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(256, output_size),
            nn.Sigmoid()
        )

    def forward(self, url):
        validity = self.model(url)
        return validity


class PhishDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X)
        self.y = torch.tensor(y, dtype=torch.long)

    def __getitem__(self, index):
        return self.X[index], self.y[index]

    def __len__(self):
        return len(self.X)


def gen_dataloaders(features, labels, batch_size):
    data = PhishDataset(features, labels)
    data_loader = DataLoader(data, batch_size=batch_size, shuffle=True)
    return data_loader


def train_loop(generator, discriminator, train_loader, loss_fn, optimizer_g, optimizer_d):
    generator.train()
    discriminator.train()
    for (features, labels) in train_loader:
        valid = Variable(Tensor(features.size(0), 1).fill_(1.0), requires_grad=False)
        fake = Variable(Tensor(features.size(0), 1).fill_(0.0), requires_grad=False)

        # Sample noise as generator input
        z = Variable(Tensor(np.random.normal(0, 1, (features.shape[0], 128))))

        # Generate a batch of images
        gen_features = generator(z)

        # Loss measures generator's ability to fool the discriminator
        g_loss = loss_fn(discriminator(gen_features), valid)

        g_loss.backward()
        optimizer_g.step()

        # ---------------------
        #  Train Discriminator
        # ---------------------

        optimizer_d.zero_grad()

        # Measure discriminator's ability to classify real from generated samples
        real_loss = loss_fn(discriminator(features), valid)
        fake_loss = loss_fn(discriminator(gen_features.detach()), fake)
        d_loss = (real_loss + fake_loss) / 2

        d_loss.backward()
        optimizer_d.step()

    return d_loss.item(), g_loss.item()


def test_loop(generator, discriminator, test_loader, loss_fn):
    generator.eval()
    discriminator.eval()

    with torch.no_grad():
        for features, labels in test_loader:
            valid = Variable(Tensor(features.size(0), 1).fill_(1.0), requires_grad=False)
            fake = Variable(Tensor(features.size(0), 1).fill_(0.0), requires_grad=False)

            # Sample noise as generator input
            z = Variable(Tensor(np.random.normal(0, 1, (features.shape[0], 128))))

            # Generate a batch of images
            gen_features = generator(z)

            # Loss measures generator's ability to fool the discriminator
            g_loss = loss_fn(discriminator(gen_features), valid)

            real_loss = loss_fn(discriminator(features), valid)
            fake_loss = loss_fn(discriminator(gen_features.detach()), fake)
            d_loss = (real_loss + fake_loss) / 2
    return d_loss.item(), g_loss.item()
