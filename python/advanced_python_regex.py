'''
write a function which reads in a scs file, and then returns a dictionary
where keys are (stanardized) degress and values are their frequencies in the
file.

Using regular expressions so that your code considers "PhD" and "Ph.D." to be
the same thing.
'''
def sub_count(pattern,degrees):
    import re
    count = 0
    for entry in degrees:
        if re.match(pattern, entry, re.I) != None:
            count += 1
    return count

def count_degrees(csv_file_name):

    import csv
    
    #raw = open('faculty.csv', 'r')
    raw = open(csv_file_name)
    
    temp = csv.reader(raw,delimiter=',')
    table = []
    for row in temp:
        table += [row]
    
    raw.close()
    
    #create list of degrees from master table
    degrees = []
    for entry in table:
        degrees += [entry[1]]
    
    D_list = ('MD', 'MA', 'SCD', 'BSED', 'PHD', '0', 'MPH', 'MS', 'JD')
    
    D_count = []
    
    #count each degree - sub_count function defined above
    
    D_count += [sub_count(r'.*M.?D.*',degrees)]
    D_count += [sub_count(r'.*M.?A.*',degrees)]
    D_count += [sub_count(r'.*Sc.?D.*',degrees)]
    D_count += [sub_count(r'.*B.?S.?ed.*',degrees)]
    D_count += [sub_count(r'.*Ph.?D.*',degrees)]
    D_count += [sub_count(r'.*0.*',degrees)]
    D_count += [sub_count(r'.*M.?P.?H.*',degrees)]
    D_count += [sub_count(r'.*M.?S.*',degrees)]
    D_count += [sub_count(r'.*J.?D.*',degrees)]
    
    #print(D_count)
    
    #combine the degree names and counts into a dictionary
    degree_dict = dict(zip(D_list,D_count))
    
    return(degree_dict)


print(count_degrees('faculty.csv'))
print()


def count_titles(csv_file_name):

    import csv
    
    #raw = open('faculty.csv', 'r')
    raw = open(csv_file_name)
    
    temp = csv.reader(raw,delimiter=',')
    table = []
    for row in temp:
        table += [row]
    
    raw.close()
    
    #create list of full titles from master table
    titles = []
    for entry in table:
        titles += [entry[2]]  #note different index
    
    D_list = ('associate','assistant','professor')
    
    D_count = []
    
    #count each degree - sub_count function defined above
    
    D_count += [sub_count(r'.*associate prof.*',titles)]
    D_count += [sub_count(r'.*assistant prof.*',titles)]
    D_count += [sub_count(r'.*professor.*',titles)]
    
    #remove assoc and assit profs from full professor count
    D_count[2] -= (D_count[0]+D_count[1])
    
    #print(D_count)
    
    #combine the position names and counts into a dictionary
    return(dict(zip(D_list,D_count)))

print(count_titles('faculty.csv'))
print()

def emails(csv_file_name):
    import csv
    
    #raw = open('faculty.csv', 'r')
    raw = open(csv_file_name)
    
    temp = csv.reader(raw,delimiter=',')
    table = []
    for row in temp:
        table += [row]
    
    raw.close()
    
    #collect email addresses
    emails = []
    for entry in table:
        emails += [entry[3]]  #note different index
    
    
    return emails[1:]
    
emails = emails('faculty.csv')
print(emails)
print()

def unique_domains(emails):
    import re
    
    #split up each email address at the '@' symbol, and disregard the first part
    domains = []
    for email in emails:
        temp = re.split(r'@',email)
        domains += [temp[1]]

    #eliminate duplicates by converting to a set
    return set(domains)

print(unique_domains(emails))


#write a list of emails to a file
def write_to_csv(list_of_emails):
    file = open('emails.csv','w')
    file.write('list of emails for problem 5\n')
    for item in list_of_emails: 
        file.write(item)
        if item != list_of_emails[-1]: file.write('\n')
    
    file.close()
    return

write_to_csv(emails)

