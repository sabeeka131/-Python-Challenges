theBoard = {'7': '' , '8': ' ' , '9': '', '4': ' ' , '5': ' ', '6': ' ' , '1': ' ' , '2': ' ' , '3': ' ' }


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


    turn = 'X'
    count = 0




    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")


        move = input()


        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue


        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] in ' ':#across the top
                
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] in ' ':#across the middle
                
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] in ' ':#across the top
                
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] in ' ':#across the top
                
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            if theBoard['3'] == theBoard['6'] == theBoard['9'] in ' ':#across the top
                
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            if theBoard['7'] == theBoard['5'] == theBoard['3'] in ' ':#across the top
                
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            if theBoard['1'] == theBoard['5'] == theBoard['9'] in ' ':#across the top
                
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break


    if count == 9:
        print("\Game Over.\n")
        print("Its a Tie!")


    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'


restart = input("Do you want to play Again?(y/n)")
if restart == "y" or restart == "Y":

        game()


if __name__ == "__main__":
    game()