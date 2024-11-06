# CS1210: HW1
######################################################################
# Welcome to HW1! You should approach HW1 much like a collection of
# QotDs, with some being more challenging than others. Unlike QotDs,
# however, you have several additional responsibilities.
#
# First, the autograder here will not be that helpful: it simply
# checks that your code has uploaded successfully, the file is named
# correctly, and the code loads cleanly in Python. So you will have to
# DEVISE YOUR OWN TEST CASES to test each individual function with the
# autograder doing it for you.
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
from random import randint
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
# Specification: newDeck() returns a new, cannonically ordered card
# deck. The parameters determine how many cards per suit and the names
# of the suits. Specifying n=13 with the usual 4 suits generates a
# regular deck; the default is to produce a 40 card deck with the
# usual four suits.
#
# Your newDeck() function should construct the deck in suit order,
# with cards within suit sorted by value. So, for example:
#
#   >>> newDeck(3, ('A', 'B'))
#   [(1, 'A'), (2, 'A'), (3, 'A'), (1, 'B'), (2, 'B'), (3, 'B')]
#
# Your solutions should use one or more comprehensions. 
#
def newDeck(n=10, suits=('spades', 'hearts', 'clubs', 'diamonds')):
    '''Makes a new deck with all the cards per suit.'''
    return([(x,y) for x in range(1, n+1) for y in suits ])
   
   

#print(newDeck(10))

#print( newDeck(3, ('A', 'B')))
#print(newDeck(10))
######################################################################
# Specification: displayCard() constructs and returns a string
# representation of a given card c using special unicode characters
# for hearts, diamonds, clubs, and spades.
#
# You don't need to do anything here: this function is useful for
# providing pretty output, such as, for example:
#
#   >>> print(', '.join([ displayCard(c) for c in newDeck()[:5] ]))
#   1♠, 2♠, 3♠, 4♠, 5♠
#
def displayCard(c):
    '''Returns a string representation of card c, a tuple.'''
    suits = {'spades':'\u2660', 'hearts':'\u2661',
             'diamonds':'\u2662', 'clubs':'\u2663'}
    return(''.join( [ str(c[0]), suits[c[1]] ] ))

######################################################################
# Specification: shuffle() takes a list (like a deck) and randomizes
# order of the cards in place. In a sense, this is the opposite of the
# in-place sorting algorithms we've been studying in class -- this of
# it as an in-place "unsorting" algorithm.
#
# The algorithm you will implement is called the Fisher-Yates-Knuth
# fair shuffle. 
#
# The general idea is usually to work from one end of the list to the
# other; in this example, we'll work right-to-left down the list,
# starting with the last element, although one could as easily work
# left-to-right.
#
# At each step, a randomly selected element from the unrandomized head
# of the list is exchanged with the last element, sort of like for
# selection sort. The process is then repeated on all-but-the-last
# element of the list, that is, on a list that is shorter by one
# position. As you work right-to-left, the tail of the list emerges
# randomized, as the head of the list is subject to reordering.
#
# So, starting with L=[1, 2, 3, 4, 5], we start with i=4 and select at
# random an element of L[0:4] (inclusive) at random and exchange it
# with L[4]. So, for example:
#      [1, 2, 3, 4, 5] becomes [1, 2, 5, 4, 3] when 3 selected
# Then, we repeat the process with i=3 selecting an
# element between L[0:3]. So, for example:
#      [1, 2, 5, 4, 3] becomes [1, 2, 4, 5, 3] when 5 selected
# and then for i=2:
#      [1, 2, 4, 5, 3] becomes [4, 2, 1, 5, 3] when 1 selected
# etc.
#
# Let's talk a bit about why Fisher-Yates-Knuth is "fair."  Here,
# "fair" is defined as the situation where "every permutation of the
# list has an equal chance of emerging from the shuffle." Another way
# to think about this is that "every element of the list has an equal
# probability of ending up in any location."
# 
# So: for the example given above, 3 was selected to occupy position 4
# in the first round (remember, Python is 0-indexed) with probability 1/5.
#
# In the second round, 5 was selected to occupy position 3 with
# probability 1/4 -- but, remember 5 "survived" the first round with
# probability 4/5, so the actual probability that 5 will occupy
# position 3 is (4/5)*(1/4) or also 1/5.
#
# In general, the probability that an element occupies position i will be:
#   ((N-1)/N)*((N-2)/(N-1))*(N-3)/(N-2)* ... * (i/(i+1))*(1/i) = 1/N
# so every element is equally likely to end up in any spot; hence the
# shuffle is "fair."
# 
# Finally, remember your function should not return a value, but
# rather should modify D.
#

