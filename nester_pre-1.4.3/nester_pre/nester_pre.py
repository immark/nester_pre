"""
This is a nester function¡Ait provide a function print_lol(), will print item of list,
whether it include nester list or not.
"""
import sys

def print_lol(the_list, indent = False, level = 0, fh = sys.stdout):
    """ This function include four args,
        "the_list" - any python list¡Cthe content of list will be show out screen or fill into a file.
        "indent" - set for indentation.
        "level" - indentating for nester list.
        "fh" - set print out destination, default - [sys.stdout].
    """
    if level < 0:
        indent = False
    for each_item in the_list:
        if isinstance(each_item,list):         
            print_lol(each_item, indent, level+1, fh)
        else:
            if indent:
                for tap_stop in range(level):
                    print("\t",end='',file = fh)
            print(each_item, file = fh)

