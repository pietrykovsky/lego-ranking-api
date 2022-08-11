from selenium import webdriver
from bs4 import BeautifulSoup

class LegoScraper():
    """Lego webstore scrapper"""

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument(" - incognito")
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")

        self.path = "/usr/local/bin/chromedriver"

    def get_html(self, url):
        """Retreive and return html from url."""
        driver = webdriver.Chrome(self.path, chrome_options=self.options)
        driver.get(url)
        html = driver.page_source
        driver.quit()

        return html

    def scrape_themes_urls(self):
        """Return list of lego themes urls."""
        html = self.get_html('https://www.lego.com/pl-pl/themes')
        soup = BeautifulSoup(html, 'html.parser')
        list = [link.get('href') for link in soup.find_all('a', class_="CategoryLeafstyles__ImagesLink-is33yg-4")]

        return list

    def scrape_sets_urls_from_theme(self, theme_url):
        """Return list of lego sets urls from theme url."""
        html = self.get_html(theme_url)
        soup = BeautifulSoup(html, 'html.parser')
        list = [link.get('href') for link in soup.find_all('a', attrs={'data-test': "product-leaf-title-link"})]

        return list

    def scrape_set(self, url):
        """Retrieve lego set fields from url and return dictionary of fields."""
        html = self.get_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        title, product_id, theme, price, available, age, elements, link, minifigures = soup
        title = title.find('span', class_="Markup__StyledMarkup-ar1l9g-0 hlipzx").string
        product_id = product_id.find('span', class_="Markup__StyledMarkup-ar1l9g-0 hlipzx")
        # to be added

def refresh_db():
    """Scrape lego webstore from lego sets and add them to database if they don't exist."""
    pass
