import matplotlib.pyplot as plt
import math
import argparse
from Model import Simple_Model

class Visualize:
  def __init__(self):
    self.index = 0
    self.layer_num = 1
    self.pair = ['conv_dw_', 'conv_pw_']
    self.show_layer = self.pair[0]
    self.fig_size = (10, 10)
    
  def proccess_each_feature_map(self, square, fmap):
    ix = 1
    plt.figure(figsize=self.fig_size)
    for _ in range(square):
      for _ in range(square):
        ax = plt.subplot(square, square, ix)
        ax.set_xticks([])
        ax.set_yticks([])
        plt.imshow(fmap[0, :, :, ix-1], cmap='gray')
        ix += 1
    plt.suptitle(f'{self.show_layer}{self.layer_num} Visualization')
    plt.savefig(f'Images/{self.show_layer}{self.layer_num}')

  def show_each_feature_map(self, feature_maps):
    for fmap in feature_maps:
      square = len(feature_maps[self.index][0][0][0])
      square = int(math.sqrt(square))
      self.index += 1
      self.proccess_each_feature_map(square, fmap)
      if self.show_layer == self.pair[0]:
        self.show_layer = self.pair[1]
      else:
        self.show_layer = self.pair[0]
        self.layer_num += 1
        
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--image_path', type=str)
  args = parser.parse_args()

  simple_model = Simple_Model()
  feature_maps = simple_model.get_feature_map(args.image_path)

  visual = Visualize()
  visual.show_each_feature_map(feature_maps)
