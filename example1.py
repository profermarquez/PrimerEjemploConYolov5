import torch
#pip install seaborn
#pip install Pillow
# pip install pandas
# pip install matplotlib
#pip install torchvision
# pip install PyYAML
# pip install opencv-python
# pip install requests   
# #


# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Images
dir = 'https://github.com/ultralytics/yolov5/raw/master/data/images/'
imgs = [dir + f for f in ('zidane.jpg', 'bus.jpg')]  # batch of images


# Inference
results = model(imgs)
results.print()  # or .show(), .save()