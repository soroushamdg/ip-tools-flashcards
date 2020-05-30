import click
from crawler import requester,extracter,saver
from drawer import seeker, stylist, designer

import logger_factory,logging
logging.getLogger(__file__)




def getExportUrl(url, filename, printv=False):

    # STAGE 1 -> GETTING DATA
    request = requester.requester(url)
    logging.debug("requester object created")

    html_content = request.extract_html()
    logging.debug("requester -> getting html content")

    assert not html_content['error'],"Error in extracting html"
    logging.debug("requester -> no error getting html content")

    extract = extracter.extracter_from_w3(html_content=html_content['content'])
    logging.debug("extracter -> extracter object created")

    data = extract.extract_data()
    if printv:
        print(data)
    logging.debug("extracter -> extract data")

    save = saver.saver(filename)
    logging.debug("saver -> saver object created")
    save.save_data_into_file(data)
    logging.debug(f"saver -> saved data into {filename}")


    return True


def exportToPPTXPNG(filename):
    # STAGE 2 -> TURNING DATA INTO FLASHCARDS


    seekobj = seeker.seeker([filename])
    logging.debug(f"seeker -> seeker object created")

    getReturnedData = seekobj.get_and_return_data()

    assert getReturnedData, "Error in reading and extracting data from csv file"

    items1 = seeker.seeker(['built_in_functions']).get_and_return_data()

    styleWithPPTXFnames = stylist.stylist(getReturnedData).set_pptx_to_item()
    assert styleWithPPTXFnames, "Error in assigning PPTX to items"

    designThem = designer.designer(styleWithPPTXFnames).design_data(True)

    assert designThem, "Error in exporting PPTX FILES"
    return True

# define commands
@click.command()

@click.option('--item','-i',multiple=True,help="add items by this command, instert like -> url filename")
@click.option('--log','-l',help ="If true will print variables in every stage, default = False",default = False,type=bool)

@click.option('--filename','-f',multiple = True,help="add filenames to turn them into pptx and png files")

def main(item,log,filename):
    if item:
        click.echo(item)
        for it in item:
            print(it.split())
            it = it.split()
            try:
                getExportUrl(it[0],it[1],printv=log)
            except Exception as msg:
                print(msg)
                logging.error(f"Error in running item -> {item}\n{msg}")
            else:
                logging.debug(f"Done -> {item}")
                print(f"Done -> {item}")
    elif filename:
        click.echo(filename)
        for it in filename:
            try:
                exportToPPTXPNG(it)
            except Exception as msg:
                print(msg)
                logging.error(f"Error in running filename -> {it}\n{msg}")
            else:
                logging.debug(f"Done -> {it}")
                print(f"Done -> {it}")
    else:
        print('enter proper inputs')



if __name__ == "__main__":
    main()