def shuffle(D):
    '''Shuffles the Deck with the Fisher-Yates-Knuth method. This is the most "fair" shuffling method'''
    for i in range(len(D) -1,0,-1):
        rand = randint(0, i)# Generate a random index thats in the list
        D[i], D[rand] = D[rand], D[i] # Swaps the current index with random index
    return (D)


#print(shuffle([1,2,3,4,5,6,7,8,9,10]))

   

######################################################################
# Specification: cut() takes a list (the deck) and exchanges the front
# and back of the deck, where front and back are defined by a randomly
# selected cut point.
#
# Remember, your function should not return a value, but rather should
# modify D. Careful! This can be a little tricky! Make sure you
# understand why.
#
def cut(D):
    '''Randomly cuts the deck and swaps the 2 indices'''
    cuts= randint(0,len(D)-1)
    D[:] = D[cuts:] + D[:cuts]
  
######################################################################
# Specification: deal() deals up to 3 cards from D to each of the
# players in a round-robin fashion, provided there are sufficent cards
# left in the deck. The parameters are D, the deck, and H, a list of N
# lists, where each sublist is a collection of cards corresponding to
# the corresponding player's hand. The function should modify D (by
# removing dealt cards) and H (by adding up to 3 cards to each
# players' hand.
#
# Note that, if the deck doesn't contain at least 3*len(H) cards, the
# function deals all the remaining cards to the players even if this
# results in some players recieving one fewer card than the others.
#
# Your function should not return a value, but rather should modify D
# and H as appropriate.
# 
def deal(D, H):
    '''This function deals out a max of 3 cards per player in a round robin style.'''
    for H2 in H:   #deals max of 3 cards to player, if enough cards in deck
        if len(D) > 0:
            H2.append(D.pop(0)) #deal card 1
        if len(D) > 0:
            H2.append(D.pop(0)) #deal card 2
        if len(D) > 0:
            H2.append(D.pop(0)) #deal card 3
        if len(D) == 0:   #stops when deck is empty
            break

######################################################################
# Specification: inputMove(i, T, H) returns (c, M) where c is a card
# selected and removed from H[i] and M is either [] (in which case we
# discard c to table), or a list of indexes in range(0, len(T)).
#
# This function is the human input version of selectMove() below. It
# relies on the numbering of cards in T and H[i] for player 0 provided
# in the play() function below (these are the indexes mentioned in the
# comments below).
#
# There is nothing for you to do for this function, but you should
# study it so that you are familiar with how it works.
#
def inputMove(i, T, H):
    '''Solicit a move, defined as (c, M), where c is the index of a card
       in this player's hand, and M, a (possibly empty) list of
       indexes of cards on the table that sum to the value of c. If M
       is empty, the move is a discard.'''
    # Prompt player i for card to play from H[i].
    while True:
        # Capture any errors from non-integer inputs.
        try:
            c = int(input('Play which card? '))
            # Validate the input; try again if not valid.
            if c < len(T) or c > len(T) + len(H[i]):
                # Invalid card index.
                continue;
            # Good input; normalize to make it wrt to H and not H+T,
            # then abort the loop.
            c = c - len(T)
            break
        except:
            # Wonky input: trap the error and try again.
            print('Choose an index from hand.')
            pass
    # Prompt player i for list of indeces to match.
    while True:
        # Capture any errors from non-integer inputs.
        try:
            M = [ int(m) for m in input('Select matching indexes separated by spaces (blank to discard): ').split() ]
            # Validate the input.
            if not all( [ 0 <= m < len(T) for m in M ] ):
                # Invalid card indexes.
                continue;
            elif M and H[i][c][0] != sum( [ T[m][0] for m in M ] ):
                # Invalid card values (don't add up).
                continue;
            # Good input: abort the loop.
            break
        except:
            # Wonky input: trap the error and try again.
            print('Enter list of indexes separated by spaces.')
            pass
    return((c, M))

