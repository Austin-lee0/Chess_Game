class Board:
    game_Tiles = {}

    def __init__(self):
        pass

    def copy(self):
        b = Board()
        b.game_Tiles = self.game_Tiles.copy()#passing through by value and passing through by reference, this is by value
        return b

    def createBoard(self):
        for tiles in range(64):
            self.game_Tiles[tiles] = Tiles(tiles,Null_Piece)

        self.game_Tiles[0] = Tiles(0,Rook(0,"B"))
        self.game_Tiles[1] = Tiles(1,Knight(1,"B"))
        self.game_Tiles[2] = Tiles(2,Bishop(2,"B"))
        self.game_Tiles[3] = Tiles(3,Queen(3,"B"))
        self.game_Tiles[4] = Tiles(4, King(4,"B"))
        self.game_Tiles[5] = Tiles(5, Bishop(5,"B"))
        self.game_Tiles[6] = Tiles (6, Knight(6,"B"))
        self.game_Tiles[7] = Tiles (7, Rook(7,"B"))

        for i in range(8,16):
            self.game_Tiles[i] = Tiles(i,Pawn(i,"B"))

        for i in range(48,56):
            self.game_Tiles[i] = Tiles(i,Pawn(i,"W"))

        self.game_Tiles[56] = Tiles(56,Rook(56,"W"))
        self.game_Tiles[57] = Tiles(57,Knight(57,"W"))
        self.game_Tiles[58] = Tiles(58,Bishop(58,"W"))
        self.game_Tiles[59] = Tiles(59,Queen(59,"W"))
        self.game_Tiles[60] = Tiles(60, King(60,"W"))
        self.game_Tiles[61] = Tiles(61, Bishop(61,"W"))
        self.game_Tiles[62] = Tiles (62, Knight(62,"W"))
        self.game_Tiles[63] = Tiles (63, Rook(63,"W"))

        #putting on the chess pieces
    def printBoard(self):
        for i in range(64):
            print('|', end = (self.game_Tiles[i].piece_on_tile.layout()))
            if ((i + 1) % 8 == 0):# writing some code!
                print("|", end = "\n")

class Tiles:
    piece_on_tile = None
    tile_coordinate = None
    def __init__(self, coordinates,piece):
        self.tile_coordinates = coordinates
        self.piece_on_tile = piece

class Piece:
    first_column = [0,8,16,24,32,40,48,56]
    neg_first_column = [-8,-16,-24,-32,-40,-48,-56]
    second_column = [1,9,17,25,33,41,49,57]
    third_column = [2,10,18,26,34,42,50,58]
    fourth_column = [3,11,19,27,35,43,51,59]
    fifth_column = [4,12,20,28,36,44,52,60]
    sixth_column = [5,13,21,29,37,45,53,61]
    seventh_column = [6,14,22,30,38,46,54,62]
    eighth_column = [7,15,23,31,39,47,55,63]

    first_row = [0,1,2,3,4,5,6,7]
    second_row = [8,9,10,11,12,13,14,15]
    third_row = [16,17,18,19,20,21,22,23]
    fourth_row = [24,25,26,27,28,29,30,31]
    fifth_row = [32,33,34,35,36,37,38,39]
    sixth_row = [40,41,42,43,44,45,46,47]
    seventh_row = [48,49,50,51,52,53,54,55]
    eighth_row = [56,57,58,59,60,61,62,63]

    first_diagonal_up = [0]
    second_diagonal_up = [8,1]
    third_diagonal_up = [16,9,2]
    fourth_diagonal_up = [24,17,10,3]
    fifth_diagonal_up = [32,25,18,11,4]
    sixth_diagonal_up = [40,33,26,19,12,5]
    seventh_diagonal_up = [48,41,34,27,20,13,6]
    eighth_diagonal_up = [56,49,42,35,28,21,14,7]
    ninth_diagonal_up = [57,50,43,36,29,22,15]
    tenth_diagonal_up = [58,51,44,37,30,23]
    eleventh_diagonal_up = [59,52,45,38,31]
    twelfth_diagonal_up = [60,53,46,39]
    thirteenth_diagonal_up = [61,54,47]
    fourteenth_diagonal_up = [62,55]
    fifteenth_diagonal_up = [63]

    first_diagonal_down = [7]
    second_diagonal_down = [6,15]
    third_diagonal_down = [5,14,23]
    fourth_diagonal_down = [4, 13, 22, 31]
    fifth_diagonal_down = [3, 12, 21, 30, 39]
    sixth_diagonal_down = [2, 11, 20, 29, 38, 47]
    seventh_diagonal_down = [1, 10, 19, 28, 37, 46, 55]
    eighth_diagonal_down = [0, 9, 18, 27, 36, 45, 54, 63]
    ninth_diagonal_down = [8,17,26,35,44,53,62]
    tenth_diagonal_down = [16,25,34,43,52,61]
    eleventh_diagonal_down = [24,33,42,51,60]
    twelfth_diagonal_down = [32,41,50,59]
    thirteenth_diagonal_down = [40,49,58]
    fourteenth_diagonal_down = [48,57]
    fifteenth_diagonal_down = [56]


