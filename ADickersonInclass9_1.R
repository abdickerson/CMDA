#Austin Dickerson
#In-Class 9-1

getwd()
setwd("C:\\Users\\Austin\\Desktop\\Virginia Tech\\CS 3654\\CMDA")
load('fdata.RData')
attach(final)
model1 <- glm(disorder ~ som1 + som2 + som3 + som4 + som5, family = "binomial")
model1
#The most important features are som1, som3, and som4
#It interprets som1 as 0.5215, which means it sees it somewhat likely to be able
#to predict the disorder
model2 <- glm(disorder ~ som6 + som7 + som8 + som9, family = "binomial")
model2
#The most important features in this model are som7
model3 <- glm(disorder ~ som10 + som11 + som12 + som13 + som14, family = "binomial")
model3
#The most important features in this model are som12

#I would say that model1 is most likely to be able to predict the disorder because
#it had the most significant features in it.