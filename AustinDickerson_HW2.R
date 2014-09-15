#Austin Dickerson
#9/14/14
#HW 2

setwd("C:\\Users\\Austin\\Desktop\\Virginia Tech\\CS 3654\\R")
load('phsample.RData')
#This dataset represents an individual person or household, with different
#variables such as personal income and occupation. The goal of this dataset is
#to predict income.
psub = subset(dpus,with(dpus, (PINCP>1000)&(ESR==1)&(PINCP<=250000)&(PERNP>1000)&(PERNP<=250000)&(WKHP>=40)&(AGEP>=20)&(AGEP<=50)&(PWGTP1>0)&COW %in% (1:7))&(SCHL %in% (1:24)))
#This creates a subset of data that matches detailed employment conditions
psub$SEX = as.factor(ifelse(psub$SEX==1, 'M', 'F'))
#This reencodes sex from 1/2 to M/F
psub$SEX = relevel(psub$SEX, 'M')
#This makes the reference sex M, so F encodes a difference form M in models
cowmap <- c("Employee of a private for-profit", 
            "Private not-for-profit employee", 
            "Local government employee", 
            "State government employee", 
            "Federal government employee", 
            "Self-employed not incorporated", 
            "Self-employed incorporated")
psub$COW = as.factor(cowmap[psub$COW])
psub$COW = relevel(psub$COW, cowmap[1])
#This reencodes the class of a worker's information into something more
#readable format
schlmap = c(
  rep("no high school diploma", 15), 
  "Regular high school diploma", 
  "GED or alternative credential", 
  "some college credit, no degree", 
  "some college credit, no degree", 
  "Associate's degree", 
  "Bachelor's degree",
  "Master's degree", 
  "Professional degree", 
  "Doctorate degree")
#This reencodes the education information into a more readable format with
#fewer levels
psub$SCHL = as.factor(schlmap[psub$SCHL])
psub$SCHL = relevel(psub$SCHL, schlmap[1])
dtrain = subset(psub, ORIGRANDGROUP >= 500)
#This creates a subset of data rows that are used for model training
dtest = subset(psub, ORIGRANDGROUP < 500)
#This creates a subset of data rows that are used for model testing
summary(dtrain$COW)
#This simply checks to make sure what we did earlier worked


url <- "http://www.repole.com/sun4cast/stats/cfb20130907.xml"
dataprob4 <- xmlToDataFrame(url)
