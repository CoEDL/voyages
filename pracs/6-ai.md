# Voyages 6 Indigenous AI

In this activity we will build the Hua Ki'i prototype AI image recognition app and consider what is required to adapt it with another language community.

Hua Ki'i was developed during a series of Indigenous Protocols and Artificial Intelligence workshops in 2019, by a team of Indigenous engineers, scholars and language activists. The app was built with a goal of developing an Indigenous language revitalisation tool. Hua Ki'i uses an object recognition system and translates the image detection results into Hawaiian. The app is easily remixed for another language, and is a great platform for exposing the bias in AI.

For more information about the background to Hua Ki'i and an introduction to Indigenous Protocols, read the Indigenous AI position paper. 
https://www.indigenous-ai.net/position-paper/


The activity is in two parts. First build the app, then train an object detection system to gain insight into the limitations that current technologies have for recognising culturally specific objects for many of the world's communities.

# Hua Ki'i

* Fork the code from https://github.com/rngwlf/hua_kii
* Follow the repo readme to set up page publishing for your forked code. 
* Remove the docs/CNAME file to avoid build errors.
* Update the dictionary file with a language of your choice. Use a language you know, or have access to a dictionary of terms.
* How can this be done efficiently/effectively/appropriately?
* How well does the target language dictionary match the source dictionary? Are any terms missing? 
* Commit the updated dictionary to update the app.
* May need to force refresh the app browser to get the updated version. 
* Does anyone want to add data versioning to the code to bust browser caching? 
* Access the app at https://YOURUSERNAME.github.io/hua_kii/ 
* If its not working, check if your device/browser has permission to use the camera.

What are some things to consider if wanting to make this with an Indigenous community in Australia?



# YOLOv5

The prototype app is limited in recognising particular objects from common categories. A bias in AI is that the categories and objects that are recognised are not always culturally relevant for a community who wants to build their own.

What is required to develop a localised object detection system? Many of the considerations here apply for speech/sign recongition, translation and language generation.


## Datasets

Publicly available datasets:

*COCO*
* https://cocodataset.org/#explore
* Commonly used for image recognition/object detection  
* Look at the [license/terms of use](https://cocodataset.org/#termsofuse)

*CIFAR*
* https://www.cs.toronto.edu/~kriz/cifar.html
* CIFAR-10: 60,000 images 10 classes  
* CIFAR-100: 100 classes containing 600 images each


## Data quality control

Clean and high-quality data is critical. Some tools exist for finding annotation mistakes, verifying models and looking at subsets of data. Eg.
https://voxel51.com/docs/fiftyone/


## Make your own dataset

Datasets can be created from scratch by taking photos/scanning  culturally relevant objects. Another approach is to bulk download images from online services such as Google/Flickr.
* Bulk download Google images: https://imgdownloader.com/
* https://flickr.com
* https://pixabay.com


## Image prep

Training object detection typically requires matching image sizes in the training data. Bulk resizing is required using tools such as [Imagemagick](https://imagemagick.org/script/mogrify.php).


## Image Labelling

A dataset of images requires labelling/annotation with polygon or rectangle shapes before training. 

Read about different types of [image annotation](https://viso.ai/computer-vision/image-annotation/). 

There are many tools that can be used to label images, including:

* [FastAnnotationSingleObject](https://github.com/udaypk/FastAnnotationSingleObject)  
Claims being able to label approx 6000 images over 8hours, is this realistic? Raccoon dataset was 2 hrs for 200 images.

* [FastAnnotationTool](https://github.com/christopher5106/FastAnnotationTool)

* [labelImg](https://github.com/tzutalin/labelImg) is a classic

* [Make sense](https://www.makesense.ai/)  
Great interface, YOLO format is not v5 so would need to be converted. [Here's a blog about it](https://towardsdatascience.com/annotate-your-image-using-online-annotation-tool-52d0a742daff).

* [Roboflow](https://app.roboflow.com/)  
Has a good annotation/training interface, some existing datasets, exports in YOLOv5 format

In the prac we won't have time to label a large dataset, but let's try downloading some images from Google and label them using Roboflow. 

## Training

Use the [Colab](https://colab.research.google.com/drive/1yW1lu7-NFU9iL_N63B5Mp6FC8rjuGqud?usp=sharing) to train YOLOv5 with the [racoon data](https://github.com/datitran/raccoon_dataset
).

* Train with 100 epochs (15min) to check the code works.
* Detect on the test images. Did it recognise anything? Try decreasing the confidence value.
* Retrain with more than 500 epochs to improve quality. BTW, 1000 epochs took 1h 20min for me.
* Detect on the test images again. Adjust the conf value.
What did it recognise now?

If you are super keen, try training a koala recogniser! What would be involved? How long do you think it would take?



# Other demos

* Pretraining https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data
```
python train.py --img 640 --batch 16 --epochs 3 --data coco128.yaml --weights yolov5s.pt
```

* Mean average precision
https://blog.roboflow.com/mean-average-precision/

* https://colab.research.google.com/github/ultralytics/yolov5/blob/master/tutorial.ipynb#scrollTo=Knxi2ncxWffW

* https://medium.com/analytics-vidhya/train-a-custom-yolov4-object-detector-using-google-colab-61a659d4868

* https://towardsdatascience.com/how-to-train-your-own-object-detector-with-tensorflows-object-detector-api-bec72ecfe1d9

* https://blog.roboflow.com/how-to-train-yolov5-on-a-custom-dataset/

* zero-shot https://github.com/openai/CLIP




