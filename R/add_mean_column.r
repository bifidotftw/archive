library(tidyverse)

data <- data %>%
	group_by($column1) %>%
	mutate(mean = mean($column2))
