import os,pathlib,csv
from options import data_path
import logger_factory,logging
logging.getLogger(__file__)
class seeker():

    def __init__(self,filenames):
        self.csvfilenames = filenames

    def get_and_return_data(self):
        files_to_ret = []
        try:
            for filename in os.listdir(data_path):
                if filename.endswith('.csv') and filename.split('.csv')[0] in self.csvfilenames:
                    logging.debug(f'Adding {filename} to export.')
                    files_to_ret.append(filename)
        except Exception as msg:
            logging.error(f'Error in finding data files -> {msg}')
            return None
        ret_dict = {}
        try:
            for file in files_to_ret:
                with open(str(pathlib.Path(data_path).joinpath(file))) as csvfile:
                    csvfile = csv.reader(csvfile)
                    next(csvfile)
                    logging.debug(f'exporting {filename}.')
                    ret_dict[file] = [func for func in csvfile if func]
        except Exception as msg:
            logging.error(f'Error in exporting data -> {msg}')
            return None
        logging.debug(f'Exported data -> \n {ret_dict}')
        return ret_dict