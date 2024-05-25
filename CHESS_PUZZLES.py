import math

class ChessPiece:
    def __init__(self, colour, ypos, xpos, has_moved=False):
        self.xpos = xpos
        self.ypos = ypos
        self.colour = colour
        self.has_moved = has_moved
        
    def move_to(self, ypos, xpos):
        self.xpos = xpos
        self.ypos = ypos
        self.has_moved = True

class Pawn(ChessPiece):
    def __init__(self, colour, ypos, xpos, has_moved=False):
        super().__init__(colour, ypos, xpos, has_moved)
        

    def legalMove(self, movingxpos, movingypos, board):
        # Pawns can move forward one square, or two squares on their first move
        # Check if the destination square is within bounds

        color_mult = -1 if self.colour == "black" else 1
        
        if movingxpos == self.xpos and board[movingypos][movingxpos] is None:
            if movingypos == (self.ypos + color_mult):
                return True
            elif not self.has_moved and movingypos == (self.ypos + color_mult * 2):
                return True
                
        # Check if we are moving by diagonal
        if  (self.ypos + color_mult) == movingypos and abs(self.xpos - movingxpos) == 1:
            # If the destination square is occupied by an opponent's piece, allow capturing
            if board[movingypos][movingxpos] is not None and board[movingypos][movingxpos].colour != self.colour:
                return True
            
            else:
                return False
            
        return False

class Castle(ChessPiece):
    def __init__(self, colour, ypos, xpos, has_moved=False):
        super().__init__(colour, ypos, xpos, has_moved)

    def legalMove(self, movingxpos, movingypos, board):
        if movingxpos == self.xpos or movingypos == self.ypos:
            if 0 <= movingypos <= 7 or 0 <= movingxpos <= 7:
                if board[movingypos][movingxpos] is not None and board[movingypos][movingxpos].colour != self.colour:
                    return True
            
                elif board[movingypos][movingxpos] is not None and board[movingypos][movingxpos].colour == self.colour:
                    return False
                else:
                    return True
        
        return False

class King(ChessPiece):
    def __init__(self, colour, ypos, xpos, has_moved=False):
        super().__init__(colour, ypos, xpos, has_moved)

    def legalMove(self, movingxpos, movingypos, board):
        if movingxpos-1 == self.xpos or movingxpos+1 == self.xpos or movingxpos == self.xpos:
            if movingypos-1 == self.ypos or movingypos+1 == self.ypos or movingypos  == self.ypos:
                if board[movingypos][movingxpos] is not None and board[movingypos][movingxpos].colour != self.colour:
                    return True
            
                elif board[movingypos][movingxpos] is not None and board[movingypos][movingxpos].colour == self.colour:
                    return False
                else:
                    return True

        return False

class Queen(ChessPiece):
    def __init__(self, colour, ypos, xpos):
        super().__init__(colour, ypos, xpos)

    def legalMove(self, movingxpos, movingypos, board):
        
        
        if movingxpos == self.xpos or movingypos == self.ypos:
                if 0 <= movingypos <= 7 or 0 <= movingxpos <= 7:
                    if board[movingypos][movingxpos] is not None and board[movingypos][movingxpos].colour != self.colour:
                        return True
                
                    elif board[movingypos][movingxpos] is not None and board[movingypos][movingxpos].colour == self.colour:
                        return False
                        
                    else:
                        return True
    
        deltax = abs(self.xpos - movingxpos)
        deltay = abs(self.ypos - movingypos)
        
        if deltax == deltay:
            if board[movingypos][movingxpos] is not None and board[movingypos][movingxpos].colour != self.colour:
                return True
            if board[movingypos][movingxpos] is not None and board[movingypos][movingxpos].colour == self.colour:
                return False
            else:
                return True
        return False


class Knight(ChessPiece):
    def __init__(self, colour, ypos, xpos):
        super().__init__(colour, ypos, xpos)

    def legalMove(self, movingxpos, movingypos, board):
        deltax = abs(self.xpos - movingxpos)
        deltay = abs(self.ypos - movingypos)
        if deltax == deltay:
            if board[movingypos][movingxpos] is not None and board[movingypos][movingxpos].colour != self.colour:
                return True
            if board[movingypos][movingxpos] is not None and board[movingypos][movingxpos].colour == self.colour:
                return False
            else:
                return True
        return False
        
class Horse(ChessPiece):
    def __init__(self, colour, ypos, xpos, has_moved=False):
        super().__init__(colour, ypos, xpos, has_moved)

    def legalMove(self, movingxpos, movingypos, board):
        deltax = abs(self.xpos - movingxpos)
        deltay = abs(self.ypos - movingypos)
        if (deltax == 1 and deltay == 2) or (deltax == 2 and deltay == 1):
            if board[movingypos][movingxpos] is not None and board[movingypos][movingxpos].colour != self.colour:
                return True
            if board[movingypos][movingxpos] is not None and board[movingypos][movingxpos].colour == self.colour:
                return False
            else:
                return True
        return False
    
