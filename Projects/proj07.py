"""
CSE 231 Project 7
    Prompt for filenames
        IP Address Location
        IP Address Attacks
        Country Names
    Gathers data from each file
        Formats data as an integer and privatizes sensitive information
    Checks which location an attack originated from(country code)
    Checks what country name corresponds with the country code found
    Counts number of attacks from each country
    Prints data if requested
"""
import pylab
from operator import itemgetter #used to sort top 10 attacks later on

def open_file(message):
    """
    Opens file. Prints an error if file isnt found and asks again. 
    Returns the file
    """
    while 1==1:
        file=input(message)#print the input message provided by skelaton code below
        try:
            file=open(file,'r')#tries to open the file
            break#breaks out of the inifinite loop if file can be opened
        except:
            print('File is not found! Try Again!')#if an error is encountered print an error
            continue#ask for new file name
    return file
         
def read_ip_location(file):
    """
    reads the ip locaiton file
    Removes spacing, and unwanted punctuation
    Turns IP into an int with the correct number of digits (after adding 0's)
    returns a list of the IPs and country codes
    """
    line_list=[]
    for line in file:
        line=line.strip()
        line=line.split(',')#remove the spaces and split by the commas
        #my code kept getting this printed with it so I used replace to remove it
        line[0]=line[0].replace(u'\ufeff', '')
        line1=line[0]#initial IP
        line2=line[1]#end IP
        line3=line[2]#country code
        attack_tuple=()
        num_list=[]
        #next few lines are to remove periods from IP and make it into an integer
        #also adds 0's to make the int the correct length
        line1_list=line1.split('.')
        for num in line1_list:
            while 1==1:
                if len(num)<3:
                    num='0'+num
                else:
                    break
            num_list.append(num)
        line1_num=num_list[0]+num_list[1]+num_list[2]+num_list[3]
        line1=(int(line1_num))
        
        #same as above but with the end IP instead of the intital IP
        num_list=[]
        line2_list=line2.split('.')
        for num in line2_list:
            while 1==1:
                if len(num)<3:
                    num='0'+num
                else:
                    break
            num_list.append(num)
        line2_num=num_list[0]+num_list[1]+num_list[2]+num_list[3]
        line2=(int(line2_num))
        attack_tuple=(line1,line2,line3)#add the IP values and country code to a tuple
        line_list.append(attack_tuple)#append the tuple to the a list
    return line_list#returnt the list

def read_ip_attack(file):
    """
    Reads file of attack IPs
    Removes spacing, and unwanted punctuation
    Turns each IP into an int with the correct number of digits
    Adds 'x' to last digits of IP for privacy
    returns a list of the IPs
    """
    line_list=[]
    ip_tuple=()
    for line in file:
        new_line=''
        #remove extra spaces and commas
        line=line.strip()
        line2=line.replace(',','')
        line2=line2.replace(' ','')
        line2=line2+'.xxx'#add "xxx" for privacy
        line=line.split('.')#split by period
        for item in line:
            while 1==1:
                if len(item)<3:
                    item='0'+item#adds 0's for correct length
                else:
                    break
            new_line=new_line+item
        ip_tuple=(int(new_line+'000'),line2)
        line_list.append(ip_tuple)
    return line_list

def read_country_name(file):
    """
    Reads file of country names and the country code they correspond with
    Seperates the two and adds them to a list
    Returns that list
    """
    country_list=[]
    for line in file:
        country_tuple=()
        line=line.strip()
        line=line.split(';')#splits country and code
        country_tuple=(line[1],line[0])#add country and code to a tuple
        country_list.append(country_tuple)#add tuple to a list
    return country_list

def locate_address(ip_list, ip_attack):
    """
    Finds the country code the attack originated from
    """
    for line in ip_list:#for each line in IP list (list of ranges and country codes)
        #if the attack IP is in the range of the IP list...
        if ip_attack >= int(line[0]) and ip_attack <= int(line[1]):
            return line[2]#...return that country code
        else:#otherwise, keep trying
            continue

def get_country_name(country_data, code):
    """
    Finds the country name that corresponds with a country code
    """
    for line in country_data:#goes through each country
        if code==line[0]:#if the country code given matches the country code from the file
            return line[1]#reuturn the country

def bar_plot(count_list, countries):
    """
    Provided by skelaton code. Plots data.
    """
    pylab.figure(figsize=(10,6))
    pylab.bar(list(range(len(count_list))), count_list, tick_label = countries)
    pylab.title("Countries with highest number of attacks")
    pylab.xlabel("Countries")
    pylab.ylabel("Number of attacks")
    
def count_attacks(country_name):
    """
    Counts the number of attacks from each country
    Returns the data
    """
    country_dict=dict()
    for item in country_name:
        if item in country_dict:#If an item is already in the dictionary, add 1
            country_dict[item]+=1
        else:#if item is not in dictionary, add the item and set its value = to 1
            country_dict[item]=1
    return country_dict       

def display_data(data_list,country_final): 
    """
    Prints out given data in correct format
    """
    for item in data_list:#For each attack found, prints the attack IP and country
        print('The IP Address: {:18} originated from {}'.format(item[0],item[1]))
    print()
    print('Top 10 Attack Countries')
    print('{:<9}{}'.format('Country','Count'))
    for item in country_final:#for each country, prints the country code and numbers of attacks
        print('{:<11}{:>3}'.format(item[0],item[1]))
    
def main():
    """
    Main function. Calls other functions and ouputs prompts for file names
    Also sorts the top 10 attacks and gathers data to send to display_data function
    """
    file = open_file("Enter the filename for the IP Address location list: ")
    ip_list = read_ip_location(file)#ip_data

    file = open_file("Enter the filename for the IP Address attacks: ")
    attack_list = read_ip_attack(file)#attack_data
    
    file = open_file("Enter the filename for the country codes: ")
    print()
    country_data = read_country_name(file)
    country_list=list()
    country_code=[]
    data_list=[]
    data_tup=()
    
    for line in attack_list:#for each attack IP
        ip_attack=line[0]#Sets the attack IP = to the privacy IP created earlier
        code=locate_address(ip_list, ip_attack)#gets the country code
        country=get_country_name(country_data,code)#usees country code to get the country name
        country_code.append(code)#adds country code to list
        data_tup=(line[1],country,code)#adds attack ip, country name, and country code to a tuple
        data_list.append(data_tup)#adds above tuple to a list
        
    country_dict=count_attacks(country_code)#creates a dictionary of country:# of attacks
    
    for key,value in country_dict.items():
        country_list.append((key,value))#adds each dictionary key:value pair to a list
        
    country_count=sorted(country_list, key=itemgetter(1,0),reverse=True)#sorts the list by # of attacks
    country_final=sorted(country_count, key=itemgetter(1),reverse=True)#sorts common # of attacks by reverse alphabetical order
    
    while len(country_final)>10:#makes list 10 items long (top 10 attacks)
        del country_final[-1]
        
    display=input('Do you want to display all data? ')
    display=display.lower()
    if display=='yes':
        display_data(data_list,country_final)
    
    answer = input("\nDo you want to plot? ")
    
if __name__ == "__main__":
    main()