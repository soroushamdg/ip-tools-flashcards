import os,pathlib,csv
from options import data_path

class seeker():

    def __init__(self,filenames):
        self.csvfilenames = filenames

    def get_and_return_data(self):
        files_to_ret = []
        for filename in os.listdir(data_path):
            if filename.endswith('.csv') and filename.split('.csv')[0] in self.csvfilenames:
                files_to_ret.append(filename)
        ret_dict = {}
        for file in files_to_ret:
            with open(str(pathlib.Path(data_path).joinpath(file))) as csvfile:
                csvfile = csv.reader(csvfile)
                ret_dict[file] = [func for func in csvfile if func]

        return ret_dict