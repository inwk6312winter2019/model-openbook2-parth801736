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

    print("Stop Number    |    Location    |    FCODE")
    for bus in buss:
        for new_re in open('Bus_Stops.csv', 'r'):
            new_re = new_re.split(",")
            if new_re[2].find(bus) >= 0:
                print(new_re[4],"",new_re[6],"",new_re[10])

bus_stop()                     