#if the destination is still in the diagonal, its a legal move, i dont need to do all that self.pos in there

    def __init_(self):
        self.pos = pos
        self.color = color

    @classmethod
    def get_down_diagonals(cls):
        return[cls.first_diagonal_down,cls.second_diagonal_down,cls.third_diagonal_down,cls.fourth_diagonal_down, cls.fifth_diagonal_down, cls.sixth_diagonal_down,cls.seventh_diagonal_down, cls.eighth_diagonal_down,cls.ninth_diagonal_down,cls.tenth_diagonal_down,cls.eleventh_diagonal_down,cls.twelfth_diagonal_down,cls.thirteenth_diagonal_down,cls.fourteenth_diagonal_down,cls.fifteenth_diagonal_down]
    @classmethod
    def get_up_diagonals(cls):
        return[cls.first_diagonal_up,cls.second_diagonal_up,cls.third_diagonal_up,cls.fourth_diagonal_up, cls.fifth_diagonal_up, cls.sixth_diagonal_up,cls.seventh_diagonal_up, cls.eighth_diagonal_up,cls.ninth_diagonal_up,cls.tenth_diagonal_up,cls.eleventh_diagonal_up,cls.twelfth_diagonal_up,cls.thirteenth_diagonal_up,cls.fourteenth_diagonal_up,cls.fifteenth_diagonal_up]

    @classmethod
    def get_columns(cls):
        return [cls.first_column, cls.second_column, cls.third_column, cls.fourth_column,cls.fifth_column,cls.sixth_column,cls.seventh_column, cls.eighth_column]
    @classmethod
    def get_rows(cls):
        return [cls.first_row, cls.second_row, cls.third_row, cls.fourth_row,cls.fifth_row,cls.sixth_row,cls.seventh_row, cls.eighth_row]

    def empty_tile_or_enemy_tile(self,board ,destination):
        if board.game_Tiles[destination].piece_on_tile.layout() == '-' or self.color == "B" and board.game_Tiles[destination].piece_on_tile.layout().islower() \
        or self.color == "W" and board.game_Tiles[destination].piece_on_tile.layout().isupper():
            return True
        else:
            return False

    def right_horizontal_check_in_way(self, board, destination):
        right_adjacent_square = self.pos + 1
        for check_tile in range(right_adjacent_square, destination):
            if board.game_Tiles[check_tile].piece_on_tile.layout() != "-":
                return False

        return True

    def left_horizontal_check_in_way(self, board, destination):
        right_destination = destination + 1
        for check_tile in range(right_destination,self.pos):
            if board.game_Tiles[check_tile].piece_on_tile.layout() != "-":
                return False
        return True

    def down_vertical_check_in_way(self, board, destination):
        down_adjacent_square = self.pos + 8
        for check_tile in range(down_adjacent_square,destination):
                #(index, element at index)

            column_list = Piece.get_columns()
            for i,col in enumerate(column_list):
                # check if piece is in the column
                if self.pos in col:
                    if board.game_Tiles[check_tile].piece_on_tile.layout() != "-" and check_tile % 8 == i:
                        return False
                    break

            #
            # if self.pos in Piece.first_column:
            #     if board.game_Tiles[check_tile].piece_on_tile.layout() != "-" and check_tile % 8 == 0:
            #         return False
            # elif self.pos in Piece.second_column:
            #     if board.game_Tiles[check_tile].piece_on_tile.layout() != "-" and check_tile % 8 == 1:
            #         return False
            # if self.pos in Piece.third_column:
            #     if board.game_Tiles[check_tile].piece_on_tile.layout() != "-" and check_tile % 8 == 2:
            #         return False
            # elif self.pos in Piece.fourth_column:
            #     if board.game_Tiles[check_tile].piece_on_tile.layout() != "-" and check_tile % 8 == 3:
            #         return False
            # elif self.pos in Piece.fifth_column:
            #     if board.game_Tiles[check_tile].piece_on_tile.layout() != "-" and check_tile % 8 == 4:
            #         return False
            # if self.pos in Piece.sixth_column:
            #     if board.game_Tiles[check_tile].piece_on_tile.layout() != "-" and check_tile % 8 == 5:
            #         return False
            # elif self.pos in Piece.seventh_column:
            #     if board.game_Tiles[check_tile].piece_on_tile.layout() != "-" and check_tile % 8 == 6:
            #         return False
            # elif self.pos in Piece.eighth_column:
            #     if board.game_Tiles[check_tile].piece_on_tile.layout() != "-" and check_tile % 8 == 7:
            #         return False
        return True

    def up_vertical_check_in_way(self,board,destination):
        down_destination = destination + 8
        for check_tile in range(down_destination,self.pos):
            column_list = Piece.get_columns()
            for i,col in enumerate(column_list):
                if self.pos in col:
                    if board.game_Tiles[check_tile].piece_on_tile.layout() != "-" and check_tile % 8 == i:
                        return False
                    break
        return True

    def same_row(self,destination):
        row_list = Piece.get_rows()
        for row in row_list:
            if self.pos in row and destination in row:
                return True
        return False
    def south_east_diagonal_check_in_way(self,board,destination):
        south_east_adjacent = self.pos + 9
        for check_tile in range(south_east_adjacent, destination):
            down_diag_list = Piece.get_down_diagonals()
            for diag in down_diag_list:
                if self.pos in diag and check_tile in diag:
                    if board.game_Tiles[check_tile].piece_on_tile.layout() != '-':
                        return False
                    break
        return True

#this function is for 9s
    def north_east_diagonal_check_in_way(self,board,destination):
        south_west_destination = destination + 7
        for check_tile in range(south_west_destination,self.pos):
            up_diag_list = Piece.get_up_diagonals()
            for diag in up_diag_list:
                if self.pos in diag and check_tile in diag:
                    if board.game_Tiles[check_tile].piece_on_tile.layout() != '-':
                        return False
                    break
        return True

    def south_west_diagonal_check_in_way(self,board,destination):
        south_west_adjacent_self_pos = self.pos + 7
        for check_tile in range(south_west_adjacent_self_pos,destination):
            up_diag_list = Piece.get_up_diagonals()
            for diag in up_diag_list:
                if self.pos in diag and check_tile in diag:
                    if board.game_Tiles[check_tile].piece_on_tile.layout() != '-':
                        return False
                    break
        return True

    def north_west_diagonal_check_in_way(self,board,destination):
        south_west_destination = destination + 9
        for check_tile in range(south_west_destination,self.pos):
            down_diag_list = Piece.get_down_diagonals()
            for diag in down_diag_list:
                if self.pos in diag and check_tile in diag:
                    if board.game_Tiles[check_tile].piece_on_tile.layout() != '-':
                        return False
                    break
        return True
#    def north_west_diagonal_check_in_way(self,board,destination):
#this function is for left down and right up negative 7s and positive 7s
    def same_up_diagonal(self, destination):
        up_diag_list = Piece.get_up_diagonals()
        for diag in up_diag_list:
            if self.pos in diag and destination in diag:
                return True
        return False

