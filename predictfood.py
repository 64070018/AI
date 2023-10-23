# feature extraction model
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.preprocessing import image

# data management
import numpy as np

# image management
import requests
import io
from PIL import Image

import pickle
# output function
modFile = 'insects_LR_mymod_monet.mod'
model_pred = pickle.load(open(modFile,'rb'))

# call MobileNetV2 as a feature extraction model
MoNet = MobileNetV2(include_top=False, weights='imagenet', classes=1000)

# function for [image link url or image path --> image ]
def getImage(imgpath):
  if imgpath.find('http')!=-1:
      r = requests.get(imgpath, allow_redirects=True, timeout=10)
      image_bytes = io.BytesIO(r.content)
      img = Image.open(image_bytes)
  else:
      img = Image.open(imgpath)
  return img

def extract_feature_resize(imgpath, model_feat):
  # get image
  img = getImage(imgpath)
  # resize image to 224 x 224
  img = img.resize((224,224))
  # change image to numpy array
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  x = preprocess_input(x)
  # feature extraction using model
  features = model_feat.predict(x, batch_size=1,verbose=0)
  features = np.ndarray.flatten(features).astype('float64')
  return features

# function for predicting from your model
def predicting_resize(imgpath, model_pred=model_pred, model_feat=MoNet):
  feat = extract_feature_resize(imgpath, model_feat)
  result = model_pred.predict([feat])[0]
  return result

image_url = "https://th.bing.com/th/id/OIP.EoTHx89h3f3w0yTkilonYAHaEo?pid=ImgDet&rs=1"

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

post_mapping = {
"chicken_curry": [
    {
        "type": "text",
        "text": "สนใจแกงกะหรี่ไก่มั้ยครับ"
    },
    {
        "type": "image",
        "originalContentUrl": "https://www.177milkstreet.com/assets/site/Recipes/Hyderabadi-Chicken-Curry.jpg",
        "previewImageUrl": "https://www.177milkstreet.com/assets/site/Recipes/Hyderabadi-Chicken-Curry.jpg"
    }

],
"chicken_wings": [
    {
        "type": "text",
        "text": "สนใจแกงกะหรี่ไก่มั้ยครับ"
    },
    {
        "type": "image",
        "originalContentUrl": "https://www.177milkstreet.com/assets/site/Recipes/Hyderabadi-Chicken-Curry.jpg",
        "previewImageUrl": "https://www.177milkstreet.com/assets/site/Recipes/Hyderabadi-Chicken-Curry.jpg"
    }

],
"fried_rice": [
    {
        "type": "text",
        "text": "สนใจแกงกะหรี่ไก่มั้ยครับ"
    },
    {
        "type": "image",
        "originalContentUrl": "https://www.177milkstreet.com/assets/site/Recipes/Hyderabadi-Chicken-Curry.jpg",
        "previewImageUrl": "https://www.177milkstreet.com/assets/site/Recipes/Hyderabadi-Chicken-Curry.jpg"
    }

],
"grilled_salmon": [
    {
        "type": "text",
        "text": "สนใจแกงกะหรี่ไก่มั้ยครับ"
    },
    {
        "type": "image",
        "originalContentUrl": "https://www.177milkstreet.com/assets/site/Recipes/Hyderabadi-Chicken-Curry.jpg",
        "previewImageUrl": "https://www.177milkstreet.com/assets/site/Recipes/Hyderabadi-Chicken-Curry.jpg"
    }

],
"hamburger": [
    {
        "type": "text",
        "text": "สนใจแกงกะหรี่ไก่มั้ยครับ"
    },
    {
        "type": "image",
        "originalContentUrl": "https://www.177milkstreet.com/assets/site/Recipes/Hyderabadi-Chicken-Curry.jpg",
        "previewImageUrl": "https://www.177milkstreet.com/assets/site/Recipes/Hyderabadi-Chicken-Curry.jpg"
    }

],
"ice_cream": [
    {
        "type": "text",
        "text": "สนใจแกงกะหรี่ไก่มั้ยครับ"
    },
    {
        "type": "image",
        "originalContentUrl": "https://www.177milkstreet.com/assets/site/Recipes/Hyderabadi-Chicken-Curry.jpg",
        "previewImageUrl": "https://www.177milkstreet.com/assets/site/Recipes/Hyderabadi-Chicken-Curry.jpg"
    }

],
"pizza": [
    {
        "type": "text",
        "text": "สนใจแกงกะหรี่ไก่มั้ยครับ"
    },
    {
        "type": "image",
        "originalContentUrl": "https://www.177milkstreet.com/assets/site/Recipes/Hyderabadi-Chicken-Curry.jpg",
        "previewImageUrl": "https://www.177milkstreet.com/assets/site/Recipes/Hyderabadi-Chicken-Curry.jpg"
    }

],
"ramen": [
    {
        "type": "text",
        "text": "สนใจแกงกะหรี่ไก่มั้ยครับ"
    },
    {
        "type": "image",
        "originalContentUrl": "https://www.177milkstreet.com/assets/site/Recipes/Hyderabadi-Chicken-Curry.jpg",
        "previewImageUrl": "https://www.177milkstreet.com/assets/site/Recipes/Hyderabadi-Chicken-Curry.jpg"
    }

],
"steak": [
    {
        "type": "text",
        "text": "สนใจแกงกะหรี่ไก่มั้ยครับ"
    },
    {
        "type": "image",
        "originalContentUrl": "https://www.177milkstreet.com/assets/site/Recipes/Hyderabadi-Chicken-Curry.jpg",
        "previewImageUrl": "https://www.177milkstreet.com/assets/site/Recipes/Hyderabadi-Chicken-Curry.jpg"
    }

],
"sushi": [
    {
        "type": "text",
        "text": "สนใจแกงกะหรี่ไก่มั้ยครับ"
    },
    {
        "type": "image",
        "originalContentUrl": "https://www.177milkstreet.com/assets/site/Recipes/Hyderabadi-Chicken-Curry.jpg",
        "previewImageUrl": "https://www.177milkstreet.com/assets/site/Recipes/Hyderabadi-Chicken-Curry.jpg"
    }

],
}



@app.route("/predict")
def predict():
    image_url = request.args.get("image")

    pred = predicting_resize(image_url)
    # opject = post_mapping[pred]
    return jsonify(
        {
            "response": pred
        })

if __name__ == "__main__":
   app.run()