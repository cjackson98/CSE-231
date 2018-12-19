"""
CSE 232 Project 6
Ask for a file to read (provide error and ask again if file doesnt exist)
Ask for state to check in the file (error if state code DNE and asks again)
Gather data from entire file and add to a list
Gather data for specific state from the list above 
Calculate data for state
Print data and ask to plot
Ask for another state code
End program if quit is entered for state code
"""
import pylab

#list of state codes to use later
STATES = {'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY'}
USERS = ["Public", "Domestic", "Industrial", "Irrigation","Livestock"]


def open_file():
    """
    opens the file. Repeatedly checks if the file exists,
    and breaks out when it does. Returns the file
    """
    while 1==1:#repeatedly asking for file until valid file is entered
        try:    
            filename = input("Input a file name: ")
            file=open(filename,'r')
            break
        except FileNotFoundError:
            print("Unable to open file. Please try again.")
    file=open(filename,'r')
    return file
    
def read_file(file):
    """
    Reads the file. Gathers data for all states and adds it to a list.
    Returns the list
    """
    header=file.readline()
    data_list=[]
    for line in file:
        line_list=line.strip().split(',')
        state = line_list[0]
        county = line_list[2]
        population = float(line_list[6])
        population=population*1000
        population=round(population,2)
        fresh_water = float(line_list[114])
        salt_water = float(line_list[115])
        public = float(line_list[18])
        domestic = float(line_list[26])
        industrial = float(line_list[35])
        try:
            irrigation = float(line_list[45])
        except ValueError:
            irrigation=float(0)
        livestock = float(line_list[59])
        tup = (state,county,population,fresh_water,salt_water,public,domestic,\
        industrial, irrigation, livestock)
        data_list.append(tup)
    return data_list
#    return data_list
#        line=line.replace(',',' ')
#        line=line.split()
#        some_list.append(line)
        

def compute_usage(state_data):
    """
    computes the data and adds it to a list. Returns that list.
    """
    compute_data=[]
    for tup in state_data:
        county=tup[1]
        population=tup[2]
        total_water=float(tup[3])+float(tup[4])
        per_person_water=float(tup[3])/population
        tup_data=(county, population, total_water, per_person_water)
        compute_data.append(tup_data)
    return compute_data
        
    
def extract_data(data_list, state):
    """
    Gathers data for state entered or all states if all is entered.
    Adds data to a list and returns that list
    """
    state_data=[]
    for tup in data_list:
        if tup[0]==state or state=='ALL':
            state_data.append(tup)
    return state_data

def display_data(state_list, state):
    """
    Outputs data in correct format
    """
    print()
    print('{:^88s}'.format("Water Usage in " + state + " for 2010"))
    print("{:22s} {:>22s} {:>22s} {:>22s}".format("County", \
    "Population", "Total (Mgal/day)", "Per Person (Mgal/person)"))
    for tup in state_list:
        print('{:22s}{:>22,}{:>22.2f}{:>22.4f}'.format(tup[0],int(tup[1]),\
        tup[2],tup[3]))
    

def plot_water_usage(some_list, plt_title):
    '''
        Creates a list "y" containing the water usage in Mgal/d of all counties.
        Y should have a length of 5. The list "y" is used to create a pie chart
        displaying the water distribution of the five groups.

        This function is provided by the project.
    '''
    # accumulate public, domestic, industrial, irrigation, and livestock data
    y =[ 0,0,0,0,0 ]

    for item in some_list:

        y[0] += item[5]
        y[1] += item[6]
        y[2] += item[7]
        y[3] += item[8]
        y[4] += item[9]

    total = sum(y)
    y = [round(x/total * 100,2) for x in y] # computes the percentages.

    color_list = ['b','g','r','c','m']
    pylab.title(plt_title)
    pylab.pie(y,labels=USERS,colors=color_list)
    pylab.show()
    #pylab.savefig("plot.png")  # uncomment to save plot to a file
    
def main():
    """
    Main function. Creates variables and calls other functions.
    """
    print("Water Usage Data from the US and its States and Territories.\n")
    file=open_file()
    data_list = read_file(file)
    #repeatedly asking for state code until valid code is entered
    while 1==1:    
        state = input("\nEnter state code or 'all' or 'quit': ")
        state=state.upper()
        if state=='QUIT':
            break
        if state=='ALL':
            pass
        elif state not in STATES:
            print("Error in state code.  Please try again.")
            continue
        if state != 'QUIT':
            state_data=extract_data(data_list, state)
            state_list=compute_usage(state_data)
            display_data(state_list, state)
            answer = input("\nDo you want to plot? ")
            answer=answer.lower()
            if answer=='yes':
                plt_title='Plot'
                plot_water_usage(state_list,plt_title)

if __name__ == "__main__":
    main()