#negatives 9 and positive 9s
    def same_down_diagonal(self,destination):
        down_diag_list = Piece.get_down_diagonals()
        for diag in down_diag_list:
            if self.pos in diag and destination in diag:
                return True
        return False


        #if self.pos in col and destination in col



class Null_Piece:#by default, each piece will be -
    def __init_(self):
        pass
    @staticmethod
    def layout():
        return "-"
    def calculateLegalMoves(board):
        pass
#1 if its in the 8th column no
#2 if its in the
class Rook(Piece):
    global check_right_white_rook
    global check_left_white_rook
    global check_right_black_rook
    global check_left_black_rook

    check_right_white_rook = False
    check_left_white_rook = False
    check_right_black_rook = False
    check_left_black_rook = False

    def __init__(self,pos,color):
        allianceReverse = None
        self.pos = pos
        self.color = color


    def check_right_black_rooks():
        global check_right_black_rook
        return check_right_black_rook

    def check_left_black_rooks():
        global check_left_black_rook
        return check_left_black_rook

    def check_right_white_rooks():
        global check_right_white_rook
        return check_right_white_rook

    def check_left_white_rooks():
        global check_left_white_rook
        return check_left_white_rook

    def layout(self):
        if self.color == "B":
            return 'R'
        else:
            return 'r'

    def calculateLegalMoves(self, board):#add later, when the king is in check, we do not append the move
        legal_moves = []
        possible_moves = [-1,-2,-3,-4,-5,-6,-7,-8,-16,-24,-32,-40,-48,-56,1,2,3,4,5,6,7,8,16, 24,32,40,48,56]#if there is a teammate in front of him, or if there is an enemy in front of the destination you want to go to, you cant move there
        possible_right_horizontal_moves = [1,2,3,4,5,6,7]
        possible_left_horizontal_moves = [-1,-2,-3,-4,-5,-6,-7]
        for index in possible_moves:
            destination = self.pos + (index)
            if 0 <= destination <= 63:
                if index in possible_right_horizontal_moves and Piece.empty_tile_or_enemy_tile(self,board,destination) and Piece.same_row(self,destination) and Piece.right_horizontal_check_in_way(self,board,destination):
                    legal_moves.append(destination)
                elif index in possible_left_horizontal_moves and Piece.empty_tile_or_enemy_tile(self,board,destination) and Piece.same_row(self,destination) and Piece.left_horizontal_check_in_way(self,board,destination):
                    legal_moves.append(destination)
                elif index in Piece.first_column and Piece.empty_tile_or_enemy_tile(self, board, destination) and Piece.down_vertical_check_in_way(self, board, destination)\
                or index in Piece.neg_first_column and Piece.empty_tile_or_enemy_tile(self, board, destination) and  Piece.up_vertical_check_in_way(self,board,destination):
                    legal_moves.append(destination)
        return legal_moves


    def move(self, destination, board):
        global check_left_black_rook
        global check_right_black_rook
        global check_left_white_rook
        global check_right_white_rook
        if self.pos == 0:
            check_left_black_rook_moved = True
        elif self.pos == 7:
            check_right_black_rook = True
        elif self.pos == 56:
            check_left_white_rook = True
        elif self.pos == 63:
            check_right_white_rook = True
        if self.color == "W":
            board.game_Tiles[self.pos] = Tiles(self.pos,Null_Piece)
            board.game_Tiles[destination] = Tiles(destination, Rook(destination,'W'))

        #    board.game_Tiles.update({Null_Piece.layout():self.pos, Pawn.layout():destination})
        else:
            board.game_Tiles[self.pos] = Tiles(self.pos,Null_Piece)
            board.game_Tiles[destination] = Tiles(destination, Rook(destination,'B'))





class Knight(Piece):
    def __init__(self,pos,color):
        self.pos = pos
        self.color = color
    def layout(self):
        if self.color == "B":
            return 'N'
        else:
            return 'n'


    def calculateLegalMoves(self, board):
        legal_moves = []
        possible_moves = [17,-17,15,-15,10,-10,6,-6]
        for index in possible_moves:
            destination = self.pos + index
            if 0 <= destination <=63:
                if(index == 17 and Piece.empty_tile_or_enemy_tile(self, board, destination) and self.pos not in Piece.eighth_column and self.pos not in Piece.seventh_row and self.pos not in Piece.eighth_row):
                    legal_moves.append(destination)
                elif(index == 15 and Piece.empty_tile_or_enemy_tile(self, board, destination) and self.pos not in Piece.first_column and self.pos not in Piece.seventh_row and self.pos not in Piece.eighth_row):
                    legal_moves.append(destination)
                elif(index == -17 and Piece.empty_tile_or_enemy_tile(self, board, destination) and self.pos not in Piece.first_column and self.pos not in Piece.first_row and self.pos not in Piece.second_row):
                    legal_moves.append(destination)
                elif(index == -15 and Piece.empty_tile_or_enemy_tile(self, board, destination) and self.pos not in Piece.eighth_column and self.pos not in Piece.first_row and self.pos not in Piece.second_row):
                    legal_moves.append(destination)
                elif(index == 10 and Piece.empty_tile_or_enemy_tile(self, board, destination) and self.pos not in Piece.eighth_column and self.pos not in Piece.seventh_column and self.pos not in Piece.eighth_row):
                    legal_moves.append(destination)
                elif(index == -6 and Piece.empty_tile_or_enemy_tile(self, board, destination) and self.pos not in Piece.eighth_column and self.pos not in Piece.seventh_column and self.pos not in Piece.first_row):
                    legal_moves.append(destination)
                elif(index == 6 and Piece.empty_tile_or_enemy_tile(self, board, destination) == '-' and self.pos not in Piece.first_column and self.pos not in Piece.second_column and self.pos not in Piece.eighth_row):
                    legal_moves.append(destination)
                elif(index == -10 and Piece.empty_tile_or_enemy_tile(self, board, destination) and self.pos not in Piece.first_column and self.pos not in Piece.second_column and self.pos not in Piece.first_row):
                    legal_moves.append(destination)

        return legal_moves
    def move(self, destination, board):
        if self.color == "W":
            board.game_Tiles[self.pos] = Tiles(self.pos,Null_Piece)
            board.game_Tiles[destination] = Tiles(destination, Knight(destination,'W'))
        #    board.game_Tiles.update({Null_Piece.layout():self.pos, Pawn.layout():destination})
        else:
            board.game_Tiles[self.pos] = Tiles(self.pos,Null_Piece)
            board.game_Tiles[destination] = Tiles(destination, Knight(destination,'B'))



