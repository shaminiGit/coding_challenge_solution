import csv
from collections import Counter
import sys
#sys.stdout = open('report.txt', 'w')
#writer = csv.writer(sys.stdout, delimiter=",")

def listofdata()->list:
    '''
    :return: returns a List of desired columns by reading the input csv
    '''
    with open('input/complaints.csv', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        headers = next(reader)
        new_data = [[i[0].split('-')[0], i[1], i[7]] for i in reader]
        '''Creating a nested dictionary did not result in the desired o/p so I tried to create tuples of year and product pair'''
        sorted_list = sorted(new_data, key=lambda x: (x[0]))
        sorted_list2 = sorted(sorted_list, key=lambda x: (x[1]))

    return sorted_list2

    

def create_tuples(List)-> set:
    '''
    :param List: List of rows from CSV
    :return: returns a set which has unique year,product tuple pairs
    '''

    list_of_tuples=[]
    for row in List:
        tup = tuple(row[0:2])
        list_of_tuples.append(tup)
    '''Checking to find the total number of unique tuple pairs created above to serve as a reference'''
    #sorted_list=sorted(list_of_tuples, key = lambda x: (x[0],x[1]),reverse=False)
    #print(sorted_list)

    set_of_tuples = set(list_of_tuples)
    return set_of_tuples

def create_dict():
    '''
    driver method which takes List,tuple_set as inout from functions listofdata and create_tuples and calls the writing_output fuction to write
    output to csv file

    '''
    List=listofdata()
    tuple_set=create_tuples(List)

    outer_dictionary = {}
    for row in List:
        tup = tuple(row[0:2])
        company = row[2]
        if tup in tuple_set: # checking if the row has the tuple pair thats added in the set.
            if tup not in outer_dictionary:
                outer_dictionary[tup] = [company]
            else:
                outer_dictionary[tup].append(company)
    writing_output(outer_dictionary)

def writing_output(dictionary):
    '''
    :param dictionary: Dictionary with a tuple as key and companies as value.
    :return: writes output to csv
    '''
    innerdictionary={}
    fo = open("output/report.csv", "w",newline='')
    writer = csv.writer(fo,delimiter=',')
    for key, value in dictionary.items():
        innerdictionary = Counter(value)
        a, b = key # appending the product and year to the list
        output_list=[]
        #print(len(b))
        #c=""
        if ","in b:
            b='"{}"'.format(b)
        #print(len(c))
        output_list.append(b.lower())
        output_list.append(a)
        sum1 = 0
        for k, v in innerdictionary.items():
            sum1 = v + sum1
        output_list.append(sum1)
        length = len(innerdictionary)
        output_list.append(length)
        percentage = round((length * 100) / sum1)
        output_list.append(percentage)
        #print(lis)
        writer.writerow(output_list)
    fo.close()

if __name__ == '__main__':
    dictionary=create_dict()








