import requests
#import random
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('HOTBITS_TOKEN')

# Hotbits API endpoint
url = "https://www.fourmilab.ch/cgi-bin/Hotbits.api"
url2 = "https://bible-api.com/?random=verse"

# API key for Hotbits
api_key = TOKEN

# Number of random bytes to request
num_bytes = 2

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
    
def TorahSays():
    torah = {
            "Genesis": [31,25,24,26,32,22,24,22,29,32,32,20,18,24,21,16,27,33,38,18,34,24,20,67,34,35,46,22,35,43,55,32,20,31,29,43,36,30,23,23,57,38,34,34,28,34,31,22,33,26],
            "Exodus": [22,25,22,31,23,30,25,32,35,29,10,51,22,31,27,36,16,27,25,26,36,31,33,18,40,37,21,43,46,38,18,35,23,35,35,38,29,31,43,38],
            "Leviticus": [17,16,17,35,19,30,38,36,24,20,47,8,59,57,33,34,16,30,37,27,24,33,44,23,55,46,34],
            "Numbers": [54,34,51,49,31,27,89,26,23,36,35,16,33,45,41,50,13,32,22,29,35,41,30,25,18,65,23,31,40,16,54,42,56,29,34,13],
            "Deuteronomy": [46,37,29,49,33,25,26,20,29,22,32,32,18,29,23,22,20,22,21,20,23,30,25,22,19,19,26,69,28,20,30,52,29,12]
        }

    # Randomly pick book, chapter, verse
    book = random.choice(list(torah.keys()))
    chapter_number = random.randint(1, len(torah[book]))
    verse_number = random.randint(1, torah[book][chapter_number - 1])

    # Query Sefaria API
    ref = f"{book}.{chapter_number}.{verse_number}"
    url = f"https://www.sefaria.org/api/texts/{ref}?context=0"
    response = requests.get(url)

    # Check response status
    if response.status_code != 200:  # <-- single line status check
        return f"Error: API request failed with status {response.status_code}"

    data = response.json()
    verse = data["text"]
    #print(url)

    # Format output like your Quran program
    output = f"Book {book} | Chapter {chapter_number}: Verse {verse_number}\n{verse}"
    #print(output)
    return output