class Bishop(Piece):
    def __init__(self,pos,color):
        self.pos = pos
        self.color = color
    def layout(self):
        if self.color == "B":
            return 'B'
        else:
            return 'b'
    def calculateLegalMoves(self, board):
        legal_moves = []
        possible_moves = [9,18,27,36,45,54,63,7,14,21,28,35,42,49, -7,-14,-21,-28,-35,-42,-49, -9,-18,-27,-36,-45,-54,-63]
        possible_moves_south_east = [9,18,27,36,45,54,63]
        possible_moves_north_west = [-9,-18,-27,-36,-45,-54,-63]
        possible_moves_south_west = [7,14,21,28,35,42,49]
        possible_moves_north_east = [-7,-14,-21,-28,-35,-42,-49]
        for index in possible_moves:
            destination = self.pos + index
            if 0 <= destination <= 63:

                if index in possible_moves_south_east and Piece.empty_tile_or_enemy_tile(self,board,destination) and Piece.south_east_diagonal_check_in_way(self,board,destination) and Piece.same_down_diagonal(self,destination):
                    legal_moves.append(destination)
                elif index in possible_moves_north_west and Piece.empty_tile_or_enemy_tile(self,board,destination) and Piece.north_west_diagonal_check_in_way(self,board,destination) and Piece.same_down_diagonal(self,destination):
                    legal_moves.append(destination)
                elif index in possible_moves_south_west and Piece.empty_tile_or_enemy_tile(self,board,destination) and Piece.south_west_diagonal_check_in_way(self,board,destination) and Piece.same_up_diagonal(self,destination):
                    legal_moves.append(destination)
                elif index in possible_moves_north_east and Piece.empty_tile_or_enemy_tile(self,board,destination) and Piece.north_east_diagonal_check_in_way(self,board,destination) and Piece.same_up_diagonal(self,destination):
                    legal_moves.append(destination)

        return legal_moves

    def move(self, destination,board):
        if self.color == "W":
            board.game_Tiles[self.pos] = Tiles(self.pos,Null_Piece)
            board.game_Tiles[destination] = Tiles(destination, Bishop(destination,'W'))
        else:
            board.game_Tiles[self.pos] = Tiles(self.pos,Null_Piece)
            board.game_Tiles[destination] = Tiles(destination, Bishop(destination,'B'))



class King(Piece):
    global check_has_moved
    global check_black_moved
    check_has_moved = False
    check_black_moved = False
    def __init__(self,pos,color):
        self.pos = pos
        self.color = color
    def layout(self):
        if self.color == "B":
            return 'K'
        else:
            return 'k'

    def calculateLegalMoves(self, board):
        legal_moves = []
        possible_moves = [2,-2,1,-1,-8,8,7,-7,9,-9]
        possible_normal_moves = [1,-1,-8,8,7,-7,9,-9]
        possible_castle = [2,-2]

        # black_rook_left = board.game_Tiles[0].piece_on_tile.check_right_black_rooks()
        # black_rook_right = board.game_Tiles[7].piece_on_tile.check_right_black_rooks()
        # white_rook_left  = board.game_Tiles[56].piece_on_tile.check_left_white_rooks()
        # white_rook_right = board.game_Tiles[63].piece_on_tile.check_right_white_rooks()

        #print(black_rook_left)
        for index in possible_moves:
            destination = self.pos + index
            if 0 <= destination <= 63:
                if index in possible_normal_moves and Piece.empty_tile_or_enemy_tile(self,board,destination):
                    legal_moves.append(destination)
                elif index in possible_castle:
                    if index == 2 and not Rook.check_right_white_rooks() and self.color == "W" and not King.white_has_moved() and Piece.empty_tile_or_enemy_tile(self,board,destination) and Piece.right_horizontal_check_in_way(self,board,destination) \
                    or index == -2 and not Rook.check_left_white_rooks() and self.color == "W" and not King.white_has_moved() and Piece.empty_tile_or_enemy_tile(self,board,destination) and Piece.left_horizontal_check_in_way(self,board,destination) and board.game_Tiles[57].piece_on_tile.layout() == "-":
                        legal_moves.append(destination)
                    elif index == 2 and not Rook.check_right_black_rooks() and self.color == "B" and not King.black_has_moved() and Piece.empty_tile_or_enemy_tile(self,board,destination) and Piece.right_horizontal_check_in_way(self,board,destination) \
                    or index == -2 and not Rook.check_left_black_rooks() and self.color == "B" and not King.black_has_moved() and not Piece.empty_tile_or_enemy_tile(self,board,destination) and Piece.left_horizontal_check_in_way(self,board,destination) and board.game_Tiles[1].piece_on_tile.layout() == "-":
                        legal_moves.append(destination)
