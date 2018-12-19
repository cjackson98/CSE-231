"""
CSE 231 Project 8
    Prompt for file
        error if file cant be opened, prompt again
    Gather data from file
        add to dictionary in form {year:data} (data is a second dictionary-
        -in the form {name:information} information is a list of tuples)
    Prompt for a year to check the information of
        gather the range of years from the file entered
        if the year input by the user is not in that range or not a year, print-
        -an error and ask again. If the input is any form of "quit," end the program
    Output the correct information for the year entered by the user
    Ask to plot
        if yes: gather information and send to plot funciton
        if no: end program
"""
import pylab as py
from operator import itemgetter

def open_file():
    '''Asks user to input a filename in an infinite loop. 
    If the file can be opened, breaks out of the loop and returns the opened file.
    Otherwise, keeps asking until a working file is found'''
    
    while 1==1:#infinite loop
        filename=input("Input a file name: ")
        try:
            file=open(filename,'r')
            break#breaks out if file can be opened
        except:#if file cant be opened, prints an error and asks for another file name
            print("Unable to open file. Please try again.")
            
    return file#returns the opened file



def update_dictionary(dictionary, year, hurricane_name, data):
    '''Adds the data to the dictionary in the form {year:data} where data
    is a dictionary in the form {name:information} and information is a list of tuples
    including data received from the create_dicionary function'''
    
    if year not in dictionary:#if the year isnt in the dictionary
        data_list=[data]
        dictionary2={hurricane_name:data_list}#create a new dictionary with the name and data
        dictionary[year]=dictionary2#sets the new year value = to the dictionary created above
        
    elif year in dictionary:#if the year IS in the dictionary
        if hurricane_name not in dictionary[year]:#check if the name is not in the dicitonary
            data_list=[data]
            dictionary[year][hurricane_name]=data_list#if name is not already in the dictionary, add it
        elif hurricane_name in dictionary[year]:#if the name is in the dictionary
            dictionary[year][hurricane_name].append(data)#add the data to the list in the dictionary
            
    return dictionary#return the completed dictionary
    


def create_dictionary(file):
    '''Creates an empty dictionary. Strips and splits each line in the file and then gathers the
    latitude,longitude,date,year,wind,pressure,and name of the hurricane.
    Puts the latitude,longitude,wind, and pressure in a tuple. 
    Sends the dictionary, year, name, and  tuple with the data to the update_dictionary function'''
    
    dictionary=dict()#create empty dictionary to add to
    
    for line in file:#for each line in the file provided by the user
        line=line.strip().split()#strip the line and split it by spaces
        #use information provided in proj08.pdf to set the line positions = to the data
        year = line[0]
        hurricane_name = line[1]
        lat = float(line[3])
        lon = float(line[4])
        date = line[5]
        try:
            wind = float(line[6])
            pressure = float(line[7]) 
        except:#if the two lines above return an error (they arent numbers) set them = to 0
            wind=0
            pressure=0
        data = (lat, lon, date, wind, pressure)#add lat, lon, date, wind, and pressure to a tuple
        update_dictionary(dictionary, year, hurricane_name, data)#send all the gathered information to the update _dicitonary function
        
    return dictionary#reutrn the new dictionary



def display_table(dictionary, year):
    '''receives information gathered from the file and the year inputed by the user
    and outputs the data in a formatted table'''
    
    hurricane_list=[]
    old_name=''

    for key,value in dictionary.items():#for each year and value in the dictionary
        if key == year:#if the year = the user entered year, continue. Otherwise try the next key:value pair
            for key2,value2 in value.items():
                for line in value2:#for each value of each year in the original dictionary
                    line=(key2,)+line#add the name to the line
                    hurricane_list.append(line)#add the line to a list
   
    sorted_list=sorted(hurricane_list,key=itemgetter(0,4,1,2),reverse=True)#sort the list
    
    print("{:^70s}".format("Peak Wind Speed for the Hurricanes in " + year))#print header
    print("{:15s}{:>15s}{:>20s}{:>15s}".format("Name","Coordinates","Wind Speed (knots)","Date"))

    final_list=[]
    
    #more sorting
    for line in sorted_list:
        if line[0] != old_name:#if the names of the hurricanes switch, add the information to the list
            final_list.append((line[0],line[1],line[2],line[4],line[3]))
            old_name=line[0]

    sort_final=sorted(final_list,key=itemgetter(0))
    
    for line in sort_final:#print the information
        print("{:15s}({:>6.2f},{:4.2f}){:>20.2f}{:>15s}".format(line[0],line[1],line[2],line[3],line[4]))
 
    
    
def get_years(dictionary):
    '''receives the dictionary with the data in it and gets a range of years to
    check if the user inputted year is available. Returns the minimum and maximum years'''
    
    sorted_dict=sorted(dictionary)#sort the dictionary
    min_year=sorted_dict[0]#first position is the minimum year
    max_year=sorted_dict[-1]#last postion is the maximum year
    
    return min_year,max_year   #return min and max



