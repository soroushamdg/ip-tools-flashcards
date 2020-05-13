"""
This script will extract wanted data from given html
"""
from bs4 import BeautifulSoup

class extracter():

    def __init__(self,html_content,index = True,firstXitems = 0):
        """
        This function will extract flashcards data from given html
        :param html_content: html content in str
        :param index: index items in output or Not, default = True
        :param firstXitems: output first X items of whole items on the page
        """
        self.htmlc = html_content