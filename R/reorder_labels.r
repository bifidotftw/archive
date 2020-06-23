'''
ggpubr sorts x-axis according to the label order (default: alphabetically)
-> To reorder x-axis labels have to be reordered

data$x-column has to be ordered in the desired way
'''

data$x-column <- factor(data$x-column, labels=unique(data$x-column))
