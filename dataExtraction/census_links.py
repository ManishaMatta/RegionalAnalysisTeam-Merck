# python /Users/Manisha/Documents/MS/SDSU/research/HDMA/Merk/RegionalAnalysisTeam-Merk/dataExtraction/census_links.py

from urllib import request
import json
from pprint import pprint
import csv
import pandas as pd



census_api_key = '8b65739ad0c20b9927ef543003f60de1f640de4e'

def execute(url_str,file_name):
    response = request.urlopen(url_str) # read the response into computer
    html_str = response.read().decode("utf-8") # convert the response into string
    if (html_str):
        dList=[]
        json_data = json.loads(html_str) # convert the string into json
        # print (json_data[0])
        dList.append(json_data[0])
        for i in json_data[1:]:
            dList.append(i)
        file = open(file_name+'.csv', 'w+', newline ='')
        with file:    
            write = csv.writer(file)
            write.writerows(dList)

# url_EconomicCensus_2017_1 = 'https://api.census.gov/data/2017/ecnbasic?get=GEO_ID,NAME,SECTOR,EMP,ESTAB,FIRM,TYPOP&for=state:*&key='+census_api_key
# execute(url_EconomicCensus_2017_1,'/Users/Manisha/Documents/MS/SDSU/research/HDMA/Merk/datasets/EconomicCensus_2017_1')
# url_EconomicCensus_2017_2 = 'https://api.census.gov/data/2017/ecnbasic?get=GEO_ID,NAME,SECTOR,EMP,ESTAB,FIRM,TYPOP&for=county:*&key='+census_api_key # NW
# execute(url_EconomicCensus_2017_2,'/Users/Manisha/Documents/MS/SDSU/research/HDMA/Merk/datasets/EconomicCensus_2017_2')
# url_EconomicCensus_2022_1 = 'https://api.census.gov/data/2017/ecnbasic?get=GEO_ID,NAME,SECTOR,EMP,ESTAB,FIRM,TYPOP&for=us:*&key='+census_api_key
# execute(url_EconomicCensus_2022_1,'/Users/Manisha/Documents/MS/SDSU/research/HDMA/Merk/datasets/EconomicCensus_2022')

# url_PopulationEstimates_2021_1 = 'https://api.census.gov/data/2021/pep/population?get=GEO_ID,NAME,STATE,REGION,DIVISION,UNIVERSE,FUNCSTAT,DENSITY_2021,POP_2021,SUMLEVEL&for=state:*&key='+census_api_key
# execute(url_PopulationEstimates_2021_1,'/Users/Manisha/Documents/MS/SDSU/research/HDMA/Merk/datasets/PopulationEstimates_2021')
# url_NationalMonthlyPopulation_2021_1='https://api.census.gov/data/2021/pep/natmonthly?get=GEO_ID,GEOCOMP,NAME,NATION,UNIVERSE,AGE,HISP,RACE,SEX,POP,SUMLEVEL,MONTHLY&for=us:*&key='+census_api_key
# execute(url_NationalMonthlyPopulation_2021_1,'/Users/Manisha/Documents/MS/SDSU/research/HDMA/Merk/datasets/NationalMonthlyPopulation_2021')

# url_ACS1_2021='https://api.census.gov/data/2021/acs/acs1?get=GEO_ID,GEOCOMP,NAME,B24022_060E,B08201_001E&for=us:*&key='+census_api_key
attributes_1="""B01001_001E,B01001_002E,B01001_026E,B02001_002E,B02001_003E,B02001_005E,B02001_004E,B02001_006E,B02001_007E,B03003_003E,B12001_004E,B12001_013E,B19123_002E,B17017_001E,B17017_002E,B27010_017E,B27010_033E,B27010_050E,B27010_066E,B09002_001E,C24030_018E,C24030_045E,B23025_006E,B23025_005E,B16004_001E,B16004_003E,B16004_024E,B16004_046E,B16004_025E,B16004_047E,B16004_004E,B16004_026E,B16004_048E,B16004_014E,B16004_036E"""
attributes_2="""B16004_058E,B16004_019E,B16004_041E,B16004_063E,B01001_003E,B01001_004E,B01001_005E,B01001_006E,B01001_007E,B01001_008E,B01001_009E,B01001_010E,B01001_011E,B01001_012E,B01001_013E,B01001_014E,B01001_015E,B01001_016E,B01001_017E,B01001_018E,B01001_019E,B01001_020E,B01001_021E,B01001_022E,B01001_023E,B01001_024E,B01001_025E,B01001_027E,B01001_028E,B01001_029E,B01001_030E,B01001_031E,B01001_032E,B01001_033E,B01001_034E"""
attributes_3="""B01001_035E,B01001_036E,B01001_037E,B01001_038E,B01001_039E,B01001_040E,B01001_041E,B01001_042E,B01001_043E,B01001_044E,B01001_045E,B01001_046E,B01001_047E,B01001_048E,B01001_049E,B15003_001E,B15003_002E,B15003_003E,B15003_004E,B15003_005E,B15003_006E,B15003_007E,B15003_008E,B15003_009E,B15003_010E,B15003_011E,B15003_012E,B15003_013E,B15003_014E,B15003_015E,B15003_016E,B15003_017E,B15003_018E,B15003_019E,B15003_020E"""
attributes_4="""B15003_021E,B15003_022E,B15003_023E,B18135_003E,B18135_014E,B18135_025E,B19113_001E,B05002_013E,B25010_001E"""
for i in range(1,5):
    url_ACS5_2022=f'https://api.census.gov/data/2022/acs/acs5?get=GEO_ID,GEOCOMP,NAME,{globals()[f"attributes_{i}"]}&for=zip%20code%20tabulation%20area:*&key='+census_api_key
    print(url_ACS5_2022)
    # execute(url_ACS5_2022,f'/Users/Manisha/Documents/MS/SDSU/research/HDMA/Merk/datasets/ACS5_2022_{i}')
