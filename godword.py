import requests
#import random
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('HOTBITS_TOKEN')

# Hotbits API endpoint
url = "https://www.fourmilab.ch/cgi-bin/Hotbits.api"
url2 = "https://bible-api.com/?random=verse"
#url3 = "https://www.sefaria.org/api/texts/random"
# API key for Hotbits
api_key = TOKEN

# Number of random bytes to request
num_bytes = 2
"""
def TorahSays():
    headers = {"accept": "application/json"}
    response = requests.get(url3, headers=headers)
    print(response.text)
"""
def BibleSays():
    # Send a GET request to the URL
    response = requests.get(url2)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the verse details from the JSON
        verse_data = data.get("verses", [{}])[0]  # Get the first verse from the list

        # Extract the relevant fields
        book_name = verse_data.get('book_name', 'Unknown Book')
        chapter_number = verse_data.get('chapter', 'Unknown Chapter')
        verse_number = verse_data.get('verse', 'Unknown Verse')
        verse_text = verse_data.get('text', 'No text available')

        # Format the output as per the required style
        output = f"Book: {book_name} | Chapter {chapter_number}: Verse {verse_number}\n{verse_text}"

        # Print the formatted output
        return output
    else:
        print("Failed to fetch data from the API.")

def GodSays(): 
    # Request random bytes from Hotbits API
    response = requests.get(url, params={"n": num_bytes, "fmt": "json", "apikey": api_key})

    # Extract the random bytes from the response
    bytes = response.json()["data"]

    # Convert the bytes to an integer between 1 and 6348
    random_number = int.from_bytes(bytes, "big") % 6348 + 1

    # Print the random number
    #print(random_number)

    # Build the API URL with the random number
    url2 = "https://api.alquran.cloud/v1/ayah/" + str(random_number) + "/en.asad"

    # Make a GET request to the URL
    response2 = requests.get(url2)

    # Check if the request was successful (status code 200)
    if response2.status_code == 200:
        # Print the verse text
        verse = response2.json()["data"]["text"]
        #print(verse)
        verse_number = response2.json()["data"]["numberInSurah"]
        chapter_number = response2.json()["data"]["surah"]["number"]

        chapter_name = response2.json()["data"]["surah"]["englishName"]
        chapter_name_eng = response2.json()["data"]["surah"]["englishNameTranslation"]

        output = "Surah " + str(chapter_number) + " | " + chapter_name +  " | " + chapter_name_eng + ": Verse " + str(verse_number) + "\n" + verse
        return output
    else:
        #print("Error: Failed to fetch verse from API")\
        output = "Something went wrong. I have logged the problem."
        return 
    
