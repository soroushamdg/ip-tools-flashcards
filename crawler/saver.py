"""
This script will save extracted data into csv file.
"""
import options
import logger_factory,logging
logging.getLogger(__file__)
import pathlib,os
import csv

class saver():
    def __init__(self,filename,index=True):
        self.filename = filename
        self.index = index

    def init_csv_file(self):
        try:
            logging.debug(f'starting initiating csv file. {self.filename}')
            with open(pathlib.Path(options.data_path).joinpath(self.filename+'.csv'),'w') as csv_file:
                logging.debug(f'{self.filename} opened.')
                writer = csv.writer(csv_file)
                row = ['index','function','description'] if self.index else ['function','description']
                writer.writerow(row)
                csv_file.close()
        except Exception as msg:
            logging.error(f'error in initiating csv file. -> {msg}')
            return False
        else:
            logging.debug(f'csv file initiated successfully {self.filename}')
            return True

    def save_data_into_file(self,data):

        assert self.init_csv_file(),"error in initiating csv file."

        try:
            logging.debug(f'starting writing into csv file. {self.filename}')
            with open(pathlib.Path(options.data_path).joinpath(self.filename+'.csv'),'a') as csv_file:
                logging.debug(f'{self.filename} opened.')
                writer = csv.writer(csv_file)
                for item in data:
                    writer.writerow(list(item))
                csv_file.close()
        except Exception as msg:
            logging.error(f'error in writing into csv file. -> {msg}')
            return False
        else:
            logging.debug(f'data file wrote successfully {self.filename}')
            return True


