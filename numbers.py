import csv
import pprint

try:
    import data
except :
    numbers = {}
    with open('numbers.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
    #        pprint.pprint(row)
            (Cityandstate, #0
             FIPScode, # 1
             Residentpopulation, #2
             Rankbasedonresidentpopulation, #3
             Medianhouseholdincome,  #4
             Medianfamilyincome, #5
             Percapitaincome, #6
             Individualsforwhompovertystatusdetermined, #7
             Familiesforwhompovertystatusdetermined, #8
             NumTotalindividuals, #9
             NumTotalfamilies, #10
             PerTotalindividuals, #11
             PerTotalfamilies)=row #12

            #print Cityandstate
            numbers[Cityandstate]=row
        f = open ("data.py","w")
        f.write("data="+pprint.pformat(numbers))
        f.close()
        import data

numbers = data.data

try:
    import capdata
except :
    #capitals.csv
    numbers = {}
    with open('capitals.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            #pprint.pprint(row)
            (State,
             Abbr,
             Date,
             Capital,
             Capitalsince,
             Landarea,
             RankPop,
             Municipalpopulation,
             Metropolitanpopulation,
             Notes,
             key,
             ig2)= row
            numbers[key]=row
        f = open ("capdata.py","w")
        f.write("data="+pprint.pformat(numbers))
        f.close()
        import capdata

capitols = capdata.data



for c in capitols.keys():
    #print c
    if c not in numbers:
        #print c
        pass
    else:
        d = numbers[c]
        print c,"\t" , d[11]