# /Users/Manisha/Documents/MS/SDSU/research/HDMA/Merk/datasets/ACS5_2021.csv

acs5_df_1=pd.read_csv(f"/Users/Manisha/Documents/MS/SDSU/research/HDMA/Merk/datasets/ACS5_2022_1.csv")
acs5_df_2=pd.read_csv(f"/Users/Manisha/Documents/MS/SDSU/research/HDMA/Merk/datasets/ACS5_2022_2.csv")
acs5_df_3=pd.read_csv(f"/Users/Manisha/Documents/MS/SDSU/research/HDMA/Merk/datasets/ACS5_2022_3.csv")
acs5_df_4=pd.read_csv(f"/Users/Manisha/Documents/MS/SDSU/research/HDMA/Merk/datasets/ACS5_2022_4.csv")

merged_df_1 = pd.merge(acs5_df_1, acs5_df_2, on=['GEO_ID', 'GEOCOMP', 'NAME','zip code tabulation area'], how='inner')
merged_df_2 = pd.merge(acs5_df_3, acs5_df_4, on=['GEO_ID', 'GEOCOMP', 'NAME','zip code tabulation area'], how='inner')
merged_df_3 = pd.merge(merged_df_1, merged_df_2, on=['GEO_ID', 'GEOCOMP', 'NAME','zip code tabulation area'], how='inner')
df_unique = merged_df_3.drop_duplicates(subset=['GEO_ID', 'GEOCOMP', 'NAME','zip code tabulation area'])



