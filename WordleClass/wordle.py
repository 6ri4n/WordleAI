import random
import enchant

class WordleClass:
    def __init__(self):
        with open('five-letter-words.txt','r') as words:
            self.five_letter_words = words.read().splitlines()
        self.player_grid = [
            ['⬛', '⬛', '⬛', '⬛', '⬛', ' '], # 1
            ['⬛', '⬛', '⬛', '⬛', '⬛', ' '], # 3
            ['⬛', '⬛', '⬛', '⬛', '⬛', ' '], # 5
            ['⬛', '⬛', '⬛', '⬛', '⬛', ' '], # 7
            ['⬛', '⬛', '⬛', '⬛', '⬛', ' '], # 9
            ['⬛', '⬛', '⬛', '⬛', '⬛', ' ']  # 11
        ]
        self.ai_grid = [
            ['⬛', '⬛', '⬛', '⬛', '⬛', ' '], # 2
            ['⬛', '⬛', '⬛', '⬛', '⬛', ' '], # 4
            ['⬛', '⬛', '⬛', '⬛', '⬛', ' '], # 6
            ['⬛', '⬛', '⬛', '⬛', '⬛', ' '], # 8
            ['⬛', '⬛', '⬛', '⬛', '⬛', ' '], # 10
            ['⬛', '⬛', '⬛', '⬛', '⬛', ' ']  # 12
        ]
        self.ai_black_tiles = []
        self.player_black_tiles = []
    
    def display_game_grid(self, player_turn, game_status, timeout, player_name, difficulty):
        # TODO: combine player and ai grid as one message
        # determine the difficulty mode
        # extreme will have 4 rows
        if difficulty == 'extreme':
            # check for win condition or timeout or last turn to display proper ending grid
            if game_status == 'player' or game_status == 'ai' or timeout == True or player_turn == 9:
                # TODO: build ai grid first and then player grid second
                # set first line to have no arrow emote
                str_game_grid = '🤖 ' + difficulty + '\n'
                # build ai grid
                for list in self.ai_grid[0:4]:
                    for element in list[0:5]:
                        str_game_grid += element
                    str_game_grid += '\n'
                # set first line to have no arrow emote
                str_game_grid += '\n' + '👤 ' + player_name + '\n'
                # build player grid
                for list in self.player_grid[0:4]:
                    for element in list:
                        str_game_grid += element
                    str_game_grid += '\n'
            else:
                # TODO: build ai grid first and then player grid second
                # determine whose turn
                if player_turn % 2 != 0:
                    # player turn so no arrow emote on ai
                    str_game_grid = '🤖 ' + difficulty + '\n'
                else:
                    # ai turn so no arrow emote on player
                    str_game_grid = '➡️ ' + '🤖 ' + difficulty + '\n'
                # build ai grid
                for list in self.ai_grid[0:4]:
                    for element in list[0:5]:
                        str_game_grid += element
                    str_game_grid += '\n'
                # determine whose turn
                if player_turn % 2 != 0:
                    # player turn so set arrow emote
                    str_game_grid += '\n' + '➡️ ' + '👤 ' + player_name + '\n'
                else:
                    # ai turn so no arrow emote on player
                    str_game_grid += '\n' + '👤 ' + player_name + '\n'
                # build player grid
                for list in self.player_grid[0:4]:
                    for element in list:
                        str_game_grid += element
                    str_game_grid += '\n'
        # normal and hard will have 6 rows
        else:
            # check for win condition or timeout or last turn to display proper ending grid
            if game_status == 'player' or game_status == 'ai' or timeout == True or player_turn == 13:
                # TODO: build ai grid first and then player grid second
                # set first line to have no arrow emote
                str_game_grid = '🤖 ' + difficulty + '\n'
                # build ai grid
                for list in self.ai_grid:
                    for element in list[0:5]:
                        str_game_grid += element
                    str_game_grid += '\n'
                # set first line to have no arrow emote
                str_game_grid += '\n' + '👤 ' + player_name + '\n'
                # build player grid
                for list in self.player_grid:
                    for element in list:
                        str_game_grid += element
                    str_game_grid += '\n'
            else:
                # TODO: build ai grid first and then player grid second
                # determine whose turn
                if player_turn % 2 != 0:
                    # player turn so no arrow emote on ai
                    str_game_grid = '🤖 ' + difficulty + '\n'
                else:
                    # ai turn so no arrow emote on player
                    str_game_grid = '➡️ ' + '🤖 ' + difficulty + '\n'
                # build ai grid
                for list in self.ai_grid:
                    for element in list[0:5]:
                        str_game_grid += element
                    str_game_grid += '\n'
                # determine whose turn
                if player_turn % 2 != 0:
                    # player turn so set arrow emote
                    str_game_grid += '\n' + '➡️ ' + '👤 ' + player_name + '\n'
                else:
                    # ai turn so no arrow emote on player
                    str_game_grid += '\n' + '👤 ' + player_name + '\n'
                # build player grid
                for list in self.player_grid:
                    for element in list:
                        str_game_grid += element
                    str_game_grid += '\n'
        # finished grid message
        return str_game_grid

    def get_random_word(self):
        # randomly picks a 5-letter word
        return random.choice(self.five_letter_words)

    def check_guess(self, guess, word, player_turn, difficulty):
        # TODO:
        # check if the guess is a valid word from the dictionary
        # check if the guess has any matches to the correct word
        # returns a boolean

        if guess == '':
            return False
        dictionary = enchant.Dict('en_US')
        #print(str(player_turn) + ' : ' + str(guess) + ' : ' + str(dictionary.check(guess)))
        # checks if the guess is a valid word
        if dictionary.check(guess):
            # check whose turn it is
            if player_turn % 2 != 0:
                # display guess on player turn
                self.player_grid[int(player_turn // 2)][5] = ' ' + guess
            else:
                # display guess on ai turn
                self.ai_grid[int((player_turn / 2) -1)][5] = ' ' + guess
            # check to see if any letters in guess match the actual word
            guess_letter_in_actual_word = 0
            actual_word = word
            for guess_letter in guess:
                if guess_letter in actual_word:
                    guess_letter_in_actual_word = True
                    break
            # check if there are any matches, if it's greater than 0 then there are matches
            if guess_letter_in_actual_word == True:
                # begin to search for matches
                for guess_index, guess_letter in enumerate(guess):
                    #print(guess_letter + ' : ' + str(actual_word) + ' : ' + str(guess_letter in actual_word))
                    # checks if the current letter in guess is in the actual word
                    if guess_letter in actual_word:
                        # if yes then begins to search for the letter in the actual word
                        for actual_word_letter in actual_word:
                            # checks if the letter in guess matches the letter in the actual word
                            #print('comparing: ' + guess_letter + ' : ' + actual_word_letter + ' - searching in: ' + actual_word)
                            if guess_letter == actual_word_letter:
                                # determine index of the letter from the actual word
                                # because the search in actual word gets reduced each iteration
                                actual_word_index = word.index(guess_letter, guess_index)
                                #print('guess index: ' + str(guess_index) + ' - actual word index: ' + str(actual_word_index))
                                if guess_index == actual_word_index:
                                    #print('match: ' + str(guess_index) + ' : ' + str(actual_word_index))
                                    # make tile green
                                    # check whose turn it is
                                    if player_turn % 2 != 0:
                                        # player turn
                                        # turn // 2 gives the row of the list, guess_index gives the column of the list
                                        self.player_grid[int(player_turn // 2)][guess_index] = '🟩'
                                    else:
                                        # ai turn
                                        # (turn / 2) - 1 gives the row of the list, guess_index gives the column of the list
                                        self.ai_grid[int((player_turn / 2) -1)][guess_index] = '🟩'
                                # otherwise it's not in the same spot
                                else:
                                    #print('!! no match: ' + str(guess_index) + ' : ' + str(actual_word_index))
                                    # check if there are any of the same guess letters in the rest of the actual word 
                                    # if there are then leave the current tile black
                                    #print(guess_letter + ' count in ' + guess[guess_index:] + ' : ' + str(guess[guess_index:].count(guess_letter)))
                                    #print(guess[guess_index:].count(guess_letter) > 1 and guess[guess_index:].count(guess_letter) > actual_word.count(actual_word_letter))
                                    if guess[guess_index:].count(guess_letter) > 1 and guess[guess_index:].count(guess_letter) > actual_word.count(actual_word_letter):
                                        #print('duplicate letter: ' + guess_letter)
                                        # continue to limit the search
                                        actual_word = actual_word[1:]
                                        break
                                    else:
                                        # otherwise make tile yellow
                                        # check whose turn it is
                                        if player_turn % 2 != 0:
                                            # player turn
                                            # turn // 2 gives the row of the list, guess_index gives the column of the list
                                            self.player_grid[int(player_turn // 2)][guess_index] = '🟨'
                                        else:
                                            # ai turn
                                            # (turn / 2) - 1 gives the row of the list, guess_index gives the column of the list
                                            self.ai_grid[int((player_turn / 2) -1)][guess_index] = '🟨'
                                # ends current letter to move onto next letter in the search
                                # continue to limit the search
                                actual_word = actual_word[1:]
                                break
                            else:
                                # no matches, black tile
                                if difficulty == 'hard' or difficulty == 'extreme':
                                    if (guess_letter in self.ai_black_tiles) == False and (guess_letter in word) == False:
                                        self.ai_black_tiles.append(guess_letter)
                                if player_turn % 2 != 0:
                                    # player turn
                                    # keep track of black tiles (incorrect letters) from the player
                                    if (guess_letter in self.player_black_tiles) == False and (guess_letter in word) == False:
                                        self.player_black_tiles.append(guess_letter)
                    else:
                        # check for possible yellow matches
                        # search the start instead of the end
                        if guess_letter in word[0:guess_index]:
                            for actual_word_index, actual_word_letter in enumerate(word[0:guess_index]):
                                if guess_letter == actual_word_letter:
                                    if guess_index != actual_word_index and guess.count(guess_letter) <= word.count(guess_letter):
                                        # make tile yellow
                                        # check whose turn it is
                                        if player_turn % 2 != 0:
                                            # player turn
                                            # turn // 2 gives the row of the list, guess_index gives the column of the list
                                            self.player_grid[int(player_turn // 2)][guess_index] = '🟨'
                                        else:
                                            # ai turn
                                            # (turn / 2) - 1 gives the row of the list, guess_index gives the column of the list
                                            self.ai_grid[int((player_turn / 2) -1)][guess_index] = '🟨'
                        # otherwise no matches, black tile
                        #print('letter not in actual word')
                        elif difficulty == 'hard' or difficulty == 'extreme':
                            if (guess_letter in self.ai_black_tiles) == False and (guess_letter in word) == False:
                                self.ai_black_tiles.append(guess_letter)
                        if player_turn % 2 != 0:
                            # player turn
                            # keep track of black tiles (incorrect letters) from the player
                            if (guess_letter in self.player_black_tiles) == False and (guess_letter in word) == False:
                                self.player_black_tiles.append(guess_letter)
                        # guess letter not in actual word - continue to limit the search
                        actual_word = actual_word[1:]
                return True
            else:
                # valid guess but no matches
                if player_turn % 2 != 0:
                    # player turn
                    for guess_letter in guess:
                        # keep track of black tiles (incorrect letters) from the player
                        if (guess_letter in self.player_black_tiles) == False and (guess_letter in word) == False:
                            self.player_black_tiles.append(guess_letter)
                return True
        else:
            # invalid word
            return False

    def check_for_win(self, player_turn):
        # TODO: check for win condition
        if player_turn % 2 != 0:
            # player turn
            # check if the guess is all green - guess matches the actual word
            if self.player_grid[int(player_turn // 2)][:5] == ['🟩', '🟩', '🟩', '🟩', '🟩']:
                return 'player'
        else:
            # ai turn
            if self.ai_grid[int((player_turn / 2) -1)][:5] == ['🟩', '🟩', '🟩', '🟩', '🟩']:
                return 'ai'
    
    def get_ai_black_tiles(self):
        return self.ai_black_tiles
    
    def get_player_black_tiles(self):
        return self.player_black_tiles

    def get_word_difficulty_normal(self, player_turn):
        # TODO: difficulty normal - generates guess that takes into account of green and yellow tiles
        if player_turn == 2:
            return self.get_random_word()
        # handle green and yellow tiles
        elif ('🟩' in self.ai_grid[int((player_turn / 2) - 1) - 1]) == True and ('🟨' in self.ai_grid[int((player_turn / 2) - 1) - 1]) == True:
            # searches for the yellow tiles from previous guess
            yellow_letters = []
            for previous_guess_index, tile in enumerate(self.ai_grid[int((player_turn / 2) - 1)]):
                if tile == '🟨':
                    yellow_letters.append(self.ai_grid[int((player_turn / 2) - 1) - 1][5][previous_guess_index + 1])
            # generate guess with the yellow letters from the previous guess
            generate_complete = False
            while not generate_complete:
                green_tiles = 0
                green_matches = 0
                ai_guess = self.get_random_word()
                # prevent guess to be the same as the previous guesses
                for guess in self.ai_grid:
                    if ai_guess == guess[5][1:]:
                        return ''
                # searches for the green tiles from previous guess
                for previous_guess_index, tile in enumerate(self.ai_grid[int((player_turn / 2) - 1) - 1]):
                    if tile == '🟩':
                        green_tiles += 1
                        for current_guess_index, letter in enumerate(ai_guess):
                            if letter == self.ai_grid[int((player_turn / 2) - 1) - 1][5][previous_guess_index + 1] and previous_guess_index == current_guess_index:
                                green_matches += 1
                temp = ''.join(yellow_letters)
                # searches to see if the guess contains the yellow letters from previous guess
                for letter in yellow_letters:
                    if temp.count(letter) != ai_guess.count(letter):
                        return ''
                if green_matches == green_tiles:
                    generate_complete = True
            #print('green and yellow')
            return ai_guess
        # handle yellow tiles only
        # check if there are any yellow tiles from previous guess
        elif ('🟨' in self.ai_grid[int((player_turn / 2) - 1) - 1]) == True and ('🟩' in self.ai_grid[int((player_turn / 2) - 1) - 1]) == False:
            # searches for the yellow tiles from previous guess
            yellow_letters = []
            for previous_guess_index, tile in enumerate(self.ai_grid[int((player_turn / 2) - 1)]):
                if tile == '🟨':
                    yellow_letters.append(self.ai_grid[int((player_turn / 2) - 1) - 1][5][previous_guess_index + 1])
            # generate guess with the yellow letters from the previous guess
            generate_complete = False
            while not generate_complete:
                ai_guess = self.get_random_word()
                # prevent guess to be the same as the previous guesses
                for guess in self.ai_grid:
                    if ai_guess == guess[5][1:]:
                        return ''
                temp = ''.join(yellow_letters)
                # searches to see if the guess contains the yellow letters from previous guess
                for letter in yellow_letters:
                    if temp.count(letter) != ai_guess.count(letter):
                        return ''
                generate_complete = True
            #print('yellow')
            return ai_guess
        # handle green tiles only
        # check if there are any green tiles from previous guess
        elif ('🟩' in self.ai_grid[int((player_turn / 2) - 1) - 1]) == True and ('🟨' in self.ai_grid[int((player_turn / 2) - 1) - 1]) == False:
            # generate guess with the green letters from the previous guess
            generate_complete = False
            while not generate_complete:
                green_tiles = 0
                green_matches = 0
                ai_guess = self.get_random_word()
                # prevent guess to be the same as the previous guesses
                for guess in self.ai_grid:
                    if ai_guess == guess[5][1:]:
                        return ''
                # searches for the green tiles from previous guess
                for previous_guess_index, tile in enumerate(self.ai_grid[int((player_turn / 2) - 1) - 1]):
                    if tile == '🟩':
                        green_tiles += 1
                        for current_guess_index, letter in enumerate(ai_guess):
                            if letter == self.ai_grid[int((player_turn / 2) - 1) - 1][5][previous_guess_index + 1] and previous_guess_index == current_guess_index:
                                green_matches += 1
                if green_matches == green_tiles:
                    generate_complete = True
            #print('green')
            return ai_guess
        # otherwise generate random guess
        else:
            generate_complete = False
            while not generate_complete:
                ai_guess = self.get_random_word()
                # prevent guess to be the same as the previous guesses
                for guess in self.ai_grid:
                    if ai_guess == guess[5][1:]:
                        return ''
                generate_complete = True
            #print('random')
            return ai_guess

    def get_word_difficulty_hard(self, player_turn):
        # TODO: difficulty hard
        # generates guess that takes into account of green, yellow, and black tiles
        # first turn guess word with 2 vowels
        if player_turn == 2:
            vowels = ['a', 'e', 'i', 'o', 'u']
            ai_guess = self.get_random_word()
            # first turn generate guess that contains at least 2 vowels
            generate_complete = False
            while not generate_complete:
                vowel_matches = 0
                for vowel in vowels:
                    if vowel in ai_guess:
                        vowel_matches += 1
                if vowel_matches >= 2:
                    generate_complete = True
                else:
                    ai_guess = self.get_random_word()
            #print('vowel')
            return ai_guess
        # handle green and yellow tiles
        elif ('🟩' in self.ai_grid[int((player_turn / 2) - 1) - 1]) == True and ('🟨' in self.ai_grid[int((player_turn / 2) - 1) - 1]) == True:
            # searches for the yellow tiles from previous guess
            yellow_letters = []
            for previous_guess_index, tile in enumerate(self.ai_grid[int((player_turn / 2) -1)]):
                if tile == '🟨':
                    yellow_letters.append(self.ai_grid[int((player_turn / 2) -1) - 1][5][previous_guess_index + 1])
            # generate guess with the yellow letters from the previous guess
            generate_complete = False
            while not generate_complete:
                green_tiles = 0
                green_matches = 0
                black_tile_state = False
                while not black_tile_state:
                    ai_guess = self.get_random_word()
                    # prevent guess to be the same as the previous guesses
                    for guess in self.ai_grid:
                        if ai_guess == guess[5][1:]:
                            return ''
                    # prevent guess to contain incorrect letters / black tiles
                    for letter in ai_guess:
                        if letter in self.ai_black_tiles:
                            return ''
                    black_tile_state = True
                # searches for the green tiles from previous guess
                for previous_guess_index, tile in enumerate(self.ai_grid[int((player_turn / 2) -1) - 1]):
                    if tile == '🟩':
                        green_tiles += 1
                        for current_guess_index, letter in enumerate(ai_guess):
                            if letter == self.ai_grid[int((player_turn / 2) - 1) - 1][5][previous_guess_index + 1] and previous_guess_index == current_guess_index:
                                green_matches += 1
                if green_matches != green_tiles:
                    return ''
                temp = ''.join(yellow_letters)
                # searches to see if the guess contains the yellow letters from previous guess
                for letter in yellow_letters:
                    if temp.count(letter) != ai_guess.count(letter):
                        return ''
                generate_complete = True
            #print('green and yellow')
            return ai_guess
        # handle yellow tiles only
        # check if there are any yellow tiles from previous guess
        elif ('🟨' in self.ai_grid[int((player_turn / 2) - 1) - 1]) == True and ('🟩' in self.ai_grid[int((player_turn / 2) - 1) - 1]) == False:
            # searches for the yellow tiles from previous guess
            yellow_letters = []
            for previous_guess_index, tile in enumerate(self.ai_grid[int((player_turn / 2) - 1)]):
                if tile == '🟨':
                    yellow_letters.append(self.ai_grid[int((player_turn / 2) -1) - 1][5][previous_guess_index + 1])
            # generate guess with the yellow letters from the previous guess
            generate_complete = False
            while not generate_complete:
                black_tile_state = False
                while not black_tile_state:
                    ai_guess = self.get_random_word()
                    # prevent guess to be the same as the previous guesses
                    for guess in self.ai_grid:
                        if ai_guess == guess[5][1:]:
                            return ''
                    # prevent guess to contain incorrect letters / black tiles
                    for letter in ai_guess:
                        if letter in self.ai_black_tiles:
                            return ''
                    black_tile_state = True
                temp = ''.join(yellow_letters)
                # searches to see if the guess contains the yellow letters from previous guess
                for letter in yellow_letters:
                    if temp.count(letter) != ai_guess.count(letter):
                        return ''
                generate_complete = True
            #print('yellow')
            return ai_guess
        # handle green tiles only
        # check if there are any green tiles from previous guess
        elif ('🟩' in self.ai_grid[int((player_turn / 2) - 1) - 1]) == True and ('🟨' in self.ai_grid[int((player_turn / 2) - 1) - 1]) == False:
            # generate guess with the green letters from the previous guess
            generate_complete = False
            while not generate_complete:
                green_tiles = 0
                green_matches = 0
                black_tile_state = False
                while not black_tile_state:
                    ai_guess = self.get_random_word()
                    # prevent guess to be the same as the previous guesses
                    for guess in self.ai_grid:
                        if ai_guess == guess[5][1:]:
                            return ''
                    # prevent guess to contain incorrect letters / black tiles
                    for letter in ai_guess:
                        if letter in self.ai_black_tiles:
                            return ''
                    black_tile_state = True
                # searches for the green tiles from previous guess
                for previous_guess_index, tile in enumerate(self.ai_grid[int((player_turn / 2) - 1) - 1]):
                    if tile == '🟩':
                        green_tiles += 1
                        for current_guess_index, letter in enumerate(ai_guess):
                            if letter == self.ai_grid[int((player_turn / 2) - 1) - 1][5][previous_guess_index + 1] and previous_guess_index == current_guess_index:
                                green_matches += 1
                if green_matches == green_tiles:
                    generate_complete = True
            #print('green')
            return ai_guess
        # otherwise generate random guess
        else:
            black_tile_state = False
            while not black_tile_state:
                ai_guess = self.get_random_word()
                # prevent guess to be the same as the previous guesses
                for guess in self.ai_grid:
                    if ai_guess == guess[5][1:]:
                        return ''
                # prevent guess to contain incorrect letters / black tiles
                for letter in ai_guess:
                    if letter in self.ai_black_tiles:
                        return ''
                black_tile_state = True
            #print('random')
            return ai_guess

    def get_word_difficulty_extreme(self, player_turn, word):
        # TODO: difficulty extreme
        # generates guess that takes into account of green, yellow, and black tiles
        # first turn guess word with 2 vowels
        # first turn randomly exclude black tiles
        if player_turn == 2:
            random_black_tiles = []
            alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            # first turn
            # randomly generate incorrect letters to put in black tile list to limit ai search
            # which increases the ai chances of winning
            incorrect_letters = 0
            while incorrect_letters < 6:
                letter = random.choice(alphabet)
                if (letter in word) == False:
                    random_black_tiles.append(letter)
                    alphabet.remove(letter)
                    incorrect_letters += 1
            vowels = ['a', 'e', 'i', 'o', 'u']
            ai_guess = self.get_random_word()
            generate_complete = False
            while not generate_complete:
                # prevent guess to contain incorrect letters / black tiles
                for letter in ai_guess:
                    if (letter in self.ai_black_tiles) == True or (letter in random_black_tiles):
                        return ''
                # randomly generate guess that contains at least 2 vowels
                vowel_matches = 0
                for vowel in vowels:
                    if vowel in ai_guess:
                        vowel_matches += 1
                if vowel_matches >= 2:
                    generate_complete = True
                else:
                    ai_guess = self.get_random_word()
            # append the letters from random_black_tiles into ai_black_tiles
            for letter in random_black_tiles:
                if (letter in self.ai_black_tiles) == False:
                    self.ai_black_tiles.append(letter)
            #print('\nblack tiles on first turn: ' + str(self.ai_black_tiles))
            #print('vowel')
            return ai_guess
        # handle green and yellow tiles
        elif ('🟩' in self.ai_grid[int((player_turn / 2) - 1) - 1]) == True and ('🟨' in self.ai_grid[int((player_turn / 2) - 1) - 1]) == True:
            # searches for the yellow tiles from previous guess
            yellow_letters = []
            for previous_guess_index, tile in enumerate(self.ai_grid[int((player_turn / 2) -1)]):
                if tile == '🟨':
                    yellow_letters.append(self.ai_grid[int((player_turn / 2) -1) - 1][5][previous_guess_index + 1])
            # generate guess with the yellow letters from the previous guess
            generate_complete = False
            while not generate_complete:
                green_tiles = 0
                green_matches = 0
                black_tile_state = False
                while not black_tile_state:
                    ai_guess = self.get_random_word()
                    # prevent guess to be the same as the previous guesses
                    for guess in self.ai_grid:
                        if ai_guess == guess[5][1:]:
                            return ''
                    # prevent guess to contain incorrect letters / black tiles
                    for letter in ai_guess:
                        if letter in self.ai_black_tiles:
                            return ''
                    black_tile_state = True
                # searches for the green tiles from previous guess
                for previous_guess_index, tile in enumerate(self.ai_grid[int((player_turn / 2) -1) - 1]):
                    if tile == '🟩':
                        green_tiles += 1
                        for current_guess_index, letter in enumerate(ai_guess):
                            if letter == self.ai_grid[int((player_turn / 2) - 1) - 1][5][previous_guess_index + 1] and previous_guess_index == current_guess_index:
                                green_matches += 1
                if green_matches != green_tiles:
                    return ''
                temp = ''.join(yellow_letters)
                # searches to see if the guess contains the yellow letters from previous guess
                for letter in yellow_letters:
                    if temp.count(letter) != ai_guess.count(letter):
                        return ''
                generate_complete = True
            #print('green and yellow')
            return ai_guess
        # handle yellow tiles only
        # check if there are any yellow tiles from previous guess
        elif ('🟨' in self.ai_grid[int((player_turn / 2) - 1) - 1]) == True and ('🟩' in self.ai_grid[int((player_turn / 2) - 1) - 1]) == False:
            # searches for the yellow tiles from previous guess
            yellow_letters = []
            for previous_guess_index, tile in enumerate(self.ai_grid[int((player_turn / 2) - 1)]):
                if tile == '🟨':
                    yellow_letters.append(self.ai_grid[int((player_turn / 2) -1) - 1][5][previous_guess_index + 1])
            # generate guess with the yellow letters from the previous guess
            generate_complete = False
            while not generate_complete:
                black_tile_state = False
                while not black_tile_state:
                    ai_guess = self.get_random_word()
                    # prevent guess to be the same as the previous guesses
                    for guess in self.ai_grid:
                        if ai_guess == guess[5][1:]:
                            return ''
                    # prevent guess to contain incorrect letters / black tiles
                    for letter in ai_guess:
                        if letter in self.ai_black_tiles:
                            return ''
                    black_tile_state = True
                temp = ''.join(yellow_letters)
                # searches to see if the guess contains the yellow letters from previous guess
                for letter in yellow_letters:
                    if temp.count(letter) != ai_guess.count(letter):
                        return ''
                generate_complete = True
            #print('yellow')
            return ai_guess
        # handle green tiles only
        # check if there are any green tiles from previous guess
        elif ('🟩' in self.ai_grid[int((player_turn / 2) - 1) - 1]) == True and ('🟨' in self.ai_grid[int((player_turn / 2) - 1) - 1]) == False:
            # generate guess with the green letters from the previous guess
            generate_complete = False
            while not generate_complete:
                green_tiles = 0
                green_matches = 0
                black_tile_state = False
                while not black_tile_state:
                    ai_guess = self.get_random_word()
                    # prevent guess to be the same as the previous guesses
                    for guess in self.ai_grid:
                        if ai_guess == guess[5][1:]:
                            return ''
                    # prevent guess to contain incorrect letters / black tiles
                    for letter in ai_guess:
                        if letter in self.ai_black_tiles:
                            return ''
                    black_tile_state = True
                # searches for the green tiles from previous guess
                for previous_guess_index, tile in enumerate(self.ai_grid[int((player_turn / 2) - 1) - 1]):
                    if tile == '🟩':
                        green_tiles += 1
                        for current_guess_index, letter in enumerate(ai_guess):
                            if letter == self.ai_grid[int((player_turn / 2) - 1) - 1][5][previous_guess_index + 1] and previous_guess_index == current_guess_index:
                                green_matches += 1
                if green_matches == green_tiles:
                    generate_complete = True
            #print('green')
            return ai_guess
        # otherwise generate random guess
        else:
            black_tile_state = False
            while not black_tile_state:
                ai_guess = self.get_random_word()
                # prevent guess to be the same as the previous guesses
                for guess in self.ai_grid:
                    if ai_guess == guess[5][1:]:
                        return ''
                # prevent guess to contain incorrect letters / black tiles
                for letter in ai_guess:
                    if letter in self.ai_black_tiles:
                        return ''
                black_tile_state = True
            #print('random')
            return ai_guess

    