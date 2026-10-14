import torch
import torch.nn as nn
import torch.nn.functional as F



class ResidualBlock(nn.Module):

    def __init__(self, in_channels, out_channels, stride=1):
        """
        Create residual block with two conv layers.

        Parameters:
            - in_channels (int): Number of input channels.
            - out_channels (int): Number of output channels.
            - stride (int): Stride for first convolution.

        """
        super().__init__()
        ############################################################
        ###                  START OF YOUR CODE                  ###
        ############################################################



        ############################################################
        ###                   END OF YOUR CODE                   ###
        ############################################################


    def forward(self, x):
        """
        Compute the forward pass through the residual block.

        Parameters:
            - x (torch.Tensor): Input.

        Returns:
            - out (torch.tensor): Output.

        """
        ############################################################
        ###                  START OF YOUR CODE                  ###
        ############################################################

        out = None

        ############################################################
        ###                   END OF YOUR CODE                   ###
        ############################################################
        return out



class ResNet(nn.Module):

    def __init__(self):
        """
        Creates a residual network.
        """
        super().__init__()
        ############################################################
        ###                  START OF YOUR CODE                  ###
        ############################################################



        ############################################################
        ###                   END OF YOUR CODE                   ###
        ############################################################


    def forward(self, x):
        """
        Compute the forward pass through the network.

        Parameters:
            - x (torch.Tensor): Input.

        Returns:
            - out (torch.Tensor): Output.

        """
        ############################################################
        ###                  START OF YOUR CODE                  ###
        ############################################################

        out = None

        ############################################################
        ###                   END OF YOUR CODE                   ###
        ############################################################
        return out