######################################################################
# Specification: selectMove(i, T, H) returns (c, M) where c is the
# index of a card in H[i] and M is either [] (in which case we discard
# c to table), or a list of indexes of cards in T, where the sum of
# the values of these cards sum to the value of c.
#
# selectMove() is essentially an autoplayer. Each time its called, it
# selects a move that specific particular player will play. This can
# be extremely complicated (e.g., attempting to optimize the final
# score), or it can be as simple as choosing a move from the set of
# legal moves at random.
#
# The helper function provided, findMoves(value), returns a list of
# tuples corresponding to all legal moves available when a player
# plays a card with the specified value (including the empty tuple,
# which corresponds with discarding the card to the table).
#
# Complete this function by adding a mechanism to choose the move from
# amongst those generated by findMoves(). You may elect to play a
# random move selected from the legal moves for a randomly selected
# card, or you may choose to be more strategic, by, for example,
# optimizing table sweeps (scopa!). It's entirely up to you as long as
# you return (c, M) corresponding to indexes into H[i] and T,
# respectively.
#
# Most of this function is provided for you. You will need to complete
# sections of the function indicated between the comment "START HERE"
# and "END HERE."
#
def selectMove(i, T, H):
    '''Automatically select a move, defined as (c, M), where c is the
       index of a card from this player's hand, and M, a (possibly
       empty) tuple of indexes of cards on the table that sum to the
       value of c (an empty M represents a discard). '''

    # Specification: findMoves() is a recursive helper function which,
    # when provided a card value, returns a list of tuples
    # representing all of the possible M value for the current table T
    # that correspond to value, including the empty tuple (represents
    # a discard).
    def findMoves(value, i=0, match=(), result=[()]):
        if value == 0:
            return(result + [match])
        elif i==len(T) or value < 0:
            return(result)
        result = findMoves(value-T[i][0], i+1, match+(i,), result)
        return(findMoves(value, i+1, match, result))

    ##################################################
    # START HERE
    ##################################################
    '''This function finds all possible moves and favors the best moves.'''
    possible = []  #gets all possible moves for each card
    for c in range(len(H[i])):
        moves = findMoves(H[i][c][0])
        possible.append((c,moves)) ## find moves for the card's value

    #favor moves
    for m in possible:
        for combo in m[1]:
            if len(combo) > 1: #prefer
                return(m[0],combo)
    
    for m in possible: #no multi card combo, take other move
        for combo in m[1]:
            if len(combo) > 0:
                return(m[0],combo)

    #no capture move, discard the card
    return (possible[0][0], ())
    


    ##################################################
    # END HERE
    ##################################################

######################################################################
# Specification: updateScores(C, S, W) updates the scoring array S
# according to the scoring priorities described in the handout, which
# are based on each player's capture pile, C[i].
#
# You will need to account for the ''sette bello,'' who captures the
# most ''ori'', who captures the most cards, and who has the best
# ''primiera.''
#
# Recall that any ''scope'' realized by player i are added to S[i] as
# they are executed.
#
def updateScores(C, S, W):
    '''This function updates the scores according to all the different ways to score points.'''
    #Sette bello
    for i in range(len(C)):
        if (7, 'diamonds') in C[i]:
            S[i] += 1 #adds 1 if u have 7 of diamonds
    
    #Most cards
    maxindex = 0
    for i in range(len(C)):
        if len(C[i]) > len(C[maxindex]):
            maxindex = i #updates it to current index
    S[maxindex] += 1
    

    #primiera
    primieras = [0] * len(C)  

    for i in range(len(C)):
        # Organize cards by suit
        suits = {
            'spades': [card[0] for card in C[i] if card[1] == 'spades'],
            'hearts': [card[0] for card in C[i] if card[1] == 'hearts'],
            'clubs': [card[0] for card in C[i] if card[1] == 'clubs'],
            'diamonds': [card[0] for card in C[i] if card[1] == 'diamonds']
        }
        
        # Calculate primiera score as the sum of the highest card in each suit
        primieras[i] = sum(max(suits[suit], default=0) for suit in suits)
        print(f"Player {i} primiera score: {primieras[i]}")  # Debugging: Check each player’s primiera score

    #update score
    S[primieras.index(max(primieras))] += 1




