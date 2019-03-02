# RGB_Feature
This is a simple demo for image retrieval based on extracting color histogram feature. I just want to do person reidentification based color histogram feature, although it didn't achieve good performance. In this repository, you can learn how to extract color histogram feature, and query an image in a dataset.\<br> 
## Note 
Reference:https://www.pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/
##  Defining image descriptor
At this phase you need to decide what aspect of the image you want to describe. Are you interested in the color of the image? The shape of an object in the image? Or do you want to characterize texture?\<br> 

In this end, we use a standard color histogram in this repository.\<br> 

The color descriptor is defined in the file "rgb_feature.py". \<br> 

## Extracting features from our own dataset
Now that we have our image descriptor defined, and extract  features (i.e. color histograms) from each image in our dataset. The process of extracting features and storing them on persistent storage is commonly called “indexing”.\<br> 

To index your dataset, you can use this command:\<br> 
`python index.py --dataset ./test_images --index index.csv` \<br>
This script shouldn’t take longer than a few seconds to run. After it is finished you will have a new file, index.csv. This file stored the image features of your dataset. \<br>
Open this file using your favorite text editor and take a look inside.\<br>
You’ll see that for each row in the .csv file, the first entry is the filename, followed by a list of numbers. These numbers are your feature vectors and are used to represent and quantify the image.

## Defining the similarity metric between two images
Now that we’ve extracted features from our dataset, we need a method to compare these features for similarity.\<br>

In this end, we use `chi-squared distance` which defined in the file "search.py". Images that have a chi-squared similarity of 0 will be deemed to be identical to each other. As the chi-squared similarity value increases, the images are considered to be less similar to each other.\<br>

## Performing a Search
In the last, the query image is referred in the file "search.py".

## Run this repository
1. `python index.py --dataset ./test_images --index index.csv`

2. `python search.py --index index1.csv --query query/0001_c1s1_002301_00.jpg --result-path ./test_images`

We will get 10 images after executing search.py, because we define limit=10 in the line 19 of file "searcher.py", you can modify the value by yourself.

#Result
query image:
![query image](https://github.com/Ixiaohuihuihui/RGB_Feature/tree/master/query/0002_c2s1_068496_01.jpg)
the search result:
[result](https://github.com/Ixiaohuihuihui/RGB_Feature/tree/master/Result)

