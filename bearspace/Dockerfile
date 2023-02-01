FROM python:3
WORKDIR /bearspace
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["scrapy", "crawl",  "bearspace_html"]