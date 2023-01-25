def draw_board(vakje):
  board = (f"{vakje[7]}|{vakje[8]}|{vakje[9]}\n"
             f"{vakje[4]}|{vakje[5]}|{vakje[6]}\n"
             f"{vakje[1]}|{vakje[2]}|{vakje[3]}")
  print(board)


def check_beurt(beurt):
  if beurt % 2 == 0: return 'O'
  else: return 'X'

def check_for_win(vakje):
  # Handle Horizontal Cases
  if   (vakje[1] == vakje[2] == vakje[3]) \
    or (vakje[4] == vakje[5] == vakje[6]) \
    or (vakje[7] == vakje[8] == vakje[9]):
    return True
  # Handle Vertical Cases
  elif   (vakje[1] == vakje[4] == vakje[7]) \
    or (vakje[2] == vakje[5] == vakje[8]) \
    or (vakje[3] == vakje[6] == vakje[9]):
    return True
  # Diagonal Cases
  elif (vakje[1] == vakje[5] == vakje[9]) \
    or (vakje[3] == vakje[5] == vakje[7]):
    return True
    
  else: return False
