def print_board_given_size(x,y,grid):
    for i in range(x):
        print(" ---"*x)
        for j in range(y):
            if grid[i][j] != 0 :
                print("| "+str(grid[i][j])+" ", end="")
            else:
                print("|   ", end="")
        print("|")

def has_someone_won(grid):
	# rows
	for x in range(0,3):
		row = set([grid[x][0],grid[x][1],grid[x][2]])
		if len(row) == 1 and grid[x][0] != 0:
			return grid[x][0]

	# columns
	for x in range(0,3):
		column = set([grid[0][x],grid[1][x],grid[2][x]])
		if len(column) == 1 and grid[0][x] != 0:
			return grid[0][x]

	# diagonals
	diag1 = set([grid[0][0],grid[1][1],grid[2][2]])
	diag2 = set([grid[0][2],grid[1][1],grid[2][0]])
	if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
		return grid[1][1]

	return 0

def is_valid_input(game,i,j):
    if j is None or i is None :
        return False
    if i > 2 or j > 2 or i < 0 or j < 0:
        return False
    if game[i][j] == 0:
        return True
    return False

def play_tic_tac_toe():
    game = [[0, 0, 0],
	        [0, 0, 0],
	        [0, 0, 0]]
    player1 = 0
    player2 = 0   
    while has_someone_won(game) == 0:
        for player in range(1,3):
            print_board_given_size(len(game),len(game[0]),game) 
            symbol = 'O'
            if player == 1 :
                symbol = 'X'
            pos = [-1,-1]
            while not is_valid_input(game,int(pos[0])-1,int(pos[1])-1):
                playerInput = input("Player "+ str(player) + " choose your cell (use i,j): ")
                if "," in playerInput:
                    pos = playerInput.strip().split(",")
            game[int(pos[0]) -1 ][int(pos[1]) - 1 ] = symbol
            if has_someone_won(game) != 0:
                print("Player " + str(player) + " has won!" )
                if player == 1 :
                    player1 += 1
                elif player == 2:
                    player2 += 1
                print("Total score\nPlayer 1: "+str(player1)+"\nPlayer 2: "+str(player2))
                play_again = input("Play again (Y/N)? : ")
                if play_again == "y":
                    game = [[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]
                break

if __name__ == "__main__":    
    play_tic_tac_toe()