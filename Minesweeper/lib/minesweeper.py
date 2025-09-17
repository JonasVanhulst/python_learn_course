# Filename: minesweeper.py
# Author: Jonas Vanhulst
# Created: 2025-09-25
# Description: Minesweeper game programmed in python.

# General imports
import random

# General defines for the gameboard
minefield_rows: int = 8
minefield_cols: int = 8

# Minefields
minefield: list[list[str]] = [['' for _ in range(minefield_rows)] for _ in range(minefield_cols)]
game_over_minefield: list[list[str]]= [['' for _ in range(minefield_rows)] for _ in range(minefield_cols)]
user_minefield: list[list[str]]= [['' for _ in range(minefield_rows)] for _ in range(minefield_cols)]

def print_header() -> None:
    """
    Printing the game header.

    Parameters:
    None

    Returns:
    None
    """
    print(r"""
 __  __ _                                                   
|  \/  (_)_ __   ___  _____      _____  ___ _ __   ___ _ __ 
| |\/| | | '_ \ / _ \/ __\ \ /\ / / _ \/ _ \ '_ \ / _ \ '__|
| |  | | | | | |  __/\__ \\ V  V /  __/  __/ |_) |  __/ |   
|_|  |_|_|_| |_|\___||___/ \_/\_/ \___|\___| .__/ \___|_|   
                                           |_|              
    """)

def print_bomb() -> None:
    """
    Printing the hit bomb when the players loses.

    Parameters:
    None

    Returns:
    None
    """
    print(r"""
          _.-^^---....,,--
      _--                  --_
     <                        >)
     |                         |
      \._                   _./
         '''--. . , ; .--'''
               | |   |
            .-=||  | |=-.
            `-=#$%&%$#=-'
               | ;  :|
      *****.-'       `-***** 
           (   BOOM!   )
            `-._____.-'
    """)

def print_win() -> None:
    """
    Printing the winning message>

    Parameters:
    None

    Returns:
    None
    """
    
    print(r"""
 __     ______  _    _   _      ____   ____  _   _  __          __   _ _ 
 \ \   / / __ \| |  | | | |    / __ \ / __ \| \ | | \ \        / /  | | |
  \ \_/ / |  | | |  | | | |   | |  | | |  | |  \| |  \ \  /\  / /_ _| | |
   \   /| |  | | |  | | | |   | |  | | |  | | . ` |   \ \/  \/ / _` | | |
    | | | |__| | |__| | | |___| |__| | |__| | |\  |    \  /\  / (_| | | |
    |_|  \____/ \____/  |______\____/ \____/|_| \_|     \/  \/ \__,_|_|_|
                                                                         
                                                                         
                  ★ ☆ ★  YOU WIN!  ★ ☆ ★
    """)

def print_welcome() -> None:
    """
    Printing the welcome message

    Parameters:
    None

    Returns:
    None
    """
    
    print(r"""
__        __   _                                   
\ \      / /__| | ___ ___  _ __ ___   ___ 
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \
  \ V  V /  __/ | (_| (_) | | | | | |  __/
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|
                                                    
    """)

def print_menu() -> None:
    """
    Printing out the game menu

    Parameters:
    None
    
    Returns:
    None
    """
    
    print(r"""
 __  __                      
|  \/  | ___ _ __  _   _ ___ 
| |\/| |/ _ \ '_ \| | | / __|
| |  | |  __/ | | | |_| \__ \
|_|  |_|\___|_| |_|\__,_|___/
                             
    """)

def print_options() -> None:
    """
    Printing out the game menu

    Parameters:
    None
    
    Returns:
    None
    """
    
    print(r"""
+------------------------------------+
|            MAIN  MENU              |
+------------------------------------+
|   [N]  ➤  New Game                 |
|   [L]  ➤  Load Game                |
|   [Q]  ➤  Quit Game                |
+------------------------------------+
    """)

def print_username_prompt() -> None:
    """
    Getting the name of the player

    Parameters:
    None
    
    Returns:
    None
    """
    
    print(r"""
__     ___                _                        
\ \   / (_) _____      __| | ___ _ __ ___   ___    
 \ \ / /| |/ _ \ \ /\ / /| |/ _ \ '_ ` _ \ / _ \   
  \ V / | |  __/\ V  V / | |  __/ | | | | |  __/   
   \_/  |_|\___| \_/\_/  |_|\___|_| |_| |_|\___|   
                                                   
    """)
    print("What is your name?")

