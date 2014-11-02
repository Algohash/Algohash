#Author: Harisankar Namasivayam
#Loading electricity data

#setwd("/To/Director")
data1<-read.table("household_power_consumption.txt", sep=';', colClasses=c("character", "character" ), header=T)
data1$Date<-strptime(paste(data1$Date, data1$Time), "%d/%m/%Y %H:%M:%S")
data2<-subset(data1, data1$Date >= as.POSIXlt('2007-02-01 00:00:00') & data1$Date < as.POSIXlt('2007-02-02 00:00:00'))

#plotting the Global Active Power histogram
png("plot1.png")
hist(data2$Global_active_power, col="red", xlab="Global Active Power (kilowatts)", main="Global Active Power")
dev.off()
