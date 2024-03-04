# python /Users/Manisha/Documents/MS/SDSU/research/HDMA/Merk/RegionalAnalysisTeam-Merk/dataExtraction/census.py

import MyCreds
# import requests
# from census import Census
# from us import states
import censusdata
import pandas as pd

class census_dataextract:
    API = f"&key={MyCreds.api_key}"
    HOST = 'https://api.census.gov/data'

    @staticmethod
    def getCensus():
        query_url = f"{census_dataextract.HOST}{year}{dataset_acronym}{g}{variables}{location}{census_dataextract.API}"
        # Use requests package to call out to the API
        response = requests.get(query_url)
        # Convert the Response to text and print the result
        print(response.text)

def main():
    # from census import Census
    # c = Census("8b65739ad0c20b9927ef543003f60de1f640de4e")



    # c = Census(os.environ.get('census_api_key'))
    # Obtain Census variables from the 2019 ACS at the tract level for the Commonwealth of Virginia (FIPS code: 51)
# C17002_001E: count of ratio of income to poverty in the past 12 months (total)
# C17002_002E: count of ratio of income to poverty in the past 12 months (< 0.50)
# C17002_003E: count of ratio of income to poverty in the past 12 months (0.50 - 0.99)
# B01003_001E: total population
# Sources: https://api.census.gov/data/2019/acs/acs5/variables.html; https://pypi.org/project/census/
    
    # WORKING !!
    geography = [("zip code tabulation area", ["92122", "92123", "92128"])]  
    # census_data=censusdata.download("acs5",2017, censusdata.censusgeo(geography), ['NAME', 'C17002_001E', 'C17002_002E', 'C17002_003E', 'B01003_001E'], key='8b65739ad0c20b9927ef543003f60de1f640de4e')
    census_data=censusdata.download("acs5",2017, censusdata.censusgeo([('state', '36'),('county', '081'),('block group', '*')]), [ 'C17002_001E', 'C17002_002E', 'C17002_003E', 'B01003_001E'], key='8b65739ad0c20b9927ef543003f60de1f640de4e')
    print(census_data)

    census_data_hsp=censusdata.download("acs5",2017, censusdata.censusgeo([('state', '36'),('county', '081'),('block group', '*')]), [ 'C17002_001E', 'C17002_002E', 'C17002_003E', 'B01003_001E'], key='8b65739ad0c20b9927ef543003f60de1f640de4e')



    # c.API("8b65739ad0c20b9927ef543003f60de1f640de4e")
    # va_census = c.acs5.state_county_tract(fields = ('NAME', 'C17002_001E', 'C17002_002E', 'C17002_003E', 'B01003_001E'),
    #                                   state_fips = states.VA.fips,
    #                                   county_fips = "*",
    #                                   tract = "*",
    #                                   year = 2017)
    # # Create a dataframe from the census data
    # va_df = pd.DataFrame(va_census)

    # # Show the dataframe
    # print(va_df.head(2))
    # print('Shape: ', va_df.shape)

# WORKING !!
    # Household Pulse Survey: HPS00All HPS Indicators : 2023: HPS Coronavirus (COVID-19) Pandemic and Recovery
    # https://api.census.gov/data/timeseries/hps?get=SURVEY_YEAR,NAME&for=state:*&key=8b65739ad0c20b9927ef543003f60de1f640de4e
    # year = '/2022'
    # dataset_acronym = 'HPSTIMESERIES.HPS00'
    # g = '?get=vaccine'
    # variables = 'NAME,B01001_001E'
    # location = '&for=us:*'
    #     # census_dataextract.getCensus()
    # response = requests.get("https://api.census.gov/data/timeseries/hps?get=SURVEY_YEAR,NAME&for=state:*&key=8b65739ad0c20b9927ef543003f60de1f640de4e")
    # response = requests.get("https://api.census.gov/data/timeseries/hps?get=SURVEY_YEAR,NAME&for=state:*&key=8b65739ad0c20b9927ef543003f60de1f640de4e")
    # print(response.content)
    # print(response.text)
    #     # test sample => https://api.census.gov/data/2019/acs/acs1?get=NAME,B01001_001E&for=us:*&key=[YOUR API KEY]
        
    # year = '/2019'
    # dataset_acronym = '/acs/acs1'
    # g = '?get='
    # variables = 'NAME,B01001_001E'
    # location = '&for=us:*'
        

if __name__ == "__main__":
    main()
