import random
class BoggleBoard:
  
  def __init__(self):
    self.board=("""    ________
    ________
    ________
    ________""")
    print(self.board)
    self.boggle_dice=[["AAEEGN"], ["ELRTTY"], ["AOOTTW"], ["ABBJOO"], ["EHRTVW"], ["CIMOTU"], ["DISTTY"], ["EIOSST"], ["DELRVY"], ["ACHOPS"], ["HIMNQU"], ["EEINSU"], ["EEGHNW"], ["AFFKPS"], ["HLNNRZ"],["DEILRX"]]

    
  def shake(self):
    board_array=[[],[],[],[]]
    for list in board_array:
        while len(list) < 4:
            dice_index=random.randrange(0,15)
            char_index=random.randrange(0,5) 
            list.append(self.boggle_dice[dice_index][0][char_index])
    
    print_board=board_array.copy()

    for list in print_board:
        for i, char in enumerate(list):
            if char=="Q":
                list[i]="Qu "
            else: list[i]=f"{char}  "
        print("".join(list))


game_one=BoggleBoard()
game_one.shake()