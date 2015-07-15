import sys

"""這是"nester模組，它提供一個函式 print_lol(), 可列印出清單項目, 不管其中是否包含套疊的清單"""
def print_lol(the_list, indent = False, level = 0, fh = sys.stdout):
    """ 此函式需要四個參數，第一個位置參數名為 "the_list", 它可以是任何python 清單。清單中資料項會被遞迴地顯示在螢幕或寫入檔案，並自成一列。
        第二個參數，名為"indent", 用於設定是否插入縮排
        第三個參數，名為"level", 用於遇到有層疊的清單時插入縮排
        第四個參數，名為"fh", 用於指定資料寫入到何處。預設值 sys.stdout """
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

#這是註解
