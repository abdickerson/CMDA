#Austin Dickerson
#Inclass11_1

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
mtcars$row.names <- mtcars$am > 0
head(mtcars$row.names)
f <- paste('row.names ~ ',paste(selVars,collapse=' + '),sep='')
tmodel <- rpart(f,data=mtcars,
                control=rpart.control(cp=0.001,minsplit=1000,
                                      minbucket=1000,maxdepth=5))
install.packages("rpart.plot")
library(rpart.plot)
prp(tmodel)
#I see that 13 of the cars have a manual transmission, the rest have automatic
#transmission
install.packages('ROCR')
library(ROCR)

mtcars$pred <- predict(tmodel, newdata = mtcars)
eval <- prediction(mtcars$pred, mtcars$row.names)

auc_calc <- performance(eval,'auc')
auc_calc@y.values