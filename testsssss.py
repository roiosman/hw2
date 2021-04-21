import Fish
import Crab
# # aqua_height = 20
# # aqua_width = 50
# # x = 3
# # y = 30
# # board = [' '] * aqua_height
# # for i in range (len(board) ):
# #     board[i] = [' '] * aqua_width
# # for i in range (aqua_height-1):
# #     board[i][0] = "|"
# #     board[i][aqua_width-1] = "|"
# # board[aqua_height - 1][0] = '\\'
# # board[aqua_height - 1][aqua_width - 1] = '/'
# # for i in range (1, aqua_width - 1):
# #     board[2][i] = "~"
# #     board[aqua_height - 1][i] = "_"
# # # for q in board:
# # #     print (*q)
# #
# # # for i in range(aqua_height - 5, aqua_height-1):
# # #     for j in range(x, x + 7):
# # #         if (i == aqua_height - 5):
# # #             if (j == x + 1 or j == x + 5):
# # #                 board[i][j] = "*"
# # #         elif (i == aqua_height - 4):
# # #             if (j == x + 2 or j == x + 3 or j == x + 4):
# # #                 board[i][j] = "*"
# # #         elif (i ==aqua_height - 3):
# # #             board[i][j] = "*"
# # #         elif (i == aqua_height - 2):
# # #             if (j == x or j == x + 6):
# # #                 board[i][j] = "*"
# #
# # # for l in board:
# # #     print (*l)
# #
# #
# # #     print(*board)
# #
# # ocy = [" "]*4
# # for i in range (len(ocy)):
# #     ocy[i] = [' ']  * 7
# # for i in range(0, 5):
# #     for j in range(0, 7):
# #         if (i == 0):
# #             if (j == 1 or j == 5):
# #                 ocy[i][j] = "*"
# #         elif (i == 1):
# #             if (j == 2 or j == 3 or j == 4):
# #                 ocy[i][j] = "*"
# #         elif (i == 2):
# #             ocy[i][j] = "*"
# #         elif (i == 3):
# #             if (j == 0 or j == 6):
# #                 ocy[i][j] = "*"
# #
# # # for m in ocy:
# # #     print (*m)
# #
# # shr = [" "] * 3
# # for i in range(len(shr)):
# #     shr[i] = [" "] * 7
# # for i in range(0, 4):
# #     for j in range(0, 7):
# #         if (i == 0):
# #             if (j == 0 or j == 3):
# #                 shr[i][j] = "*"
# #         elif (i == 1):
# #             if (j != 0):
# #                 shr[i][j] = "*"
# #         elif (i == 2):
# #             if (j == 2 or j == 4):
# #                 shr[i][j] = "*"
# # # for m in shr:
# # #     print (*m)
# #
# # mol = [" "] * 3
# # for i in range(len(mol)):
# #     mol[i] = [" "] * 8
# # for i in range(0, 4):
# #     for j in range(0, 8):
# #         if (i == 0):
# #             if (j == 1 or j == 2 or j == 3 or j ==4 or j == 7):
# #                 mol[i][j] = "*"
# #         elif (i == 1):
# #             mol[i][j] = "*"
# #         elif (i == 2):
# #             if (j == 1 or j == 2 or j == 3 or j == 4 or j == 7):
# #                 mol[i][j] = "*"
# #
# # # for m in mol:
# # #     print (*m)
# #
# #
# # sca = [" "] * 5
# # for i in range(len(sca)):
# #     sca[i] = [" "] * 8
# # for i in range(0, 6):
# #     for j in range(0, 8):
# #         if (i == 0):
# #             if (j ==0 or j == 1 or j == 2 or j == 3 or j == 4 or j == 5):
# #                 sca[i][j] = "*"
# #         elif (i == 1):
# #             if ( j == 4 or j== 5 or j == 6):
# #                 sca[i][j] = "*"
# #         elif (i == 2):
# #             if (j == 2 or j == 3 or j == 4 or j == 5 or j == 6 or j == 7):
# #                 sca[i][j] = "*"
# #         elif (i == 3):
# #             if ( j == 4 or j== 5 or j == 6):
# #                 sca[i][j] = "*"
# #         if (i == 4):
# #             if (j ==0 or j == 1 or j == 2 or j == 3 or j == 4 or j == 5):
# #                 sca[i][j] = "*"
# # #
# # # for m in sca:
# # #     print (*m)
# #
# # for i in range(aqua_height - 6, aqua_height - 1):
# #     for j in range(x, x + 8):
# #         board[i][j] = sca[i - (aqua_height - 6)][j - x]
# # # for i in range(aqua_height - 4, aqua_height - 1):
# # #     for j in range(x, x + 7):
# # #         board[i][j] = shr[i-(aqua_height - 4)][j-x]
# # # for i in range(aqua_height - 5, aqua_height - 1):
# # #     for j in range(15, 15 + 7):
# # #         board[i][j] = ocy[i-(aqua_height - 5)][j-15]
# # for q in board:
# #     print (*q)
# # marks = 90
# # result = isinstance(marks, int)
# # if result:
# #     print("Yes given variable is an instance of type int")
# # else:
# #     print("No given variable is not an instance of type int")
# shr = [" "] * 3
# for i in range(len(shr)):
#     shr[i] = [" "] * 7
# for i in range(0, 4):
#     for j in range(0, 7):
#         if (i == 0):
#             if (j == 0 or j == 3):
#                 shr[i][j] = "*"
#         elif (i == 1):
#             if (j != 0):
#                 shr[i][j] = "*"
#         elif (i == 2):
#             if (j == 2 or j == 4):
#                 shr[i][j] = "*"