#be able to check if the correct rook has moved or not
        return legal_moves

    def move(self,destination,board):
        global check_has_moved
        global check_black_moved
        if self.pos == 60 and self.color == "W" and destination == 62 or self.pos == 4 and self.color == "B" and destination == 6:
            rook_previous_spot = destination + 1
            rook_new_spot = self.pos + 1
            board.game_Tiles[self.pos] = Tiles(self.pos, Null_Piece)
            board.game_Tiles[destination] = Tiles(destination, King(destination,"W"))
            board.game_Tiles[rook_previous_spot] = Tiles(rook_previous_spot, Null_Piece)
            board.game_Tiles[rook_new_spot] = Tiles(rook_new_spot,Rook(rook_new_spot,"W"))
            check_has_moved = True
            return True
        if self.pos == 60 and self.color == "W" and destination == 58 or self.pos == 4 and self.color == "B" and destination == 2:
            rook_previous_spot = destination - 2
            rook_new_spot = self.pos - 1
            board.game_Tiles[self.pos] = Tiles(self.pos, Null_Piece)
            board.game_Tiles[destination] = Tiles(destination, King(destination,"W"))
            board.game_Tiles[rook_previous_spot] = Tiles(rook_previous_spot, Null_Piece)
            board.game_Tiles[rook_new_spot] = Tiles(rook_new_spot,Rook(rook_new_spot,"W"))
            check_has_moved = True
            return True


        if self.color == "W":
            board.game_Tiles[self.pos] = Tiles(self.pos,Null_Piece)
            board.game_Tiles[destination] = Tiles(destination,King(destination,"W"))
            check_has_moved = True
        else:
            board.game_Tiles[self.pos] = Tiles(self.pos, Null_Piece)
            board.game_Tiles[destination] = Tiles(destination, King(destination, "B"))
            check_blacked_moved = True

    def white_has_moved():
        global check_has_moved
        return check_has_moved
    def black_has_moved():
        global check_black_moved
        return check_black_moved

class Queen(Piece):
    def __init__(self,pos,color):
        self.pos = pos
        self.color = color
    def layout(self):
        if self.color == "B":
            return 'Q'
        else:
            return 'q'

#now why don't we just add the check horizontal, vertical and diagonal shit into the Piece, so every piece can inherit those functions

    def calculateLegalMoves(self, board):
        legal_moves = []
        possible_moves = [8,16,24,32,40,48,56,-8,-16,-24,-32,-40,-48,-56,9,18,27,36,45,54,63,-9,-18,-27,-36,-45,-54,-63,7,14,21,28,35,42,49,-7,-14,-21,-28,-35,-42,-49,1,2,3,4,5,6,7,-1,-2,-3,-4,-5,-6,-7]

        possible_moves_south_east = [9,18,27,36,45,54,63]
        possible_moves_north_west = [-9,-18,-27,-36,-45,-54,-63]
        possible_moves_south_west = [7,14,21,28,35,42,49]
        possible_moves_north_east = [-7,-14,-21,-28,-35,-42,-49]

        possible_right_horizontal_moves = [1,2,3,4,5,6,7]
        possible_left_horizontal_moves = [-1,-2,-3,-4,-5,-6,-7]


        for index in possible_moves:
            destination = self.pos + index
            if 0<=destination<= 63:
                if index in possible_moves_south_east and Piece.empty_tile_or_enemy_tile(self,board,destination) and Piece.south_east_diagonal_check_in_way(self,board,destination) and Piece.same_down_diagonal(self,destination) and destination not in legal_moves:
                    legal_moves.append(destination)
                elif index in possible_moves_north_west and Piece.empty_tile_or_enemy_tile(self,board,destination) and Piece.north_west_diagonal_check_in_way(self,board,destination) and Piece.same_down_diagonal(self,destination):
                    legal_moves.append(destination)
                elif index in possible_moves_south_west and Piece.empty_tile_or_enemy_tile(self,board,destination) and Piece.south_west_diagonal_check_in_way(self,board,destination) and Piece.same_up_diagonal(self,destination) and destination not in legal_moves:
                    legal_moves.append(destination)
                elif index in possible_moves_north_east and Piece.empty_tile_or_enemy_tile(self,board,destination) and Piece.north_east_diagonal_check_in_way(self,board,destination) and Piece.same_up_diagonal(self,destination) and destination not in legal_moves:
                    legal_moves.append(destination)
                if index in possible_right_horizontal_moves and Piece.empty_tile_or_enemy_tile(self,board,destination) and Piece.same_row(self,destination) and Piece.right_horizontal_check_in_way(self,board,destination) and destination not in legal_moves:
                    legal_moves.append(destination)
                elif index in possible_left_horizontal_moves and Piece.empty_tile_or_enemy_tile(self,board,destination) and Piece.same_row(self,destination) and Piece.left_horizontal_check_in_way(self,board,destination) and destination not in legal_moves:
                    legal_moves.append(destination)
                elif index in Piece.first_column and Piece.empty_tile_or_enemy_tile(self, board, destination) and Piece.down_vertical_check_in_way(self, board, destination)\
                or index in Piece.neg_first_column and Piece.empty_tile_or_enemy_tile(self, board, destination) and  Piece.up_vertical_check_in_way(self,board,destination):
                    legal_moves.append(destination)

        return legal_moves

    def move(self,destination,board):
        if self.color == "W":
            board.game_Tiles[self.pos] = Tiles(self.pos,Null_Piece)
            board.game_Tiles[destination] = Tiles(destination,Queen(destination,"W"))
        else:
            board.game_Tiles[self.pos] = Tiles(self.pos, Null_Piece)
            board.game_Tiles[destination] = Tiles(destination, Queen(destination, "B"))

class Pawn(Piece):
    allianceReverse = None
    def __init__(self,pos,color):
        self.pos = pos
        self.color = color
        if self.color == "B":
            self.allianceReverse = 1
        else:
            self.allianceReverse = -1
    def layout(self):
        if self.color == "B":
            return 'P'
        else:
            return 'p'

    def firstMove(self):
        if(self.color == "B" and self.pos in Piece.second_row):
            return True
        elif(self.color == "W" and self.pos in Piece.seventh_row):
            return True
        else:
            return False

#if its an 8, and nothing is in front, its a legal move,
#if its a 16, nothing is in front, and first move,
#if 7 or 9, if not piece_on_tile.layout == "-", opposite color of pawn, its a legal move
#15 and 17 are enpassants fuckers, if opposing move 16 for the first time,
#piece thats in front is a pawn of opposite color
#its the same turn
    def calculateLegalMoves(self, board):
        legal_moves = []
        possible_moves = [8,16,9,7, 17, 15]

        for index in possible_moves:
            destination = self.pos + (index*self.allianceReverse)
            if 0<= destination <= 63:
                if (index == 8 and board.game_Tiles[destination].piece_on_tile.layout() == "-"):
                    legal_moves.append(destination)
                elif (index == 16 and board.game_Tiles[destination].piece_on_tile.layout() == "-" and self.firstMove() and Piece.down_vertical_check_in_way(self,board,destination)):
                    legal_moves.append(destination)
