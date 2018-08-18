'''Hello!
This code is part of a project undertaken at the Center for Ecological Sciences, Indian Institute of Science, Bengaluru.
This project is being undertaken at the Guttal Lab, in association with Sumithra Shankaran and Professor Vishwesha Guttal.

Brief Introduction:
- This code is used to detect different types of alga in the frame.
- Primarily used for analysis and conservation purposes.
- The code is written entirely in Python (for now).
- The code is written entirely from scratch.

Cheers
Sarthak J Shetty
25/07/2018'''

#cv2 is OpenCV which will be used to carry out pixel modification
import cv2
#DataFrame building is carried out using pandas
import pandas as pd
#numpy is used to modify arrays and generate arrays as and when required
import numpy as np
#argparse is used to manage the input arguments
import argparse
#Importing the library to extract time
from datetime import datetime
#Importing os here to make a status_logger folder and .txt file
import os

def pre_processing():
	'''These set of instructions are the preliminary codes that have to be run to obtain the program start
	times and the log_name

	This function makes the directories required for the status_logger(), image_dumper() & dataframe_dumper()'''

	'''The log_name is used as a common reference for the session'''
	log_name = str(datetime.now().date())+"_"+str(datetime.now().time().hour)+"_"+str(datetime.now().time().minute)
	
	if not os.path.exists("Data_Logs"):
		os.makedirs("Data_Logs")
	
	#Location of the entire data_dump
	data_dump_path = "Data_Logs/"+"Data_Logs"+"_"+log_name
	if not os.path.exists(data_dump_path):
		os.makedirs(data_dump_path)

	#Location of the session image dumps
	image_dump_path = "Data_Logs/"+"Data_Logs"+"_"+log_name+"/"+"Image_Dump"
	if not os.path.exists(image_dump_path):
		os.makedirs(image_dump_path)
	
	#Location of the session status log
	status_log_dump_path = "Data_Logs"+"/"+"Data_Logs"+"_"+log_name+"/"+"Status_Log"
	if not os.path.exists(status_log_dump_path):
		os.makedirs(status_log_dump_path)
		log = open(status_log_dump_path+"/"+"StatusLog"+".txt", 'a')
		log.write("Session:"+str(datetime.now().day)+'/'+str(datetime.now().month)+'/'+str(datetime.now().year)+"\n")
		log.write("Time:"+str(datetime.now().time().hour)+":"+str(datetime.now().time().minute)+":"+str(datetime.now().time().second)+"\n"+"\n")
		log.close()

	#Location of the dataframe dumps
	dataframe_dump_path = "Data_Logs/"+"Data_Logs"+"_"+log_name+"/"+"DataFrame_Dump"
	if not os.path.exists(dataframe_dump_path):
		os.makedirs(dataframe_dump_path)

	return log_name, image_dump_path, status_log_dump_path, dataframe_dump_path

def status_logger(status_key):
	'''This function serves as a status logger, where each function referenced is
	noted and passed onto a .txt file, where it can be referred to for future purposes.
	Basically the print function within each function will be logged.

	A status_key is a unique string assigned to each function, that is passed onto the status logger
	log_name is the name given to the entire session, obtained from the time when the process starts'''
	print(status_key)
	log = open(status_log_dump_path+"/"+"StatusLog"+".txt", 'a')
	log.write(str(datetime.now().time().hour)+":"+str(datetime.now().time().minute)+":"+str(datetime.now().time().second)+status_key+"\n")
	log.close()

def program_start(log_name):
	'''This function is used to denote the start of the program in the StatsLog of the session'''
	start_status_key = "[INFO] Program Session"+":"+" "+log_name+" "+"Status: Start"+"\n"
	status_logger(start_status_key)

def program_end(log_name):
	'''This function is used to denote the successful end of the program in the StatsLog of the session'''
	print("\n")
	end_status_key = "[INFO] Program Session"+":"+" "+log_name+" "+"Status: End"
	status_logger(end_status_key)

def parser():
	'''This is an argument parsing function
	It reads the file that has to be analyzed by this code
	It further compartmentalizes the code, makes it easier to debug'''
	parser_status_key = "[INFO] Parser has obtained filename"
	status_logger(parser_status_key)

	parser = argparse.ArgumentParser()
	parser.add_argument("--file_name", help="image-to-analyze")
	#parser.add_argument("--algal_color", help="color-of-algae-to-detect", type=str)
	args = parser.parse_args()
	if args.file_name:
		file_name = args.file_name
		parser_status_key="[INFO]  Image name:"+" "+file_name+"\n"
		status_logger(parser_status_key)
		return file_name

	parser_status_key = "[INFO] Parser has passed on"+" "+file_name
	status_logger(parser_status_key)

