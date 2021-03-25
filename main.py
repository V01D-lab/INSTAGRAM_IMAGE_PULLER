import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def main(url):

    ##setting the driver and making it headless (making it run in the background)

    firefox_options = Options()

    firefox_options.add_argument("--headless")

    browser = webdriver.Firefox(options=firefox_options)

    ##getting the url 
    
    browser.get(url)

    ##finding and extracting the image

    element = browser.find_element_by_class_name('FFVAD')

    img = element.get_attribute('src')

    print(f'img link --> {img}')

    getting_img = requests.get(img)

    
    file = open("img.jpeg", "wb")
    file2 = open("img.png", "wb")

    file.write(getting_img.content)
    file2.write(getting_img.content)

    file.close()
    file2.close()



if __name__ == '__main__':

    url = input('image url --> ')
    main(url)