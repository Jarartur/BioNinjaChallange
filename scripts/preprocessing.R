data <- read.csv("zmergowane_pliki.csv",sep = ";")


#library("trio")
#library("dplyr")
library("snpStats")

ped <- trio::read.pedfile("raw_data/BioNinjaHack_obesity.ped", first.row = NA,
             coded = NULL, naVal = 0, sep = " ",
             p2g = FALSE, non.rs.IDs = FALSE, cols4ID=FALSE)

merge <- cbind(data, ped)
merge2 <- subset(merge, log_BMI != -9)

write.table(merge2, file = "final.csv", sep = ";", quote = FALSE, row.names = FALSE, col.names = TRUE)

#Program to chsquare test
# fam <- '/BioNinjaHack_obesity.fam'
# bim <- 'raw_data/BioNinjaHack_obesity2.bim'
# bed <- 'raw_data/BioNinjaHack_obesity.bed'
# sample <- read.plink(bed, bim, fam)
# bim2 <- read.csv(bim, sep = '\t', header = FALSE)
# bim2 <- bim2 %>% distinct(V2, .keep_all = TRUE)
# write.table(merge, file = "raw_data/BioNinjaHack_obesity2.bim", sep = "\t", quote = FALSE, row.names = FALSE, col.names = FALSE)



