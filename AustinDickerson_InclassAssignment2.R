#Austin Dickerson In-class Assignment 2
#https://github.com/abdickerson/CMDA

setwd("C:\\Users\\Austin\\Desktop\\Virginia Tech\\CS 3654\\R")

load('exampleData.rData')
names(custdata)
#Individual summary statistics for each variable in dataset
summary(custdata$is.employed)
#is.empployed has missing values, which most likely means that these people are not employed
summary(custdata$income)
#income has an outlier in that it has a negative value, which could mean that person
#is in debt, but it could mean multiple things, we are not really sure what it means
summary(custdata$age)
#age has an outlier in that the highest age is 146.7, and nobody lives to be that old
summary(custdata$state.of.res)
#state.of.res has an issue with units, you are left to assume that the units are
#the number of people living in each state
summary(custdata$custid)
#custid also has an issue with units, I have no idea what these numbers represent
summary(custdata$sex)
#sex has no issues with it, everything is straight forward, either they are M or F
summary(custdata$marital.stat)
#marital.stat also has nothing wrong with it, everything is categorized, and there
#are not any NA's or outliers
summary(custdata$health.ins)
#there also appears to be nothing wrong with heatlh.ins, there are no NA's or outliers
summary(custdata$housing.type)
#housing.type has NA's, which could mean they didn't fall into any of the categories
#but we are not sure
summary(custdata$recent.move)
#recent.move also has NA's, which might mean they don't have a home, but again we
#are not sure
summary(custdata$num.vehicles)
#num.vehicles also has NA's, which probably means they do not own a car
summary(custdata$is.employed.fix1)
#is.employed.fix1 has issues, but it is confusing, I am not sure what these
#categories mean
summary(custdata$age.normalized)
#age.normalized has outliers, in that it has negative values
summary(custdata$Median.Income)
#Median.Income doesn't seem to have any issues, everything seems normal
summary(custdata$income.norm)
#income.norm has outliers in that there are negative values as its lowest value
summary(custdata$gp)
#gp has issues with units, it doesn't say what these numbers represent
summary(custdata$income.lt.30k)
#income.lt.30k has issues, I am not too sure what these categories represent
summary(custdata$age.range)
#age.range doesn't seem to have any issues, everything seems to be normal
summary(custdata$Income)
#income has NA's, which could mean they

#2
uciCar <- read.table( 'http://www.win-vector.com/dfiles/car.data.csv', sep=',', header=T)
names(uciCar)
#Observations about individual category summaries
summary(uciCar$buying)
#buying has the issue in that all the values are the same, meaning there might be
#only one value
summary(uciCar$maint)
summary(uciCar$doors)
summary(uciCar$persons)
summary(uciCar$lug_boot)
summary(uciCar$safety)
#All the above categories have the same issue where all the summary numbers are the
#same, which might mean there is only one value to summarize
summary(uciCar$rating)
#there appears to be nothing wrong with this category, everything seems to make
#sense

#3
d <- read.table(paste('http://archive.ics.uci.edu/ml/', 'machine-learning-databases/statlog/german/german.data', sep=''), header=T)
names(d) <- c('Status.of.existing.checking.account',
              'Duration.in.month', 'Credit.history', 'Purpose',
              'Credit.amount', 'Savings account/bonds',
              'Present.employment.since','Installment.rate.in.percentage.of.disposable.income',
              'Personal.status.and.sex', 'Other.debtors/guarantors',
              'Present.residence.since', 'Property', 'Age.in.years',
              'Other.installment.plans', 'Housing',
              'Number.of.existing.credits.at.this.bank', 'Job',
              'Number.of.people.being.liable.to.provide.maintenance.for',
              'Telephone', 'foreign.worker', 'Good.Loan')
mapping <- list('A11'='... < 0 DM',
                'A12'='0 <= ... < 200 DM',
                'A13'='... >= 200 DM / salary assignments for at least 1 year',
                'A14'='no checking account',
                'A30'='no credits taken/all credits paid back duly',
                'A31'='all credits at this bank paid back duly',
                'A32'='existing credits paid back duly till now',
                'A33'='delay in paying off in the past',
                'A34'='critical account/other credits existing (not at this bank)',
                'A40'='car (new)',
                'A41'='car (used)',
                'A42'='furniture/equipment',
                'A43'='radio/television',
                'A44'='domestic appliances',
                'A45'='repairs',
                'A46'='education',
                'A47'='(vacation - does not exist?)',
                'A48'='retraining',
                'A49'='business',
                'A410'='others',
                'A61'='... < 100 DM',
                'A62'='100 <= ... < 500 DM',
                'A63'='500 <= ... < 1000 DM',
                'A64'='.. >= 1000 DM',
                'A65'='unknown/ no savings account',
                'A71'='unemployed',
                'A72'='... < 1 year',
                'A73'='1 <= ... < 4 years',
                'A74'='4 <= ... < 7 years',
                'A75'='.. >= 7 years',
                'A91'='male : divorced/separated',
                'A92'='female : divorced/separated/married',
                'A93'='male : single',
                'A94'='male : married/widowed',
                'A95'='female : single',
                'A101'='none',
                'A102'='co-applicant',
                'A103'='guarantor',
                'A121'='real estate',
                'A122'='if not A121 : building society savings agreement/life insurance',
                'A123'='if not A121/A122 : car or other, not in attribute 6',
                'A124'='unknown / no property',
                'A141'='bank',
                'A142'='stores',
                'A143'='none',
                'A151'='rent',
                'A152'='own',
                'A153'='for free',
                'A171'='unemployed/ unskilled - non-resident',
                'A172'='unskilled - resident',
                'A173'='skilled employee / official',
                'A174'='management/ self-employed/highly qualified employee/ officer',
                'A191'='none',
                'A192'='yes, registered under the customers name',
                'A201'='yes',
                'A202'='no')
summary(d$Personal.status.and.sex)
#There are more males who are either single, married or widowed, than there are females
#who fall under the same categories
summary(d$Other.debtors)
#According to these numbers, more people do not take out a loan for cars than those who
#are a guarntor or co-applicant

install.packages("hexbin")
library(hexbin)
help(package=hexbin)
names(custdata)
custdata2 <- subset(custdata,
                    (custdata$age > 0 & custdata$age < 100
                     & custdata$income > 0))
ggplot(custdata2, aes(x=age, y=income)) + geom_hex(binwidth=c(5, 100000))
#This, I think, better visualizes the data than the scatterplot. I think it makes it
#easier to visualize the number of people in each category over a bunch of dots on
#a graph
ggplot(custdata2, geom_bar(aes(x=income, fill=num.vehicles))) + theme_bw()+ ggtitle("Income vs Number of Vehicles")
#I used a bar graph. I noticed that the higher the income, the more vehicles that
#person owns
ggplot(custdata) + geom_bar(aes(x=income.lt.30K, fill=recent.move), position="dodge") + theme_bw()+ ggtitle("Recent moves vs Incomes less than 30K")
#I used a bar graph for this, I noticed that the recent moves were fairly balanced
#between those who do and don't have an income less than 30K