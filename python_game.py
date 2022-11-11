board = list(range(1, 10))
win_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

def draw_board():
    print("_____________")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
    print("_____________")

def take_input(player_token):
    while True:
        value = input("where i should take a : " + player_token + ':')
        if value not in "123456789":
            print('this field is not out board')
            continue
        value = int(value)
        if str(board[value - 1]) in "XO":
            print("this field is not empty")
            continue
        board[value - 1] = player_token
        break

def check_win():
    for el in win_coord:
        if board[el[0] - 1] == board[el[1] - 1] == board[el[2] - 1]:
            return board[el[1] - 1]
    else:
        return False

def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        if counter > 3:
            winner = check_win()
            if winner:
                draw_board()
                print(winner, 'wins')
                break
        counter += 1
        if counter > 8:
            print('Friendship')
            break
main()