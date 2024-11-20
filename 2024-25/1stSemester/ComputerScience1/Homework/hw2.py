# CS1210: HW2
######################################################################
# Welcome to HW2! Please read the accompanying handout carefully, and
# post your questions on Piazza.
#
# Remember, the autograder here will not be that helpful: it simply
# checks that your code has uploaded successfully and the file is
# named correctly. You will have to DEVISE YOUR OWN TEST CASES to test
# each individual function with the autograder doing it for you.
#
# Second, while each function comes with a specification, you will be
# RESPONSIBLE FOR ALL ADDITIONAL DOCUMENTATION, including a doc string
# for each function and helpful in-line comments (think: brief and
# meaningful!). See the other functions provided for insight into the
# expected level and type of comments you should be adding.
#
# Third, you should feel free to insert, e.g., additional print
# statements in your code for debugging purposes but BE CAREFUL and
# COMMENT THESE OUT in your final uploaded version (extraneous print
# statements can interfere with the autograder).
#
# Good luck! Don't wait to get started.
#
# We'll need this function later.
from random import choice
import os 
print(os.getcwd()) # Prints the current working directory
from string import printable
from math import log		# NEW: needed for entropy calculation
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely your own work, and
#  2) you have not shared it with anyone.
#
# ToDo: Change the word "hawkid" between the two double quote marks to
# match your own hawkid. Your hawkid is the "login identifier" (not
# your email address) that you use to login to all University
# services.
#
def signed():
    return(["cmcano"])