def image_viewer(image):
	'''Instead of repetitively writing code to view image
	Function to view the file here has been written'''

	image_viewer_status_key = "[INFO] Image window is open"
	status_logger(image_viewer_status_key)

	cv2.imshow("Image",image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	image_viewer_status_key = "[INFO] Image window has been closed"
	status_logger(image_viewer_status_key)
	return image

def image_reader(file_name, label):
	'''Preprocessing statements
	Enter the file here'''

	image_reader_status_key = "[INFO]"+" "+label+" "+"has been identified on disc"
	status_logger(image_reader_status_key)
	
	image = cv2.imread(file_name)
	image_dumper(image, label)
	image_reader_status_key = "[INFO]"+" "+label+" "+"has been passed on"
	status_logger(image_reader_status_key)
	return image

def image_dumper(image, label):
	'''Instead of calling OpenCV multiple times, we write one function and call it multiple times
	This image is used to write the image to the disk, so that it can be checked
	for correctness and analysis'''
	
	image_dumper_status_key = "[INFO]"+" "+label+" "+"image is being written to the disc"
	status_logger(image_dumper_status_key)

	cv2.imwrite(image_dump_path+"/"+label+".png",image)
	image_dumper_status_key = "[INFO]"+" "+label+" "+"image has been written to the disc"
	status_logger(image_dumper_status_key)

def image_pre_processing(image):
	image_pre_processing_status_key = "[INFO] Image is being preprocessed"
	status_logger(image_pre_processing_status_key)

	'''This function applies the Gaussian blur to the image
	Function also resizes to reduce computation cycles.
	We save the resized disk to the image so that once we integrate the findCountours()
	function, we can have the contours drawn onto the resized image, rather than the larger image.'''

	image = cv2.resize(image, (0,0), fx = 0.25, fy = 0.25)
	image_dumper(image, "Post_Resizing_Image")
	image_resize_status_key = "[INFO] Image has been resized"
	status_logger(image_resize_status_key)

	image = cv2.GaussianBlur(image, (25,25), 0)
	image_dumper(image,"Post_Processing_Image")
	image_pre_processing_status_key = "[INFO] Image has been processed for further steps"
	status_logger(image_pre_processing_status_key)

	return image

def dataframe_builder(image, label):
	'''Building a 2D dataframe using Pandas
	The dataframe will have the same dimensions as the image
	Each cell of the dataframe will contain the 1*3 matrix
	The cell will have the RGB value of the pixel'''
	dataframe_builder_status_key = "[INFO]"+" "+label+" "+"is being built"
	status_logger(dataframe_builder_status_key)
	
	dataframe = pd.DataFrame(index = np.arange(0, image.shape[0]), columns = np.arange(0, image.shape[1]))
	dataframe_viewer(dataframe, label)
	dataframe_builder_status_key = "[INFO]"+" "+label+" "+"has been built"
	status_logger(dataframe_builder_status_key)

	return dataframe

def dataframe_viewer(dataframe, label):
	dataframe_viewer_status_key = "[INFO] Viewing:"+" "+label
	status_logger(dataframe_viewer_status_key)

	'''Function to view the dataframe after each function
	to make sure that the pixel values are not modified or changed unexpectedly'''
	
	print(dataframe)

def dataframe_dumper(dataframe, label):
	dataframe_dumper_status_key = "[INFO]"+" "+label+" "+"is being dumped to disc"
	status_logger(dataframe_dumper_status_key)

	'''This function dumps the dataframe generated for each image to the disc, using the log_name and
	label as reference'''
	
	'''This function dumps the pixel data for different dataframes (either red_channel_data or )'''
	dataframe.to_csv(dataframe_dump_path+"/"+label+".csv")

	dataframe_dumper_status_key = "[INFO]"+" "+label+" "+"has been dumped to disc"
	status_logger(dataframe_dumper_status_key)

def pixel_extractor(image, dataframe):
	pixel_extractor_status_key = "[INFO] Image pixels are being transferred to dataframe"
	status_logger(pixel_extractor_status_key)

	'''The idea is to read the pixel values from the image
	Then store it in a pandas data-frame
	Import it into a .csv file for future analysis
	Devise an algorithm to determine threshold
	Compare pixel value with each, and isolate the differing ones'''
	
	for row_counter in range(0, image.shape[0]):
		for col_counter in range(0, image.shape[1]):
			dataframe.loc[row_counter][col_counter] = image[row_counter][col_counter]

	dataframe_viewer(dataframe,"Pixel_DataFrame")
	dataframe_dumper(dataframe,"Pixel_DataFrame")

	pixel_extractor_status_key = "[INFO] Image pixels have been transferred to the dataframe"
	status_logger(pixel_extractor_status_key)

	#image_viewer(image)
	return dataframe

def max_channel_value(image, dataframe):
	max_channel_value_status_key = "[INFO] Pixel channel with highest value is being extracted"
	status_logger(max_channel_value_status_key)

	'''This function determines the channel with the maximum value of a particular pixel.
	Once the channel with the maximum value has been identified, the rest of the channels are turned to 0.'''
	
	for row_counter in range(0, image.shape[0]):
		for col_counter in range(0, image.shape[1]):
			max_channel_value = np.max(dataframe.loc[row_counter][col_counter])
			for channels in range(0, len(dataframe.loc[row_counter][col_counter])):
				if((dataframe.loc[row_counter][col_counter][channels]) != max_channel_value):
					dataframe.loc[row_counter][col_counter][channels] = 0
	
	image_dumper(image,"Maximum_Channel_Value_Image")
	dataframe_viewer(dataframe, "Maximum_Channel_Value_DataFrame")
	dataframe_dumper(dataframe,"Maximum_Channel_Value_DataFrame")

	max_channel_value_status_key = "[INFO] Pixel channel with highest value have been extracted"
	status_logger(max_channel_value_status_key)

	#image_viewer(image)
	return dataframe

def red_value_determiner(image, dataframe):
	red_value_determiner_status_key = "[INFO] Entering the red_value_determiner function"
	status_logger(red_value_determiner_status_key)

	'''This function retains only the pixels that are red in color.
	Every other channel is throttled to 0.'''
	
	for row_counter in range(0, image.shape[0]):
		for col_counter in range(0, image.shape[1]):
			for channel in range(0, len(dataframe.loc[row_counter][col_counter])):
					if(channel != 2):
						dataframe.loc[row_counter][col_counter][channel] = 0

	image_dumper(image, "Red_Value_Image")
	dataframe_viewer(dataframe, "Red_Value_DataFrame")
	dataframe_dumper(dataframe, "Red_Value_DataFrame")

	red_value_determiner_status_key = "[INFO] Pixels with red channel values have been captured"
	status_logger(red_value_determiner_status_key)

	#image_viewer(image)
	return dataframe

def red_value_extractor(image, dataframe):
	red_value_extractor_status_key = "[INFO] Extracting Red Channel Value"
	status_logger(red_value_extractor_status_key)

	'''This function stores the red channel values of all the pixels
	and stores it in a dataframe.
	We can run separate analysis on this later, for thresholding etc.
	Here, red_channel_data is a dataframe that provides the red channel pixel values.'''
	
	red_channel_data = dataframe_builder(image, "Red_Channel_Value_DataFrame")
	for row_counter in range(0, image.shape[0]):
		for col_counter in range(0, image.shape[1]):
			red_channel_data.loc[row_counter][col_counter] = dataframe.loc[row_counter][col_counter][2]

	dataframe_viewer(red_channel_data, "Red_Value_Extractor_DataFrame")
	dataframe_dumper(red_channel_data, "Red_Value_Extractor_DataFrame")

	red_value_extractor_status_key = "[INFO] Red Channel Value has been extracted"
	status_logger(red_value_extractor_status_key)

	return red_channel_data

def mean_calculator(image, dataframe):
	mean_calculator_status_key = "[INFO] Calculating the mean value of red pixels"
	status_logger(mean_calculator_status_key)

	'''Improvement from the previous block of code:
	The mean was being calculated over all the pixels available. Thereby hampering the mean,
	causing it to be massively reduced.  Foolishness on my part. Now we calculate the total and
	divide it over only the number of pixels that we have visited.'''

	#This value calculates the sum of the red channel of all the available pixels
	counter = 0
	#This counter determines the number of pixels that the loop has visited
	mean = 0
	#This counter determines the number of pixels that the loop has visited
	total = 0

	'''This function is designed to determine the mean value of the red.
	channel data. Pixels which possess values beyond that threshold will be classified as alga.'''
	for row_counter in range(0, image.shape[0]):
		for col_counter in range(0, image.shape[1]):
			if(dataframe.loc[row_counter][col_counter]>0):
				total = total+dataframe.loc[row_counter][col_counter]
				counter = counter+1

	counter = int(counter)
	total = int(total)
	mean = int(total/(counter))

	total_status_key = "[INFO] Sum of red pixel values: "+str(total)
	status_logger(total_status_key)

	counter_status_key = "[INFO] Number of red pixels visited: "+str(counter)
	status_logger(counter_status_key)

	mean_calculator_status_key = "[INFO] Mean value of red pixels is: "+str(mean)
	status_logger(mean_calculator_status_key)

	return mean

def classify_red_pixels(image, dataframe, mean):
	classify_red_pixels_status_key = "[INFO] Classifying pixels with red channel value greater thcan mean:"+" "+str(mean)
	status_logger(classify_red_pixels_status_key)

	'''This function is used to express only the pixels in which the value of the red channel is greater
	than the mean calculated by the mean_calculator() function'''
	for row_counter in range(0, image.shape[0]):
		for col_counter in range(0, image.shape[1]):
			if(dataframe.loc[row_counter][col_counter][2]<(mean)):
				dataframe.loc[row_counter][col_counter][2] = 0

	image_dumper(image, "Classified_Red_Pixels_Image")
	dataframe_viewer(dataframe, "Classified_Red_Pixels_DataFrame")
	dataframe_dumper(dataframe, "Classified_Red_Pixels_DataFrame")

	classify_red_pixels_status_key = "[INFO] Pixels with red channel value greater than mean have been classified"
	status_logger(classify_red_pixels_status_key)

def pre_contouring(image):
	'''The main purpose of this function is to carry out a
	series of functions on the image.
	It involves two operation:
		- Converting color to B/W
		- Threshold the image'''
	pre_contouring_status_key = "[INFO] Contours are being collected"
	status_logger(pre_contouring_status_key)

	grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	grayscale_status_key = "[INFO] Grayscale image has been dumped to disc"
	image_dumper(grayscale_image, "GrayScale_Image")
	status_logger(grayscale_status_key)

	threshold_value, thresholded_grayscale_image = cv2.threshold(grayscale_image, 0, 255, 0)
	thresholded_grayscale_image_status_key="[INFO] Thresholded grayscale image is being dumped to disc"
	image_dumper(thresholded_grayscale_image, "Thresholded_GrayScale_Image")
	status_logger(thresholded_grayscale_image_status_key)

	return threshold_value, thresholded_grayscale_image

def contouring(threshold_value, thresholded_grayscale_image):
	contouring_status_key = "[INFO] Contours are being identified from the thresholded grayscale image"
	status_logger(contouring_status_key)

	''''This function applies contours on the image passed to it
	The contours are applied based on co-ordinates passed to it
	from the pre_contouring() function'''
	thresholded_image, contours, hierarchy = cv2.findContours(thresholded_grayscale_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	pre_contouring_status_key = "[INFO] Contours have been collected"
	status_logger(pre_contouring_status_key)

	image_to_contour = image_reader(file_name, "Original_Image")
	pre_processed_image_to_contour = cv2.resize(image_to_contour, (0,0), fx=0.25, fy=0.25)

	contoured_image = cv2.drawContours(pre_processed_image_to_contour, contours, -1, (0,255,0), 2)
	image_dumper(contoured_image, "Contoured_Image")
	contoured_image_status_key = "[INFO] Image has been contoured"
	status_logger(contouring_status_key)

#Model being called beyond this

#Function to describe the log_name and also start and stop times
log_name, image_dump_path, status_log_dump_path, dataframe_dump_path = pre_processing()

#Logging the start of the program
program_start(log_name)

#Function to parse the file_name argument
file_name = parser()

#Accepts the file_name and extracts the image, bloated image_viewer file
image = image_reader(file_name, "Original_Image")

#Pre-processing functions, including resize and Gaussian blur
post_processed_image = image_pre_processing(image)

#Builds the initial dataframe, referenced directly to the image
pixel_data = dataframe_builder(post_processed_image, "Pixel_DataFrame")

#Extracts the pixels from the image and transfers them to the dataframe
pixel_data = pixel_extractor(post_processed_image, pixel_data)

#Extracts the maximum valued channel, and reduces all other values to 0
max_channel_value(post_processed_image, pixel_data)

#Retains only red channel value
red_value_determiner(post_processed_image, pixel_data)

#Captures red channel data
red_channel_data = red_value_extractor(post_processed_image, pixel_data)

#Calculates the mean and total value of the all red-value of the pixels
red_channel_mean = mean_calculator(post_processed_image, red_channel_data)

#Classifies the red pixels that lie above the calculated mean value
classify_red_pixels(post_processed_image, pixel_data, red_channel_mean)

#B/W Image is thresholded before contouring
threshold_value, thresholded_grayscale_image = pre_contouring(post_processed_image)

#Contours are determined and applied onto the 
contouring(threshold_value, thresholded_grayscale_image)

#Logging the end of the program
program_end(log_name)