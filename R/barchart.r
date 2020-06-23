library(ggpubr)
library(ggsci)
library(RColorBrewer)

pdf(file='barchart.pdf')

ggbarplot(
	iris,
	x='Species',
	y='Petal.Length',
	title='Test Bar Chart',
	ylab='Size',
	add=c('mean_sd','jitter'),
	add.params=list(color='black'),
) + theme(plot.title = element_text(hjust = 0.5))

dev.off()
