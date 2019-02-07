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

    buss = []

    for st in new_street:
        for der in fout2:
            new_der = der.split(",")
            if new_der[7] == "Accessible":
                h = new_der[6].strip()
                h = h.lower()
                if h.find(st) >= 0:
                     buss.append(new_der[2])

bus_stop()                     