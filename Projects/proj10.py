###########################################################
#   Phase 1
#       Promp for first move
#           Error if invalid move
#           Switch players
#           If a mill is formed, prompt for a piece to remove
#               Error if invalid move
#           Repeat until all 18 pieces have been played
#   Phase 2
#       Prompt for two locations (origin and destination)
#           Error if invalid move
#           If mill is formed, prompt for location to remove
#               Error if invalid location
#           Repeat until a player has only 2 piece remaining
#               Print BANNER
###########################################################




import NMM #import class provided

#Banner to display when somone wins
BANNER = """
    __        _____ _   _ _   _ _____ ____  _ _ _ 
    \ \      / /_ _| \ | | \ | | ____|  _ \| | | |
     \ \ /\ / / | ||  \| |  \| |  _| | |_) | | | |
      \ V  V /  | || |\  | |\  | |___|  _ <|_|_|_|
       \_/\_/  |___|_| \_|_| \_|_____|_| \_(_|_|_)

"""

#title of game and rules
RULES = """
  _   _ _              __  __            _       __  __                 _     
 | \ | (_)_ __   ___  |  \/  | ___ _ __ ( )___  |  \/  | ___  _ __ _ __(_)___ 
 |  \| | | '_ \ / _ \ | |\/| |/ _ \ '_ \|// __| | |\/| |/ _ \| '__| '__| / __|
 | |\  | | | | |  __/ | |  | |  __/ | | | \__ \ | |  | | (_) | |  | |  | \__ \
 |_| \_|_|_| |_|\___| |_|  |_|\___|_| |_| |___/ |_|  |_|\___/|_|  |_|  |_|___/
                                                                                        
    The game is played on a grid where each intersection is a "point" and
    three points in a row is called a "mill". Each player has 9 pieces and
    in Phase 1 the players take turns placing their pieces on the board to 
    make mills. When a mill (or mills) is made one opponent's piece can be 
    removed from play. In Phase 2 play continues by moving pieces to 
    adjacent points. 
    
    The game is ends when a player (the loser) has less than three 
    pieces on the board.

"""

#Game commands
MENU = """

    Game commands (first character is a letter, second is a digit):
    
    xx        Place piece at point xx (only valid during Phase 1 of game)
    xx yy     Move piece from point xx to point yy (only valid during Phase 2)
    R         Restart the game
    H         Display this menu of commands
    Q         Quit the game
    
"""
def is_in_mill(board, place, player):
    """
        Checks if a piece is in a mill. 
        Used to check if the piece can be removed or not
    """
    in_mill=False
    for group in board.MILLS:#for each possible mill
        if place in group:#if the place selected is in that mill
            if board.points[group[0]]==player:#if the first value == the player
                if board.points[group[1]]==player:#and the second value
                    if board.points[group[2]]==player:#and the third
                        in_mill=True#the place is in a mill
    return in_mill

def is_all_mill(board, player):
    """
        Checks if all of a players current pieces are in a mill.
        If so, those pieces can be removed. Returns number of pieces not in a mill
    """
    not_in_mill=set()
    in_mill=set()
    placed_set=placed(board,player)#make a set of all the players pieces
    for group in board.MILLS:
        if board.points[group[0]]==player:
                if board.points[group[1]]==player:
                    if board.points[group[2]]==player:
                        in_mill.add(group[0])#if there is a mill, add each place to a set
                        in_mill.add(group[1])
                        in_mill.add(group[2])
    not_in_mill=in_mill^placed_set#get the unique values of each set
    num_placed=len(not_in_mill)#get the length
    return num_placed#return the length (it will be 0 if all pieces are in a mill)
        
def count_mills(board, player):
    """
        Counts the number of mills currently on the board for a given player.
        Returns the count
    """
    count=0
    for group in board.MILLS:#for each possible mill

        if board.points[group[0]]==player:#if position 1 in the mill == the player
            
            if board.points[group[1]]==player:#and position 2 == the player
        
                if board.points[group[2]]==player:#and position 3 == the player
                    count+=1#add 1 to the count
    return count
            
