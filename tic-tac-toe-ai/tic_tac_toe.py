import random as rd

def refresh():
   print("\033[H\033[J", end = '') 

# temporary for testing
# draws board
def draw_board(board):
   refresh()
   print(f"{board[0]} | {board[1]} | {board[2]}")
   print("--+---+--")
   print(f"{board[3]} | {board[4]} | {board[5]}")
   print("--+---+--")
   print(f"{board[6]} | {board[7]} | {board[8]}")

def check_board(conditions, board):
   for a, b, c in conditions:
      if board[a] == board[b] == board[c] and board[a] != " ":
         return board[a]
   if " " not in board:
         return "Tie"
   return None

def minimax(board, depth, is_maximizing, conditions):
    winner = check_board(conditions, board)
    if winner == "X":   
        return 1
    elif winner == "O": 
        return -1
    elif winner == "Tie":
        return 0

    if is_maximizing: 
        best_score = -999
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, False, conditions)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:  
        best_score = 999
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, True, conditions)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score


def ai_move(board, conditions, difficulty):
   if difficulty < 2:
      for a, b, c in conditions:
         line = [board[a], board[b], board[c]]
         if line.count("X") == 2 and line.count(" ") == 1:
               return [a, b, c][line.index(" ")]  
         
      for a, b, c in conditions:
         line = [board[a], board[b], board[c]]
         if line.count("O") == 2 and line.count(" ") == 1:
               return [a, b, c][line.index(" ")]  
      
      if difficulty == 1:
         if board[4] == " ":
            return 4
         
         for move in [0, 2, 6, 8]:
            if board[move] == " ":
                  return move
      
      choices = [i for i, v in enumerate(board) if v == " "]
      return rd.choice(choices)
   else: 
      best_score = -999
      move = None
      for i in range(9):
         if board[i] == " ":
               board[i] = "X"  # try the move
               score = minimax(board, 0, False, conditions)
               board[i] = " "  # undo move
               if score > best_score:
                  best_score = score
                  move = i
      return move


board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

draw_board(board)

locations = [0, 0, 0, 0, 0, 0, 0, 0, 0]

remaining = locations.count(0)
choices = [i for i, val in enumerate(locations) if val == 0]

difficulty = int(input("Choose a difficulty(0- fair, 1- mostly fair, 2- unfair): "))

while remaining != 0:
   
   selected = ai_move(board, conditions, difficulty)
   locations[selected] = 1
   board[selected] = "X"
   draw_board(board)
   winner = check_board(conditions=conditions, board=board)
   if winner: 
      print(winner)
      break

   print(locations)
   player  = int(input("select location: "))
   while locations[player] == 1:
      player  = int(input("Location already selected, try again: "))
   locations[player] = 1
   board[player] = "O"
   draw_board(board)
   winner = check_board(conditions=conditions, board=board)
   if winner: 
      print(winner)
      break

   choices = [i for i, val in enumerate(locations) if val == 0]
   remaining = locations.count(0)
   if remaining == 0:
      break

