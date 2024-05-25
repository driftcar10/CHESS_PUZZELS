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
        self.board[5][6] = Pawn(colour1, 5, 6)
        self.board[6][6] = Pawn(colour2, 6, 6)
        self.board[6][5] = Pawn(colour2, 6, 5)
        self.board[5][3] = Queen(colour1, 5, 3)


    def print_board(self):
        piece_emojis = {
            "Pawn_black": "♟️",
            "Pawn_white": "♙",
            "Castle_black": "♜",
            "Castle_white": "♖",
            "Horse_black": "♞",
            "Horse_white": "♘",
            "Knight_black": "♝",
            "Knight_white": "♗",
            "Queen_black": "♛",
            "Queen_white": "♕",
            "King_black": "♚",
            "King_white": "♔"
        }
        column_labels = "ABCDEFGH"
        print("  ", " ".join(column_labels))
        for i, row in enumerate(self.board):
            print(i+1, end="  ")
            for piece in row:
                if piece:
                    piece_name = piece.__class__.__name__ + "_" + piece.colour
                    print(piece_emojis[piece_name], end=' ')
                else:
                    print('_', end=' ')
            print()

    def move_piece(self, startx, starty, endx, endy):
        piece = self.board[starty][startx]
        if not piece:
            print("No piece at the given position.")
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



# Game Loop
def play_chess():
    board = ChessBoard()
    player = 1
  
    while True:
        board.print_board()
        start = input("Enter starting position (e.g., A2): ").upper()
        end = input("Enter ending position (e.g., A4): ").upper()
        try:
            startx, starty = ord(start[0]) - ord('A'), int(start[1])-1
            endx, endy = ord(end[0]) - ord('A'), int(end[1])-1
        except ValueError:
            print("These are not the dro.. no, the inputs you are looking for!")
            continue

        if 0 <= startx <= 7 and 0 <= starty <= 7 and 0 <= endx <= 7 and 0 <= endy <= 7:
            if board.move_piece(startx, starty, endx, endy):
                player = 3 - player  # Switch players
            else:
                print("Try again.")
        else:
            print("Invalid coordinates. Coordinates must be within the board.")

play_chess()
