# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import re
import pandas as pd


class BearspacePipeline:

    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        """
            I wanted to separate data cleaning part from spider.
            Extract media, height and width from raw data.
        """
        height_cm = None
        width_cm = None
        media = None
        price = int(float(item['price_gbp'].replace('£', '').replace(',', '').strip()))  # I could use regex
        for index, text in enumerate(item['raw_data']):
            regex = '((?<![\/])(?:\d+(?:[.,]\d+)?(?:\s|x)*)+?)'
            founds = re.findall(regex, text)
            if founds and len(founds) > 1:
                height_cm = float(founds[0].replace('x', '').strip())
                width_cm = float(founds[1].replace('x', '').strip())
                break  # if dimensions are found, do not search in next row
            elif index == 0:  # if there are now dimensions, check if media text is in first row bellow the image
                media = text
        new_item = {'url': item['url'], 'title': item['title'], 'media': media, 'height_cm': height_cm,
                    'width_cm': width_cm,
                    'price_gbp': price}
        self.items.append(new_item)
        return new_item

    def close_spider(self, spider):
        """
            When scraping is done, write dataframe in csv file.
            Name of the file is spider name.
        """
        df = pd.DataFrame.from_records(self.items)
        df.to_csv(f'{spider.name}.csv', index=False)
