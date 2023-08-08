#======== command-line tool implementation =================
from PIL import Image
import requests
import click
from utilities import Brain_tumor_prediction

@click.command()
@click.option('--url', default = None, help='enter image url')
@click.option('--img', default = None, help='image filename')

def prediction(url, img):
  """Trained multi-task deep learning model to predict MRI tumor classification and
  localization"""

  if url is not None:
    image = Image.open(requests.get(url, stream = True).raw)
    Brain_tumor_prediction(image)
  elif img is not None:
    Brain_tumor_prediction(image)
  elif url is not None & img is not None:
    print('provide either accesble MRI url or the filename on your computer')
  else:
    print('No image provided')

if __name__ == '__main__':
    prediction()