#if the move is index == 7, this is a caputuring move, its an opposing piece
                elif (index == 7 and not board.game_Tiles[destination].piece_on_tile.layout()== "-"):
                    if self.color == "B" and Piece.empty_tile_or_enemy_tile(self, board, destination) and Piece.same_up_diagonal(self,destination):
                        legal_moves.append(destination)
                    if self.color == "W" and board.game_Tiles[destination].piece_on_tile.layout().isupper() and Piece.same_up_diagonal(self,destination):
                        legal_moves.append(destination)

                elif(index == 9 and not board.game_Tiles[destination].piece_on_tile.layout()== "-"):
                    if self.color == "B" and board.game_Tiles[destination].piece_on_tile.layout().islower() and Piece.same_down_diagonal(self,destination):
                        legal_moves.append(destination)
                    if self.color == "W" and board.game_Tiles[destination].piece_on_tile.layout().isupper() and Piece.same_down_diagonal(self,destination):
                        legal_moves.append(destination)
# and self.color == "W" and islower() and Piece.same_up_diagonal(self, destination)

                else:
                    pass #skip enpassant for now
        return legal_moves

    def move(self, destination, board):
        if self.color == "W":
            board.game_Tiles[self.pos] = Tiles(self.pos,Null_Piece)
            board.game_Tiles[destination] = Tiles(destination, Pawn(destination,'W'))


        #    board.game_Tiles.update({Null_Piece.layout():self.pos, Pawn.layout():destination})
        else:
            board.game_Tiles[self.pos] = Tiles(self.pos,Null_Piece)
            board.game_Tiles[destination] = Tiles(destination, Pawn(destination,'B'))
    #def en_passant(self,destination,board):
    def promotion(self,destination ,board):
        value_input = False
        if destination in Piece.first_row and self.color == 'W':

#why didn't that work, self pos is the new position of the tile
#that is so weird, why does it do that? the move piece was registered, the piece was supposed to move, and then
            while not value_input:
                promote_string = input("Promote your pawn by typing the first initial of the piece you want to promote into:")
                try:
                    if promote_string == "q" or promote_string == "Q":
                        board.game_Tiles[self.pos] = Tiles(self.pos,Null_Piece)
                        board.game_Tiles[destination] = Tiles(self.pos,Queen(destination,"W"))
                        value_input = True
                    elif promote_string == "n" or promote_string == "N":
                        board.game_Tiles[self.pos] = Tiles(self.pos,Null_Piece)
                        board.game_Tiles[destination] = Tiles(destination,Knight(destination,"W"))
                        value_input = True
                    elif promote_string == "b" or promote_string == "B":
                        board.game_Tiles[self.pos] = Tiles(self.pos,Null_Piece)
                        board.game_Tiles[destination] = Tiles(self.pos,Bishop(destination,"W"))
                        value_input = True
                    elif promote_string == "r" or promote_string == "R":
                        board.game_Tiles[self.pos] = Tiles(self.pos,Null_Piece)
                        board.game_Tiles[destination] = Tiles(self.pos,Rook(destination,"W"))
                        value_input = True
                    else:
                        print("Please select a legit option")
                except ValueError:
                    print("Please select a legit option")

        if destination in Piece.eighth_row and self.color == 'B':
            while not value_input:
                promote_string = input("Promote your pawn by typing the first initial of the piece you want to promote into:")
                try:
                    if promote_string == "q" or promote_string == "Q":
                        board.game_Tiles[self.pos] = Tiles(self.pos,Null_Piece)
                        board.game_Tiles[destination] = Tiles(self.pos,Queen(destination,"B"))
                        value_input = True
                    elif promote_string == "n" or promote_string == "N":
                        board.game_Tiles[self.pos] = Tiles(self.pos,Null_Piece)
                        board.game_Tiles[destination] = Tiles(destination,Knight(destination,"B"))
                        value_input = True
                    elif promote_string == "b" or promote_string == "B":
                        board.game_Tiles[self.pos] = Tiles(self.pos,Null_Piece)
                        board.game_Tiles[destination] = Tiles(self.pos,Bishop(destination,"B"))
                        value_input = True
                    elif promote_string == "r" or promote_string == "R":
                        board.game_Tiles[self.pos] = Tiles(self.pos,Null_Piece)
                        board.game_Tiles[destination] = Tiles(self.pos,Rook(destination,"B"))
                        value_input = True
                    else:
                        print("Please select a legit option")
                except ValueError:
                    print("Please select a legit option")





                #    board.game_Tiles[self.pos] = '-'
        #    board.game_Tiles[destination] = Tiles(destination, Pawn(destination,'W'))
        #    board.game_Tiles.update({Null_Piece.layout():self.pos,Pawn.layout():destination})
#    def promotion(self, string_piece, board):
#how would i move a piece?
#what is passed into move? the destination_move
#what is also necessary to move a piece? the board?
#now how would i move the piece to the destination square?