def place_piece_and_remove_opponents(board, player, destination):
    """
        Adds and removes pieces from the board when necessary. Raises errors if move is not valid
    """
    initial_count=count_mills(board,player)#get the number of mills before a piece is placed/removed
    cont = False#used to only check if mill is formed when the move is valid
    if destination in board.points and board.points[destination]==' ':#if the move is valid
        board.assign_piece(player,destination)#add the piece
        after_count=count_mills(board,player)#count the new number of mills
        cont = True#continue = true. Used later to check if mill is formed
    elif destination.lower()=='h':#if h is entered print the menu
        print(MENU)
    elif destination.lower()=='r':#if r is entered, do nothin
        pass
    elif destination not in board.points:#if move is not valid raise error
        raise RuntimeError('Not a valid location')
    elif board.points[destination]=='X' or board.points[destination]=='O':#if move already has a piece, raise an error
        raise RuntimeError('Error:	Piece already in location.')
    if cont:
        if initial_count != after_count:#if the initial mill count is not the same as the after mill count
            print('A mill was formed!')
            print(board)
            initial_count=0#reset initial and after mill counts
            after_count=0
            remove_piece(board, player)#send to remove_piece function
     
def move_piece(board, player, origin, destination):
    """
        Used in phase 2 to move pieces. Raises errors if move is not valid.
    """
    initial_count=count_mills(board,player)#count number of mills before the move
    opponent=get_other_player(player)#gets the opponent (opposite of player)

    if origin not in board.points:#if first point is invalid
        raise RuntimeError("Error:	Invalid origin point")
    elif destination not in board.points:#if second point is invalid
        raise RuntimeError("Invalid command: Not a valid point")
    elif board.points[origin]==opponent:#if the first point is your opponents point
        raise RuntimeError("Invalid command: Origin point does not belong to player")
    elif board.points[origin]==' ':#if the origin point has no piece
        raise RuntimeError("Error: No piece in origin location")
    elif board.points[destination] != ' ':#if the destination point already has a piece in its location
        raise RuntimeError("Error:	Piece already in location")    
    else:#if no errors raised
        board.clear_place(origin)#remove origin point
        board.assign_piece(player,destination)#place piece at destination
        
    after_count=count_mills(board,player)#count number of mills after the move
    in_mill=is_in_mill(board, destination, player)#check if piece is in a mill
    if in_mill:
        initial_count=0#if piece is in a mill, reset the initial count
        #The above if statement helps if a piece is moved from 1 mill to a different mill.
    if after_count > initial_count:#if the after mill count is greater than the initial mill count
        print('A mill was formed!')
        print()
        print(board)
        initial_count=after_count#set initial count = to after count for next loop
        remove_piece(board, player)#send to the remove piece function to remove the piece
        
def points_not_in_mills(board, player):
    """
        Counts the number of points not in a mill. Returns that number.
        Similar to the is_all_mill function which I felt more comfortable with
        so I generally used that function.
    """
    A = set() #set of occupied points
    
    #loop over each point in the entire board:
        #if that point is occupied by the player:
            #add that point to the set A
    for point in board.points:
        if board.points[point]==player:
            A.add(point)
    
    B = set() #set of occupied points that are also in the mills
    
    #loop over each triplet in the board.MILLS:
        #if the player occupies all positions in the triplet:
            #use set union to include the triplet in the set B
    for group in board.MILLS:
        
        if board.points[group[0]]==player:
            
            if board.points[group[1]]==player:
        
                if board.points[group[2]]==player:
                    B.add(group[0])
                    B.add(group[1])
                    B.add(group[2])
    C = set()
    C = A - B#take the difference of the two
    return C#gives a set of points that are not in a mill

def placed(board,player):
    """
        Creates a set of all points that have a piece
        owned by the player. Returns the set
    """
    placed_set=set()
    for item in board.points:#for every possible point on the board
        if board.points[item]==player:#if that point == player
            placed_set.add(item)#add it to the set
    return placed_set
    
