import csv
from collections import Counter
import sys
#sys.stdout = open('report.txt', 'w')
#writer = csv.writer(sys.stdout, delimiter=",")

with open('complaints.csv', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    headers = next(reader)

    new_data = [[i[0].split('-')[0], i[1], i[7]] for i in reader]
    '''Creating a nested dictionary did not result in the desired o/p so I tried to create tuples of year and product pair'''
    lis1 = []
    for row in new_data:
        tup = tuple(row[0:2])
        lis1.append(tup)
    '''Checking to find the total number of unique tuple pairs created above to serve as a reference'''
    set1 = set(lis1)
    dic = {}
    innerdic = {}

    for row in new_data:
        tup = tuple(row[0:2])
        company = row[2]
        if tup in set1: # checking if the row has the tuple pair thats added in the set.
            if tup not in dic:
                dic[tup] = [company]
            else:
                dic[tup].append(company)
    fo = open("report.csv", "w",newline='')
    writer = csv.writer(fo,delimiter=',')
    for key, value in dic.items():
        innerdic = Counter(value)
        a, b = key # appending the product and year to the list
        lis=[]
        #print(len(b))
        #c=""
        if ","in b:
            b='"{}"'.format(b)
        #print(len(c))
        lis.append(b.lower())
        lis.append(a)
        sum1 = 0
        for k, v in innerdic.items():
            sum1 = v + sum1
        lis.append(sum1)
        length = len(innerdic)
        lis.append(length)
        percentage = round((length * 100) / sum1)
        lis.append(percentage)
        #print(lis)
        writer.writerow(lis)
    fo.close()









