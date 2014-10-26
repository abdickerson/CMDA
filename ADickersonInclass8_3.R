#Austin Dickerson
#InClass8_3
getwd()
setwd("C:\\Users\\Austin\\Desktop\\Virginia Tech\\CS 3654\\CMDA")
data <- load('fdata.RData')
attach(data)
model <- lm(data$video ~ data$som1 + data$som2 + data$som3 + data$som4 + data$som5 + data$som6 + data$som7 + data$som8 + data$som9 + data$som10 + data$som11 + data$som12 + data$som13 + data$som14)
summary(model)
#These results show that the model is accurate in predicting the disorder score. The
#somatic features are most indicative of the physical responses in the disorder.