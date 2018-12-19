"""
CSE 231 Project #4
Prompt for a ch
    if the ch is more than 1 digit or the return key is pressed, stop asking
    for ch
        check the state of ch (if it moves to the next state or not. 
        Or if it repeats)
        if it does, continue until '!' is entered and set state to 4 (laughing)
        if it doesn't set state to 5 (not laughing)
        if any characters are entered after state is set to 4, change state to 5
        print laughing if state = 4 and not laughing if state = 5
"""

def get_ch(): #prompt for ch
    ch="1"
    ch = input("Enter a character or press the Return key to finish: ")
    return ch

def find_state(state, ch):
    """
    Continue through states, checking the letters for H->a/o->H/!->etc. then
    return the last state reached
    """
    #print('FIND_STATE CH 1', ch) ---- used for testing
    if state==1: #check states
        #print('ONE') ---- used for testing
        if ch=='h':
            #print('TWO') ---- used for testing
            state=2
            return state
        else:
            #print('THREE') ---- used for testing
            state=5
    elif state==2:
        #print('FOUR') ---- used for testing
        if ch=='o' or 'a':
            #print('FIVE') ---- used for testing
            state=3
            return state
        else:
            #print('SIX') ---- used for testing
            state=5
            return state
    elif state==3:
        #print('SEVEN') ---- used for testing
        if ch=='h':
            #print('EIGHT') ---- used for testing
            state=2
            return state
        elif ch=='!':
            #print('NINE') ---- used for testing
            state=4
            return state
        else:
            #print('TEN') ---- used for testing
            state=5
            return state
    elif state==4:
        if ch is not '': #if any other ch is entered set state=5
            state=5
        return state
    if state==5:
        return state
    #print('END FIND_STATE AND STATE', state) ---- used for testing


def main():
    """
    main function. initialize variables and call other functions
    """
    print("I can recognize if you are laughing or not.")
    print("Please enter one character at a time.")

    #initialize variables
    string=""
    state=1
    ch='1'
    laughing = False

    while ch is not '':
        """
        repeatedly ask for characters unless multiple characters are entered or
        return is entered
        """
        #print('WHILE PRE GET_CH',ch,string,state) ---- used for testing
        ch=get_ch()
        if len(ch)>1:#if more than 1 character is entered, try again
            print("Invalid input, please try again.")
            continue
        if ch=='':#if return is pressed, stop asking for characters
            break
        string=string+ch#add the character entered to a string including all characters
        #print('STATE PRE FIND_STATE', state) ---- used for testing
        state = find_state(state,ch)
        if state==4:#if state 4 is reached, you are laughing
            laughing = True
        if state==5:#if state 5 is reached, you are not laughing
            laughing = False
        #print('STATE POST FIND_STATE', state) ---- used for testing

    # when user enters an empty string, you should print the results
    print("\nYou entered", string)
    if laughing:
        print("You are laughing.")
    else:
        print("You are not laughing.")

main()
