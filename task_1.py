from lxml import html
import re
import pandas as pd
from datetime import datetime

html_page_link = 'candidateEvalData/webpage.html'
html_content = html.parse(html_page_link)


def get_value(xpath):
    """
        function to not repeat same code to check if value is there
        return: extracted text from html
    """
    value = html_content.xpath(xpath)
    if value:
        return value[0]


def get_artist_name(name):
    """
        clean artist name
    """
    if name:
        if '(' in name:
            name = name.split('(')[0].strip()
        return name


def get_price(price):
    """
        clean price string and return int
    """
    if price:
        return int(re.sub(r'[(),]|([a-zA-Z])*', "", price).strip())


def get_price_range(price_range):
    """
        get two prices from range and normalize them
    """
    if price_range:
        one, two = price_range.split('-')
        return f'{get_price(one)} , {get_price(two)}'


def get_date(date):
    """
        get date and reformat it
    """
    if date:
        date = date.strip().replace(',', '')
        return datetime.strptime(date, "%d %B %Y").strftime("%Y-%m-%d")


painting = {
    'artist_name': get_artist_name(get_value('.//*[@class="lotName"]/text()')),
    'painting_name': get_value('.//*[@class="itemName"]/i/text()'),
    'price_GBP': get_price(get_value('.//*[contains(@id, "PriceRealizedPrimary")]/text()')),
    'price_US': get_price(get_value('.//*[contains(@id, "PriceRealizedSecondary")]/text()')),
    'price_GBP_est': get_price_range(get_value('.//*[contains(@id, "PriceEstimatedPrimary")]/text()')),
    'price_US_est': get_price_range(get_value('.//*[contains(@id, "PriceEstimatedSecondary")]/text()')),
    'image_link': get_value('.//img[@id="imgLotImage"]/@src'),
    'sale_date': get_date(get_value('.//*[contains(@id, "SaleDate")]/text()'))
}
df_painting = pd.DataFrame(data=painting, index=[0])
df_painting.to_csv('task_1.csv', index=False)
