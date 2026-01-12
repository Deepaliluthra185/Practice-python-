g =[[2,0,1],
    [1,2,1],
    [2,1,1]]

# def check_winner(game):
#     for row in game:
#         if row[0]==row[2]==row[3]!=0:
#             print(f"winner is {row[0]}")

#     for col in range(3):
#         if game[0][col]==game[0][col]==game[2][col]!=0:
#             print(f"winner is {game[0][col]}")

#         if game[0][0]==game[1][1]==game[2][2]:
#             print(f"winner is {game[0][0]}")

#         elif game[0][2]==game[1][1]==game[2][0]!=0:
#             print(f"winner is {game[0][2]}")

# check_winner(g)
def check_winner(game):

    # Check rows
    for row in game:
        if row[0] == row[1] == row[2] != 0:
            return print(f"Player {row[0]} wins")

    # Check columns
    for col in range(3):
        if game[0][col] == game[1][col] == game[2][col] != 0:
            return print(f"Player {game[0][col]} wins")

    # Check main diagonal
    if game[0][0] == game[1][1] == game[2][2] != 0:
        return print(f"Player {game[0][0]} wins")

    # Check anti-diagonal
    if game[0][2] == game[1][1] == game[2][0] != 0:
        return print(f"Player {game[0][2]} wins")

    return print("No winner")



print(g[0][1])
    