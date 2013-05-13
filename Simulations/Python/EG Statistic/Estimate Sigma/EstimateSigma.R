library(MASS)
mydata = read.csv("PlantData.csv")
x<-fitdistr(mydata$Size,"lognormal")
print(x)