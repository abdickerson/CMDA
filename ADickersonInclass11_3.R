#Austin Dickerson
#In-Class11_3

data(mtcars)
head(mtcars)
?mtcars
#mpg is miles per gallon, which represents the mpg of the car
#cyl is the number of cylinders in the car
#disp the displacement of the car measured in cubic inches
#hp is the gross horsepower of the car
#drat is the rear axle ratio of the car
#wt is the weight of the car
#qsec is the 1/4 mile time
#vs is the the V/S of a car
#am is the transmission(1 for manual, 0 for automatic)
#gear is the number of forward gears
#carb is the number of carburetors

knnTrain <- mtcars[,selVars]
response <- mtcars$vs > 0
install.packages('class')
library(class)

system.time(knnDecision <- knn(knnTrain,knnTrain,response,k=200,prob=T))
knnPred <- ifelse(knnDecision==TRUE,
                  attributes(knnDecision)$prob,
                  1-(attributes(knnDecision)$prob))
library(ROCR)
eval <- prediction(knnPred, response) 
auc_calc <- performance(eval,'auc')
auc_calc@y.values

f <- paste('response ~ ',paste(selVars,collapse=' + '),sep='') 
system.time(gmodel <- glm(as.formula(f),
                          data=knnTrain,
                          family=binomial(link='logit')))
log_predict <- predict(gmodel, 
                       newdata=knnTrain, 
                       type = "response")
eval <- prediction(log_predict, response) 
auc_calc <- performance(eval,'auc')
auc_calc@y.values

library(rpart)
f <- paste('response ~ ',paste(selVars,collapse=' + '),sep='')
system.time(tmodel <- rpart(f,data=mtcars,
                            control=rpart.control(cp=0.001,minsplit=1000,
                                                  minbucket=1000,maxdepth=5)))
mtcars$pred <- predict(tmodel, newdata = mtcars)
mtcars$response <- mtcars$am > 0

eval <- prediction(mtcars$pred, mtcars$response) 
auc_calc <- performance(eval,'auc')
auc_calc@y.values

mtcars$response <- mtcars$am > 0
install.packages("e1071")
library(e1071)
system.time(fit <- naiveBayes(as.formula(f), data=mtcars))
system.time(naivB_pred <- predict(fit, mtcars, type = 'raw'))
head(naivB_pred)
eval <- prediction(naivB_pred[,2], dTrain$response) 
auc_calc <- performance(eval,'auc')
auc_calc@y.values

#As far as time efficiency goes, the knn does the best, but if you account for time
#efficiency and AUC, then the logistic does the best overall. I did not run into any
#problems.
