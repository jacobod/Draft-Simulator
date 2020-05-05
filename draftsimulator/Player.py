

class Player:
    """Player class. 

    Parameters
    ----------
    position: str
        Standardized string representing position (ex: 'qb' = Quarterback)
    name: str
        Player name
    draft_score: float
        Grade from 0-10, represents expert and media consensus.
    projected_round: int
        When player is sent to be selected
    red_flags: float
        0 to 5, rating of risk factor for player given off-field concerns or other
        hard to quantify attributes (weak conference, low size, etc)
        
    """
    def __init__(
        self,
        position,
        name,
        draft_score,
        projected_round,
        red_flags
    ):

        self.position = position
        self.name = name 
        self.draft_score = draft_score
        self.projected_round = projected_round
        self.red_flags = red_flags

    
    def get_attribs(self):
        return {
            "name":self.name,
            "position":self.position,
            "draft_score":self.draft_score,
            "projected_round":self.projected_round,
            "red_flags":self.red_flags
        }