class engine(): #create a constructor
#create a is_checkmate function
#create a display game using a while loop


    def init(self, checkmate):
        self.checkmate = checkmate
    def is_checkmate(self):#still need to implement this
        return False
    def check_for_check_white(boards):
        for i in range(0,64):
            piece_selected = boards.game_Tiles[i].piece_on_tile
            if piece_selected.layout().isupper():  #this would get each pieces calculate legal moves, a list of legal moves
                for j in piece_selected.calculateLegalMoves(boards):
                    if boards.game_Tiles[j].piece_on_tile.layout() == 'k':
                        return True
        return False
                         #board.game_Tiles[j] are destinations of the piece that we are calculating
    #create a function, own king in check -> checks if your move has caused your own king to be in check
    #thinking about creating a copy of the board, after the move has been made on that board, if the king is in check after the move has been made, do another move
    def check_for_check_black(board):
        for i in range(0,64):
            piece_selected = board.game_Tiles[i].piece_on_tile
            if piece_selected.layout().islower():
                for j in piece_selected.calculateLegalMoves(board):
                    if board.game_Tiles[j].piece_on_tile.layout() == 'K':
                        return True
        return False

    #the move shouldnt register if the turn is white == 1 and check_for_check_white is true
    # move shouldnt register if turn == -1 and check_for_check_black is true
    def display(self):
        turn = 1
        count = 0
        chess_board = Board()
        chess_board.createBoard()
        global destination_move
        while (self.is_checkmate() is False):
            chess_board.printBoard()
            #1.) check to see if opponent just put you in check
            #2.) the opponent can only move such that they are now out of check
            #3.) include when you can't move your piece because the king will be in check
            #
            #
            #
            valid_input = False
            while not valid_input:

                try:
                    piece_tile = int(input("""Please select the Piece's tile that you want to move."""))
                    valid_input = True
                except ValueError:
                    print("Please select a legal tile")
                    continue
            print(chess_board.game_Tiles[piece_tile].piece_on_tile.layout())

            if(chess_board.game_Tiles[piece_tile].piece_on_tile.layout() == '-'):
                print("Please select a tile with a piece on it")
            if turn == 1 and chess_board.game_Tiles[piece_tile].piece_on_tile.layout().isupper(): #white's turn but selected black piece
                print("It's not black's turn. Please select a white piece.")
            if turn == -1 and chess_board.game_Tiles[piece_tile].piece_on_tile.layout().islower():
                print("It's not white's turn. Please select a black piece.")
                #or isupper(board.game_Tiles[piece_tile].piece_on_tile.layout()) and whites turn vice versa, then pick the right color
            if turn == 1 and chess_board.game_Tiles[piece_tile].piece_on_tile.layout().islower() or turn == -1 and chess_board.game_Tiles[piece_tile].piece_on_tile.layout().isupper():
                if(chess_board.game_Tiles[piece_tile].piece_on_tile.layout() == 'P' or chess_board.game_Tiles[piece_tile].piece_on_tile.layout() == 'p'):
                    print("you've selected a pawn")
                    selected_piece = chess_board.game_Tiles[piece_tile].piece_on_tile#does this get the piece that we need?
                    print(selected_piece.calculateLegalMoves(chess_board))
                    while valid_input:
                        try:
                            destination_move = int(input("""Please select the destination tile that you want the piece to move to."""))
                            valid_input = False
                        except ValueError:
                            print("Please select one of the legal destinations.")
                            continue
                    print(chess_board.game_Tiles[destination_move].piece_on_tile.layout())

                    if(destination_move in selected_piece.calculateLegalMoves(chess_board)):
                        #if move is en passant, call the en passant function instead of the move function
                        copy_chess_board = chess_board.copy()
                        selected_piece.move(destination_move,copy_chess_board)
                        selected_piece.promotion(destination_move,copy_chess_board)

                        if turn == 1 and engine.check_for_check_white(copy_chess_board):
                            print("whites king must be in check")
                        elif turn == -1 and engine.check_for_check_black(copy_chess_board):
                            print("blacks king must be in check")
                        else:
                            selected_piece.move(destination_move, chess_board)
                            selected_piece.promotion(destination_move,chess_board)
                            turn = turn *-1
                            count = count + 1
                            #possibly another while loop with the move function testing if the your color king is in check or not after the move, that would test if your move is legal after the move, and if your king is in check after the previous turn, it would check if the move is legit
                        #when the king is out of check, the board finally moves, if it doesnt, the same board is displayed, nothing has changed. the newboard is reset everytime in some loop

                    else:
                        print("""That is not a legal move. Please select a legal move >:(""")

                if chess_board.game_Tiles[piece_tile].piece_on_tile.layout() == 'N' or chess_board.game_Tiles[piece_tile].piece_on_tile.layout() == 'n':
                    print("you've selected a knight")
                    selected_piece = chess_board.game_Tiles[piece_tile].piece_on_tile#does this get the piece that we need?
                    print(selected_piece.calculateLegalMoves(chess_board))
                    while valid_input:
                        try:
                            destination_move = int(input("""Please select the destination tile that you want the piece to move to."""))
                            valid_input = False
                        except ValueError:
                            print("Please select one of the legal destinations.")
                            continue
                    print(chess_board.game_Tiles[destination_move].piece_on_tile.layout())

                    if(destination_move in selected_piece.calculateLegalMoves(chess_board)):
                        copy_chess_board = chess_board.copy()
                        selected_piece.move(destination_move,copy_chess_board)
                        if turn == 1 and engine.check_for_check_white(copy_chess_board):
                            print("whites king must be in check")
                        elif turn == -1 and engine.check_for_check_black(copy_chess_board):
                            print("blacks king must be in check")
                        else:
                            selected_piece.move(destination_move, chess_board)
                            count = count + 1
                            turn = turn * -1
                    else:
                        print("""That is not a legal move. Please select a legal move >:(""")

                if chess_board.game_Tiles[piece_tile].piece_on_tile.layout() == 'R' or chess_board.game_Tiles[piece_tile].piece_on_tile.layout() == "r":
                    print("You've selected a rook")
                    selected_piece = chess_board.game_Tiles[piece_tile].piece_on_tile
                    print(selected_piece.calculateLegalMoves(chess_board))
                    while valid_input:
                        try:
                            destination_move = int(input("""Please select the destination tile that you want the piece to move to."""))
                            valid_input = False
                        except ValueError:
                            print("Please select one of the legal destinations.")
                            continue
                    print(chess_board.game_Tiles[destination_move].piece_on_tile.layout())

                    if(destination_move in selected_piece.calculateLegalMoves(chess_board)):
                        copy_chess_board = chess_board.copy()
                        selected_piece.move(destination_move,copy_chess_board)
                        if turn == 1 and engine.check_for_check_white(copy_chess_board):
                            print("whites king must be in check")
                        elif turn == -1 and engine.check_for_check_black(copy_chess_board):
                            print("blacks king must be in check")
                        else:
                            selected_piece.move(destination_move, chess_board)
                            count = count + 1
                            turn = turn * -1
                    else:
                        print("Please select a legal move >:(")

                if chess_board.game_Tiles[piece_tile].piece_on_tile.layout() == 'B' or chess_board.game_Tiles[piece_tile].piece_on_tile.layout() == "b":
                    print("You've selected a Bishop")
                    selected_piece = chess_board.game_Tiles[piece_tile].piece_on_tile
                    print(selected_piece.calculateLegalMoves(chess_board))
                    while valid_input:
                        try:
                            destination_move = int(input("""Please select the destination tile that you want the piece to move to."""))
                            valid_input = False
                        except ValueError:
                            print("Please select one of the legal destinations.")
                            continue
                    print(chess_board.game_Tiles[destination_move].piece_on_tile.layout())
                    if(destination_move in selected_piece.calculateLegalMoves(chess_board)):
                        copy_chess_board = chess_board.copy()
                        selected_piece.move(destination_move,copy_chess_board)
                        if turn == 1 and engine.check_for_check_white(copy_chess_board):
                            print("whites king must be in check")
                        elif turn == -1 and engine.check_for_check_black(copy_chess_board):
                            print("blacks king must be in check")
                        else:
                            selected_piece.move(destination_move, chess_board)
                            count = count + 1
                            turn = turn * -1
                    else:
                        print("Please select a legal move >:(")

                if chess_board.game_Tiles[piece_tile].piece_on_tile.layout() == 'Q' or chess_board.game_Tiles[piece_tile].piece_on_tile.layout() == "q":
                    print("You've selected a Queen")
                    selected_piece = chess_board.game_Tiles[piece_tile].piece_on_tile
                    print(selected_piece.calculateLegalMoves(chess_board))
                    while valid_input:
                        try:
                            destination_move = int(input("""Please select the destination tile that you want the piece to move to."""))
                            valid_input = False
                        except ValueError:
                            print("Please select one of the legal destinations.")
                            continue
                    print(chess_board.game_Tiles[destination_move].piece_on_tile.layout())
                    if(destination_move in selected_piece.calculateLegalMoves(chess_board)):
                        copy_chess_board = chess_board.copy()
                        selected_piece.move(destination_move,copy_chess_board)
                        if turn == 1 and engine.check_for_check_white(copy_chess_board):
                            print("whites king must be in check")
                        elif turn == -1 and engine.check_for_check_black(copy_chess_board):
                            print("blacks king must be in check")
                        else:
                            selected_piece.move(destination_move, chess_board)
                            count = count + 1
                            turn = turn * -1
                    else:
                        print("Please select a legal move >:(")

                if chess_board.game_Tiles[piece_tile].piece_on_tile.layout() == 'K' or chess_board.game_Tiles[piece_tile].piece_on_tile.layout() == "k":
                    print("You've selected a King")
                    selected_piece = chess_board.game_Tiles[piece_tile].piece_on_tile
                    print(selected_piece.calculateLegalMoves(chess_board))
                    while valid_input:
                        try:
                            destination_move = int(input("""Please select the destination tile that you want the piece to move to."""))
                            valid_input = False
                        except ValueError:
                            print("Please select one of the legal destinations.")
                            continue
                    print(chess_board.game_Tiles[destination_move].piece_on_tile.layout())
                    if(destination_move in selected_piece.calculateLegalMoves(chess_board)):
                        copy_chess_board = chess_board.copy()
                        selected_piece.move(destination_move,copy_chess_board)
                        if turn == 1 and engine.check_for_check_white(copy_chess_board):
                            print("whites king must be in check")
                        elif turn == -1 and engine.check_for_check_black(copy_chess_board):
                            print("blacks king must be in check")
                        else:
                            selected_piece.move(destination_move, chess_board)
                            count = count + 1
                            turn = turn * -1
                    else:
                        print("Please select a legal move >:(")