def print_loading_dev() -> None:
    """
    Printing out the message of development

    Parameters:
    None
    
    Returns:
    None
    """
    
    print(r"""
 __        ______   _     _   _                _                       
 \ \      / /  _ \ | |   (_) | |              | |                      
  \ \ /\ / /| | | || |__  _  | |     ___  __ _| |_ ___  _ __ ___  ___  
   \ V  V / | |_| || '_ \| | | |    / _ \/ _` | __/ _ \| '__/ _ \/ __| 
    \_/\_/  |____/ |_.__/| | | |___|  __/ (_| | || (_) | | |  __/\__ \ 
                        _/ | |______\___|\__,_|\__\___/|_|  \___||___/ 
                       |__/                                            
                                                                        
          ⚙️  This feature is in development...
                 Please try again later! ⚙️
    """)

def print_goodbye() -> None:
    """
    Printing out a thanks for playing message

    Parameters:
    None
    
    Returns:
    None
    """
    
    print(r"""
   ____                  _ _               
  / ___|___  _ __   __ _| | | ___ _ __ ___ 
 | |   / _ \| '_ \ / _` | | |/ _ \ '__/ __|
 | |__| (_) | | | | (_| | | |  __/ |  \__ \
  \____\___/|_| |_|\__,_|_|_|\___|_|  |___/
                                           
             👋 Thanks for playing!
    """)
    
    exit()

def print_error() -> None:
    """
    Printing error message

    Parameters:
    None
    
    Returns:
    None
    """
    
    print(r"""
  ____                        _     _             
 / ___| _   _  ___  ___ ___  | |__ (_)_ __   __ _ 
 \___ \| | | |/ _ \/ __/ __| | '_ \| | '_ \ / _` |
  ___) | |_| |  __/\__ \__ \ | | | | | | | | (_| |
 |____/ \__,_|\___||___/___/ |_| |_|_|_| |_|\__, |
                                            |___/ 
                                                  
        ⚠️  Oops... Something went wrong! ⚠️
    """)

def create_minefield(mines: int) -> None: 
    """
    Creating the 8x8 minefield filled with the amout of mines the user wants.
    The bombs will placed randomly in the field.

    Parameters:
    mines (int): total of wanted mines by the user

    Returns:
    None
    """
    
    row: int = 0
    col: int = 0

    # Looping through the cols and rows
    while col < minefield_cols:
        row = 0
        while row < minefield_rows:
            minefield[row][col] = '-' # Filling the field with stripes
            user_minefield[row][col] = minefield[row][col]
            game_over_minefield[row][col] = minefield[row][col]
            row += 1
        col += 1
        
    # Generate random mine locations
    all_positions: list[tuple[int, int]] = [(r, c) for r in range(minefield_rows) for c in range(minefield_cols)]
    mine_locations: list[tuple[int, int]] = random.sample(all_positions, mines)

    # Place mines in minefield
    for r, c in mine_locations:
        minefield[r][c] = '*' # Assigning a star into the field as a mine
        game_over_minefield[r][c] = minefield[r][c]
        
def print_minefield() -> None:
    """
    Printing the minefield into the terminal

    Parameters:
    None

    Returns:
    None
    """
    
    col : int = 1
    # Print the minefield
    print('  A B C D E F G H')
    for r in user_minefield:
        print(col, ' '.join(r))
        col += 1
        
    print("\n\n")

def print_game_over_minefield() -> None:
    """
    Printing the minefield with the mine locations.

    Parameters:
    None

    Returns:
    None
    """
    
    col : int = 1
    # Print the minefield
    print('  A B C D E F G H')
    
    # Using the gameover_minefield because this has the mines locations.
    for r in game_over_minefield:
        print(col, ' '.join(r))
        col += 1
        
def parse_move_input(move: str) -> tuple[int, str]:
    """
    Parsing the player move, the move can be first digit or char so this has to be parsed.

    Parameters:
    move (str): Player move (a1, 1a, A1 or 1A).

    Returns:
    tuple[int, str]: the digit and char individualy.
    """
    
    move: str = move.strip().lower() # Collecting the input and set it to lowercase

    digit = None
    letter = None

    # Parsing the string to find which is the digit and which is the char
    for char in move:
        if char.isdigit():
            digit = int(char)
        elif char.isalpha():
            letter = char

    # Returning the tulpe
    if digit is not None and letter is not None:
        return digit, letter
    else:
        print("No valid input!")
    
def print_game_over(game_status: bool) -> None:
    """
    Checking the game status

    Parameters:
    game_status (bool): true or false (if the has ended by clearing all the fields or not).

    Returns:
    None
    """
    
    if game_status == True:
        print_win()
    else:
        print_game_over_minefield()
        print_bomb()
    exit()
    
