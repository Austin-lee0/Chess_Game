class Board:
    game_Tiles = {}

    def __init__(self):
        pass
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
        count = 0
        for i in range(64):
            print('|', end = (self.game_Tiles[i].piece_on_tile.layout()))
            count = count +1
            if count == 8:# writing some code!
                print("|", end = "\n")
                count = 0
class Tiles:
    piece_on_tile = None
    tile_coordinate = None
    def __init__(self, coordinates,piece):
        self.tile_coordinates = coordinates
        self.piece_on_tile = piece

class Piece:
    first_column = [0,8,16,24,32,40,48,56]
    second_column = [1,9,17,25,33,41,49,57]
    third_column = [2,10,18,26,34,42,50,58]
    fourth_column = [3,11,19,27,35,43,51,59]
    fifth_column = [4,12,20,28,36,44,52,60]
    sixth_column = [5,13,21,29,37,45,53,61]
    seventh_column = [6,14,22,30,38,46,54,62]
    eigth_column = [7,15,23,31,39,47,55,63]
    def __init_(self):
        pass


class Null_Piece:#by default, each piece will be -
    def __init_(self):
        pass
    @staticmethod
    def layout():
        return "-"
#1 if its in the 8th column no
#2 if its in the
class Rook(Piece):
    def __init__(self,pos,color):
        allianceReverse = None
        self.pos = pos
        self.color = color

    def layout(self):
        if self.color == "B":
            return 'R'
        else:
            return 'r'
    def calculateLegalMoves(self, board):#add later, when the king is in check, we do not append the move
        legal_moves = []
        possible_moves = [-1,-2,-3,-4,-5,-6,-7,-8,-16,-24,-32,-40,-48,-56,1,2,3,4,5,6,7,8,16,32,40,48,56]#if there is a teammate in front of him, or if there is an enemy in front of the destination you want to go to, you cant move there
        for index in possible_moves:
            destination = self.pos + (index)
            if 0<=destination <=63:
                if index == 1 and board.game_Tiles[destination].piece_on_tile.layout() == '-' and self.pos not in Piece.eigth_column \
                 or index == 1 and self.color == "B" and islower(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.eigth_column \
                  or index == 1 and self.color == "W" and isupper(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.eigth_column:
                        legal_moves.append(destination)

                elif index == 2 and board.game_Tiles[destination].piece_on_tile.layout() == '-' and self.pos not in Piece.eigth_column and self.pos not in Piece.seventh_column \
                 or index == 2 and self.color == "B" and islower(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.eigth_column and self.pos not in Piece.seventh_column \
                  or index == 2 and self.color == "W" and isupper(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.eigth_column and self.pos not in Piece.seventh_column:
                        legal_moves.append(destination)

                elif index == 3 and board.game_Tiles[destination].piece_on_tile.layout() == '-' and self.pos not in Piece.eigth_column and self.pos not in Piece.seventh_column and self.pos not in Piece.sixth_column \
                 or index == 3 and self.color == "B" and islower(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.eigth_column and self.pos not in Piece.seventh_column and self.pos not in Piece.sixth_column \
                  or index == 3 and self.color == "W" and isupper(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.eigth_column and self.pos not in Piece.seventh_column and self.pos not in Piece.sixth_column:
                        legal_moves.append(destination)

                elif index == 4 and board.game_Tiles[destination].piece_on_tile.layout() == '-' and self.pos not in Piece.eigth_column and self.pos not in Piece.seventh_column and  self.pos not in Piece.sixth_column and  self.pos not in Piece.fifth_column \
                 or index == 4 and self.color == "B" and islower(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.eigth_column and self.pos not in Piece.seventh_column and  self.pos not in Piece.sixth_column and  self.pos not in Piece.fifth_column \
                  or index == 4 and self.color == "W" and isupper(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.eigth_column and self.pos not in Piece.seventh_column and  self.pos not in Piece.sixth_column and  self.pos not in Piece.fifth_column:
                        legal_moves.append(destination)


                elif index == 5 and board.game_Tiles[destination].piece_on_tile.layout() == '-' and self.pos not in Piece.eigth_column and self.pos not in Piece.seventh_column and  self.pos not in Piece.sixth_column and  self.pos not in Piece.fifth_column and  self.pos not in Piece.fourth_column \
                 or index == 5 and self.color == "B" and islower(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.eigth_column and self.pos not in Piece.seventh_column and  self.pos not in Piece.sixth_column and  self.pos not in Piece.fifth_column and  self.pos not in Piece.fourth_column \
                  or index == 5 and self.color == "W" and isupper(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.eigth_column and self.pos not in Piece.seventh_column and  self.pos not in Piece.sixth_column and  self.pos not in Piece.fifth_column and  self.pos not in Piece.fourth_column:
                        legal_moves.append(destination)

                elif index == 6 and board.game_Tiles[destination].piece_on_tile.layout() == '-' and self.pos not in Piece.eigth_column and self.pos not in Piece.seventh_column and  self.pos not in Piece.sixth_column and  self.pos not in Piece.fifth_column and  self.pos not in Piece.fourth_column and  self.pos not in Piece.third_column \
                 or index == 6 and self.color == "B" and islower(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.eigth_column and self.pos not in Piece.seventh_column and  self.pos not in Piece.sixth_column and  self.pos not in Piece.fifth_column and  self.pos not in Piece.fourth_column and  self.pos not in Piece.third_column \
                  or index == 6 and self.color == "W" and isupper(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.eigth_column and self.pos not in Piece.seventh_column and  self.pos not in Piece.sixth_column and  self.pos not in Piece.fifth_column and  self.pos not in Piece.fourth_column and  self.pos not in Piece.third_column:
                        legal_moves.append(destination)

                elif index == 7 and board.game_Tiles[destination].piece_on_tile.layout() == '-' and self.pos in Piece.first_column \
                 or index == 7 and self.color == "B" and islower(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos in Piece.first_column \
                  or index == 7 and self.color == "W" and isupper(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos in Piece.first_column:
                        legal_moves.append(destination)

                elif index == -1 and board.game_Tiles[destination].piece_on_tile.layout() == '-' and self.pos not in Piece.first_column \
                 or index == -1 and self.color == "B" and islower(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.first_column \
                  or index == -1 and self.color == "W" and isupper(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.first_column:
                        legal_moves.append(destination)

                elif index == -2 and board.game_Tiles[destination].piece_on_tile.layout() == '-' and self.pos not in Piece.first_column and self.pos not in Piece.second_columnor \
                 or index == -2 and self.color == "B" and islower(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.first_column and self.pos not in Piece.second_column \
                  or index == -2 and self.color == "W" and isupper(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.first_column and self.pos not in Piece.second_column:
                        legal_moves.append(destination)

                elif index == -3 and board.game_Tiles[destination].piece_on_tile.layout() == '-' and self.pos not in Piece.first_column and self.pos not in Piece.second_column and self.pos not in Piece.third_column \
                 or index == -3 and self.color == "B" and islower(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.first_column and self.pos not in Piece.second_column and self.pos not in Piece.third_column \
                  or index == -3 and self.color == "W" and isupper(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.first_column and self.pos not in Piece.second_column and self.pos not in Piece.third_column:
                        legal_moves.append(destination)

                elif index == -4 and board.game_Tiles[destination].piece_on_tile.layout() == '-' and self.pos not in Piece.first_column and self.pos not in Piece.second_column and  self.pos not in Piece.third_column and self.pos not in Piece.fourth_column \
                 or index == -4 and self.color == "B" and islower(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.first_column and self.pos not in Piece.second_column and self.pos not in Piece.third_column and  self.pos not in Piece.fourth_column \
                  or index == -4 and self.color == "W" and isupper(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.first_column and self.pos not in Piece.second_column and self.pos not in Piece.third_column and  self.pos not in Piece.fourth_column:
                        legal_moves.append(destination)


                elif index == -5 and board.game_Tiles[destination].piece_on_tile.layout() == '-' and self.pos not in Piece.first_column and self.pos not in Piece.second_column and self.pos not in Piece.third_column and self.pos not in Piece.fourth_column and self.pos not in Piece.fifth_column \
                 or index == -5 and self.color == "B" and islower(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.first_column and self.pos not in Piece.second_column and self.pos not in Piece.third_column and self.pos not in Piece.fourth_column and self.pos not in Piece.fifth_column \
                  or index == -5 and self.color == "W" and isupper(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.first_column and self.pos not in Piece.second_column and self.pos not in Piece.third_column and self.pos not in Piece.fourth_column and self.pos not in Piece.fifth_column:
                        legal_moves.append(destination)

                elif index == -6 and board.game_Tiles[destination].piece_on_tile.layout() == '-' and self.pos not in Piece.first_column and self.pos not in Piece.second_column and self.pos not in Piece.third_column and  self.pos not in Piece.fourth_column and self.pos not in Piece.fifth_column and self.pos not in Piece.sixth_column \
                 or index == -6 and self.color == "B" and islower(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.first_column and self.pos not in Piece.second_column and self.pos not in Piece.third_column and self.pos not in Piece.fourth_column and self.pos not in Piece.fifth_column and self.pos not in Piece.sixth_column \
                  or index == -6 and self.color == "W" and isupper(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos not in Piece.first_column and self.pos not in Piece.second_column and self.pos not in Piece.third_column and self.pos not in Piece.fourth_column and self.pos not in Piece.fifth_column and self.pos not in Piece.sixth_column:
                        legal_moves.append(destination)

                elif index == -7 and board.game_Tiles[destination].piece_on_tile.layout() == '-' and self.pos in Piece.eigth_column \
                 or index == -7 and self.color == "B" and islower(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos in Piece.eigth_column \
                  or index == -7 and self.color == "W" and isupper(board.game_Tiles[destination].piece_on_tile.layout()) and self.pos in Piece.eigth_column:
                        legal_moves.append(destination)
                     # if its an opposite piece color or the tile is blank, its a legal move
                elif index in [8,16,32,40,48,56,-8,-16,-24,-32,-40,-48,-56] and board.game_Tiles[destination].piece_on_tile.layout() == '-' \
                 or index in [8,16,32,40,48,56,-8,-16,-24,-32,-40,-48,-56] and  self.color == "B" and islower(board.game_Tiles[destination].piece_on_tile.layout()) \
                  or index in [8,16,32,40,48,56,-8,-16,-24,-32,-40,-48,-56] and self.color == "W" and isupper(board.game_Tiles[destination].piece_on_tile.layout()):
                        legal_moves.append(destination)




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
        possible_moves = [1,2,3,4,5,6,7,8,16,32,40,48,56]
# Two places up and one to the right or left -> 25, 23
# Two places left and
#
#

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
        possible_moves = [1,2,3,4,5,6,7,8,16,32,40,48,56]

class King(Piece):
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
        possible_moves = [1,2,3,4,5,6,7,8,16,32,40,48,56]

class Queen(Piece):
    def __init__(self,pos,color):
        self.pos = pos
        self.color = color
    def layout(self):
        if self.color == "B":
            return 'Q'
        else:
            return 'q'

    def calculateLegalMoves(self, board):
        legal_moves = []
        possible_moves = [1,2,3,4,5,6,7,8,16,32,40,48,56]

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
        second_row = [8,9,10,11,12,13,14,15]
        seventh_row = [48,49,50,51,52,53,54,55]
        if(self.color == "B" and self.pos in second_row):
            return True
        elif(self.color == "W" and self.pos in seventh_row):
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
                elif (index == 16 and board.game_Tiles[destination].piece_on_tile.layout() == "-" and self.firstMove()):
                    legal_moves.append(destination)
#if the move is index == 7, this is a caputuring move, its an opposing piece
                elif (index == 7 and not board.game_Tiles[destination].piece_on_tile.layout()== "-"):
                    if self.color == "B" and board.game_Tiles[destination].piece_on_tile.layout().islower() and self.pos not in Piece.first_column:
                        legal_moves.append(destination)
                    if self.color == "W" and board.game_Tiles[destination].piece_on_tile.layout().isupper() and self.pos not in Piece.first_column:
                        legal_moves.append(destination)
                elif(index == 9 and not board.game_Tiles[destination].piece_on_tile.layout()== "-"):
                    if self.color == "B" and board.game_Tiles[destination].piece_on_tile.layout().islower() and self.pos not in Piece.eigth_column:
                        legal_moves.append(destination)
                    if self.color == "W" and board.game_Tiles[destination].piece_on_tile.layout().isupper() and self.pos not in Piece.eigth_column:
                        legal_moves.append(destination)
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
        #    board.game_Tiles[self.pos] = '-'
        #    board.game_Tiles[destination] = Tiles(destination, Pawn(destination,'W'))
        #    board.game_Tiles.update({Null_Piece.layout():self.pos,Pawn.layout():destination})
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
    def display(self):
        chess_board = Board()
        chess_board.createBoard()
        turn = 1
        global destination_move
        while (self.is_checkmate() is False):
            chess_board.printBoard()
            valid_input = False
            while not valid_input:
                try:
                    piece_tile = int(input("""Please select the Piece's tile that you want to move."""))
                    valid_input = True
                except ValueError:
                    continue
            print(chess_board.game_Tiles[piece_tile].piece_on_tile.layout())
            if(chess_board.game_Tiles[piece_tile].piece_on_tile.layout() == '-'):
                print("Please select a tile with a piece on it")
                #or isupper(board.game_Tiles[piece_tile].piece_on_tile.layout()) and whites turn vice versa, then pick the right color
            if(chess_board.game_Tiles[piece_tile].piece_on_tile.layout() == 'P' or chess_board.game_Tiles[piece_tile].piece_on_tile.layout() == 'p'):
                print("you've selected a pawn")
                selected_piece = chess_board.game_Tiles[piece_tile].piece_on_tile#does this get the piece that we need?
                print(selected_piece.calculateLegalMoves(chess_board))
                destination_move = int(input("""Please select the destination tile that you want the piece to move to."""))
                print(chess_board.game_Tiles[destination_move].piece_on_tile.layout())

            if(destination_move in selected_piece.calculateLegalMoves(chess_board)):
                selected_piece.move(destination_move, chess_board)
            else:
                print("""That is not a legal move. Please select a legal move >:(""")

#piece_move -> going to select the piece on that tile
#destination move, is that move legal, based on the piece on that tile



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



#select queen that can move -> please move the piece to a desired square
    #

    #

#select knight that can move -> please move the piece to a desired square
    #
    #

#select bishop that can move -> please move the piece to a desired square
    #
    #

#select rock that can move -> please move the piece to a desired square
    #
    #

#select king that can move -> please move the piece to a desired square
    #
    #


    #goal is to do calculate legal moves for rook and pawn and then create an engine


#check function, if any opposite piece has a calculate legal move on king, then the king is in check
