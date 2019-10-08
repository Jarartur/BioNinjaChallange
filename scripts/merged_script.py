import pandas as pd
import os

#load data
BioNinjaHack_obesityBIM = pd.read_csv('C:\\Users\\ubunt\\OneDrive\\Pulpit\\Biohackaton\Otylosc\\BioNinjaHack_obesity.bim', sep = '\t', header = None)
BioNinjaHack_obesityFAM = pd.read_csv('C:\\Users\\ubunt\\OneDrive\\Pulpit\\Biohackaton\Otylosc\\BioNinjaHack_obesity.fam', sep = '\t', header = None)
BioNinjaHack_obesityMAP = pd.read_csv('C:\\Users\\ubunt\\OneDrive\\Pulpit\\Biohackaton\Otylosc\\obesity_bioninjahack.map', sep = '\t', header = None)
BMI_excel = pd.read_excel('C:\\Users\\ubunt\\OneDrive\\Pulpit\\Biohackaton\Otylosc\\Pheno_log_BMI_zakodowany.xlsx',index_col=None)
AGE_excel = pd.read_excel('C:\\Users\\ubunt\\OneDrive\\Pulpit\\Biohackaton\Otylosc\\Pheno_SEX_AGE_ZAKODOWANE.xlsx',index_col=None)
BioNinjaHack_obesityPED = pd.read_csv('C:\\Users\\ubunt\\OneDrive\\Pulpit\\Biohackaton\Otylosc\\BioNinjaHack_obesity.ped', sep = ' ',header = None)


#Rename cols
BioNinjaHack_obesityBIM = BioNinjaHack_obesityBIM.rename(columns={0: "chr", 1: "snp_id", 2: "position", 3: "koordynaty_w_parach", 4: "Allel1", 5: "Allel2"})
BioNinjaHack_obesityFAM = BioNinjaHack_obesityFAM.rename(columns={0: "FamilyID", 1: "IID", 2: "fatherID", 3: "motherID", 4: "sex", 5: "Phenotype"})
BioNinjaHack_obesityPED = BioNinjaHack_obesityPED.rename(columns={0: "FamilyID", 1: "IID", 2: "fatherID", 3: "motherID", 4: "sex", 5: "Phenotype"})





#Merging after IID
MergedData = pd.DataFrame().copy()
df = pd.merge(BMI_excel, AGE_excel, left_on=['IID'], right_on=['IID'], how='outer')

MergedData = df[['FID_x','IID','log_BMI','SEX_y','AGE',]]

#save to csv
MergedData.to_csv('ZmergowanePliki.csv', sep = ';', index=False )


