data(EuStockMarkets)
mode(EuStockMarkets)
class(EuStockMarkets)

logR = diff(log(EuStockMarkets))

pdf("quantile.pdf", width=6, height=5)
index.names = dimnames(logR)[[2]]
par(mfrow=c(2,2))
for(i in 1:4)
{
	qqnorm(logR[,i],datax=T,main=index.names[i])
	qqline(logR[,i],datax=T)
	print(shapiro.test(logR[,i]))
}
graphics.off()