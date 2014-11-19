#Austin Dickerson
#InClass 12_1

library(ROCR)
library(rpart)
library(class)

names(mtcars)
head(mtcars$am)

mtcars$response <- mtcars$am > 0

install.packages('kernlab')
library(kernlab)
mSVMV <- ksvm(as.formula(f),data = mtcars, kernel = 'vanilladot') #bad kernel function
f <- paste('response ~ ',paste(selVars,collapse=' + '),sep='')

svm_pred <- predict(mSVMV, newdata = mtcars, type = 'response')
head(svm_pred)

eval <- prediction(svm_pred, mtcars$response) 
auc_calc <- performance(eval,'auc')
auc_calc@y.values

mSVMV1 <- ksvm(as.formula(f),data = mtcars, kernel = 'rbfdot') 

svm_pred1 <- predict(mSVMV1, newdata = mtcars, type = 'response')
head(svm_pred1)
eval <- prediction(svm_pred1, mtcars$response) 
auc_calc <- performance(eval,'auc')
auc_calc@y.values