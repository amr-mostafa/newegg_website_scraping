
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

print('Starting scraping ..')
robots_url = 'https://www.newegg.com/p/pl?d=robot&PageSize=36'

# make http request to the robots page resource
robots_client = urlopen(robots_url)

# read the response data which is HTML content
robots_resources = robots_client.read()

# close the http connection
robots_client.close()

# parse the html page to beautiful soup parser, convert tags to variables
robots_parser = soup(robots_resources, 'html.parser')

# fetch the container out of the body
robots_list = robots_parser.find('div', {'class':'list-wrap'})
robots_products = robots_list.findAll('div', {'class':'item-container'})

# getting robot data
robot_title = robots_products[0].find('div', {'class':'item-info'}).find('a', {'class':'item-title'}).text
print(robot_title)

robot_brand = robots_products[0].div.div.a.img['title']
print(robot_brand)

robot_shipping_price = robots_products[0].find('li', {'class':'price-ship'}).text
print(robot_shipping_price)