
class Player:
    
    def __init__(self, checker):
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        s = ''
        s += 'Player ' + str(self.checker)

        return s
    
    def opponent_checker(self):
        if self.checker == 'X':
            return 'O'
        return 'X'
    
    def next_move(self, b):
        """ Get a next move for this player 
        that is valid for the board b."""
        self.num_moves += 1
        
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == True:
                return col
            else:
                print('Try Again!')
                



        
        
        
        
        
        