######################################################################
# Wordle, with hints.
class Wordle():
    # The __init__(self) method is called on construction of a new
    # object of class Wordle. It initializes the game statistics and
    # reads in the dictionary of legal words from the specified file.
    def __init__(self, filename='words.dat', cheat=False):
        '''Initialization method called by class constructor.'''
        self.G = 0		# Games played
        self.W = 0		# Games won
        self.cheat = cheat
        self.state = 5*'.'	# State of the current game
        with open(filename, 'r') as infile:
            self.D = infile.read().lower().split()
        print("{} words read.".format(len(self.D)))

    # The __repr__(self) method is the default method used to print a
    # representation of this object. We won't bother with __str__().
    def __repr__(self):
        '''Prints out the state of the game as the object representation.'''
        return(self.state)

    # evalGuess(self, guess, target) compares guess, a lower-case
    # string, to the hidden target word. It returns a feedback string
    # that is equal in length to both word and target, consisting of
    # either upper or lower case characters from word or the '.'
    # character.
    #
    # The general approach is to construct the feedback string as a
    # list of characters by jointly iterating over guess and target,
    # retaining upper cased matching letters or the non-matching '.'
    # character. Any characters in the guess that do not match the
    # target word are retained in extra for further processing.
    #
    # We then scan the guess again, and if its i.th letter is not a
    # match but is in extra (the mispositioned matches), replace the
    # '.' with a lower case version.
    #
    def evalGuess(self, guess, target):
        '''Takes a guess and compares it to the target word, returning a feedback 
           pattern that embodies all the hard constraints (matching letters/locations) 
           and soft constraints (matchine letters but not locations.'''
        feedback = []   # Construct feedback
        extra = []      # Unmatched letters from target

        # Find matches between guess and target while building pool of
        # unmatched letters from target.
        for i in range(5):
            if guess[i] == target[i]:
                # Match; update feedback.
                feedback.append(guess[i].upper())
            else:
                feedback.append('.')
                # Add unmatched target letter to extra.
                extra.append(target[i])

        # Now scan your guess again looking to incorporate any extra
        # (unmatched) characters from target wherever they may occur.
        #if self.cheat:
        #    print("Unmatched target letters: {}".format(extra))
        for i in range(5):
            if feedback[i] == '.' and guess[i] in extra:
                feedback[i] = extra.pop(extra.index(guess[i])).lower()

        # Splice the feedback back together and return it.
        return(''.join(feedback))

    # This tricky method implements Wordle's hard mode. It returns
    # True if the feedback is consistent with guess, where
    # "consistent" ensures that every upper-case feedback letter
    # occurs in the corresponding letter location, and every
    # lower-case feedback letter also occurs, but not at that
    # corresponding letter location.
    #
    def consistent(self, feedback, guess):
        '''Returns True if feedback pattern is consistent with
           guess, and False otherwise.'''
        reqd=[]     # unmatched lowercase feedback
        pool=[]     # unmatched guess letters

        # Step through guess and feedback in lock step.
        for i in range(len(feedback)):
            if feedback[i].isupper():
                # This is a required match letter!
                if guess[i] != feedback[i].lower():
                    # Failure to match required letter/position. 
                    #if self.cheat:
                    #    print("{}.1a: {} != {}".format(i, feedback[i], guess[i]))
                    return(False)
                #elif self.cheat:
                #   print("{}.1b: {} == {}".format(i, feedback[i], guess[i]))
            elif feedback[i] == '.':
                # Add corresponding guess letter to pool.
                #if self.cheat:
                #    print("{}.2: adding {} to pool".format(i, guess[i]))
                pool.append(guess[i])
            elif feedback[i] == guess[i]:
                # Reject guesses with letters that match lower-case
                # feedback.
                #
                # NEW: in the original wordle8.py implementation, this
                # feature was only turned on in cheat mode. But a
                # quick review of the original NYTimes Wordle puzzle
                # confirms that, for example, guessing "steal" is not
                # consistent with feedback that reads ".t..." simply
                # because the 't' in 'steal' should not be allowed to
                # match a lower-case 't' in the feedback: if "steal"
                # were a consistent guess, then the feedback pattern
                # would have read ".T...."  and not ".t...."
                #if self.cheat:
                #    print("{}.3: won't match {} to {}".format(i, guess[i], feedback[i]))
                return(False)
            elif feedback[i] in pool:
                # Required letter is available in pool (has already been encountered).
                #if self.cheat:
                #    print("{}.4: consuming {} from {}".format(i, feedback[i], pool))
                #    print("{}.4: adding {} to pool".format(i, guess[i]))
                pool.pop(pool.index(feedback[i]))
                # Don't forget to add current letter for future use.
                pool.append(guess[i])
            else:
                # Required letter is not available in pool (not yet encountered).
                #if self.cheat:
                #    print("{}.5: postponing {}".format(i, feedback[i]))
                #    print("{}.5: adding {} to pool".format(i, guess[i]))
                reqd.append(feedback[i])
                # Don't forget to add current letter for future use.
                pool.append(guess[i])
        # So far so good. Now make sure all remaining required letters
        # did eventually end up in the pool.
        #if self.cheat:
        #    print("{}.6: reqd={}, pool={}".format(i, reqd, pool))
        for letter in reqd:
            if letter in pool:
                pool.pop(pool.index(letter))
            else:
                return(False)
        return(True)
    
    # NEW: expandPattern() takes a pattern, like the feedback string
    # returned by evalGuess() which represents a set of "hard"
    # constraints (uppercase letters) and "soft" constraints
    # (lowercase letters). It also takes a dictionary representing the
    # "soft" constraints, where the keys are the lower case letters in
    # pattern and the values are the number of times that lower case
    # letter occurs in the pattern. Finally, there is a third
    # parameter that is used to construct the instantiated pattern as
    # you descend the recursion. It returns the set of all of the
    # mutually-exclusive instantiated patterns that match the pattern.
    def expandPattern(self, pattern, softCnt, match=''):
        """
        Generate all valid patterns for the given pattern, considering remaining soft constraints.
        """

        def isValidMatch(softCnt):
            """
            Helper function that checks if all soft constraints are satisfied.
            """
            return all(softCnt[char] == 0 for char in softCnt)

        def processCharacter(char, softCnt, match):
            """
            Helper function that processes the current character in the pattern.
            """
            matches = set()

            # If the character is uppercase, it must be added directly
            if char.isupper():
                return self.expandPattern(pattern, softCnt, match + char)

            # For lowercase letters or '.', try all possible soft matches
            if char.islower() or char == '.':
                # Attempt each soft constraint
                for softChar, count in softCnt.items():
                    if count > 0 and softChar != char:
                        # Clone the soft constraints and decrement the used soft character
                        updatedSoft = softCnt.copy()#clones
                        updatedSoft[softChar] -= 1
                        matches.update(self.expandPattern(pattern, updatedSoft, match + softChar))

                # Always try adding '.'
                matches.update(self.expandPattern(pattern, softCnt, match + '.'))

            return matches

        # Base case: If the match length reaches the feedback pattern length
        if len(match) == 5:
            if isValidMatch(softCnt):
                return {match.upper()}  # Return as a valid match
            return set()  # No valid match if soft constraints are not satisfied

        # Recursive case: Process the current character
        currentChar = pattern[len(match)]
        return processCharacter(currentChar, softCnt, match)