#
# piece_move -> going to select the piece on that tile
# destination move, is that move legal, based on the piece on that tile



    #while
engine_object = engine()
engine_object.display()

#chess_board = Board()
#chess_board.createBoard()
#chess_board.printBoard()

#select piece you want to move by selecting the numbered square, then press enter
#then, select where you want to move the square by entering in the square you want to move




#the user interface

#this is going to be a while loop ->
#input the piece that you want to select, by inputing the box of the piece that you are going to use

#if select "-", please select a piece of your color
    #return to top

#selected piece of your color, but can't move -> that piece can't move, select another one
    #return to the top

#select opponents piece, -> please select a piece of your color
    #return to the top

#select pawn that can move -> please move the piece to a desired square ->
    #input is illegal
        #Black: if input is not in calculateLegalMoves.legal_moves
            #please enter a legal move
            #goes back to the top of selecting a piece
        #white: if input is not in calculateLegalMoves.legal_moves
            #please enter a legal move

    #input is legal
        #Black: if input is in calculateLegalMoves.legal_moves
            #move pawn to destinated area -> board.game_Tiles[input]
            #if turn is over switch the turn color, count the turn in the background
        #white: if input is in calculateLegalMoves.legal_moves,
            #move pawn to destinated area -> board.game_Tiles[input]
            #if turn is over, switch the turn color, count the turn in the background



    #goal is to do calculate legal moves for rook and pawn and then create an engine


#check function, if any opposite piece has a calculate legal move on king, then the king is in check

#how do we check if enemy piece is attacking the king?# at the end of each turn, check king in check
#force player to move the king, if their king is in check, or to move a piece, so its not in check anymore
#enpassant, check if the previous turn, the opponent had moved a pawn on an adjacent column two tiles, also, the pawn doing the enpassant is a on row 4 white and row 5 for black
#castling: checking if squares between the king and rook are being attacked by the opponent, also check if any piece is between too -> put in engine,
#promotion: if a pawn makes it to the end rank, first or eighth row, depending on the color, they may promote to an object of the player's choice
#turns
