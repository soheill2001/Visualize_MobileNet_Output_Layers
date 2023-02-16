# MobileNet Feature Map Visualization
This is a Python repository that contains two files `Model.py` and `Visualize.py`.

`Model.py` defines a simple model class that uses MobileNet to extract feature maps from an input image. The `Simple_Model` class takes an image path as input and returns the feature maps for specific layers of the MobileNet model.

`Visualize.py` defines a class Visualize that takes the feature maps returned by `Simple_Model` and visualizes them. The script creates a grid of feature maps for each layer and saves them in the Images directory.
## MobileNet
MobileNet is a convolutional neural network architecture that is designed for mobile and embedded vision applications. The architecture is based on depthwise separable convolutions, which greatly reduces the number of parameters and computational cost while maintaining high accuracy.

In this code, we use the MobileNet model pre-trained on the ImageNet dataset to extract feature maps from an input image.
## Requirements
To run the mobilenet_feature_map_visualization.py script, you will need the following:
```
tensorflow
keras
numpy
Pillow
matplotlib
```
You can install the required dependencies using pip:
```
pip install -r requirements.txt
```
## Usage
To use this code, you can follow these steps:

Clone the repository to your local machine:
```
git clone https://github.com/<username>/<repository_name>.git
```