def get_player_move() -> tuple[bool, bool]:
    """
    Getting the player move and returning game state

    Parameters:
    None

    Returns:
    tulpe[bool, bool]: status and ended by dead ot not
    """
    
    move_y: int = 0
    game_ended: bool = check_field() # Checking if the completed field has been cleared exept the mines.

    print("Please enter your input:")
    move = str(input()) # Collecting the userinput as string

    x, y = parse_move_input(move) # Getting the digit as x and the char as y from the parsed input.

    # Assigning the char to a digit to work in the minefield build up.
    if y.upper() in 'ABCDEFGH':
        move_y = ord(y.upper()) - ord('A')
    else:
        print("Invalid letter.")
        return False, game_ended  # Ensure tuple return

    if minefield[x-1][move_y] == '-':
        print(x, move_y)
        user_minefield[x-1][move_y] = '0'
        return False, game_ended  # Tuple return
    elif minefield[x-1][move_y] == '*':
        return True, False  # Game over and ended
    else:
        print("You have already searched this field!")
        return False, game_ended  # Tuple return
   
def check_field() -> bool:
    """
    Checking of the complete field has been cleared execpt the mines.

    Parameters:
    None

    Returns:
    bool: completed or not
    """
    
    for row in range(minefield_rows):
        for col in range(minefield_cols):
            if user_minefield[row][col] == '-':
                if minefield[row][col] != '*':
                    return False
                else:
                    return True
    return False    

def check_cleared_fields() -> int:
    """
    Couting the cleared fields

    Parameters:
    None

    Returns:
    int: Sum of the cleared fields.
    """
    
    cleared_fields: int = 0
    
    for row in range(minefield_rows):
        for col in range(minefield_cols):
            if user_minefield[row][col] != '-':
                if minefield[row][col] != '*':
                    cleared_fields += 1
    return cleared_fields

def calculate_score(moves: int, total_mines: int) -> None:
    """
    Calculating the process of the user in the game

    Parameters:
    moves (int): Total player moves.
    total_mines (int): Total mines that are in the field.

    Returns:
    None
    """
    
    total_safe_fields = (minefield_rows * minefield_cols) - total_mines
    score_percent = (check_cleared_fields() / total_safe_fields) * 100
    print(f"Your process: {score_percent:.2f}%")

def apply_flood_fill() -> None:
    pass

def play_game(game_tag: str) -> None:
    """
    Using all the above functions to make the game playable

    Parameters:
    game_tag (str): Username fo the player.
    
    Returns:
    None
    """
    
    print("\n──────────────────────────────────────────────────────────────────────────────")
    print(f" 💣  So {game_tag}, how many bombs do you want on the 8x8 field?")
    print("──────────────────────────────────────────────────────────────────────────────")
    user_bombs: int = int(input(" ➤ Enter number of bombs: ")) # Gathering the wanted mines

    print("\n✨ Setting up the battlefield... ✨")
    print(f"🔥 {user_bombs} bombs have been planted. Stay sharp, {game_tag}! 💣\n") # Returning the choise of the user as confirmation.

    # Creating the minefield with the wanted amount of mines
    create_minefield(user_bombs)
    print(r"""
    ╔═══════════════════════════════════════════╗
    ║   🎉 New Minesweeper Field Created! 🎉   ║
    ╚═══════════════════════════════════════════╝
            Have Fun and Watch Out for 💣 !!
    """)

    game_over: bool = False
    game_ended: bool = False
    game_moves: int = 0
    
    # While the player has not been hitted a mine or cleared all fields the game continious to run.
    while not (game_over or game_ended):
        calculate_score(moves=game_moves, total_mines= user_bombs)
        print_minefield()
        game_over, game_ended = get_player_move()
        game_moves += 1 # Adding the move with one
    
    print_game_over(game_status=game_ended)

def play_minesweeper() -> None:
    """
    Playing and configuring the game

    Parameters:
    None

    Returns:
    None
    """
    
    menu_choise: str = ""
    
    print_welcome()
    print_username_prompt()
    username: str = input() # Asking the player to give a username
    
    print_menu()
    print_options()
    
    while menu_choise not in ['n', 'l', 'q']:
        print("Enter your command:")
        menu_choise = input().lower()
    
    match menu_choise:
        case 'n':
            play_game(game_tag = username) # Launching the game        
        case 'l':
            print_loading_dev()
        case 'q':
            print_goodbye()
        case _:
            print_error()
            
        