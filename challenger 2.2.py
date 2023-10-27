#program for create objects batsman and bowler classes and call the play() method for each objects
#create base class player
class player:
  def play(self):
    print("The player is playing cricket.")
#create derived class batsman
class Batsman(player):
  def play(self):
    print("The batsman is batting.")
#create derived class bowler
class Bowler(player):
  def play(self):
    print("The bowler is bowling.")
#creating objects
batsman = Batsman()
bowler = Bowler()
#call the method play()
batsman.play()
bowler.play()