from selenium import webdriver

from decimal import Decimal

from bs4 import BeautifulSoup

class LegoScraper():
    """Lego webstore scrapper"""

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(" - incognito")
        self.options.add_argument("--headless")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--no-sandbox")

        self.path = "/usr/local/bin/chromedriver"

    def get_html(self, url):
        """Retreive and return html from url."""
        driver = webdriver.Chrome(self.path, chrome_options=self.options)
        driver.get(url)
        html = driver.page_source
        driver.quit()

        return html

    def get_page_count(self, url):
        """Retrieve page count from url."""
        html = self.get_html(url)
        soup = BeautifulSoup(html, 'html.parser')

        pages = soup.find_all(
            'a',
            class_='Paginationstyles__PageLink-npbsev-7'
        )

        return len(pages)

    def scrape_themes_urls(self, themes_url):
        """Return list of lego themes urls."""
        html = self.get_html(themes_url)
        soup = BeautifulSoup(html, 'html.parser')
        list = ['https://www.lego.com' + link.get('href') for link in soup.find_all('a', class_="CategoryLeafstyles__ImagesLink-is33yg-4")]

        return list

    def scrape_sets_urls_from_theme(self, theme_url):
        """Return list of lego sets urls from theme url."""
        list = []
        page_count = self.get_page_count(theme_url)

        for page in range(1, page_count+1):
            html = self.get_html(theme_url + f'?page={page}')
            soup = BeautifulSoup(html, 'html.parser')

            list = ['https://www.lego.com' + link.get('href') for link in soup.find_all('a', attrs={'data-test': "product-leaf-title-link"})]

        return list

    def scrape_set(self, url):
        """Retrieve lego set fields from url and return dictionary of fields."""
        html = self.get_html(url)
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find(attrs={'property': 'og:title'})['content']
        product_id = soup.find(attrs={'property': 'product:retailer_item_id'})['content']
        price = soup.find(attrs={'property': 'product:price:amount'})['content']
        available = soup.find(attrs={'data-test': 'product-overview-availability'}).find(class_='Markup__StyledMarkup-ar1l9g-0 gkoBeO').string
        age = soup.find(attrs={'data-test': 'ages-value'}).find(class_='Markup__StyledMarkup-ar1l9g-0 gkoBeO').string
        elements = soup.find(attrs={'data-test': 'pieces-value'}).find(class_='Markup__StyledMarkup-ar1l9g-0 gkoBeO').string
        try:
            minifigures = soup.find(attrs={'data-test': 'minifigures-value'}).find(class_='Markup__StyledMarkup-ar1l9g-0 gkoBeO').string
        except:
            minifigures = None

        str_list = title.split('|')
        theme = str_list[1]

        lego_set = {
            'title': title[:(title.find('®')+1)],
            'product_id': product_id,
            'theme': theme[1:len(theme)-1],
            'price': Decimal(price),
            'available': available,
            'age': age,
            'elements': int(elements),
            'link': url,
            'minifigures': minifigures,
        }

        return lego_set