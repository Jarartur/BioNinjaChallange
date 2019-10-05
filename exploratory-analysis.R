Data = (K:\\bioninja_19\\Bioninjas-2019-master\\zmergowane_pliki.csv, header = True, sep = ';')

library(ggplot2)
library(dplyr)

table(Data$SEX_y) 
# 2719 male, 2824 female

hist(Data$log_BMI)
# połowa danych dotyczy osób otyłych

males <- filter(Data, Data$SEX_y == 1)
females <- filter(Data, Data$SEX_y == 2)

hist(males$log_BMI)
hist(females$log_BMI)

plot(Data$AGE, Data$log_BMI)
plot(males$AGE, males$log_BMI)
plot(females$AGE, females$log_BMI)

hist(Data$AGE)

