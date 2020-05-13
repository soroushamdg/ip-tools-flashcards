"""
This script will request and get html from given url
"""

import requests
import logging,logging_factory

class extracter():
    def __init__(self,url,attempts = 3):
        self.url = url
        self.attempts = attempts


    def extract_html(self):
        for attempt in range(self.attempts):
            logging.info(f"trying to get html content from {self.url}, attempt : {attempt+1}")
            try:
                logging.debug("starting request get url")
                r = requests.get(self.url)
            except:
                logging.error(f"Error in get request, attempt : {attempt+1}")
                continue
            logging.debug("checking status code")
            if r.status_code != 200:
                logging.error(f"Error in server side, request code :{r.status_code}")
                continue
            else:
                logging.debug("checking downloaded html content")
                if r.content:
                    return {'status_code':r.status_code,'content':r.content,'error':False}
                else:
                    continue
        logging.error(f"Couldn't get data. try again later")
        return {'status_code':r.status_code,'error':True}

