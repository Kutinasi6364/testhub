import csv

with open("cf.csv", "w") as cf:
    cf = csv.writer(cf, delimiter=",")
    cf.writerow(["1-1", "1-2", "1-3"])
    cf.writerow(["2-1", "2-2", "2-3"])

with open("cf.csv", "r") as cf:
    cf = csv.reader(cf, delimiter=",")
    for row in cf:
        print(",".join(row))
