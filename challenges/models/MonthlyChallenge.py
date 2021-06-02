import json

class Challenge():
    def __init__(self, title, status='added') -> None:
        self._title:str = title
        self._status:str = status
        
class MonthlyChallenge():
    def __init__(self, month) -> None:
        self._month=month
        self._challenges=[]
    
    def add_challenge(self, challenge: Challenge):
        self._challenges.append(challenge)
        return True

challenge = MonthlyChallenge('May')
challenge.add_challenge(Challenge('May challenge1'))
print(json.dumps(challenge, default=lambda o: o.__dict__))
