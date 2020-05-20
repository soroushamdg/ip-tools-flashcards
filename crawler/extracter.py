"""
This script will extract wanted data from given html
"""
from bs4 import BeautifulSoup
import logger_factory,logging
logging.getLogger(__file__)

class extracter_from_w3():

    def __init__(self,html_content,index = True,firstXitems = None):
        """
        This function will extract flashcards data from given html
        :param html_content: html content in str
        :param index: index items in output or Not, default = True
        :param firstXitems: output first X items of whole items on the page
        """

        self.bs = BeautifulSoup(html_content,features="html.parser")
        self.index = index
        self.range = firstXitems * 2 if firstXitems else None
        logging.debug("new extracter_from_w3 object created!")

    def clean_description(self,text):
        text = text.replace('\n','')
        text = text.replace('\r', '')
        text = text.replace(',', '')
        return text

    def extract_rows(self):
        logging.debug("finding table")
        try:
            table = self.bs.find(lambda tag: tag.name == 'table')
        except Exception as msg:
            logging.error(f"error in finding table tag -> {msg}")
            return False
        try:
            return table.findAll(lambda tag: tag.name=='td')
        except Exception as msg:
            logging.error(f"error in finding td tags -> {msg}")
            return False

    def extract_data_from_rows(self,rows):
        if rows:
            logging.debug("starting getting functions")
            functions = [item.find('a').text if item.find('a') else item.text for item in rows[:self.range:2] if item]
            logging.debug("starting getting descriptions")
            descriptions = [self.clean_description(item.text) for item in rows[1:self.range+1:2]] if self.range else [self.clean_description(item.text) for item in rows[1:self.range:2]]
            try:
                return list(zip(list(range(len(functions))),functions,descriptions)) if self.index else list(zip(functions,descriptions))
            except Exception as msg:
                logging.error("Error in zipping functions and descriptions")
                return False

        else:
            logging.error("erron in rows, input in False or None")

    def extract_data(self):
        try:
            data = self.extract_data_from_rows(self.extract_rows())
        except Exception as msg:
            logging.error(f"can't get and extract information from html -> {msg}")
            return False
        else:
            if data:
                return data
            else:
                logging.error("extract data output is None or False")
                return False
