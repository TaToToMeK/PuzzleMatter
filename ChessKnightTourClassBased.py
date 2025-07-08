class ChessKnightTour:
    def __init__(self, n, show_looped_solutions_only):
        self.n = n
        self.moves_pattern = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        self.occupied_fields = set()
        self.solution = {}
        self.move_count = 2  # first move to be done at given startx, starty
        self.solutions_counter = 0
        self.checkpoints = set()
        self.show_looped_solutions_only= show_looped_solutions_only

    def is_valid_move(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n and (x, y) not in self.occupied_fields

    def make_move(self, x, y, move_count):
        self.occupied_fields.add((x, y))
        self.solution[(x, y)] = move_count

    def undo_move(self, x, y):
        self.occupied_fields.remove((x, y))
        del self.solution[(x, y)]

    def define_checkpoints(self):
        for x in [1, self.n - 2]:
            for y in [2, self.n - 3]:
                self.checkpoints.add((x, y))
                self.checkpoints.add((y, x))

    def check_onecheckpoint(self, corner, a, b, x, y):
        if (x, y) == a and b in self.occupied_fields and corner not in self.occupied_fields:
            return False
        elif (x, y) == b and a in self.occupied_fields and corner not in self.occupied_fields:
            return False
        else:
            return True

    def check_checkpoints(self, x, y):
        if not self.check_onecheckpoint((0, 0), (1, 2), (2, 1), x, y):
            return False
        if not self.check_onecheckpoint((0, self.n - 1), (1, self.n - 3), (2, self.n - 2), x, y):
            return False
        if not self.check_onecheckpoint((self.n - 1, 0), (self.n - 2, 2), (self.n - 3, 1), x, y):
            return False
        if not self.check_onecheckpoint((self.n - 1, self.n - 1), (self.n - 2, self.n - 3), (self.n - 3, self.n - 2), x, y):
            return False
        return True

    def show_partial_solution(self):
        for x in range(self.n):
            row = ''
            for y in range(self.n):
                if (x, y) not in self.solution:
                    row += ' -'
                else:
                    row += ' ' + str(self.solution[(x, y)]).rjust(3, " ")
            print(row)
        print()

    def jump_knight(self, x, y, show_looped_solutions_only,move_count):
        if move_count > self.n * self.n:
            self.solutions_counter += 1
            print('solution #', self.solutions_counter, '; LeftUpCorner visited at move =', self.solution[0, 0])
            if not show_looped_solutions_only or self.solution[0, 0] == self.n * self.n:
                self.show_partial_solution()
            return False  # Wszystkie pola są pokryte
        if (x, y) in self.checkpoints and move_count < self.n * self.n:
            if not self.check_checkpoints(x, y):
                return False  # Ślepy narożnik

        for dx, dy in self.moves_pattern:
            new_x, new_y = x + dx, y + dy
            if self.is_valid_move(new_x, new_y):
                self.make_move(new_x, new_y, move_count)
                if self.jump_knight(new_x, new_y, show_looped_solutions_only, move_count + 1):
                    self.show_partial_solution()
                    return True
                self.undo_move(new_x, new_y)
        return False

    def solve(self, startx, starty):
        self.occupied_fields.clear()
        self.occupied_fields.add((startx, starty))
        self.solution = {(startx, starty): 1}
        self.define_checkpoints()
        self.jump_knight(startx, starty, self.show_looped_solutions_only, self.move_count)
        print("No more solutions found.")

if __name__ == '__main__':
    solver = ChessKnightTour(n=6, show_looped_solutions_only=True) # board size is n x n
    solver.solve(2, 1)

'''    
    solver = ChessKnightTour(n=6, show_looped_solutions_only=True) # board size is n x n
    solver.solve(2, 1)
solution # 49578 ; LeftUpCorner visited at move = 36
  36  33  24  13  10   3
  23  12  35   2  25  14
  34   1  32  11   4   9
  19  22   5  28  15  26
   6  31  20  17   8  29
  21  18   7  30  27  16


'''