def prepare_plot(dictionary, year):
    '''Receives the dictionary and user submitted year. Creates a list of names, max wind 
    speeds, and coordinates for the year all sorted in the same way and adds them all 
    to a tuple. Returns the tuple to be used later'''
    
    coord_list=[]
    
    for key,value in dictionary.items():
        if key == year:#if year = inputed year
            for key2,value2 in value.items():
                data=[]#clear data list
                for item in value2:
                    data.append((item[0],item[1]))#add lat and lon to data list
                    data=sorted(data,key=itemgetter(0))#sort data_list
                coord_list.append(data)#append data_list to coord_list before clearing data_list

    hurricane_list=[]
    name_list=[]
    speed_list=[]

    #adds information for each hurricane a list and adds the name of the hurricane
    #to the beginning of that list
    for key,value in dictionary.items():
        if key == year:
            for key2,value2 in value.items():
                for line in value2:
                    line=(key2,)+line
                    hurricane_list.append(line)
                    
    sorted_list=sorted(hurricane_list,key=itemgetter(0,4,1,2),reverse=True)#sorts the list
        
    final_list=[]
    old_name=''
    
    for line in sorted_list:#adds all info to a list and sorts it
        if line[0] != old_name:
            final_list.append((line[0],line[1],line[2],line[4],line[3]))
            old_name=line[0]
    sort_final=sorted(final_list,key=itemgetter(0))
    
    #for each line in the final list, append the name and max speed values to their appropriate lists
    for line in sort_final:
        name_list.append(line[0])
        speed_list.append(line[3])
        
    data_tup=(name_list,coord_list,speed_list)#add name list, coordinate list, and speed list to a tuple
    
    return data_tup#return the tuple



def plot_map(year, size, names, coordinates):
    '''Receives inputed year, size(number of items in the dictionary), names, and
    coordinates of the hurricanes and uses them to plot a map. Prints the map'''
    
    # The the RGB list of the background image
    img = py.imread("world-map.jpg")

    # Set the max values for the latitude and longitude of the map
    max_longitude, max_latitude = 180, 90
    
    # Set the background image on the plot
    py.imshow(img,extent=[-max_longitude,max_longitude,\
                          -max_latitude,max_latitude])
    
    # Set the corners of the map to cover the Atlantic Region
    xshift = (50,190) 
    yshift = (90,30)
    
    # Show the atlantic ocean region
    py.xlim((-max_longitude+xshift[0],max_longitude-xshift[1]))
    py.ylim((-max_latitude+yshift[0],max_latitude-yshift[1]))
	
    # Generate the colormap and select the colors for each hurricane
    cmap = py.get_cmap('gnuplot')
    colors = [cmap(i/size) for i in range(size)]
    
    
    # plot each hurricane's trajectory
    for i,key in enumerate(names):
        lat = [ lat for lat,lon in coordinates[i] ]
        lon = [ lon for lat,lon in coordinates[i] ]
        py.plot(lon,lat,color=colors[i],label=key)
    

     # Set the legend at the bottom of the plot
    py.legend(bbox_to_anchor=(0.,-0.5,1.,0.102),loc=0, ncol=3,mode='expand',\
              borderaxespad=0., fontsize=10)
    
    # Set the labels and titles of the plot
    py.xlabel("Longitude (degrees)")
    py.ylabel("Latitude (degrees)")
    py.title("Hurricane Trayectories for {}".format(year))
    py.show() # show the full map



def plot_wind_chart(year,size,names,max_speed):
    '''Receives inputed year, size(number of items in the dictionary), names, and
    max speeds of the hurricanes and uses them to plot a chart that shows the
    category of the hurricane. Prints the chart'''
    
    # Set the value of the category
    cat_limit = [ [v for i in range(size)] for v in [64,83,96,113,137] ]
    
    
    # Colors for the category plots
    COLORS = ["g","b","y","m","r"]
    
    # Plot the Wind Speed of Hurricane
    for i in range(5):
        py.plot(range(size),cat_limit[i],COLORS[i],label="category-{:d}".format(i+1))
        
    # Set the legend for the categories
    py.legend(bbox_to_anchor=(1.05, 1.),loc=2,\
              borderaxespad=0., fontsize=10)
    
    py.xticks(range(size),names,rotation='vertical') # Set the x-axis to be the names
    py.ylim(0,180) # Set the limit of the wind speed
    
    # Set the axis labels and title
    py.ylabel("Wind Speed (knots)")
    py.xlabel("Hurricane Name")
    py.title("Max Hurricane Wind Speed for {}".format(year))
    py.plot(range(size),max_speed) # plot the wind speed plot
    py.show() # Show the plot
    
    

def main():
    '''Calls other functions. Intitializes some variables. Prompts for year and
    whether or not to plot and prints some titles / visual outputs'''
    
    file=open_file()
    dictionary=create_dictionary(file)#create dictionary
    
    print("Hurricane Record Software")
    
    min_year,max_year=get_years(dictionary)#get min and max years
    
    print("Records from {:4s} to {:4s}".format(min_year, max_year))#print year range
    
    while 1==1:#infinite loop
        input_year=input("Enter the year to show hurricane data or 'quit': ")
        
        if input_year.isdigit():
            if input_year>=min_year and input_year<=max_year:#if the year entered is in the range of years allowed
                display_table(dictionary,input_year)#calls display table function
                plot=input("\nDo you want to plot? ")
                if plot.lower()=='yes':
                    data_tup=prepare_plot(dictionary,input_year)#prepare info for plotting
                    for key,value in dictionary.items():
                        size=len(value)#gets size of dictionary
                    plot_map(input_year,size,data_tup[0],data_tup[1])
                    plot_wind_chart(input_year,size,data_tup[0],data_tup[2])
                else:
                    continue#if the year entered isnt a number, ask again
            else:
                print("Error with the year key! Try another year")
                continue#if the year entered isnt in the range, ask again
        else:#if the year entered isnt a number
            if input_year.lower() == 'quit':
                break#break out of loop when user enters any form of "quit"
            else:
                print("Error with the year key! Try another year")
                continue
    pass
    
if __name__ == "__main__":
    main()