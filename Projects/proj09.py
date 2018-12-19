###########################################################
#  CSE 231 Project 9
#
#Prompt for a file
#   Check that the file can be opened. Print an error and ask again if it cant be
#Read the data in the file and add it to a list
#    Send data to get_hashtag function to get a list of the hashtags in the file
#        Send each hashtag to validate_hastag function to confirm that they are hashtags
#Use the data in the file to get a list of usernames
#Send data and usernames to a function to create a histogram for how often each hashtag is used
#Sort data to get the top 3 hashtags used individually and overall
#Print the data
#Ask to plot
#   If user wants to plot, send data to the plot function
###########################################################i
import string, calendar, pylab
from operator import itemgetter#used for sorting later on

MONTH_NAMES = [calendar.month_name[month] for month in range(1,13)]

def open_file():
    '''asks for what file to open. If a file is entered that doesnt exist,
    prints an error and asks again. If the file is found, breaks out of the loop
    and returns a fp for that file'''
    while True:
        filename = input("Input a filename: ")
        try:
            fp = open(filename,'r')
            break#Break out if the function can be opened
        except FileNotFoundError:
                print("Error in input filename. Please try again.")
#    fp = open('smalldata.csv','r')-----Used for quick testing

    return fp

def validate_hashtag(s):
    '''confirms that the word/string is actaully a hashtag and not just a number
    or a 1 letter word, Returns True/False for hashtag'''
    hashtag=False
    if len(s)>2 and s[0]=='#':#if the word is longer than 1 letter and starts with #
        for item in s[1:]:
            if item in string.punctuation:#if word contains punctuation after the hashtag
                hashtag=False#not a hashtag
                break#stop checking the rest of the word becuase once extra punctuation is found,
                #it can no longer be a hashtag
            else:
                hashtag=True
    return hashtag

def get_hashtags(s):
    '''returns a list of valid hashtags in a tweet'''
    s=s.replace(',',' ')
    s=s.strip().split()#split the data into a list after removing extra spaces
    hashtag_list=[]
    hashtag=False
    for word in s:#for each word
        if word[0]=='#':#if the word starts with '#'
            hashtag=validate_hashtag(word)#send the word to the validate_hashtag function
            if hashtag:#if it is a hashtag
                hashtag_list.append(word)#add to list of hastags
    return hashtag_list

def read_data(fp):
    '''collects username, month, and list of hashtags for each tweet and adds
    them each to a list. Returns the list'''
    data_list=[]
    for line in fp:#for each tweet
        hashtag_list=get_hashtags(line)#send the tweet to the get_hashtags function
        start_list=[]#reset this list for every tweet
        line=line.replace(',',' ')
        line=line.strip().split()#strip the data of extra spaces and split it into a list
        name = line[0]#the first word in the list is the name
        month = line[1]#second word is the month
        name=str(name)#change name into a string
        month=int(month)#change month into an integer
        start_list.append(name)#add to the list
        start_list.append(month)#add to the list
        start_list.append(hashtag_list)#add the list of hashtags to the list
        data_list.append(start_list)#add the list of name,month,hashtags to the final list
    return data_list

def get_histogram_tag_count_for_users(data,usernames):
    '''creates a histogram of hashtags for how often they occur in the form of 
    a dictionary with key:value pair where key is the hashtag and value is the
    number of occurances. Returns the dictionary'''
    data_dict=dict()
    for line in data:#for each tweet
        if line[0] in usernames:#if the name in the tweet is in the list of usernames
            for item in line[2]:#for each hashtag
                if item in data_dict:
                    data_dict[item]+=1#add 1 to the value in the dictionary if it exists
                else:
                    data_dict[item]=1#add the item if not already in the dictionary
    return data_dict

def get_tags_by_month_for_users(data,usernames):
    '''creates a list of tuples where each tuple is in the form (month,{unique hashtags}.
    The list should be 12 items long (one for each month). Returns the list'''
    #[ ( 1 , { } ) , ( 2 , { } ) ]
    hashtags_month=[]
    hashtag_tuple=()
    sorted_data=sorted(data,key=itemgetter(1))#sort the data
    for i in range(1,13):#for the 12 months
        hashtag_set=set()#resets the set for each month
        for line in sorted_data:
            if i==line[1]:
                for item in line[2]:
                    hashtag_set.add(item)#add hashtag to the set (wont add duplicates)
        hashtag_tuple=(i,hashtag_set)#make a tuple of the month and the set of hashtags
        hashtags_month.append(hashtag_tuple)#hadd the tuple to the list
    return hashtags_month

def get_user_names(data_list):
    '''Creates a list of usernames from the file. Sorts alphabetically and returns it.'''
    user_set=set()
    user_list=[]
    for line in data_list:
        user_set.add(line[0])#add each username to the set (wont add duplicates)
    for item in user_set:
        user_list.append(item)#add each unique username to a list
    user_list.sort()#sort the list
    return user_list

def three_most_common_hashtags_combined(data,users):
    '''creates a dictionary with key:value pairs of hashtag:count. Adds those to a list
    and sorts them by count. Removes all but the top 3 values and returns the list.'''
    hashtag_count_dict=dict()
    for line in users:
        for item in data:
            if item[0]==line:#if the names are the same
                for x in item[2]:
                    if x in hashtag_count_dict:
                        hashtag_count_dict[x]+=1#add 1 to dictionary value
                    else:
                        hashtag_count_dict[x]=1#create key in dictionary if it doesnt already exist
    common_list=[]
    for key,value in hashtag_count_dict.items():#add each key,value pair to a list
        common_list.append((value,key))
    sorted_list=sorted(common_list,key=itemgetter(0),reverse=True)#sort the list
    sorted_list=sorted_list[:3]#take the top 3 results
    
    return sorted_list

