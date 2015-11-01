from __future__ import print_function
import sys

def print_lol(res, indent = True, level = 0, dest = None):
    '''
    Parameters
    ----------
    res - any python list.
    indent - set the indentation or True by default.    
    level - indent for nested list.(must use with indent parameter)
    dest - set print out destination, or to sys.stdout by default.

    Try it now!    
    '''
  
    if dest == None:
        dest = sys.stdout
    if level < 0:
        indent = False

    if isinstance(res, str) or isinstance(res, int) :
        if sys.version_info < (3, 0):
            print >> dest, res
        print(res, file=dest)
    elif isinstance(res, dict):
        print_lol(printDict(res, level), indent, level+1, dest)

    else:
        for item in res:
            if  isinstance(item, list) or  isinstance(item, tuple):
                print_lol(item, indent, level+1, dest)
            elif  isinstance(item, dict):
                print_lol(item, indent, level+1, dest) 
            else:
                if indent:                
                    for tap_stop in range(level):
                        print("    ",end = '',  file = dest)
                print(item, file = dest)

def printDict(obj_in, level):
    tmp = []
    tmpStr =''
    for key, value in (obj_in.items()):
        if  isinstance(value, list) or isinstance(value, tuple) or isinstance(value, dict):
            for valueItem in value:
                tmpStr += str(valueItem) + ' '
            value = tmpStr
        tmp.append(str(key) + ':  '+ str(value))
        tmpStr=''
    return tmp
