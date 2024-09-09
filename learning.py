import cv2
import numpy as np
import modi_plus
from modi_plus.module.output_module import display, led
from modi_plus.moudule.input_module import button
import requests
import time
import io

def compute_hog_feature(img,hog_descriptor):
    h = hog_descriptor.compute(img)
    return h

hog = cv2.HOGDescriptor()

features = []
lables = []

eWorld_images = []
road31_images = []
park228_images = []
godrock_images = []
daeguArtMuseum_images = []
daeguPark_images = []
sparkland_images = []
songhaepPark_images = []
westdoorMarket_images = []
susungLake_images = []
kimgwanseokRoad = []
daeguScienceMuseum = []

img_path = '/Users/dgsw8th41/Desktop/popularPlace/'

for i in range(1,11):
    eWorld_images.append(f"{img_path}eWorld"+str(i)+".png")
    
for i in range(1,11):
    road31_images.append(f"{img_path}31road"+str(i)+".png")
    
for i in range(1,11):
    park228_images.append(f"{img_path}228park"+str(i)+".png")
    
for i in range(1,11):
    godrock_images.append(f"{img_path}godrock"+str(i)+".png")

for i in range(1,11):
    daeguArtMuseum_images.append(f"{img_path}daeguartmuseum"+str(i)+".png")
    
for i in range(1,11):
    daeguPark_images.append(f"{img_path}daegupark"+str(i)+".png")
    
for i in range(1,11):
    sparkland_images.append(f"{img_path}sparkland"+str(i)+".png")
    
for i in range(1,11):
    songhaepPark_images.append(f"{img_path}songhaepark"+str(i)+".png")
    
for i in range(1,11):
    westdoorMarket_images.append(f"{img_path}westdoormarket"+str(i)+".png")
    
for i in range(1,11):
    susungLake_images.append(f"{img_path}susunglake"+str(i)+".png")
    
for i in range(1,11):
    kimgwanseokRoad.append(f"{img_path}kimgwangseokroad"+str(i)+".png")
    
for i in range(1,11):
    daeguScienceMuseum.append(f"{img_path}daegusciencemuseum"+str(i)+".png")
    
    
    
for img_path in eWorld_images:
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 256))
    h = compute_hog_feature(img, hog)
    features.append(h)
    lables.append(3)
    
for img_path in road31_images:
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 256))
    h = compute_hog_feature(img, hog)
    features.append(h)
    lables.append(3)
    
for img_path in park228_images:
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 256))
    h = compute_hog_feature(img, hog)
    features.append(h)
    lables.append(3)
    
for img_path in godrock_images:
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 256))
    h = compute_hog_feature(img, hog)
    features.append(h)
    lables.append(3)
    
for img_path in daeguArtMuseum_images:
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 256))
    h = compute_hog_feature(img, hog)
    features.append(h)
    lables.append(3)
    
for img_path in daeguPark_images:
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 256))
    h = compute_hog_feature(img, hog)
    features.append(h)
    lables.append(3)
    
for img_path in sparkland_images:
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 256))
    h = compute_hog_feature(img, hog)
    features.append(h)
    lables.append(3)
    
for img_path in songhaepPark_images:
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 256))
    h = compute_hog_feature(img, hog)
    features.append(h)
    lables.append(3)
    
for img_path in westdoorMarket_images:
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 256))
    h = compute_hog_feature(img, hog)
    features.append(h)
    lables.append(3)
    
for img_path in susungLake_images:
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 256))
    h = compute_hog_feature(img, hog)
    features.append(h)
    lables.append(3)
    
for img_path in kimgwanseokRoad:
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 256))
    h = compute_hog_feature(img, hog)
    features.append(h)
    lables.append(3)
    
for img_path in daeguScienceMuseum:
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 256))
    h = compute_hog_feature(img, hog)
    features.append(h)
    lables.append(3)