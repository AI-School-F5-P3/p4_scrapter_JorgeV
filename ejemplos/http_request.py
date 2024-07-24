import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"

# Step 1: Send a GET request to the specified URL
response = requests.get(url)

# Step 2: Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Save the HTML content to a text file for reference
with open("quotes_http_request.txt", "w", encoding="utf-8") as file:
    file.write(str(soup))
print("Page content has been saved to quotes_http_request.txt")


# Step 4: Extract movie data from the parsed HTML and store it in a list
movies_data = []
for movie in soup.find_all('div', class_='lister-item-content'):
    title = movie.find('a').text
    genre = movie.find('span', class_='genre').text.strip()
    stars = movie.find('div', class_='ipl-rating-star').find('span', class_='ipl-rating-star__rating').text
    runtime = movie.find('span', class_='runtime').text
    rating = movie.find('span', class_='ipl-rating-star__rating').text
    movies_data.append([title, genre, stars, runtime, rating])

# Step 5: Create a Pandas DataFrame from the extracted movie data
df = pd.DataFrame(movies_data, columns=['Title', 'Genre', 'Stars', 'Runtime', 'Rating'])

# Display the resulting DataFrame
df
