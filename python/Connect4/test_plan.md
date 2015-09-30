
Controller Tests
================

* update_board
 * Given a valid column and player, is board updated
 * Given a valid column and invalid str player, is board not updated
 * Given a valid column and invlaid int player, is board not updated
 * Given a non existent column and a valid player, is board not updated
 * given an incorrect param type column a valid player, is board not updated

* check_winner
 * Given board with 3 set x positions and a choice of x to complete 4, does win return True
 * Given board with no win conditions, does win return False
 * Given a board that is not a list of lists, does it raise an error

* check_tie
 * Given lists are full, does tie return True

 * Given lists are not full, does tie return False
 * Given a board that is not a list of lists, does it raise an error

* get_player_name
 * Given a user name, is name saved
 * Given an invalid user name, does it prevent name from being saved
 * Given no user input, does it prevent name from being saved

* update_turn
 * Given player name, is turn updated

* turn_validator
 * Given a correct column, does it return True
 * Given a column that doesn't exist, does it return False
 * Given a column that is full, does it return False
 * Given a column that has invalid param type, does it return False

* main


Model Tests
===========

* get_player
 * test for player that exists, should get back the existing player
 * test for player that doesn't exist, shouldn't get that player
* set_player
 * test adding player with a string
 * test adding a player that already exists
 * test adding a player with a non string name
 * test giving a non string type param, should raise error
* get_column
 * test asking for column that exists i.e. 1-7, we expect a list to be returned
 * test asking for a column that doesn't exits
 * test asking for a column with a non int index, is error raised
* get_row
 * test asking for row that may exists i.e. 1-6, we expect a list to be returned
 * test asking for a row that doesn't exits
 * test asking for a row with a non int index, is error raised
* add_piece
 * test asking to add to column that exists i.e. 1-7, we expect True if success
 * test asking for a column that doesn't exits, we expect false
 * test asking for a column that is full i.e. column row len > 6, we expect false
 * test asking for a column with a non int index, is error raised


View Tests
==========

* prompt_turn
 * prompt is given a single input, returns single char string
 * prompt is given multiple inputs, returns multiple char strings
 * No input given, repeats prompt
* show_instructions
 * does it print instructions, horray
* win_statement
 * does win statement print
* tie_statement
 * does tie statement print
* print_board
 * does board print given a correct board
 * does board catch invalid sized boards
 * does board catch invalid type parameters
* prompt_name
 * prompt is given a single input, returns single char string
 * prompt is given multiple inputs, returns multiple char strings
 * No input given, repeats prompt