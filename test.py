import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the webpage to scrape
url = "https://slang.in.th"

# Send an HTTP GET request to the URL
response = requests.get(url)
# print(response.text)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    find_word = soup.find_all("a")

    word = []
    new_word = []
    for i in find_word:
        i = str(i).split('<a href="')
        i = str(i[-1]).split('"')
        if (str(i[0]).startswith("/term")):
            new_url = url + str(i[0])
            print(new_url)
            res = requests.get(new_url)
            if res.status_code == 200:
                new_soup = BeautifulSoup(res.text, 'html.parser')
                new_find_word = new_soup.find("div", {"class": "jsx-4271398823 value"})
                new_find_word = str(new_find_word).split('<div class="jsx-4271398823 value">')
                new_find_word = str(new_find_word[-1]).split('</div>')

                print(new_find_word[0])
                new_word.append(new_find_word[0])
                with open("slang_data.csv", "w", newline="", encoding="utf-8") as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerow(["meaning"])
                    for row in new_word:  # Skip the header row
                            print(row)
                            csv_writer.writerow([row])
        # print(i[0])
        # word.append(i[0])

    # # Create a CSV file to store the scraped data


    print("Data has been scraped and saved to slang_data.csv.")
else:
    print("Failed to retrieve the web page.")

