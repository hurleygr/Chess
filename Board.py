from tkinter import *

#   Use canvas to create a board


class ChessBoard:
    def __init__(self):
        self.ID_board = [[None for _ in range(8)] for _ in range(8)]
        main = Tk()
        # 400 pixels by 400 pixels, white background
        board_length = 400      # needs to be divisible by 8
        square_size = board_length // 8
        self.chess_board = Canvas(main, width=board_length, height=board_length, bg='white')

        dark_color = '#b58863'      # hex code for brownish color
        light_color = '#f0d9b4'     # hex code for tannish color
        select_color = '#dac352'
        # piece images, look into converting to base64 encoded strings
        # assign images to label or something to prevent garbage collection

        # piece = chess_board.create_image(x,y, anchor = tk.NW)

        self.white_pawn = PhotoImage(file='/Users/griffin/Downloads/White Pawn.gif')
        self.black_pawn = PhotoImage(file='/Users/griffin/Downloads/Black Pawn.gif')
        self.white_rook = PhotoImage(file='/Users/griffin/Downloads/White Rook.gif')
        self.black_rook = PhotoImage(file='/Users/griffin/Downloads/Black Rook.gif')
        self.white_knight = PhotoImage(file='/Users/griffin/Downloads/White Knight.gif')
        self.black_knight = PhotoImage(file='/Users/griffin/Downloads/Black Knight.gif')
        self.white_bishop = PhotoImage(file='/Users/griffin/Downloads/White Bishop.gif')
        self.black_bishop = PhotoImage(file='/Users/griffin/Downloads/Black Bishop.gif')
        self.white_queen = PhotoImage(file='/Users/griffin/Downloads/White Queen.gif')
        self.black_queen = PhotoImage(file='/Users/griffin/Downloads/Black Queen.gif')
        self.white_king = PhotoImage(file='/Users/griffin/Downloads/White King.gif')
        self.black_king = PhotoImage(file='/Users/griffin/Downloads/Black King.gif')

        # coordinates for creating rectangles in Canvas object
        top_left_coords = [0, 0]
        bottom_right_coords = [square_size, square_size]

        for row in range(8):
            if row % 2:
                light = False       # Every other row starts with a light square
            else:
                light = True
            for col in range(8):
                if light:
                    color = light_color
                else:
                    color = dark_color

                self.chess_board.create_rectangle(top_left_coords[0], top_left_coords[1],
                                                  bottom_right_coords[0], bottom_right_coords[1], fill=color)
                light = not light   # Change rectangle color for next rectangle

                # increment x coordinates by 50 pixels (initial board dimensions divided by 8)
                top_left_coords[0] += square_size
                bottom_right_coords[0] += square_size

            # bring x coordinates back to initials, increment y coordinates
            top_left_coords[0] = 0
            top_left_coords[1] += square_size
            bottom_right_coords[0] = square_size
            bottom_right_coords[1] += square_size

        # Put blackPieces on board
        # store create_image id's, use them with move method to move.
        # have them stored on board in CHess.py. For movement

        for offset in range(0, board_length, square_size):
            file = offset // square_size
            self.ID_board[1][file] = self.chess_board.create_image(-5 + offset, square_size - 3, anchor=NW, image=self.black_pawn)

            # store ID before its overwritten
        self.ID_board[0][0] = self.chess_board.create_image(-5, -3, anchor=NW, image=self.black_rook)
        self.ID_board[0][1] = self.chess_board.create_image(1 * square_size - 5, -3, anchor=NW, image=self.black_knight)
        self.ID_board[0][2] = self.chess_board.create_image(2 * square_size - 5, -3, anchor=NW, image=self.black_bishop)
        self.ID_board[0][3] = self.chess_board.create_image(3 * square_size - 5, -3, anchor=NW, image=self.black_queen)
        self.ID_board[0][4] = self.chess_board.create_image(4 * square_size - 5, -3, anchor=NW, image=self.black_king)
        self.ID_board[0][5] = self.chess_board.create_image(5 * square_size - 5, -3, anchor=NW, image=self.black_bishop)
        self.ID_board[0][6] = self.chess_board.create_image(6 * square_size - 5, -3, anchor=NW, image=self.black_knight)
        self.ID_board[0][7] = self.chess_board.create_image(7 * square_size - 5, -3, anchor=NW, image=self.black_rook)

        # Put white pieces on board
        for offset in range(0, board_length, square_size):
            file = offset // square_size
            self.ID_board[6][file] = self.chess_board.create_image(-5 + offset, board_length - 2 * square_size - 3, anchor=NW, image=self.white_pawn)
        second_row_height = board_length - square_size - 3
        self.ID_board[7][0] = self.chess_board.create_image(-5, second_row_height, anchor=NW, image=self.white_rook)
        self.ID_board[7][1] = self.chess_board.create_image(1 * square_size - 5, second_row_height, anchor=NW, image=self.white_knight)
        self.ID_board[7][2] = self.chess_board.create_image(2 * square_size - 5, second_row_height, anchor=NW, image=self.white_bishop)
        self.ID_board[7][3] = self.chess_board.create_image(3 * square_size - 5, second_row_height, anchor=NW, image=self.white_queen)
        self.ID_board[7][4] = self.chess_board.create_image(4 * square_size - 5, second_row_height, anchor=NW, image=self.white_king)
        self.ID_board[7][5] = self.chess_board.create_image(5 * square_size - 5, second_row_height, anchor=NW, image=self.white_bishop)
        self.ID_board[7][6] = self.chess_board.create_image(6 * square_size - 5, second_row_height, anchor=NW, image=self.white_knight)
        self.ID_board[7][7] = self.chess_board.create_image(7 * square_size - 5, second_row_height, anchor=NW, image=self.white_rook)

        # moving pieces
        self.selected_piece = None
        self.selected_square = None
        self.previous_color = None
        self.target_square = None

        def click(event):
            if self.chess_board.find_withtag(CURRENT):
                if not self.selected_piece:
                    closest = self.chess_board.find_overlapping(event.x, event.y, event.x, event.y)
                    for objects in closest:
                        if self.chess_board.type(objects) == 'image':
                            if not self.selected_piece:
                                self.selected_piece = objects
                        elif self.chess_board.type(objects) == 'rectangle':
                            if not self.selected_square:
                                self.selected_square = objects
                                self.previous_color = self.chess_board.itemcget(self.selected_square, 'fill')
                    self.chess_board.itemconfig(self.selected_square, fill=select_color)
                else:
                    closest = self.chess_board.find_overlapping(event.x, event.y, event.x, event.y)
                    for objects in closest:
                        if self.chess_board.type(objects) == 'image':
                            if not self.target_piece:
                                self.target_piece = objects
                        elif self.chess_board.type(objects) == 'rectangle':
                            if not self.target_square:
                                self.target_square = objects
                    self.chess_board.itemconfig(self.selected_square, fill=self.previous_color)
                    # define target destination

                    row_move = self.chess_board.coords(self.target_square)[0] - self.chess_board.coords(self.selected_square)[0]
                    col_move = self.chess_board.coords(self.target_square)[1] - self.chess_board.coords(self.selected_square)[1]

                    # call is_valid_move
                    # if valid, move piece. otherwise reset variables and colors and stuff

                    self.chess_board.move(self.selected_piece, row_move, col_move)


                    self.selected_piece = None
                    self.selected_square = None
                    self.target_piece = None
                    self.target_square = None


            main.update()
            self.chess_board.update()

        self.chess_board.bind('<Button-1>', click)

        # idk why but this is necessary
        self.chess_board.pack()
        main.update()
        main.mainloop()
