import random  
from ps9pr3 import *

class AIPlayer(Player):
    """will look ahead some number of moves into the future to 
    assess the impact of each possible move that it could make 
    for its next move, and it will assign a score to each possible move"""
    
    def __init__(self, checker, tiebreak, lookahead):
        """constructs a new AIPlayer object"""
        
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    
    def __repr__(self):
        """returns a string representing an AIPlayer object"""
        s = super().__repr__()
        s += ' (' + str(self.tiebreak) + ', ' + str(self.lookahead) + ')'
        
        return s
    
    def max_score_column(self, scores):
        """returns the index of the column with the maximum score"""
        idx = [i for i in range(len(scores)) if scores[i] == max(scores)]
        
        if self.tiebreak == 'RIGHT':
            return idx[-1]
        elif self.tiebreak == 'LEFT':
            return idx[0]
        elif self.tiebreak == 'RANDOM':
            return random.choice(idx)
        
    
    def scores_for(self, b):
        """returns a list of scores – one for each col in board b
        """
        scores = [50] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opp_AI = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opp_AI.scores_for(b)
                if max(opp_scores) == 0:
                    scores[col] = 100
                elif max(opp_scores) == 50:
                    scores[col] = 50
                elif max(opp_scores) == 100:
                    scores[col] = 0
                b.remove_checker(col)
        return scores
    
    def next_move(self, b):
        """return the called AIPlayer‘s judgment of its best possible move"""
        self.num_moves += 1
        scores = self.scores_for(b)
        best = self.max_score_column(scores)
        
        return best
                
                
            

        
        