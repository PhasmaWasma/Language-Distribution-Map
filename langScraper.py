#program designed to scrape data from https://www.cia.gov/the-world-factbook/field/languages/ 

#program should return a dictionary 'lanData', with countries as the key and dictionaries as the values.
#nested dictionaries will have the format of language as the key, and percent speakers as the value

import requests
import json 

def fetch_cia_world_factbook_data():
    url = 'https://raw.githubusercontent.com/iancoleman/cia_world_factbook_api/master/data/factbook.json'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
        
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

def create_language_dictionary(data):
    lanData = {}

    for country, country_data in data['countries'].items():
        lanData[country] = {}
        addlist = []
        #print(f'country: {country}')
        try:
            for data in country_data['data']['people']['languages']['language']:
                addlist.append(data)
        except:
            pass
        
        lanData[country] = addlist
        
    with open(f"language_data.json", "w") as write_file:
        json.dump(lanData, write_file, separators=(',', ':'))

    print("Language Data JSON Exported")

    return lanData

def main():
    factbook_data = fetch_cia_world_factbook_data()

    if factbook_data:
        #print("running 1")
        language_dictionary = create_language_dictionary(factbook_data)
        print(f"finished product: {language_dictionary}")

if __name__ == "__main__":
    main()
