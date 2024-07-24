from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# URL of the IMDb list
url = "https://www.imdb.com/list/ls566941243/"

# Set up Chrome options to run the browser in incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

# Initialize the Chrome driver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the IMDb list URL
driver.get(url)

# Wait for the page to load (adjust the wait time according to your webpage)
driver.implicitly_wait(10)

# Get the HTML content of the page after it has fully loaded
html_content = driver.page_source

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Save the HTML content to a text file for reference
with open("imdb_selenium_html.txt", "w", encoding="utf-8") as file:
    file.write(str(soup))
print("Page content has been saved to imdb_selenium_html.txt")

# Extract movie data from the parsed HTML
movies_data = []
for movie in soup.find_all('div', class_='lister-item-content'):
    title = movie.find('a').text
    genre = movie.find('span', class_='genre').text.strip()
    stars = movie.select_one('div.ipl-rating-star span.ipl-rating-star__rating').text
    runtime = movie.find('span', class_='runtime').text
    rating = movie.select_one('div.ipl-rating-star span.ipl-rating-star__rating').text
    movies_data.append([title, genre, stars, runtime, rating])

# Create a Pandas DataFrame from the collected movie data
df = pd.DataFrame(movies_data, columns=['Title', 'Genre', 'Stars', 'Runtime', 'Rating'])

# Display the resulting DataFrame
print(df)

# Close the Chrome driver
driver.quit()