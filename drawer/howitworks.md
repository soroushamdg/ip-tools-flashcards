seeker.py will look for data files, names given input and in output
will return a dictionary containing {'filename':data as array}

then stylist.py will look for available template pptxs and will return a dictionary as {'filename':[(funcname,func description,image template pptx file)]

and then the designer.py will open each item in dict got from stylist.py and export it into a png file, and then save it into:
 /exports
    +/filename
        +/functions
            [-] images