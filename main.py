
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

with open('robots.csv', 'w') as robots_file:
    # write the columns labels
    robots_file.write('product_name' + ',' + 'brande' + ',' + 'shipping' + '\n')

    # loop through all robots products
    for robot in robots_products:
        try:
            robot_title = robot.find('div', {'class': 'item-info'}).find('a', {'class': 'item-title'}).text
        except:
            robot_title = None

        try:
            robot_brand = robot.div.div.a.img['title']
        except:
            robot_brand = None

        try:
            robot_shipping_price = robot.find('li', {'class': 'price-ship'}).text
        except:
            robot_shipping_price = None

        # write all data into the file as comma separated values
        robots_file.write(robot_title.replace(',', '|') + ',' + str(robot_brand) + ',' + robot_shipping_price + ',' + '\n')
