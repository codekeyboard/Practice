matrix = [[0,0,0],
          [0,0,0],
          [0,0,0]]
win = 0
player =1

def play(x,player):
    col = int(x%10)
    row = int(x // 10)
    if matrix[row][col] == 0:
        matrix[row][col] = player
    else:
        print("Cell already Taken ! Try again")
        return False
    return True

def print_board():
    for row in matrix:
        print(row)

def check_win(player):
    #check row
    for row in matrix:
        all_match = True
        for item in row:
            if item != player:
                all_match = False
                break
        if all_match: return True

    #check column:
    for col in range(3):
        all_match = True
        for row in range(3):
            if matrix[row][col] != player:
                all_match = False
                break
        if all_match: return True
    

    #check diognal
    all_match = True
    for i in range(3):
        if matrix[i][i] != player:
            all_match = False
    if all_match: return True
        
    all_match = True
    for i in range(3):
        if matrix[i][2-i] != player:
            all_match = False
    if all_match: return True
            


def is_full():
    for row in matrix:
        for item in row:
            if item == 0 :
                return False
    return True




while win == 0:
    print_board()
    x = int(input(f"Enter Row and Column as xy for player {player}: "))
    if play(x, player):
        if check_win(player):
            print_board()
            print(f"Player {player} wins!")
            break
        elif is_full():
            print_board()
            print("It's a draw!")
            break
        player = 2 if player == 1 else 1