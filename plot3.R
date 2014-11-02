#Loading electricity data

#setwd("/To/Director")
data1<-read.table("household_power_consumption.txt", sep=';', colClasses=c("character", "character" ), header=T)
data1$Date<-strptime(paste(data1$Date, data1$Time), "%d/%m/%Y %H:%M:%S")
data2<-subset(data1, data1$Date >= as.POSIXlt('2007-02-01 00:00:00') & data1$Date < as.POSIXlt('2007-02-02 00:00:00'))

#plotting the Global Active Power histogram
png("plot3.png")
with(data2, plot(data2$Date, data2$Sub_metering_1,xlab="Datetime", ylab="Energy sub metering"), type="n")
with(data2, lines(data2$Date, data2$Sub_metering_1, "l"))
with(data2, points(data2$Date, data2$Sub_metering_2,  "l", col="red"))
with(data2, points(data2$Date, data2$Sub_metering_3, "l", col="blue"))
legend("topright", pch="-", col=c("black", "red", "blue"), legend=c("submeter1", "submeter2", "submeter3"))
dev.off()