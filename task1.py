fout = open('StreetCenterlines.csv','r') #open and read file named StreetCenterlines.csv

# Easy: A tuple of (STR_NAME,FULL_NAME,FROM_STR,TO_STR)

def func_tuple():
    for item in fout:
        item = item.split(",")
        string = (item[2],item[4],item[6],item[7])
        print(string)  
