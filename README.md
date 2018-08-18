# Coral Reef Analysis

This is a project undertaken at the <a href="https://teelabiisc.wordpress.com" title="TEE-Lab, IISc" target="_blank">Theoretical Ecology & Evolution Lab</a> in the <a href="http://ces.iisc.ernet.in" title="CES, IISc" target="_blank">Center for Ecological Sciences</a>, <a href="https://iisc.ac.in" title="IISc, Bengaluru" target="_blank">Indian Institute of Science</a>, for the identification of algal colonies in images of coral reefs.

:warning: <strong>Code is buggy</strong> :warning: 

## Introduction:

The code is written in Python, and makes use of packages such as <a title="Numpy" href="http://www.numpy.org/" target="_blank">numpy</a>, <a href="https://pandas.pydata.org/" title="Pandas" target="_blank">pandas</a> and <a href="https://opencv.org/" title="OpenCV" href="_blank">OpenCV</a>.

### Model Overview:

1. A ```parser()``` function is used to read input parameters from the user. The parameters used right now are ```--file_name``` and ```--color_mode```. 

	- ```--file_name``` is used to locate the image which has to be analysed.
	- ```--color_mode``` is used to specify the type of algal colony to be classified in the given sample.
	
2. The ```file_name``` argument is then passed onto the ```image_reader()``` which accepts the arguments from the ```parser()``` and extracts the image from the disc.

3.  The image is then viewed for the convenience of the user using the ```image_viewer()``` function.

4. The image is then passed onto the ```pre_processing()``` functions, which performs the following functions as mentioned:
	- ```cv2.resize()```  which is used to resize the image, making it faster to carry out computations. The image is scaled to a quarter of the origin image size, along both the axes.
	- ```cv2.GaussianBlur()``` which is used to apply a <a href="https://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html?highlight=gaussian%20blur#cv2.GaussianBlur" title="Gaussian Blur" target="_blank">Gaussian Blur</a> on the image, thereby reducing the noise levels associated with it.

5. The pandas ```dataframe``` is built next. The dimensions are equivalent to the dimensions of the image. Python passing arguments by reference. Hence, manipulation of the elements of the ```dataframe``` brings about changes in the channel values of the images.

6. The pixel information of the image is then transferred into the pandas ```dataframe``` using the ```pixel_extractor()``` function, where different operations can be run on it to modify pixel values.

7. We then apply the ```max_channel_value()``` function, to cycle through each of the pixel and then express only the channel which possess the maximum value in comparison to the rest of channels belonging to that pixel.

8. To start out, we detect the presence of red algae in the images provided, hence filter the pixels which contain only the red channel as the maximum channel value. This is done using the ```red_value_determiner()```.

9. In order to threshold and run analysis (such as regression), we transfer the pixels onto another pandas ```dataframe``` using the ```red_value_extractor()``` function.

### Results: