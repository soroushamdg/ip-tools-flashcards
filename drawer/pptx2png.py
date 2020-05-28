import sys
import os

try:
    from comtypes import client
except:
    print("Install comtypes from http://sourceforge.net/projects/comtypes/")
    sys.exit(-1)

def convert2png(pptxfilename):
    f = os.path.abspath(pptxfilename)
    print(os.path.abspath(f))
    if not os.path.exists(f):
        print("No such file!")
        sys.exit(-1)

    powerpoint = client.CreateObject('Powerpoint.Application')
    powerpoint.Presentations.Open(f)
    powerpoint.ActivePresentation.Export(f, 'PNG')
    powerpoint.ActivePresentation.Close()
    powerpoint.Quit()

    print(f"Converting successfully finished. -> {pptxfilename}")
    return True