from PIL import Image
import requests
import click
import cv2
import tensorflow as tf

def Brain_tumor_prediction(model, image):
  IMAGE_SIZE = 256
  # Resize the image

  try:
      img = tf.image.resize(images=image, size=[IMAGE_SIZE, IMAGE_SIZE])

      # preprocess the image
      img = tf.keras.applications.resnet50.preprocess_input(img)

      #======load model================================
      #model = load_model("Seg_multi-task-v2.hdf5", compile=False)

      imag = tf.expand_dims(img, axis=0)

      #==== detect tumor and locate it======
      predict = model.predict(imag)

      #plot the result and label
      mri = io.imread(img)
      img_ = cv2.cvtColor(mri, cv2.COLOR_BGR2RGB)

      #Obtain the predicted label
      label = np.argmax(pred[0])
      if label == 0:
          label = 'No Tumor'
      else:
          label = 'Tumor present'

      #=============predicted MRI mask==========================
      predicted_mask = np.asarray(predict[1])[0].squeeze().round()

      #== plot the prediction and label
      img_[predicted_mask == 1] = (0, 255, 0)
      plt.title.set_title(label, fontsize=40)
      plt.imshow(img_)
  except Exception as e:
    print('Input correct image in jpeg or tif format and ensure the file is not corrupt')
