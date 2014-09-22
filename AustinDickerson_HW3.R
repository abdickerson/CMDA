#Austin Dickerson
# HW 3
#There has been some discrepency over what dataset we are going to use, but
#for this assignment I am using offensive statistics for D1 college football teams,
#data from espn.com

getwd()
setwd("C:\\Users\\Austin\\Desktop\\Virginia Tech\\CS 3654\\CMDA")

offensedata = read.table('CollegeOffense.csv', sep = ',', header = T)
offensedata
names(offensedata)
#Everything seems ok with this
summary(offensedata$RK)
#A summary really isn't necessary here, since it just lists all the schools in D1 football
summary(offensedata$TEAM)
#Everything also seems ok here
summary(offensedata$YDS)
#Also seems good
summary(offensedata$YDS.G)
#Also seems ok
summary(offensedata$PASS)
#Nothing unusual about this summary
summary(offensedata$P.YDS.G)
#Also seems good
summary(offensedata$RUSH)
#Also seems ok
summary(offensedata$R.YDS.G)
#Also seems good, nothing unusual
summary(offensedata$PTS)
#Also seems ok
summary(offensedata$PTS.G)

library(ggplot2)
#Using a histogram to show the districution of rushing yards per game.
ggplot(footballdata) + geom_histogram(aes(x=R.YDS.G), binwidth=25) + theme_bw()
#Using a scatterplot to show rushing yards per game and points per game
ggplot(footballdata, aes(x=R.YDS.G,y=PTS.G)) + geom_point() + ylim(0,100) + theme_bw() + ggtitle("Scatterplot of Points per game and rushing yards per game")
#Using a scatterplot to show relationship between total points and total yards
ggplot(footballdata, aes(x=YDS.G,y=PTS)) + geom_point() + ylim(0,100) + theme_bw() + ggtitle("Scatterplot of total points and total yards")
