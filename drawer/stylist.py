import pathlib,os,random
from options import pptxs_path
import logger_factory,logging
logging.getLogger(__file__)

class stylist():
    def __init__(self,items_list : dict):
        self.items_list = items_list

    def look_for_pptx(self,items_number):
        logging.debug(f'Finding pptx templates for {items_number} files.')
        return random.choices([item for item in os.listdir(pptxs_path) if item.endswith(".pptx")],k=items_number)


    def set_pptx_to_item(self):
        logging.debug(f'Starting setting pptx templates.')
        ready_dict = {}
        try:
            for key,item in self.items_list.items():
                logging.debug(f'Starting setting pptx templates for header -> {key} \n items -> {item}')
                try:
                    ready_dict[key] = [item for item in zip(item,self.look_for_pptx(len(item)))]
                except Exception as msg:
                    logging.error(f'error in adding item {key} -> {item}\n  -> {msg}')
                    return None
        except Exception as msg:
            logging.error(f"error in iterating items_list.items. -> {msg}")
            return None
        logging.debug(f'finished setting pptx templates \n{ready_dict}')
        print(ready_dict)
        return ready_dict