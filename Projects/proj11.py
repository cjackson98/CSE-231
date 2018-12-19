###########################################################
#   CSE 231 Project 11
#   Loop:
#    Display board and current player
#        Prompt for position to place piece at
#            Raise an error if the point provided is invalid
#        Place piece in spot if position is valid
#            Raise error if spot is occupied or not in range of board
#    Check for a winner
#        If no winner, switch players and continue loop
#           Continue until winner is found.
#        If winner is found, stop asking for a position and display winning...
#        ...and  player. Break out of loop
###########################################################


class GoPiece(object):
    '''Used to create/gather data for the pieces in the game.'''
    
    def __init__(self,color='black'):
        '''Initializes variables used in the class. Creates the game piece.'''
        self.__color=color
        if self.__color!="black" and self.__color!="white":
            raise MyError('Wrong color.')#raise error if the color is black or white
    
    
    def __str__(self):
        '''Converts color provided into a game piece and returns it'''
        if self.__color=='black':
            return ' ● '
        elif self.__color=='white':
            return ' ○ '
    
    
    def get_color(self):
        '''Gets the color of a piece and returns it'''
        return (self.__color)
    
#    def __repr__(self): #Used for testing
#        return self.__str__()
            
    
class MyError(Exception):
    """ Used for when an error is encountered """
    def __init__(self,value):
        self.__value = value
    def __str__(self):
        return self.__value


class Gomoku(object):
    '''Class that contains most of the code for the game. Assigns pieces,
    checks for winners, prompts for positions, creates board, etc.'''
    
    def __init__(self,board_size=15,win_count=5,current_player='black'):
        ''' Initializes variables to be used in the rest of the class. Raises error
        if the board size/win count arent integers or if the color is not black or white'''
        self.__board_size=board_size
        self.__win_count=win_count
        self.__current_player=current_player
        
        if type(self.__board_size)!=int:
            raise ValueError
        if type(self.__win_count)!=int:
            raise ValueError
        if self.__current_player!="black" and self.__current_player!="white":
            raise MyError('Wrong color.')  

        self.__go_board = [ [ ' - ' for j in range(self.__board_size)] for i in range(self.__board_size)]
 
            
    def assign_piece(self,piece,row,col):
        ''' Places a piece at the specified position. Raises error if the position
        is not in the range of the board.'''
        row=int(row)
        col=int(col)
        if row < 1 or row > self.__board_size:
            raise MyError('Invalid position.')
        if col < 1 or col > self.__board_size:
            raise MyError('Invalid position.')
        if self.__go_board[row-1][col-1]!=' - ':
            raise MyError('Position is occupied.')
        self.__go_board[row-1][col-1]=piece
        
            
    def get_current_player(self):
        ''' Gets the current player (the player whose turn it is currently) and
        returns the color of their piece as a string'''
        return(str(self.__current_player))
        
    
    def switch_current_player(self):
        ''' Returns the opposite (of the player whose turn it is) players color
        as a string. '''
        current_player=Gomoku.get_current_player(self)
        if current_player=='black':
            self.__current_player='white'
            return 'white'
        elif current_player=='white':
            self.__current_player='black'
            return 'black'
        
        
    def __str__(self):
        """ Provided. Formats/creates board and current players turn. """
        s = '\n'
        for i,row in enumerate(self.__go_board):
            s += "{:>3d}|".format(i+1)
            for item in row:
                s += str(item)
            s += "\n"
        line = "___"*self.__board_size
        s += "    " + line + "\n"
        s += "    "
        for i in range(1,self.__board_size+1):
            s += "{:>3d}".format(i)
        s += "\n"
        s += 'Current player: ' + ('●' if self.__current_player == 'black' else '○')
        return s
        
    
    def current_player_is_winner(self):
        ''' Checks to see if the current player (whose turn is it) has 5 pieces
        in a row horizontally, vertically, or diagonally.'''
        piece=self.__current_player
        piece=GoPiece(piece)
        ctr=0#ctr of how many pieces in a row a player has
        win=False
        
        for item in self.__go_board:#horizontal
            for x in item:#for each value in each row
                x=str(x)#convert the value at the current position to a string
                piece=str(piece)#converts the piece to a string
                if x == piece:#if the two are the same, add one to the counter
                    ctr+=1
                else:#if the two arent the same, reset the counter
                    ctr=0
                if ctr>=5:#if the counter reaches 5 or more pieces in a row
                    win=True#player wins
                    break#stop checking
            if win==True:#if a winner has already been found, stop checking
                break
            
            
        if win==False:#Only do this if a winner has not been found yet
            for row in range(self.__board_size):#vertical
                for col in range(self.__board_size):#for each item in each column
                    x=str(self.__go_board[col][row])#get the value at the position
                    piece=str(piece)
                    if x == piece:
                        ctr+=1
                    else:
                        ctr=0
                    if ctr>=5:#if the counter reaches 5 or more pieces in a row
                        win=True#player wins
                        break#stop checking
                if win==True:#if winner found, stop checking
                    break
                
        from collections import defaultdict
        diag_list = defaultdict(list)#an automatically intialized empty list from collections
        for row in range(self.__board_size):#each row
                for col in range(self.__board_size):#each column
                        diag_list[col-row].append(self.__go_board[row][col])#append the item at [row][col] to the list at place [column-row]
                        #"diag_list[col-row].append" is possible because of "from collections import defaultdict" and "diag_list = defaultdict(list)"
        for key,value in diag_list.items():#iterate through the list (of diagonal rows)
            for item in value:#for each item in the diagonal row
                item=str(item)
                piece=str(piece)
                if piece==item:#if the the item = the piece, add 1 and continue
                    ctr+=1
                else:#if the item is not the players piece, reset the count
                    ctr=0
                if ctr>=5:#once the count reaches 5 or more, break out of the loop and win = True
                    win=True
                    break
        
        #The following is the same as the block above but when appending to the list
        #I changed the place its being appended to from x-y to x+y to account for the 
        #opposite diagonal direction (e.g. positive vs negative slope)
        diag_list = defaultdict(list)#create an empty dictionary with lists
        for row in range(self.__board_size):
                for col in range(self.__board_size):
                        diag_list[col+row].append(self.__go_board[row][col])
        for key,value in diag_list.items():
            for item in value:
                item=str(item)
                piece=str(piece)
                if piece==item:
                    ctr+=1
                else:
                    ctr=0
                if ctr>=5:
                    win=True
                    break
               
        return win#return win (true or false)
    
    