def remove_piece(board, player):
    """
        Takes board and player. Prompts for a location to remove, checks for errors
        and removes that piece from the board.
    """
    a=1#used in in while loop for infinite loop
    opponent=get_other_player(player)#gets the opponent (opposite of player)
    while a==1:#infinite loop until broken out
        remove_command=input('Remove a piece at :> ')#prompt for piece
        if len(remove_command)>2:#if not provided in correct format, print an error
            print('Invalid command: Not a valid point')
            print('Try again.')
            continue#go back to the prompt
        if board.points[remove_command]==opponent:#if the point given == your opponents piece
            in_mill=is_in_mill(board, remove_command, opponent)#check to see if its in a mill
            num_not_in_mill=is_all_mill(board, opponent)#check to see if all the opponents peices are in mills
            if in_mill==False or num_not_in_mill==0:#if the piece is not in a mill or all of their pieces ARE in mills
                board.clear_place(remove_command)#clear the location given
                a+=1#change a to stop the loop
            elif in_mill==True:#if the piece is in a mill, print an error
                print("Invalid command: Point is in a mill")
                print('Try again.')
                continue#go back to the prompt
        elif board.points[remove_command]==player:#If you try to remove your own piece, print error
            print('Invalid command: Point does not belong to player')
            print('Try again.')
            continue
        elif board.points[remove_command]==' ':#if no piece in the provided location, print error
            print('Invalid command: Point does not belong to player')
            print('Try again.')
            continue
                   
def is_winner(board, player):
    """
        Checks to see if a player has less than 3 pieces (2 remaining or less).
        Returns True/False depending on if they do or dont.
    """
    opponent=get_other_player(player)#get the opponent (opposite of player)
    placed_set=placed(board,opponent)#get the number of pieces on the opponenets board in a set
    opponent_count=len(placed_set)#get the length of the set
    if opponent_count<3:#if the length<3, set = to true
        player_win=True
    else:#otherwise, false
        player_win=False
    return player_win
   
def get_other_player(player):
    """
        Get the other player. Provided in skeleton code
    """
    return "X" if player == "O" else "O"

def main():
    """
        Main function. Calls other functions and initializes variables
    """
    #Loop so that we can start over on reset
    command='a'
    while True and command is not 'endgame':#command changes to endgame when game is done which then breaks out of the loop
        #Setup stuff. Prints rules, menu, and board
        print(RULES)
        print(MENU)
        board = NMM.Board()#creates board
        print(board)
        
        player = "X"#starting player is X
        placed_count = 0 # total of pieces placed by "X" or "O", includes pieces placed and then removed by opponent
        
        # PHASE 1
        print(player + "'s turn!")
        command = input("Place a piece at :> ").strip().lower()
        print()
        #Until someone quits or we place all 18 pieces...
        while command != 'q' and placed_count != 18:
            try:
                place_piece_and_remove_opponents(board, player, command)#send to fucntion
                if command.lower() != 'h' and command.lower() != 'r':#if input is not one of the commands
                    player=get_other_player(player)#switch to other player for next turn
                placed_count+=1#add 1 to placed count
            except RuntimeError as error_message:#if an error is raised, print try again
                print("{:s}\nTry again.".format(str(error_message)))
            if command.lower()!='h' and command.lower()!='r':#if input is not one of the commands
                print(board)#print board and whos turn it is again
                print(player + "'s turn!")
            if command.lower()=='r':#if input is r, break out of this loop and start beginning loop again (restart game)
                break
            if placed_count < 18:#as long as there are less than 18 pieces placed
                command = input("Place a piece at :> ").strip().lower()#prompt for next piece
                print()
            else:#once 18 pieces are placed, print phase 2
                print("**** Begin Phase 2: Move pieces by specifying two points")
                command = input("Move a piece (source,destination) :> ").strip().lower()
                
#        Go back to top if reset
        if command == 'r':
            continue

        # PHASE 2 of game
        while command != 'q':
            command = command.split()#split the two points provided
            try:
                if len(command)<2:#if less than 2 points are given, raise an error
                    raise RuntimeError("Invalid number of points")
                move_piece(board, player, command[0], command[1])#send points given to the move_piece function
                player=get_other_player(player)#switch players
            #Any RuntimeError you raise inside this try lands here
            except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message))) 
            opponent=get_other_player(player)#get the opponent
            player_win=is_winner(board, opponent)#check to see if opponenet lost
            if player_win:#if player won, print the banner and end the game
                print(BANNER)
                command='endgame'#used to end the game
                break#breaks out current loop
            print(board)
            print(player + "'s turn!")
            command = input("Move a piece (source,destination) :> ").strip().lower()#prompt again and continue throught the loop as normal
            print()
            
        #If we ever quit we need to return
        if command == 'q':
            return
            
if __name__ == "__main__":
    main()