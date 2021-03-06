fout = open('Street_Centrelines.csv','r') #open and read file named StreetCenterlines.csv

# Easy: A tuple of (STR_NAME,FULL_NAME,FROM_STR,TO_STR)

def func_tuple():
    #fout = open('Street_Centrelines.csv','r') #open and read file named StreetCenterlines.csv
    for item in fout:
        item = item.split(",")
        string = (item[2],item[4],item[6],item[7]) #item[2]=STR_NAME,item[4]=FULL_NAME,item[6]=FROM_STR,item[7]=TO_STR (columns in files)
        print(string)  

# A histogram of the different types of maintenance. 
        
def maintanance_histogram():
    #fout = open('Street_Centrelines.csv','r') #open and read file named StreetCenterlines.csv
    mydict = dict()
    for item in fout:
        item = item.split(",")
        if item[12] not in mydict:
            mydict[item[12]] = 1
        else:
            mydict[item[12]] += 1
    print(mydict)

#List of unique owners for the streets ["OWN"]

def owner_list():
    fout = open('Street_Centrelines.csv','r') #open and read file named StreetCenterlines.csv
    owners = []
    for item in fout:
        item = item.split(",")
        item = item[11].strip()
        if item not in owners:
            owners.append(item)
    print(owners)

# Different types of Street classes ["ST_CLASS"] and a list of streets undereach class
def get_street_class():
    str_class = []
    fout = open("Street_Centrelines.csv","r")
    for item in fout:
        item = item.split(",")
        item = item[10].strip()
        item = item.replace(" ","")
        if item not in str_class:
            if len(item) >= 1:
                str_class.append(item)
    return str_class

def street_class():
    str_class = get_street_class()
    print(str_class)
    for street in str_class:
        print(".",street)
        for item in fout:
            item = item.split(",")
            item_ = item[10].strip()
            item_ = item_.lower()
            item_ = item_.replace(" ","")
            print(item[12])

func_tuple()
maintanance_histogram()
owner_list()
street_class()