# MICHAEL JORDAN VS LEBRON JAMES!!!!!!
import random

# Define the Player class to represent a basketball player
class Player:
  def __init__(self, fname, lname, mid_range_acc, three_pt_acc, rebound, speed, has_ball = False):
    # Initialize player attributes: first name, last name, shooting accuracy, rebounding, speed, and possession status
    self.fname = fname
    self.lname = lname
    self.mid_range_acc = mid_range_acc
    self.three_pt_acc = three_pt_acc
    self.rebound = rebound
    self.speed = speed
    self.has_ball = has_ball
    self.position = 30  # Initial position on the court, 30 feet away from the basket
    self.score = 0  # Player's score starts at 0
  
  # Method to handle dribble-drive action (moving towards the basket)
  def dribble_drive(self, other_player):
    if self.has_ball:  # Check if the player has the ball
      print('{} tries to drive to the basket...'.format(self.fname))
      if self.speed > other_player.speed:  # Check if the player is faster than the defender
        drive_success = random.randint(1,5)  # 60% chance of successfully driving closer
        if drive_success >= 3:
          if self.position <= 0:
            print('{} is right at the basket. He can\'t get any closer.'.format(self.fname))
          else:
            self.position -= 5  # Move closer to the basket
            print('What a move! {} is now only {} feet from the basket.'.format(self.lname, self.position))
        else:
          if self.position <= 0:
            print('{} is right at the basket. He can\'t get any closer.'.format(self.fname))
          else:
            print('{} is denied entry. Excellent defense by {}.'.format(self.fname, other_player.lname))
      else:
        # If the player is slower than the defender, they have a 40% chance of success
        drive_success = random.randint(1,5)
        if drive_success == 1 or drive_success == 2:
          if self.position <= 0:
            print('{} is right at the basket. He can\'t get any closer.'.format(self.fname))
          else:
            self.position -= 5
            print('What a move! {} is now only {} feet from the basket.'.format(self.lname, self.position))
        else:
          if self.position <= 0:
            print('{} is right at the basket. He can\'t get any closer.'.format(self.fname))
          else:
            print('{} is denied entry. Excellent defense by {}.'.format(self.fname, other_player.lname))
    else:
      # If the player doesn't have the ball, inform that they're on defense
      print('{player} is on defense. He doesn\'t have possession.'.format(player=self.lname))

  # Method to handle shooting
  def shoot(self, other_player):
    if self.has_ball:  # Check if the player has the ball
      if self.position >= 24:  # If the player is beyond 24 feet, attempt a 3-point shot
        print('{} pulls up from three...'.format(self.lname))
        shot_success = random.randint(1,10)
        if self.three_pt_acc >= 4:  # If the player has a decent 3-point accuracy
          if shot_success >= 7:  # 30% chance of scoring
            self.score += 3  # Add 3 points
            print('Got it! What a shot by {}!'.format(self.lname))
            print('SCORE: {player} - {player_score}, {other_player} - {other_player_score}'.format(player=self.lname, player_score=self.score, other_player=other_player.lname, other_player_score=other_player.score))
            self.take_ball_out(other_player)  # Switch ball possession
          else:
            print('Missed!')
            self.get_rebound(other_player)  # Attempt to get the rebound
        else:  # Lower 3-point accuracy results in a harder chance to score
          if shot_success >= 8:
            self.score += 3
            print('Got it! What a shot by {}!'.format(self.lname))
            print('SCORE: {player} - {player_score}, {other_player} - {other_player_score}'.format(player=self.lname, player_score=self.score, other_player=other_player.lname, other_player_score=other_player.score))
            self.take_ball_out(other_player)
          else:
            print('Missed!')
            self.get_rebound(other_player)
      else:
        # If within 24 feet, attempt a mid-range shot
        print('{} pulls from mid-range...'.format(self.lname))
        shot_success = random.randint(1,10)
        if self.mid_range_acc >= 8:  # Higher mid-range accuracy gives a better chance
          if shot_success >= 4:  # 60% chance of scoring
            self.score += 2  # Add 2 points
            print('Got it! What a shot by {}!'.format(self.lname))
            print('SCORE: {player} - {player_score}, {other_player} - {other_player_score}'.format(player=self.lname, player_score=self.score, other_player=other_player.lname, other_player_score=other_player.score))
            self.take_ball_out(other_player)
          else:
            print('Missed!')
            self.get_rebound(other_player)
    else:
      # Player doesn't have the ball
      print('{player} is on defense. He doesn\'t have possession.'.format(player=self.lname))

  # Method to switch possession of the ball after scoring
  def take_ball_out(self, other_player):
    if self.score < 21 and other_player.score < 21:  # Game continues until a player scores 21
      self.position = 30  # Reset positions
      other_player.position = 30
      self.has_ball = True  # The player now has the ball
      other_player.has_ball = False  # Other player loses the ball
      print('{} is now taking the ball out from behind the arc.'.format(self.fname))

  # Method to handle rebounds after missed shots
  def get_rebound(self, other_player):
    if self.rebound > other_player.rebound:  # Higher rebound attribute increases chances of grabbing the rebound
      rebound_success = random.randint(1,10)
      if rebound_success >= 5:
        print('{} grabs the offensive board.'.format(self.lname))
      else:
        print('{} grabs the defensive board.'.format(other_player.lname))
        other_player.take_ball_out(self)
    else:
      rebound_success = random.randint(1,10)
      if rebound_success >= 1:
        print('{} grabs the defensive board.'.format(other_player.lname))
        other_player.take_ball_out(self)
      else:
        print('{} grabs the offensive board.'.format(self.lname))
        
  # String representation of the Player object
  def __repr__(self):
    return '{} {} is one of the greatest basketball players to ever lace \'em up.'.format(self.fname, self.lname)