class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.populate_board()

    def populate_board(self):
        #black
        #Rook
        colour1 = "white"
        colour2 = "black"
        # example of figure placement: self.board[7][0] = Castle(colour2, 7, 0, True)
        self.board[6][0] = Pawn(colour1, 6, 0)
        self.board[6][1] = Pawn(colour1, 6, 1)
        self.board[6][2] = Pawn(colour1, 6, 2)
        self.board[6][5] = Pawn(colour1, 6, 5)
        self.board[5][7] = Pawn(colour1, 5, 7)
        self.board[4][6] = Pawn(colour1, 4, 6)
        self.board[3][4] = Pawn(colour1, 3, 4)
        
        self.board[7][2] = King(colour1, 7, 2)
        
        self.board[7][3] = Castle(colour1, 7, 3)
        self.board[7][7] = Castle(colour1, 7, 7)
        
        self.board[5][5] = Horse(colour1, 5, 5)
        self.board[4][4] = Horse(colour1, 4, 4)
        
        self.board[4][2] = Knight(colour1, 4, 2)
        self.board[3][6] = Knight(colour1, 3, 6)

        
        
        self.board[2][2] = Pawn(colour2, 2, 2)
        self.board[2][4] = Pawn(colour2, 2, 4)
        self.board[2][6] = Pawn(colour2, 2, 6)
        self.board[1][0] = Pawn(colour2, 1, 0)
        self.board[1][1] = Pawn(colour2, 1, 1)
        self.board[1][5] = Pawn(colour2, 1, 5)
        self.board[1][7] = Pawn(colour2, 1, 7)
        
        self.board[1][3] = Knight(colour2, 1, 3)
        self.board[0][7] = Knight(colour2, 0, 7)
        
        self.board[1][6] = Horse(colour2, 1, 6)
        
        self.board[0][0] = Castle(colour2, 0, 0)
        self.board[0][4] = Castle(colour2, 0, 4)
       
        self.board[0][6] = King(colour2, 0, 6)
        
        self.board[0][5] = Queen(colour2, 0, 5)
        
    def print_board(self):
        piece_emojis = {
            "Pawn_black": "\u265F",
            "Pawn_white": "\u2659",
            "Castle_black": "\u265C",
            "Castle_white": "\u2656",
            "Horse_black": "\u265E",
            "Horse_white": "\u2658",
            "Knight_black": "\u265D",
            "Knight_white": "\u2657",
            "Queen_black": "\u265B",
            "Queen_white": "\u2655",
            "King_black": "\u265A",
            "King_white": "\u2654"
        }
        column_labels = "ABCDEFGH"
        print("  ", " ".join(column_labels))
        for i, row in enumerate(self.board):
            print(i+1, end="  ")
            for piece in row:
               if piece:
                   piece_name = piece.__class__.__name__ + "_" + piece.colour
                   print("{}".format(piece_emojis[piece_name]), end=' ')
               else:
                   print('_', end=' ')
            print()

    def move_piece(self, startx, starty, endx, endy, player_colour):
        piece = self.board[starty][startx]
        if not piece:
            print("No piece at the given position.")
            return False
            
        if piece.colour != player_colour:
            print("You cannot do that")
            return False

        if piece.legalMove(endx, endy, self.board):  # Passing the board instance
            self.board[endy][endx] = piece
            self.board[starty][startx] = None
            piece.move_to(endy, endx)
        
            print("Moved", piece.__class__.__name__, "to", endy, endx)  # Debugging print
            return True
        else:
            print("Illegal move.")
            return False
            
    def check_puzzle(self):
        if self.board[2][5] is not None and self.board[2][5].__class__.__name__ == "Horse" and self.board[2][5].colour == "white":
            return True
        return False
        
def print_clue():
    print(" __________________________________________________________________________ ")
    print("|  1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18 |")
    print("|                                                                          |")
    print("|1  H                                                                   He |")
    print("|                                                                          |")
    print("|2  Li  Be                                          B   .   N   .   F   Ne |")
    print("|                                                                          |")
    print("|3  Na  Mg                                          Al  Si  P   S   ..  Ar |")
    print("|                                                                          |")
    print("|4  .   Ca  Sc  Ti  V   Cr  Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr |")
    print("|                                                                          |")
    print("|5  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd  In  Sn  Sb  Te  I   Xe |")
    print("|                                                                          |")
    print("|6  Cs  Ba  *   Hf  Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn |")
    print("|                                                                          |")
    print("|7  Fr  Ra  **  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Nh  Fl  Mc  Lv  Ts  Og |")
    print("|__________________________________________________________________________|")
    print("|                                                                          |")
    print("|                                                                          |")
    print("| Lantanoidi*   La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu |")
    print("|                                                                          |")
    print("|  Aktinoidi**  Ac  Th  Pa  U   Np  Pu  Am  Cm  Bk  Cf  Es  Fm  Md  No  Lr |")
    print("|__________________________________________________________________________|")
    return
    

# Game Loop
def play_chess():
    board = ChessBoard()
    player = 1
    player_colour = "white"
    print("Solve this chess puzzle to recieve the next clue. Whites turn.")
    while True:
        board.print_board()
        start = input("Enter starting position (e.g., A2): ").upper()
        end = input("Enter ending position (e.g., A4): ").upper()
        try:
            startx, starty = ord(start[0]) - ord('A'), int(start[1])-1
            endx, endy = ord(end[0]) - ord('A'), int(end[1])-1
        except ValueError:
            print("These are not the dro.. the inputs you are looking for!")
            continue

        if 0 <= startx <= 7 and 0 <= starty <= 7 and 0 <= endx <= 7 and 0 <= endy <= 7:
            if board.move_piece(startx, starty, endx, endy, player_colour):
                board.print_board()

                if board.check_puzzle():
                    print("You win")
                    print_clue()
                    s = input("Press any key to close ")
                    return
                else:
                    print("Try again.")
                    play_chess()
        else:
            print("Invalid coordinates. Coordinates must be within the board.")

play_chess()
