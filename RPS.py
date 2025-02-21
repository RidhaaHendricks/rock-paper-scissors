# The example function below keeps track of the opponent's history and plays 
# whatever the opponent played two plays ago. It is not a very good player so 
# you will need to change the code to pass the challenge.
import random

winning_play = {
  "R": "P",
  "P": "S",
  "S": "R"
}

def player(prev_play, opponent_history=[]):
  play = ""

  if prev_play == "":
    opponent_history = []
    play = random.choice(["R", "P", "S"])
  elif len(opponent_history) < 3:
    opponent_history.append(prev_play)
    play = random.choice(["R", "P", "S"])
  elif opponent_history[-1] == opponent_history[-2]:
    opponent_history.append(prev_play)
    play = winning_play[prev_play]
  elif opponent_history[-1] != opponent_history[-2]:
    opponent_history.append(prev_play)
    play = winning_play[winning_play[prev_play]]
  else:
    opponent_history.append(prev_play)
    play = random.choice(["R", "P", "S"])

  return play