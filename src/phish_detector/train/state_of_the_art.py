from datetime import datetime

import torch.optim

from src.phish_detector.classes.state_of_the_art import Generator, Discriminator, train_loop, gen_dataloaders, test_loop


def sota_train(X, y, X_val, y_val, epochs, batch_size):
    train_loader = gen_dataloaders(X, y, batch_size)
    test_loader = gen_dataloaders(X_val, y_val, batch_size)

    generator = Generator(128, 10)
    discriminator = Discriminator(10, 1)
    opt_g = torch.optim.Adam(generator.parameters(), lr=0.001)
    opt_d = torch.optim.Adam(discriminator.parameters(), lr=0.001)

    loss_fn = torch.nn.BCELoss()

    for i in range(epochs):
        d_loss, g_loss = train_loop(generator, discriminator, train_loader, loss_fn, opt_g, opt_d)
        val_d_loss, val_g_loss = test_loop(generator, discriminator, test_loader, loss_fn)
        print(f"Epochs: {i + 1}")
        print(f"Train - Generator Loss: {g_loss} - Discriminator Loss: {d_loss}")
        print(f"Validation - Generator Loss: {val_g_loss} - Discriminator Loss: {val_d_loss}")

    torch.save(generator, f"./models/sota/genearator.pth")
    torch.save(discriminator, f"./models/sota/discriminator.pth")
