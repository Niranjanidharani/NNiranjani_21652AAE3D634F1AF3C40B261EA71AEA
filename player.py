# Define the base class player
class player:
  def play(self):
    print("The player is playing cricket.")

# Define the derived class Batsman
class batsman(player):
  def play(self):
    print("The batsman is batting.")

# Define the derived class Bowler
class Bowler(player):
 def play(self):
   print("The bowler is bowling.")


# Create object of Batsman and Bowler classes
batsman=batsman()
bowler=Bowler()

# Call the play() method of each object 
batsman.play()
bowler.play()