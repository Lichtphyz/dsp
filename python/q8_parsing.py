# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

def read_data(filename):
    """Returns a list of lists representing the rows of the csv file data.

    Arguments: filename is the name of a csv file (as a string)
    Returns: list of lists of strings, where every line is split into a list of values. 
        ex: ['Arsenal', 38, 26, 9, 3, 79, 36, 87]
    """
    
    #open file
    contents = open(filename, mode = "r")
    
    #copy each line of the file to an entry of a new list
    list_of_lines = []
    for line in contents:
        list_of_lines += [line]
    
    #remove the headings line
    list_of_lines = list_of_lines[1:]
    
    #remove the /n from the end of each line
    for i in range(len(list_of_lines) - 1):
        list_of_lines[i] = list_of_lines[i][0:-1]
    
    #convert each string into a list of elements
    parsed_data = []
    for team in list_of_lines:
        parsed_data += [team.split(',')]
    
    #close the file
    contents.close()
    #print(parsed_data)
    return parsed_data


def get_index_with_min_abs_score_difference(goals):
    """Returns the index of the team with the smallest difference
    between 'for' and 'against' goals, in terms of absolute value.

    Arguments: parsed_data is a list of lists of cleaned strings
    Returns: integer row index
    """
    
    #input headings:  Team,Games,Wins,Losses,Draws,Goals,Goals Allowed,Points

    #check for the difference between the goals for and against,
    #keeping track each time the difference is small than the previous team
    s_diff_id = 0
    min_score_diff = 9999
    index = 0
    
    
    for team in goals:
        #print("this",team)
        score_diff = abs( int(team[5]) - int(team[6]) )
        if score_diff < min_score_diff:
            min_score_diff = score_diff
            s_diff_id = index
            #print(s_diff_id)
        index += 1
    
    return s_diff_id

def get_team(index_value, parsed_data):
    """Returns the team name at a given index.
    
    Arguments: index_value is an integer row index
               parsed_data is the output of `read_data` above
               
    Returns: the team name
    """

    return parsed_data[index_value][0]


#data = read_data("football.csv")
#teamid,goaltable = get_index_with_min_abs_score_difference(data)
#print(data)
#print(teamid)
#output = get_team(teamid,goaltable)
#print(output)

footballTable = read_data('football.csv')
minRow = get_index_with_min_abs_score_difference(footballTable)
print(str(get_team(minRow, footballTable)))