#  population, race,gender, poverty, labor , language, age,education, income
df_unique=df_unique.rename(columns={"B01001_001E":"Total_Population",
                                  "B01001_002E":"Male_Total_Population" ,
                                  "B01001_026E":"Female_Total_Population",
                                  "B02001_002E":"White_Total_Population",
                                  "B02001_003E":"Black_AfricanAmerican_Total_Population",
                                  "B02001_005E":"Asian_Total_Population",
                                  "B02001_004E":"AmericanIndian_AlaskaNative_Total_Population",
                                  "B02001_006E":"NativeHawaiian_OtherPacificIslander_Total_Population",
                                  "B02001_007E":"Other_Race_Total_Population",
                                  "B03003_003E":"Hispanic_Latino_Total_Population",
                                  "B12001_004E":"Married_Male",
                                  "B12001_013E":"Married_Female",
                                  "B19123_002E":"Total_households_PublicAssistance",
                                  "B17017_001E":"Poverty_Status",
                                  "B17017_002E":"Income_below_PovertyLevel",
                                  "B27010_017E":"No_HealthInsurance_Coverage_less19",
                                  "B27010_033E":"No_HealthInsurance_Coverage_19_34",
                                  "B27010_050E":"No_HealthInsurance_Coverage_35_64",
                                  "B27010_066E":"No_HealthInsurance_Coverage_more65",
                                  "B09002_001E":"Total_households_Children_Below18",
                                  "C24030_018E":"Male_Professional",
                                  "C24030_045E":"Female_Professional",
                                  "B23025_006E":"ArmedForces_LaborForce",
                                  "B23025_005E":"Unemployed_LaborForce",               
                                  "B16004_001E":"Total_English_Spoken_Home",
                                  "B16004_003E":"English_Spoken_Home_15_17",
                                  "B16004_024E":"English_Spoken_Home_18_64",
                                  "B16004_046E":"English_Spoken_Home_65more",
                                  "B16004_025E":"Only_English_Spoken_Home_18_64",
                                  "B16004_047E":"Only_English_Spoken_Home_65more",
                                  "B16004_004E":"Spanish_Spoken_Home_15_17",
                                  "B16004_026E":"Spanish_Spoken_Home_18_64",
                                  "B16004_048E":"Spanish_Spoken_Home_65more",
                                  "B16004_014E":"Asian_PacificIsland_Spoken_Home_15_17",
                                  "B16004_036E":"Asian_PacificIsland_Spoken_Home_18_64",
                                  "B16004_058E":"Asian_PacificIsland_Spoken_Home_65more",
                                  "B16004_019E":"Other_Spoken_Home_15_17",
                                  "B16004_041E":"Other_Spoken_Home_18-64",
                                  "B16004_063E":"Other_Spoken_Home_65more",
                                  "B01001_003E":"Male_Population_Less5",
                                  "B01001_004E":"Male_Population_5_9",
                                  "B01001_005E":"Male_Population_10_14",
                                  "B01001_006E":"Male_Population_15_17",
                                  "B01001_007E":"Male_Population_18_19",
                                  "B01001_008E":"Male_Population_20",
                                  "B01001_009E":"Male_Population_21",
                                  "B01001_010E":"Male_Population_22_24",
                                  "B01001_011E":"Male_Population_25_29",
                                  "B01001_012E":"Male_Population_30_34",
                                  "B01001_013E":"Male_Population_35_39",
                                  "B01001_014E":"Male_Population_40_44",
                                  "B01001_015E":"Male_Population_45_49",
                                  "B01001_016E":"Male_Population_50_54",
                                  "B01001_017E":"Male_Population_55_59",
                                  "B01001_018E":"Male_Population_60_61",
                                  "B01001_019E":"Male_Population_62_64",
                                  "B01001_020E":"Male_Population_65_66",
                                  "B01001_021E":"Male_Population_67_69",
                                  "B01001_022E":"Male_Population_70_74",
                                  "B01001_023E":"Male_Population_75_79",
                                  "B01001_024E":"Male_Population_80_84",
                                  "B01001_025E":"Male_Population_more85",
                                  "B01001_027E":"Female_Population_Less5",
                                  "B01001_028E":"Female_Population_5_9",
                                  "B01001_029E":"Female_Population_10_14",
                                  "B01001_030E":"Female_Population_15_17",
                                  "B01001_031E":"Female_Population_18_19",
                                  "B01001_032E":"Female_Population_20",
                                  "B01001_033E":"Female_Population_21",
                                  "B01001_034E":"Female_Population_22_24",
                                  "B01001_035E":"Female_Population_25_29",
                                  "B01001_036E":"Female_Population_30_34",
                                  "B01001_037E":"Female_Population_35_39",
                                  "B01001_038E":"Female_Population_40_44",
                                  "B01001_039E":"Female_Population_45_49",
                                  "B01001_040E":"Female_Population_50_54",
                                  "B01001_041E":"Female_Population_55_59",
                                  "B01001_042E":"Female_Population_60_61",
                                  "B01001_043E":"Female_Population_62_64",
                                  "B01001_044E":"Female_Population_65_66",
                                  "B01001_045E":"Female_Population_67_69",
                                  "B01001_046E":"Female_Population_70_74",
                                  "B01001_047E":"Female_Population_75_79",
                                  "B01001_048E":"Female_Population_80_84",
                                  "B01001_049E":"Female_Population_more85",
                                  "B15003_001E":"Total_EducationalAttainment_more25",
                                  "B15003_002E":"No_School_EducationalAttainment_more25",
                                  "B15003_003E":"Nursery_School_EducationalAttainment_more25",
                                  "B15003_004E":"Kindergarten_EducationalAttainment_more25",
                                  "B15003_005E":"1stGrade_EducationalAttainment_more25",
                                  "B15003_006E":"2stGrade_EducationalAttainment_more25",
                                  "B15003_007E":"3stGrade_EducationalAttainment_more25",
                                  "B15003_008E":"4stGrade_EducationalAttainment_more25",
                                  "B15003_009E":"5stGrade_EducationalAttainment_more25",
                                  "B15003_010E":"6stGrade_EducationalAttainment_more25",
                                  "B15003_011E":"7stGrade_EducationalAttainment_more25",
                                  "B15003_012E":"8stGrade_EducationalAttainment_more25",
                                  "B15003_013E":"9stGrade_EducationalAttainment_more25",
                                  "B15003_014E":"10stGrade_EducationalAttainment_more25",
                                  "B15003_015E":"11stGrade_EducationalAttainment_more25",
                                  "B15003_016E":"12stGrade_EducationalAttainment_more25",
                                  "B15003_017E":"High_School_EducationalAttainment_more25",
                                  "B15003_018E":"GED_EducationalAttainment_more25",
                                  "B15003_019E":"College_less1_EducationalAttainment_more25",
                                  "B15003_020E":"College_nodegree_EducationalAttainment_more25",
                                  "B15003_021E":"Associate_degree_EducationalAttainment_more25",
                                  "B15003_022E":"Bachelor_degree_EducationalAttainment_more25",
                                  "B15003_023E":"Master_degree_EducationalAttainment_more25",
                                  "B18135_003E":"Disability_Under19",
                                  "B18135_014E":"Disability_19_64",
                                  "B18135_025E":"Disability_Over65",
                                  "B19113_001E":"Median_family_income", 
                                  "B05002_013E":"Place_of_Birth_ Nativity_CitizenshipStatus",  
                                  "B25010_001E":"Average_Household_Size"})

df_unique.to_csv("/Users/Manisha/Documents/MS/SDSU/research/HDMA/Merk/datasets/ACS5_2022_rename.csv")
                                  
