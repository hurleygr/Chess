# Chess

Basic desktop chess app. Uses tkinter for chess board gui. 
Board functionality is complete. Need to add move validation. 
Step 1:
Need to figure out way to check if kings are in check, if next move will make them in check, or if they are in check, does next move get them out of it. Would rather not iterate through every piece and every possible square they could move to every time a move is made. Might be some redundancy with checking if moves are valid but still. 
Checking if other moves are valid is just: does it obey move rules, is it that colors turn, does it not pass through a piece, or land on piece of same color. Is it not pinned to the king, which is basically the check thing. 
So outlining the brute force method:
Have an 8x8 list of lists where entries are set to 0 if no threat, 1 if threatened by white, 2 if threatened by black, 3 if threatened by both. 
Or something along those lines. After every move, go through every piece, and walk it along every path it could follow, stopping if it runs into another piece (or goes off the board obviously), and each square it walks is set to the appropriate number depending on its current state and the color of piece we're looking at. There are 32 pieces. And there could be nearly 30 squares to look at. For a queen in the center of the board for example its 29 I think. 
If it were possible to just update board based on moves instead of remaking it each time that would be fine.
But how to take into account that moving a piece "reveals" some moves, blocks others? 
I picture each piece as having vectors radiating from it. With magnitude and direction. And every other piece is an obstacle. 
Vectors would be simple to setup for each Piece type, and then just use current coordinates. Its just an x,y graph with possible moves as slopes (or knights and their weirdness). Checking if one "slope" intersects a kings square is easy. Doing that for every one and we're back to the initial problem basically. Unless it can be updated. 
