
from tensorflow.keras.applications import MobileNet
from tensorflow.keras.applications.mobilenet import preprocess_input
from keras.models import Model
from numpy import expand_dims
from PIL import Image
from tensorflow.keras.utils import img_to_array

class Simple_Model:
  def __init__(self):
    self.main_model = MobileNet()
    self.output_layers = ['conv_dw_1', 'conv_pw_1', 'conv_dw_2', 'conv_pw_2',
                          'conv_dw_3', 'conv_pw_3', 'conv_dw_4', 'conv_pw_4',
                          'conv_dw_5', 'conv_pw_5', 'conv_dw_6', 'conv_pw_6',
                          'conv_dw_7', 'conv_pw_7', 'conv_dw_8', 'conv_pw_8',
                          'conv_dw_9', 'conv_pw_9', 'conv_dw_10', 'conv_pw_10',
                          'conv_dw_11', 'conv_pw_11', 'conv_dw_12', 'conv_pw_12',
                          'conv_dw_13', 'conv_pw_13']
    self.input_shape = (224, 224)
    self.build_model()

  def build_model(self):
    outputs = [self.main_model.get_layer(i).output for i in self.output_layers]
    self.simple_model = Model(inputs=self.main_model.inputs, outputs=outputs)
  
  def get_feature_map(self, img_path):
    img = Image.open(img_path)
    img = img.resize(self.input_shape)
    img = img_to_array(img)
    img = expand_dims(img, axis=0)
    img = preprocess_input(img)
    return self.simple_model.predict(img)
