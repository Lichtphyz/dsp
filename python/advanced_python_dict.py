

#def count_titles():

import csv
import re

raw = open('faculty.csv', 'r')
#raw = open(csv_file_name)

temp = csv.reader(raw,delimiter=',')
table = []
for row in temp:
    table += [row]

raw.close()

#create lists for each column in the faculty table
names = []
for entry in table[1:]: names += [entry[0]]  #note different index
degrees = []
for entry in table[1:]: degrees += [entry[1]]  #note different index
titles = []
for entry in table[1:]: titles += [entry[2]]  #note different index
emails = []
for entry in table[1:]: emails += [entry[3]]  #note different index
    
#create last names list from the full names list
last_names = []
for name in names: last_names += [re.split(r' ',name)[-1]]


#combine the position names and counts into a dictionary
#NOTE:  some last names have multiple entries!!!
faculty_dict = {}
for i in range(len(last_names)):
    if last_names[i] not in faculty_dict.keys():
        faculty_dict[last_names[i]] = [[ degrees[i],titles[i],emails[i] ]]
    elif last_names[i] in faculty_dict.keys():
        print(last_names[i], faculty_dict[last_names[i]] )
        faculty_dict[last_names[i]] =   faculty_dict[last_names[i]] + [[ degrees[i],titles[i],emails[i] ]]

#print(faculty_dict)


#print('\n', faculty_dict['Li'])


'''Submitted version::
def get_dict():

    import csv
    import re

    raw = open('faculty.csv', 'r')
    #raw = open(csv_file_name)

    temp = csv.reader(raw,delimiter=',')
    table = []
    for row in temp:
        table += [row]

    raw.close()

    #create lists for each column in the faculty table
    names = []
    for entry in table[1:]: names += [entry[0]]  #note different index
    degrees = []
    for entry in table[1:]: degrees += [entry[1]]  #note different index
    titles = []
    for entry in table[1:]: titles += [entry[2]]  #note different index
    emails = []
    for entry in table[1:]: emails += [entry[3]]  #note different index

    #create last names list from the full names list
    last_names = []
    for name in names: last_names += [re.split(r' ',name)[-1]]


    #combine the position names and counts into a dictionary
    #NOTE:  some last names have multiple entries!!!
    faculty_dict = {}
    for i in range(len(last_names)):
        if last_names[i] not in faculty_dict.keys():
            faculty_dict[last_names[i]] = [[ degrees[i],titles[i],emails[i] ]]
        elif last_names[i] in faculty_dict.keys():
            #print(last_names[i], faculty_dict[last_names[i]] )
            faculty_dict[last_names[i]] =   faculty_dict[last_names[i]] \
            + [[ degrees[i],titles[i],emails[i] ]]

    return faculty_dict
    '''
    
    
###7th problem
split_names = []
for name in names: split_names += [re.split(r' ',name)]
tup_names = []
for name in split_names: tup_names += [tuple(name)]

#combine the position names and counts into a dictionary
#NOTE:  some last names have multiple entries!!!
faculty_dict = {}
for i in range(len(tup_names)):
    if tup_names[i] not in faculty_dict.keys():
        faculty_dict[tup_names[i]] = [ degrees[i],titles[i],emails[i] ]
    elif tup_names[i] in faculty_dict.keys():
        #print(names[i], faculty_dict[last_names[i]] )
        faculty_dict[tup_names[i]] =   faculty_dict[tup_names[i]] \
        + [[ degrees[i],titles[i],emails[i] ]]

print('\n', faculty_dict[('Mingyao', 'Li')])