#print(w.expandPattern("E.v..", {'v':1}))
#print(w.expandPattern('.at.Y', {'t':1, 'a':1}))

    # NEW: Returns a good word to play. The result should be the word
    # in S that corresponds to the highest entropy value.
    '''
    Function to determine the best guess based on maximum entropy and the given target.
    '''
    def hint(self, S, target):
        def calculate_entropy(bins, remainingWords):
            """
            Helper function to compute entropy based on how words are distributed into bins.
            """
            total_words = len(remainingWords)
            return sum(-count / total_words * log(count / total_words, 2) for count in bins.values())

        def generate_feedback_bins(candidate, target, S):
            """
            helper function to create the bins of the remaining words
            """
            bins = {}

            # Generate feedback pattern between candidate and the target word
            feedback = self.evalGuess(candidate, target)

            # Expand the feedback pattern using soft constraints
            soft_constraints = {char: feedback.count(char) for char in feedback if char.islower()}
            expanded_patterns = self.expandPattern(feedback, soft_constraints)

            # Use the expanded patterns to categorize words in S
            for word in S:
                # Check if the word fits any of the expanded patterns
                for pattern in expanded_patterns:
                    # Generate the feedback for this word compared to the candidate
                    word_feedback = self.evalGuess(candidate, word)
                    if word_feedback == pattern:
                        bins[pattern] = bins.get(pattern, 0) + 1

            return bins
        
        highest_entropy = -1 #starts at -1 to ensure no entropy can be lower because it needs to be non-negative
        top_guess = None

        # Evaluate each word in S
        for candidate in S:
            # Generate feedback bins for the current candidate
            feedbackBins = generate_feedback_bins(candidate, target, S)

            # Calculate entropy for this candidate
            entropy_value = calculate_entropy(feedbackBins, S)
            #print(f"Word: {candidate}, Entropy: {entropy_value}")

            # Update the best guess if this candidate is better
            if entropy_value > highest_entropy:
                highest_entropy = entropy_value
                top_guess = candidate
                #print(f"New best guess: {top_guess} (Entropy: {highest_entropy})")

        return top_guess

    # Play one or more rounds of Wordle: select a target word and
    # initialize the available letters.
    def play(self):
        '''Driver function that manages repeated Wordle games.'''
        # NEW: helper function that converts guess history (now a list
        # of tuples rather than a string) into a nicely formatted
        # string and prints it out. This is used in several places
        # throughout the Wordle().play() method.
        def showHistory(history):
            print("Game history:")
            if history:
                print('\n'.join([ "  {}: {} => {}".format(i+1, *history[i]) for i in range(len(history)) ]))
            else:
                print('  No history.')

        # Setup the game.
        more = True		# Continue to play while True
        # Print opening banner. NEW: added instructions for generating a hint.
        print('Welcome to Wordle!')
        print('Enter your guess, or ? for history; $ for a hint; + for new game; or . to exit')

        # Each outer loop corresponds to a new puzzle.
        while more:
            self.state = 5*'.'               # Reset state of game
            target = choice(self.D)
                 # Target word
            letters = list(printable[10:36]) # Unguessed letters
            # NEW: Changed history from a string to a list of (guess,
            # feedback) tuples. We'll need to do some extra work to
            # make this look pretty when we print it out, hence the
            # showHistory() helper function above.
            history = []		     # History of (guess, feedback) entries
            S = set(self.D)	             # Remaining possible solutions
            N = 6	   		     # Remaining guesses

            # Cheating!
            if self.cheat:
                print("Sshhhh....the solution is '{}'".format(target))

            # NEW: Increment game counter. We completely forgot to
            # keep track of how many games were played!
            self.G = self.G + 1

            # Repeat while guesses remain. Each loop here represents a
            # guess or processing of a control instruction (which does
            # not count as a guess).
            while N > 0: 
                # Show legal letters.
                print("Available: {}".format(' '.join(letters)))

                # Prompt the user for a guess. 
                guess = input("\nWordle[{}]  ".format(self.state)).strip().lower()

                # Game management.
                if guess == '.':            # All done!
                    more = False	    # No more games
                    showHistory(history)    # NEW: call history function
                    print("Quit: the target word was {}\n".format(target))
                    break
                elif guess == '+':          # Abort this game
                    showHistory(history)    # NEW: call history function
                    print("Abort: the target word was {}\n".format(target))
                    print("Generating a new Wordle.")
                    break
                elif guess == '?':	    # Show guess history
                    showHistory(history)    # NEW: call history function
                    continue
                elif guess == '~':
                    self.cheat = not self.cheat
                    if self.cheat:
                        print("Sshhhh....the solution is '{}'".format(target))
                    continue
                elif guess == '$' and N == 6:
                    # NEW: Hints are not available for first guess.
                    print("Sorry, no hints on your opening guess.")
                    continue
                elif guess == '$':
                    # NEW: Invoke the Wordle().hint() method to get
                    # the best next word according to our information
                    # theoretical analysis.
                    print("May I suggest {}?".format(self.hint(S, target)))
                    continue
                elif guess in [ guess[0] for guess in history ]:      # No repeated guesses
                    print("You've already guessed {}!".format(guess))
                    continue
                elif guess not in self.D:   # Illegal word.
                    print("Unrecognized word: '{}'".format(guess))
                    continue
                elif not self.consistent(self.state, guess):
                    print("Guess not consistent with prior information {}.".format(self.state))
                    continue
                elif self.cheat and guess not in S:
                    # NEW: In addition to being consistent with
                    # feedback, we can also be stricter, and check
                    # that the guess is still a "legal" solution. But
                    # the NY Times does not prevent you from making
                    # stupid, inconsistent, guesses, so this is not
                    # our default behavior. So we'll only turn it on
                    # in cheat mode, since you're already cheating we
                    # can also save you from yourself.
                    #
                    # Recall that S, which is initialized as a set of
                    # D, the list of legal words, is used to keep
                    # track of all the remaining words that are still
                    # consistent with all of the prior guesses. 
                    print("Guess inconsistent with prior feedback.")
                    continue

                # Accept guess, decrement count, and update feedback.
                self.state = self.evalGuess(guess, target)

                # Add to history. NEW: format of history has changed
                # from a string to a list of (guess, feedback) tuples.
                history.append((guess, self.state))
                N = N - 1

                # If we're done, exit the loop; otherwise accept next guess. NEW: 
                if guess == target:
                    showHistory(history)    # NEW: call history function
                    print("Woot! You win!")
                    print("Generating a new Wordle.")
                    self.W = self.W + 1     # NEW: keep track of the wins.
                    break

                # Update list of available letters. Unlike the real game, we
                # can't shade letters, so the semantics here will be a bit
                # different: an upper case letter is in the word, while lower
                # case are as yet undetermined.
                for i in range(len(self.state)):
                    if guess[i] not in letters:
                        continue
                    elif self.state[i] == '.' and guess[i] not in self.state.lower():
                        letters[letters.index(guess[i])] = '.'
                    else:
                        letters[letters.index(guess[i])] = guess[i].upper()

                # NEW: Update S, the set of remaining possible
                # solutions. S is initialized at the beginning of each
                # game to be a set version of self.D, the dictionary
                # of all legal words. Here, we revise S by removing
                # any words that are inconsistent with the current
                # guess. In this way, S contains all of the remaining
                # legal words -- including the target word -- that are
                # consistent with all guesses so far.
                S = { word for word in S if set(word) <= { l.lower() for l in letters if l != '.' } and
                                            self.consistent(self.state, word) }
            else:
                showHistory(history)    # NEW: call history function
                print("Sorry: the target word was {}\n".format(target))
                print("Generating a new Wordle.")
        print("Thanks for playing Wordle!")
        print("You solved {:.2%} of games played.".format(self.W/self.G))





w=Wordle()
#print(w.expandPattern("E.v..", {'v':1}))
#print(w.expandPattern('.at.Y', {'t':1, 'a':1}))
w.play()