def main():
    board = Gomoku()#create board
    print(board)
    win=False#default value for win is false
    play = input("Input a row then column separated by a comma (q to quit): ")
    piece=GoPiece()#get the piece
    while play.lower() != 'q':
        play_list = play.strip().split(',')#split the input into seperate values
        try:
            if len(play_list)!=2:#if more or less than 2 values are provided, raise an error
                raise MyError("Incorrect input.")
            for item in play_list:
                if item.replace('-','').isnumeric()==False:#make sure each value is a number (remove - when checking)
                    raise MyError("Incorrect input.")
            board.assign_piece(piece, play_list[0], play_list[1])#place piece at position
            if board.current_player_is_winner()==True:#check for winner
                win=True

        except MyError as error_message:#if an error is ever raised
            print("{:s}\nTry again.".format(str(error_message)))#try again
            print(board)#print board
            play = input("Input a row then column separated by a comma (q to quit): ")#ask for input again
            continue#skip the remaining code in the loop
        if win==False:#if no winner is found yet, switch players and ask for next input
            piece=board.switch_current_player()
            piece=GoPiece(piece)
            print(board)
            play = input("Input a row then column separated by a comma (q to quit): ")
        elif win==True:#if a winner is found, print winning board and player
            print(board)
            print("{} Wins!".format(board.get_current_player()))
            break#stop looping through and end the game


if __name__ == '__main__':
    main()