# Game class to handle the overall flow of the game
class Game:
  def __init__(self):
    self.winning_score = 21  # Winning score for the game

  # Method to start the game between two players
  def start_game(self, player1, player2):
    player1.score = 0
    player2.score = 0
    player1.position = 30
    player2.position = 30
    print('Good afternoon! It\'s the matchup we\'ve all been waiting for: {} vs {}!'.format(player1.lname, player2.lname))
    print('Only one rule: First to 21 wins!')
    print('We will flip a coin to see who gets the first possession. The player on offense will take the ball out from the 3 point line.')

  # Method to flip a coin to decide first possession
  def coin_flip(self):
    coin_side = random.randint(1,2)  # Randomly decide heads or tails
    return coin_side

  # String representation of the Game object
  def __repr__(self):
    return 'This is a one on one basketball game to {} points. The two players are widely regarded as the two best players to ever play the game.'.format(self.winning_score)

# Game instance and player objects
ball_game = Game()
jordan = Player('Michael', 'Jordan', 9, 4, 6, 8)
lebron = Player('Lebron', 'James', 8, 3, 8, 7)

# Display introduction art
print(""" 
              JORDAN VS LEBRON 2024              .
                         ,-; . ,
                ________i_,',//
          _odHHHHHHHHHHHHHHHHbo_
        dP^'         ;.| ||,; `^?b
       |H           ))`'||/';    H|
        ?bo.     .=;'   |||.' ,odP
          `?oo.-','     ||'oodP'
            /'  /      / |/
           |   |    _-'  ||
          ||  |   ,'     J|
          | \ |   |     / |
           |_\ L  L  .-' |
            \.)`-.;-;__./
              "-._;_.-"
""")

# Player selection
player_selection = int(input('Please select a player. Type 1 for JORDAN or 2 for LEBRON.  '))
while player_selection != 1 and player_selection != 2:  # Ensure valid input
  player_selection = input('Oops. Please type either 1 or 2.  ')

ball_game.start_game(jordan, lebron)

# Assign player based on input
if player_selection == 1:
  player_one = jordan
  player_two = lebron
else:
  player_one = lebron
  player_two = jordan

# Coin toss to decide who starts with the ball
heads_or_tales = int(input('Please type 1 for HEADS or 2 for TALES.  '))

while heads_or_tales != 1 and heads_or_tales != 2:  # Ensure valid input
  heads_or_tales = input('Oops. Please type either 1 or 2. ')

# Display coin flip result
if heads_or_tales == 1:
  print('{p1} has chosen HEADS.'.format(p1=player_one.lname))
else:
  print('{p1} has chosen TAILS.'.format(p1=player_one.lname))

coin_toss_results = ball_game.coin_flip()

# Determine possession based on coin flip
if heads_or_tales == coin_toss_results:
  print('{p1} has won the toss!'.format(p1=player_one.lname))
  player_one.take_ball_out(player_two)
else:
  print('{p2} has won the coin toss!'.format(p2=player_two.lname))
  player_two.take_ball_out(player_one)

# Main game loop
while player_one.score < ball_game.winning_score and player_two.score < ball_game.winning_score:
  if player_two.has_ball:
    # Randomly decide whether the player drives or shoots
    random_choice = random.randint(1,2)
    if random_choice == 2:
      player_two.dribble_drive(player_one)
    else:
      player_two.shoot(player_one)
  else:
    # Player with possession chooses to drive or shoot
    p1_move = int(input('Type 1 to drive to the hole or 2 to take the shot. '))
    if p1_move == 1:
      player_one.dribble_drive(player_two)
    else:
      player_one.shoot(player_two)

# End game result
if player_one.score >= ball_game.winning_score:
  print('{} wins the game!'.format(player_one.lname))
elif player_two.score >= ball_game.winning_score:
  print('{} wins the game!'.format(player_two.lname))
else:
  print('We\'ll call it a draw!')
