import logging
from options import log_path
import sys
log_format = '%(asctime)s,%(process)d,%(levelname)5s,%(name)8s,%(message)s'
logging.getLogger(__name__).addHandler(logging.StreamHandler(sys.stdout))
logging.basicConfig(level=logging.DEBUG,
                        format=log_format,
                        filename=log_path,
                        filemode='a')
