from selenium import webdriver
from bs4 import BeautifulSoup
import time

def extract_quotes(soup):

    quotes = []
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
        author_url = quote.find('a')['href']
        quotes.append({'text': text, 'author': author, 'tags': tags, 'author_url': author_url})
    return quotes


def extract_author_bio(author_url):

    driver.get('https://quotes.toscrape.com' + author_url)
    # Wait for the page to load (adjust the wait time according to your webpage)
    driver.implicitly_wait(3)
    # Get the HTML content of the page after it has fully loaded
    html_content = driver.page_source    
    soup = BeautifulSoup(html_content, 'html.parser')
    author_bio = soup.find('div', class_='author-details')
    name = author_bio.find('h3', class_='author-title').get_text().strip()
    birth_date = author_bio.find('span', class_='author-born-date').get_text().strip()
    birth_place = author_bio.find('span', class_='author-born-location').get_text().strip()
    description = author_bio.find('div', class_='author-description').get_text().strip()
    return {'name': name, 'birth_date': birth_date, 'birth_place': birth_place, 'description': description}


def scrape_all_quotes():

    base_url = 'https://quotes.toscrape.com'
    page_url = '/page/1/'
    all_quotes = []

    while page_url:
        # Navigate to one URL
        driver.get(base_url + page_url)
        # Wait for the page to load (adjust the wait time according to your webpage)
        driver.implicitly_wait(3)
        # Get the HTML content of the page after it has fully loaded
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        quotes = extract_quotes(soup)
        all_quotes.extend(quotes)
        # Extract bio for each author
        for quote in quotes:
            bio = extract_author_bio(quote['author_url'])
            quote.update(bio)
            time.sleep(1)  # To avoid overwhelming the server

        # Find the next page URL
        next_page = soup.find('li', class_='next')
        if next_page:
            page_url = next_page.find('a')['href']
        else:
            page_url = None

    return all_quotes


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

# Scrape all quotes
quotes_data = scrape_all_quotes()

with open("quotes.txt", "w", encoding="utf-8") as file:
    file.write(str(quotes_data))
print("Page content has been saved to quotes.txt")

# Print the extracted quotes and author bios
for quote in quotes_data:
    print(quote)

# Close the Selenium WebDriver
driver.quit()