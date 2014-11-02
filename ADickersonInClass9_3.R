#Austin Dickerson
#InClass9-3

getwd()
setwd('C:\\Users\\Austin\\Desktop\\Virginia Tech\\CS 3654\\CMDA')
load("NatalRiskData.rData")
train <- sdata[sdata$ORIGRANDGROUP<=5,]
test <- sdata[sdata$ORIGRANDGROUP>5,]
complications <- c("ULD_MECO", "ULD_PRECIP", "ULD_BREECH")
riskfactors <- c("URF_DIAB", "URF_CHYPER", "URF_PHYPER", "URF_ECLAM")
y <- "atRisk"
x <- c("PWGT", "UPREVIS", "CIG_REC", "GESTREC3", "DPLURAL", complications, riskfactors)
fmla <- paste(y, paste(x, collapse="+"), sep="~")
print(fmla)
model <- glm(fmla, data=train, family=binomial(link="logit"))
train$pred <- predict(model, newdata=train, type="response")
test$pred <- predict(model, newdata=test, type="response")
library(ggplot2)
ggplot(train, aes(x=pred, color=atRisk)) + geom_density()
confusion.test <- table(pred=test$pred>0.5, target = test$target)
confusion.test
accuracy <- (confusion.test[2,2] + confusion.test[1,1])/sum(confusion.test[,])
accuracy 
precision <- confusion.test[2,2] / sum(confusion.test[2,])
precision
recall <- confusion.test[2,2] / sum(confusion.test[,2])
recall