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
        print(f"to x:{movingxpos}")
        print(f"to y:{movingypos}")
        print(f"from x:{self.xpos}")
        print(f"from y:{self.ypos}")

        color_mult = -1 if self.colour == "black" else 1
        print(f"color_mult: {color_mult}")
        
        if movingxpos == self.xpos and  board[movingypos][movingxpos] is None:
            if movingypos == (self.ypos + color_mult):
                print("moving one")
                return True
            elif not self.has_moved and movingypos == (self.ypos + color_mult * 2):
                print("moving two (first move)")
                return True
                
        # Check if we are moving by diagonal
        if  (self.ypos + color_mult) == movingypos and abs(self.xpos - movingxpos) == 1:
            # If the destination square is occupied by an opponent's piece, allow capturing
            if board[movingypos][movingxpos] is not None and board[movingypos][movingxpos].colour != self.colour:
                print("capturing")
                return True
            
            else:
                print("ally")
                return False
            
        print("Meow")
        return False

class Castle(ChessPiece):
    def __init__(self, colour, ypos, xpos):
        super().__init__(colour, ypos, xpos)

    def legalMove(self, movingxpos, movingypos, board):
        if (self.xpos == movingxpos or self.ypos == movingypos):
            return True
        return False


class Bishop(ChessPiece):
    def __init__(self, colour, ypos, xpos):
        super().__init__(colour, ypos, xpos)

    def legalMove(self, movingxpos, movingypos, board):
        if abs(movingxpos - self.xpos) == abs(movingypos - self.ypos):
            return True
        return False


class King(ChessPiece):
    def __init__(self, colour, ypos, xpos):
        super().__init__(colour, ypos, xpos)

    def legalMove(self, movingxpos, movingypos, board):
        if movingxpos-1 == self.xpos or movingxpos+1 == self.xpos or movingxpos == self.xpos:
            if movingypos-1 == self.ypos or movingypos+1 == self.ypos or movingypos  == self.ypos:
                if board[movingypos][movingxpos] is not None and board[movingypos][movingxpos].colour != self.colour:
                    print("capturing")
                    return True
            
                elif board[movingypos][movingxpos] is not None and board[movingypos][movingxpos].colour == self.colour:
                    print("ally")
                    return False
                else:
                    print("Moving 1")
                    return True

        print("Meow")
        return False

class Queen(ChessPiece):
    def __init__(self, colour, ypos, xpos):
        super().__init__(colour, ypos, xpos)

    def legalMove(self, movingxpos, movingypos, board):
        if abs(movingxpos - self.xpos) == abs(movingypos - self.ypos):
            return True
        if (self.xpos == movingxpos or self.ypos == movingypos):
            return True
        return False


class Knight(ChessPiece):
    def __init__(self, colour, ypos, xpos):
        super().__init__(colour, ypos, xpos)

    def legalMove(self, movingxpos, movingypos, board):
        if (self.xpos - movingxpos == 3 or movingxpos-self.xpos == 3) and (self.ypos - movingypos == 2 or movingypos-self.ypos == 2):
            return True
        elif (self.ypos - movingypos == 3 or movingypos-self.ypos == 3) and (self.xpos - movingxpos == 2 or movingxpos-self.xpos == 2):
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
        self.board[7][6] = Pawn(colour2, 7, 6)
        self.board[7][7] = King(colour1, 7, 7)


    def print_board(self):
        piece_emojis = {
            "Pawn_black": "♟️",
            "Pawn_white": "♙",
            "Castle_black": "♜",
            "Castle_white": "♖",
            "Knight_black": "♞",
            "Knight_white": "♘",
            "Bishop_black": "♝",
            "Bishop_white": "♗",
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
        print("Moving piece from", starty, startx, "to", endy, endx)  # Debugging print
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


class MinimaxChessPlayer:
    def __init__(self, colour):
        self.colour = colour

#    def get_legal_moves(self, board):
#        legal_moves = []
#        for y in range(8):
#            for x in range(8):
#                piece = board[y][x]
#                if piece and piece.colour == self.colour:
#                    for dy in range(-1, 2):
#                        for dx in range(-1, 2):
#                            if dy == 0 and dx == 0:
#                                continue
#                            new_x, new_y = x + dx, y + dy
#                            if 0 <= new_x < 8 and 0 <= new_y < 8:
#                                if piece.legalMove(new_x, new_y, board):
#                                    legal_moves.append(((x, y), (new_x, new_y)))
#        return legal_moves
    def simulate_move(self, board, move):
        start, end = move
        new_board = [row[:] for row in board]
        x, y = start
        new_x, new_y = end
        new_board[new_y][new_x] = new_board[y][x]
        new_board[y][x] = None
        return new_board

    def evaluate_board(self, board):
        # Simple evaluation function: count pieces
        score = 0
        for row in board:
            for piece in row:
                if piece:
                    if piece.colour == self.colour:
                        score += self.get_piece_value(piece)
                    else:
                        score -= self.get_piece_value(piece)
        return score

    def get_piece_value(self, piece):
        # Assign values to pieces for evaluation
        if isinstance(piece, Pawn):
            return 1
        elif isinstance(piece, Knight) or isinstance(piece, Bishop):
            return 3
        elif isinstance(piece, Castle):
            return 5
        elif isinstance(piece, Queen):
            return 9
        elif isinstance(piece, King):
            return 1000  # Arbitrarily high value for the king
        return 0

    def ai_move(board, ai_player):
        legal_moves = ai_player.get_legal_moves(board)
        best_move = None
        best_score = -math.inf
        for move in legal_moves:
            new_board = ai_player.simulate_move(board, move)
            score = ai_player.evaluate_board(new_board)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

# Game Loop
def play_chess():
    board = ChessBoard()
    player = 1
    ai_player = MinimaxChessPlayer("white")  # Example: AI plays as white

    while True:
        print("Player", player, "'s turn")
        board.print_board()
        start = input("Enter starting position (e.g., A2): ").upper()
        end = input("Enter ending position (e.g., A4): ").upper()
        startx, starty = ord(start[0]) - ord('A'), int(start[1])-1
        endx, endy = ord(end[0]) - ord('A'), int(end[1])-1

        if 0 <= startx <= 7 and 0 <= starty <= 7 and 0 <= endx <= 7 and 0 <= endy <= 7:
            if board.move_piece(startx, starty, endx, endy):
                player = 3 - player  # Switch players
            else:
                print("Try again.")
        else:
            print("Invalid coordinates. Coordinates must be within the board.")

        # AI player's turn
"""
        ai_best_move = ai_move(board.board, ai_player)
        if ai_best_move:
            start, end = ai_best_move
            startx, starty = start
            endx, endy = end
            if board.move_piece(startx, starty, endx, endy):
                player = 3 - player  # Switch players
            else:
                print("AI made an invalid move. Game ends.")
                break
        else:
            print("AI cannot make a move. Game ends.")
            break
"""
play_chess()
