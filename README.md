# HENI Task

## Task 1 - task_1.py
*My comments during task 1:*  
- I could use regex for artist name and price range and not split function.
- I saw that you imported **requests** module. Maybe to check if image is online?
- "A dataframe of 1 row and 7 columns where the columns are" - but there are 8 columns
- "Price realised in USD (6 370 908)" - should be 16 370 908?
- Not sure if numbers on output have space on purpose? I used integers.

    
## Task 2 - task_2.py
*My comments during task 2:*  
- I could find more elegant way than inline if else for values
- I am not sure if I am allowed to split row by "Image:" to get correct value


## Task 3 - Scrapy project

My Idea was to write 3 different spiders. In the end I couldn't fit in 30 minutes to finish API spider.
1. HTML (*bearspace_html.py*) - Finds product links in HTML and request pagination links.
2. SITEMAP (*bearspace_sitemaps.py*) - Finds product links in sitemaps. I found start link in robots.txt file.
3. API (*bearspace_api.py*) - I was very close to finish it. There is an API that returns structured data in json. I would need more time to analyze request payload and headers. There is an API for all listings and detail page as well. You can set high limit and get all products with one request.

Command to run:

    $ scrapy crawl <spider_name>

#### Explanation:
I made variable **raw_data** to extract all text bellow the image. In pipelines file there is a function that clean raw data and extract correct values. I wanted to separate cleaning data part from spider.

I noticed that sometimes dimensions can be in the first row bellow the image. If that's the case, then media value is empty.


## Task 4 - task_4 file

- **INNER JOIN** - all matches in both tables
- **LEFT JOIN** - all matches in both tables + remaining rows from left table
- **RIGHT JOIN** - all matches in both tables + remaining rows from right table
- **FULL JOIN** - select all records from tables even if rows don't match (null values will be in that case)

1.     SELECT arr_time, origin, dest, air.name FROM flights AS f INNER JOIN airlines AS air ON air.carrier = f.carrier;
2.     SELECT arr_time, origin, dest, air.name FROM flights AS f INNER JOIN airlines AS air ON air.carrier = f.carrier WHERE air.name LIKE '%JetBlue%'
3.     SELECT f.origin, COUNT(*) AS "numFlights" FROM flights AS f INNER JOIN airlines AS air ON air.carrier = f.carrier WHERE air.name LIKE '%JetBlue%' GROUP BY f.origin ORDER BY f.origin
4.     SELECT f.origin, COUNT() AS "numFlights" FROM flights AS f INNER JOIN airlines AS air ON air.carrier = f.carrier WHERE air.name LIKE '%JetBlue%' GROUP BY f.origin HAVING COUNT() > 100 ORDER BY f.origin

*My comments during task 4:*
- I can explain more joins with examples in the call
- First I thought that queries are independent (With one query we can finish all)


## Others

- I made simple Dockerfile
- I added all results files (csv) to GitHub (task_1.csv, task_2.csv, bearspace_html.csv, bearspace_sitemaps.csv)