# web scraping for products from "newegg" website
* A simple python script that extracts the first page of the list of products titled "robot" from:  
"https://www.newegg.com/p/pl?d=robot&PageSize=36"
* Then save the products name, brand, and shipping price in a CSV file

## Resources used
* Python 3.7.3
* **Packages**: [BeautifulSoub4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [urllib.request](https://docs.python.org/3/library/urllib.request.html)

## Project Demo
https://youtu.be/R0Ca5PhJ33U

## Prerequisites
You must install beautifusoup4 package.
Open CMD and run this command
```
pip install beautifulsoup4
```

## Run the project
The project is only 1 python script __main.py__  and you will run it to extract the data from the website  
Open CMD and run this command to run the script
```
python main.py
```

## Script Output
Script generates __robots.csv__ file with 3 columns for all scraped products names, brand, shipping price  

![](https://i.ibb.co/PzNLYpH/aaaaaaaaaaaa.png)

## License
This project is licensed under the GNU General Public License.