def three_most_common_hashtags_individuals(data,users):
    '''Creates a list of 3 tuples each of which is in the form (count, hashtag, username). Count is the number of
    times a hashtag shows up only for a user in usernames. The 3 tuples are the 3 highest counts in decreasing order'''
    new_dict=dict()
    list1=[]
    for name in users:
        dict1=get_histogram_tag_count_for_users(data,name)#send data to get_histogram_tag_count_for_users to make a dictionary
        for key,value in dict1.items():#for each key,value pair
            tup=(key,name)#make a tuple of key,value
            if key in new_dict:#if the key is already in the dictionary
                new_dict[tup]=new_dict[tup]+value#add the values
            else:
                new_dict[tup]=value#otherwise, create the key
    for key,value in new_dict.items():
        list1.append((value,key[0],key[1]))#add key,value pair to a list
    sorted_list=sorted(list1,key=itemgetter(0),reverse=True)#sort the list
    sorted_list=sorted_list[:3]#get top 3 results
    return sorted_list
                
            
def similarity(data_list,user1,user2):
    '''Compares the hashtags for each user. Returns the number of hashtags used
    by both users in that month. Returns a list of tuples (month, shared hashtags)'''
    sorted_data=sorted(data_list,key=itemgetter(1))
    similarity_list=[]
    user_set1=set()
    user_set2=set()
    
    for i in range(1,13):#for 12 months
        user_set1=set()
        user_set2=set()
        for line in sorted_data:
            if line[0]==user1:
                    if line[1]==i:
                        for item in line[2]:
                            user_set1.add(item)#add user1 hashtags to a set
                    
            if line[0]==user2:
                    if line[1]==i:
                        for item in line[2]:
                            user_set2.add(item)#add user2 hashtags to a set 
                
        similarity_tuple=(i,(user_set1&user_set2))#make a tuple of the month, and the common hashtags between user1 and user2 (&)
        similarity_list.append(similarity_tuple)#add the tuple to a list
    return similarity_list


def plot_similarity(x_list,y_list,name1,name2):
    '''Plot y vs. x with name1 and name2 in the title.'''
    
    pylab.plot(x_list,y_list)
    pylab.xticks(x_list,MONTH_NAMES,rotation=45,ha='right')
    pylab.ylabel('Hashtag Similarity')
    pylab.title('Twitter Similarity Between '+name1+' and '+name2)
    pylab.tight_layout()
    pylab.show()
    # the next line is simply to illustrate how to save the plot
    # leave it commented out in the version you submit
    #pylab.savefig("plot.png")


def main():
    '''Main function. Calls other functions and prints information'''
    # Open the file
    fp=open_file()
    # Read the data from the file
    data_list=read_data(fp)
    # Create username list from data
    user_list=get_user_names(data_list)
    #create a histogram
    get_histogram_tag_count_for_users(data_list,user_list)
    #create a list of unique hashtags per month
    get_tags_by_month_for_users(data_list,user_list)
    
    # Calculate the top three hashtags combined for all users
    three_combined=three_most_common_hashtags_combined(data_list,user_list)
    
    # Print them
    print()
    print("Top Three Hashtags Combined")
    print("{:>6s} {:<20s}".format("Count","Hashtag"))
    for item in three_combined:
        print("{:>6} {:<20}".format(item[0],item[1]))
    print()
        
    
    # Calculate the top three hashtags individually for all users
    three_individual=three_most_common_hashtags_individuals(data_list,user_list)
    
    
    # Print them
    print("Top Three Hashtags by Individual")
    print("{:>6s} {:<20s} {:<20s}".format("Count","Hashtag","User"))
    for item in three_individual:
        print("{:>6} {:<20} {:<20}".format(item[0],item[1],item[2]))
    print()
    
    
    # Prompt for two user names from username list
    print("Usernames: ", ', '.join(user_list))
    while True:  # prompt for and validate user names
        user_str = input("Input two user names from the list, comma separated: ")
        user_str=user_str.strip().split(',')
        valid=False
        for item in user_list:
            for word in user_str:
                if item.lower()==word.lower():
                    valid=True
                    break
        if valid==False:
            print("Error in user names.  Please try again")
        elif valid==True:
            break
    print()
    user1=user_str[0]
    user2=user_str[1]
    user1=user1.replace(' ','')#remove extra spaces
    user2=user2.replace(' ','')#remove extra spaces
    
    # Calculate similarity for the two users
    similarity_list=similarity(data_list,user1,user2)
    
    # Print them
    print('Similarities for {} and {}'.format(user1,user2))
    print("{:12s}{:6s}".format("Month","Count"))
    for item in similarity_list:
        print("{:12s}{:<6}".format(MONTH_NAMES[item[0]-1],len(item[1])))
    print()

#   Prompt to plot or not and plot if 'yes'
    choice = input("Do you want to plot (yes/no)?: ")
    if choice.lower() == 'yes':
        #create x_list and y_list
        x_list=[1,2,3,4,5,6,7,8,9,10,11,12]
        y_list=[]
        for item in similarity_list:
            y_list.append(len(item[1]))#create y_list of number of hashtag occurances
        plot_similarity(x_list,y_list,user1,user2)

if __name__ == '__main__':
    main()

