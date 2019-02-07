import csv
def bus_stop():
    street = []
    new_street = []
    fout1 = open('Street_Centrelines.csv', 'r')
    fout2 = open('Bus_Stops.csv', 'r')
    for item in fout1:
        new_item = item.split(",")
        if new_item[10] == "ARTERIAL":
            strt = new_item[4].strip()
            strt = strt.lower()
            if strt not in street:
                 street.append(strt)
    for stre in street:
         if stre not in new_street:
             new_street.append(stre)