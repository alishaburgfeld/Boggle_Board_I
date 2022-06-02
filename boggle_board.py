import random
class BoggleBoard:
  
  def __init__(self):
    self.board=("""    ________
    ________
    ________
    ________""")
    print(self.board)

  def shake(self):
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    boardstr=""
    for i in range(0,17):
      char=random.randrange(0,25)
      boardstr+=alpha[char]
    self.board= f"""    {boardstr[0:4]}
    {boardstr[4:8]}
    {boardstr[8:12]}
    {boardstr[12:16]}"""
    print(self.board)


game_one=BoggleBoard()
game_one.shake()
