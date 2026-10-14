import torch
import torch.nn as nn
import torch.nn.functional as F



__all__ = ['Discriminator', 'Generator']



def init_params(module):
    """
    Initialize parameters in convolution and batchnorm layers.

    Parameters:
        - module (nn.Module): Layer with parameters.

    """
    ############################################################
    ###                  START OF YOUR CODE                  ###
    ############################################################

    pass

    ############################################################
    ###                   END OF YOUR CODE                   ###
    ############################################################



class Discriminator(nn.Module):

    def __init__(self, channels, depth):
        """
        Create discriminator network.

        Parameters:
            - channels (int): Number of output channels.
            - depth (int): Depth of intermediate feature maps.

        """
        super().__init__()
        ############################################################
        ###                  START OF YOUR CODE                  ###
        ############################################################



        ############################################################
        ###                   END OF YOUR CODE                   ###
        ############################################################
        self.apply(init_params)


    def forward(self, x):
        """
        Compute forward pass through network.

        Parameters:
            - x (torch.Tensor): Input images.

        Returns:
            - p (torch.Tensor): Probability of being real.

        """
        ############################################################
        ###                  START OF YOUR CODE                  ###
        ############################################################

        p = None

        ############################################################
        ###                   END OF YOUR CODE                   ###
        ############################################################
        return p



class Generator(nn.Module):

    def __init__(self, latent_dim, channels, depth):
        """
        Create generator network.

        Parameters:
            - latent_dim (int): Dimension of latent vectors.
            - channels (int): Number of output channels.
            - depth (int): Depth of intermediate feature maps.

        """
        super().__init__()
        ############################################################
        ###                  START OF YOUR CODE                  ###
        ############################################################



        ############################################################
        ###                   END OF YOUR CODE                   ###
        ############################################################
        self.apply(init_params)


    def forward(self, z):
        """
        Compute forward pass through network.

        Parameters:
            - z (torch.Tensor): Latent vectors.

        Returns:
            - x (torch.Tensor): Fake images.

        """
        ############################################################
        ###                  START OF YOUR CODE                  ###
        ############################################################

        x = None

        ############################################################
        ###                   END OF YOUR CODE                   ###
        ############################################################
        return x