######################################################################
# Specification: play() governs game play for N players (2 by default)
# using a len(suits)*K-card deck (40 by default).
#
# The game is played in a series of ''hands'' until a player reaches W
# points (default 11). Each ''hand'' is divided in a sequence of
# ''tricks,'' where a trick involves a player playing a card in their
# hand by either adding it to the table or using it to capture cards
# from the table. For more complete information, read the handout.
#
# Most of this function is provided for you. You will need to complete
# sections of the function indicated between the comment "START HERE"
# and "END HERE."
#
def play(N=2, K=10, suits=('spades', 'hearts', 'clubs', 'diamonds'), W=11):
    '''Manages a game up to W points for N players using a len(S)*N deck of cards.'''
    S = [ 0 ] * N		   # Player scores (human is S[0])
    # Record last player to take a card from T

    # Play a game.
    while max(S) < W:
        D = newDeck(K, suits)	       # Create a deck
        H = [ [] for i in range(N) ]   # Player hands (human is H[0])
        C = [ [] for i in range(N) ]   # Player's capture pile (human is C[0])
        last = None                    # Last player to capture from table
        # Play the hand.
        while D:
            # Cut the deck and deal the cards.
            print("\n=========\nDealing...", end='')
            # Shuffle the deck.
            shuffle(D)
            # Cut the deck.
            cut(D)
            # Deal 3 cards to each player in H.
            deal(D, H)
            # Create a list T representing the table, and populate it with
            # the first 4 cards from what remains of D (make sure to
            # remove cards on T from what remains of D).
            T,D[:4] = D[:4],[]
            print("{} cards remain".format(len(D)))

            # Hand continues while the first player's hand is not empty.
            while H[0]:
                # For each player.
                for i in range(0, len(H)):
                    # First, make sure player i has something left to
                    # play in case there was an uneven distribution of
                    # cards (occurs when D runs out). Because of how
                    # we dealt the cards, as soon as player i runs out
                    # of cards, the remaining players >i will have
                    # empty hands as well, so we can exit the loop.
                    if not H[i]:
                        break
                    
                    # Good to go. Show the state of the game from
                    # player 0's perspective (i.e., do not reveal
                    # player i's hand, because player 0 is watching).
                    print("\n=========\nPlayer {}'s turn:".format(i))
                    print('  Table:  {}'.format(', '.join([ "[{}] {}".format(j, displayCard(T[j])) for j in range(len(T)) ] )))

                    # Determine next move: remember, player 0 is by
                    # definition the human player, so move generation
                    # is different.
                    if i == 0:
                        # Human player
                        print('  MyHand: {}'.format(', '.join([ "[{}] {}".format(j+len(T), displayCard(H[i][j])) for j in range(len(H[i])) ] )))
                        (c, M) = selectMove(i, T, H)
                    else:
                        # Auto player
                        (c, M) = selectMove(i, T, H)
                    
                    ##################################################
                    # START HERE
                    ##################################################
                    # Execute the move (c, M); make sure you update
                    # the variable last if the player captures any
                    # cards.
                    '''This updates the players pile, their deck and the table.'''
                    # if no matches, discard to table and removes card from hand    
                    if not M:
                        T.append(H[i].pop(c))

                    #if a match, put the selected card and all matches into pile
                    else:
                        #add matching cards from table to the pile
                        C[i].append(H[i].pop(c))#Add selected card to pile
                        C[i].extend(T[j] for j in M) #add matching cards to the pile
                        T = [T[j] for j in range(len(T)) if j not in M]
                       
                        last = i


                        ##################################################
                        # END HERE
                        ##################################################

                    # Update your score for a "scopa" when you've
                    # swept the table. This is the only time a point
                    # is awarded during a hand; all other points are
                    # assigned by updateScores() at the end of the
                    # hand.
                    if M and not T:
                        print("\n=========\nScopa! Scopa!\n=========\n")
                        S[i] = S[i]+1

        # Hand over. Gift any remaining cards on table to player
        # who made the last capture (= last).
        if T:
            print("Done: awarding {} from table to Player {}".format(', '.join([ displayCard(c) for c in T ]), last))
            C[last].extend(T)

        # Update player scores as described in the handout. Remember,
        # any clean "scope" (table sweeps) have already been
        # recorded. 
        updateScores(C, S, W)
        print("Current scores: {}".format(S))

    # Game over. Indicate who won.
    print("Game over: Player {} wins with a score of {} points.".format(S.index(max(S)), S[S.index(max(S))]))

play()