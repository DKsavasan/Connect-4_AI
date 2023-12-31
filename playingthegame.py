 from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b
        

def process_move(p, b):
    """function will perform all of the steps involved 
    in processing a single move by player p on board b"""
    
    print(str(p) + "'s turn")
    
    colnum = p.next_move(b)
    b.add_checker(p.checker, colnum)
    
    print()
    print(b)
    
    if b.is_win_for(p.checker) == True:
        print(str(p) + ' wins in ' + str(p.num_moves) + ' moves')
        print('Congratulations!')
        return True
    elif b.is_full() == True:
        print("It's a tie")
        return True
    else:
        return False
    
    

class RandomPlayer(Player):
    """used for an unintelligent computer player that 
    chooses at random from the available columns"""
    
    def next_move(self, b):
        cols = []
        
        for col in range(b.width):
            if b.can_add_to(col) == True:
                cols += [col]
        
        option = random.choice(cols)
        return option




    
    
        
    
            









    



