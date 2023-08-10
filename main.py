import json
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from utils import Brain_tumor_prediction

app = Flask(__name__)
@app.route('/predict', methods = ['POST'])
def seg_predict():
  try:
      if request.method == 'POST':
        if ('file' in request.files['file'])
          img = request.files['file'].stream
        else:
          url = request.get_data()
          img = Image.open(requests.get(url, stream = True).raw)
        pred = Brain_tumor_prediction(model, img)                 
      return render_template("result.html", pred)

  except:
      error = "File cannot be processed."
         return render_template("result.html", err=error)

# Driver code
if __name__ == "__main__":
    model = load_model("Seg_multi-task-v2.hdf5", compile=False)
    app.run(port=9000, debug=True)
