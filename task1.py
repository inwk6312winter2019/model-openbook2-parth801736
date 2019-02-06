fout = open('Street_Centrelines.csv','r') #open and read file named StreetCenterlines.csv

# Easy: A tuple of (STR_NAME,FULL_NAME,FROM_STR,TO_STR)

def func_tuple():
    for item in fout:
        item = item.split(",")
        string = (item[2],item[4],item[6],item[7]) #item[2]=STR_NAME,item[4]=FULL_NAME,item[6]=FROM_STR,item[7]=TO_STR (columns in files)
        print(string)  

# A histogram of the different types of maintenance. 
        
def maintanance_histogram():
    mydict = dict()
    for item in fout:
        item = item.split(",")
        if item[12] not in mydict:
            mydict[item[12]] = 1
        else:
            mydict[item[12]] += 1
    print(mydict)