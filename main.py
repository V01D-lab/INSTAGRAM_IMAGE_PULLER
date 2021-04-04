import requests
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import glob


def main(url):

    ##setting the driver and making it headless (making it run in the background)

    main_dir = os.getcwd()

    print(main_dir)

    driver = main_dir + '\geckodriver.exe'

    firefox_options = Options()

    firefox_options.add_argument("--headless")

    browser = webdriver.Firefox(executable_path=driver ,options=firefox_options)

    ##getting the url 
    
    browser.get(url)

    ##finding and extracting the image

    element = browser.find_element_by_class_name('FFVAD')

    img = element.get_attribute('src')

    print(f'img link --> {img}')

    getting_img = requests.get(img)

    img_count = len(glob.glob1(main_dir, "*.jpeg"))

    file = open(f"img{img_count}.jpeg", "wb")

    file.write(getting_img.content)

    file.close()


if __name__ == '__main__':

    while True:
        url = input('image url --> ')
        main(url)