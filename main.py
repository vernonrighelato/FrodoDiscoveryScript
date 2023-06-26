import os
import csv

'''
This script uses the frodo number to discover which frodos are live on the network
'''

def writeToCSV(filename, row):
    with open(filename, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)


prouter_combos = ['03', '05', '06', '09', '10', '12']
linecard = 0
interface = 1
interface_string = ""
counter = 0
prefix = "frodo-"
dns_suffix = ".frodo.ox.ac.uk"
for combo in prouter_combos:
    while linecard < 6:
        while interface < 49:
            if interface < 10:
                interface_string = "0" + str(interface)
            else:
                interface_string = str(interface)
            frodo_number = combo + '0' + str(linecard) + interface_string
            frodo_fqdn = prefix + frodo_number + dns_suffix
            r = os.system("ping -n 1 -w 10 " + frodo_fqdn)
            row = [frodo_fqdn]
            if r == 0:
                print(frodo_fqdn + " is live")
                writeToCSV("live_frodos.csv", row)
                counter += 1
            else:
                print(frodo_fqdn + " no response")
                writeToCSV("dead_frodos.csv", row)
            interface += 1
        interface = 1
        linecard +=1
    linecard = 1
print(str(counter) + " frodos")
