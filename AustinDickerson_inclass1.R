#Austin Dickerson in class assignment

#set working directory to CMDA folder
getwd()
setwd("C:\\Users\\Austin\\Desktop\\Virginia Tech\\CS 3654\\CMDA")
getwd()

#Import cars1 dataset
carsdata<-read.table('cars1.csv', sep=',', header=T)

#Dimensions
dim(carsdata)
#It has 50 rows and two columns

#Assign value of [2, 2]
var1 <- carsdata[2, 2]
#Variable names are speed and distance

#Values of 1st and second columns
carsdata[,1]
carsdata[,2]

#Assigning new name for first column
SPEED = carsdata[,1]
SPEED

#Retrieve values at row 15
carsdata[15,]
