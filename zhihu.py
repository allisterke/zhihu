from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import re
import codecs
import argparse


def download(args):
    browser = webdriver.Firefox()
    browser.get(args.link)

    title = browser.find_element_by_class_name('QuestionHeader-title').text
    if not os.path.isdir(title):
        os.mkdir(title)
    os.chdir(title)
    scroll_js = 'window.scrollBy(0, window.innerHeight)'
    while True:
        browser.execute_script(scroll_js)
        if browser.find_elements_by_class_name('QuestionAnswers-answerButton'):
            break
    for i, element in enumerate(browser.find_elements_by_class_name('RichContent-inner')):
        with codecs.open('%04d.txt' % i, 'w', encoding='utf-8') as f:
            print(element.text, file=f)
    # browser.quit()


def main():
    parser = argparse.ArgumentParser(description='Process arguments.')
    parser.add_argument('--link', type=str,
                        help='the zhihu link that you want to download')

    args = parser.parse_args()
    download(args)

if __name__ == '__main__':
    main()
