# Multi-task-Brain-Tumor-detection-and-segmentation
Multi-task deep learning approach is developed for simultaneous MRI tumor classification and segmentation prediction.
* classification weight is considered in the classification part loss function during training to handle unbalanced data
* Focal Tversky loss and Tversky index are adopted for the segmentation part. The model achieved a high Tversky index and low focal loss.

Link to the trained model with weights: https://drive.google.com/file/d/1-2oegcI5wBI747_bbCvJIn2QrkuJZW-T/view?usp=drive_link

* **MRI and mask data sampling**

![alt text](https://github.com/Michael-HK/Multi-task-Brain-Tumor-detection-and-segmentation/blob/main/images/MRI%20sampling.png?raw=true)

* **Proposed multi-task deep learning training plots**

![alt text](https://github.com/Michael-HK/Multi-task-Brain-Tumor-detection-and-segmentation/blob/main/images/model%20training%20plots.png?raw=true)

* **Classification part evaluation**
The proposed model achieved 95% accuracy on the validation data
![alt text](https://github.com/Michael-HK/Multi-task-Brain-Tumor-detection-and-segmentation/blob/main/images/classification%20report.png?raw=true)
![alt text](https://github.com/Michael-HK/Multi-task-Brain-Tumor-detection-and-segmentation/blob/main/images/classification%20confusion%20matrix.png?raw=true)


* **Segmentation prediction example**

![alt text](https://github.com/Michael-HK/Multi-task-Brain-Tumor-detection-and-segmentation/blob/main/images/segmentation%20prediction.png?raw=true)

* **Simultaneous tumor classification and segmentation my the proposed Multi-task deep learning model**

![alt text](https://github.com/Michael-HK/Multi-task-Brain-Tumor-detection-and-segmentation/blob/main/images/tumor%20MRI%20clasisfication%20and%20segmentation.png?raw=true)

