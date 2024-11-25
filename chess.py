from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        self.__position = new_position

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        
        row, col = self.position
        direction = 1 if self.color == "white" else -1
        moves = [(row + direction, col)]
        return [move for move in moves if self.is_position_on_board(move)]

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        return [move for move in moves if self.is_position_on_board(move)]

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        
        row, col = self.position
        moves = []
        for i in range(1, 8):
            moves.extend([(row + i, col + i), (row + i, col - i),
                          (row - i, col + i), (row - i, col - i)])
        return [move for move in moves if self.is_position_on_board(move)]

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        
        row, col = self.position
        moves = []
        for i in range(1, 8):
            moves.extend([(row + i, col), (row - i, col), (row, col + i), (row, col - i)])
        return [move for move in moves if self.is_position_on_board(move)]

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
       
        row, col = self.position
        moves = []
        for i in range(1, 8):
            moves.extend([(row + i, col), (row - i, col), (row, col + i), (row, col - i),
                          (row + i, col + i), (row + i, col - i),
                          (row - i, col + i), (row - i, col - i)])
        return [move for move in moves if self.is_position_on_board(move)]

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        
        row, col = self.position
        moves = [
            (row + 1, col), (row - 1, col),
            (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row + 1, col - 1),
            (row - 1, col + 1), (row - 1, col - 1)
        ]
        return [move for move in moves if self.is_position_on_board(move)]

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    pieces = [
        Pawn("white", (2, 2)),
        Pawn("black", (7, 7)),
        Knight("black", (1, 2)),
        Bishop("white", (4, 4)),
        Rook("black", (1, 1)),
        Queen("white", (5, 5)),
        King("black", (8, 8)),
    ]
    
    for piece in pieces:
        print(piece)
        print("Possible moves:", piece.possible_moves())
