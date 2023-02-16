#The overall goal of this program is to build a Sudoku game. it has 3 modes 
# easy, medium and hard
import random 

#board list to capture the number for the display board
board_display=[[' ',' ',' ',' ',' ',' ',' ',' ',' '],
               [' ',' ',' ',' ',' ',' ',' ',' ',' '],
               [' ',' ',' ',' ',' ',' ',' ',' ',' '],
               [' ',' ',' ',' ',' ',' ',' ',' ',' '],
               [' ',' ',' ',' ',' ',' ',' ',' ',' '],
               [' ',' ',' ',' ',' ',' ',' ',' ',' '],
               [' ',' ',' ',' ',' ',' ',' ',' ',' '],
               [' ',' ',' ',' ',' ',' ',' ',' ',' '],
               [' ',' ',' ',' ',' ',' ',' ',' ',' '],]

easy_mode = 35
medium_mode = 30
hard_mode = 25

#creating a list to store the numbers in the specific rows, columns or sections         
row_lst=[[],[],[],[],[],[],[],[],[]] 
col_lst=[[],[],[],[],[],[],[],[],[]] 
section_lst=[[],[],[],[],[],[],[],[],[]] 

#Creating a fuction to define the 9 different sections of 3*3 each
def sections(row_num,col_num):
    if row_num<=3 and col_num<=3:
        return section_lst[0]
    elif row_num<=3 and col_num>=4 and col_num<=6:
        return section_lst[1]
    elif row_num<=3 and col_num>=7 and col_num<=9:
        return section_lst[2]
    elif col_num<=3 and row_num>=4 and row_num<=6:
        return section_lst[3]
    elif row_num>=4 and row_num<=6 and col_num>=4 and col_num<=6:
        return section_lst[4]
    elif row_num>=4 and row_num<=6 and col_num>=7 and col_num<=9:
        return section_lst[5]
    elif row_num>=7 and row_num<=9 and col_num<=3:
        return section_lst[6]
    elif row_num>=7 and row_num<=9 and col_num>=4 and col_num<=6:
        return section_lst[7]
    elif row_num>=7 and row_num<=9 and col_num>=7 and col_num<=9:
        return section_lst[8]

# Function to setup intial board with random numbers in different sections/rows/column
# based on the difficuly level of the game      
def setup_game_board(game_mode):
    count=0
    
    if game_mode == 'e':
        init_count = easy_mode
    elif game_mode == 'm':
        init_count = medium_mode
    elif game_mode == 'h':
        init_count = hard_mode
    
    while count<init_count:
        random_row_num=random.randint(1,9)
        random_col_num=random.randint(1,9)
        random_num=random.randint(1,9)
        if board_display[random_row_num-1][random_col_num-1] !=' ':
            continue 
        elif random_num in row_lst[random_row_num-1] or random_num in col_lst[random_col_num-1] or random_num in sections(random_row_num,random_col_num):
            continue
        else:
            board_display[random_row_num-1][random_col_num-1]=random_num
            row_lst[random_row_num-1].append(random_num)
            col_lst[random_col_num-1].append(random_num)
            sections(random_row_num,random_col_num).append(random_num)
            count+=1
    display_game_board()

#Creating the game board. It display all the numbers on the game board based on user 
# selection
def display_game_board():
    print('|=====================================|')
    for i in range(3):
        for j in range(3):
            print('|',board_display[i][j],end =" ")
        print('|',end="")
        for j in range(3):
            print('|',board_display[i][j+3],end =" ")
        print('|',end="")    
        for j in range(3):
            print('|',board_display[i][j+6],end =" ")  
        print('|')
        if i < 2 :
            print('|-----------  -----------  -----------|')
    print('|===========  ===========  ===========|')
    for i in range(3):
        for j in range(3):
            print('|',board_display[i+3][j],end =" ")
        print('|',end="")
        for j in range(3):
            print('|',board_display[i+3][j+3],end =" ")
        print('|',end="")    
        for j in range(3):
            print('|',board_display[i+3][j+6],end =" ")  
        print('|')
        if i < 2 :
            print('|-----------  -----------  -----------|')
    print('|===========  ===========  ===========|')
    for i in range(3):
        for j in range(3):
            print('|',board_display[i+6][j],end =" ")
        print('|',end="")
        for j in range(3):
            print('|',board_display[i+6][j+3],end =" ")
        print('|',end="")    
        for j in range(3):
            print('|',board_display[i+6][j+6],end =" ")  
        print('|')
        if i < 2 :
            print('|-----------  ------------  ----------|')
    print('|=====================================|')

# function to define the main logic of the same. Based on user input (add or remove),
# it checks if the number can be added in particular row, col or section or throw error
# or if the number can be remove from the display board and other lists
def game_logic(player_input,row_num,col_num):
    
    if player_input == 'a':
        num=int(input('Enter in a number 1-9: '))
        while board_display[row_num-1][col_num-1] !=' ':
            print('X')
            row_num=int(input('Enter row number: '))
            col_num=int(input('Enter col number: '))
            num=int(input('Enter in a number 1-9: '))
        if num in row_lst[row_num-1] or num in col_lst[col_num-1] or num in sections(row_num,col_num):
            print('X')
        else:
            board_display[row_num-1][col_num-1]=num
            row_lst[row_num-1].append(num)
            col_lst[col_num-1].append(num)
            sections(row_num,col_num).append(num)
    elif player_input == 'r':
        if board_display[row_num-1][col_num-1] != ' ':
            num = board_display[row_num-1][col_num-1]
            board_display[row_num-1][col_num-1] = ' '
            row_lst[row_num-1].remove(num)
            col_lst[col_num-1].remove(num)
            sections(row_num,col_num).remove(num)

# choose game mode (easy, medium or hard)
game_mode_input=input('Choose game mode: easy (e) or medium (m) or hard (h): ')    
setup_game_board(game_mode_input)


# play the game
while True:
    player_input=input('add (a) or remove (r) or quit (q): ')
    if player_input=='q':
        break 

    row=int(input('Enter row number: '))
    col=int(input('Enter col number: '))
    
    game_logic(player_input,row,col)

    display_game_board()