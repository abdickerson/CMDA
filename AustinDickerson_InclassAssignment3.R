#Austin Dickerson
#In class Assignment 3

getwd()
setwd("C:\\Users\\Austin\\Desktop\\Virginia Tech\\CS 3654\\R")

load("exampleData1.rData")
newdata <- merge(custdata, medianincome)
norm.income <- (newdata$income/newdata$Median.Income)
summary(norm.income)
#This would be appropriate to use when you are trying to decide if you should take
#a new job in a different state, depending on what the average income in that
#state is compared to where you are now

#Split's the new dataset into a 30% training set and 70% testing set
testSet <- subset(custdata, custdata$gp <= 0.3)
trainingSet <- subset(custdata, custdata$gp > 0.3)

