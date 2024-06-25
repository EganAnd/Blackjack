import random
import os
from art import logo
play_again = False
if play_again == False:
  play_start = input("Would you like to play Blackjack? y/n \n")
  if play_start == "y":
    game_on = True
  else:
    print("See ya!")
elif play_again == True:
  game_on = True
while game_on:

  def deal_card():
    card = random.choice(deck)
    return card

  print(logo)
  deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
  player_hand = []
  dealer_hand = ["X"]
  playing = True
  is_winner = False
  player_hand.append(deal_card())
  player_hand.append(deal_card())
  dealer_hand.append(deal_card())
  def display_hands_play():
    print(f"Player hand is {player_hand} and the score is {sum(player_hand)}\n")
    print(f"Dealer hand is {dealer_hand}\n")
  def display_hands_deal():
    print(f"Player hand is {player_hand} and the score is {sum(player_hand)}\n")
    print(f"Dealer hand is {dealer_hand} and the score is {sum(dealer_hand)}\n")
  def calculate_score(hand):
    global playing
    score = sum(hand)
    if len(hand) ==2 and score == 21:
      score = 0
    if score == 0:
      print("Blackjack!")
      playing = False

    if score > 21:
      for index, value in enumerate(hand):
        if value == 11:
          hand[index] = 1
          score = sum(hand)

    if score > 21:
      playing = False
      is_winner = True
    return score

  while is_winner == False:
    while playing:
      display_hands_play()
      player_score = calculate_score(player_hand)
      if player_score == 0:
        break
      deal_again = input("Would you like another card? y/n\n")
      if deal_again == "y":
        player_hand.append(deal_card())
        player_score = calculate_score(player_hand)
        if player_score > 21:
          print("Busted")
          is_winner = True
      else:
        playing = False

    dealer_hand[0] = deal_card()
    dealer_score = calculate_score(dealer_hand)

    while dealer_score < 17:
      if player_score >21 or player_score == 0 or dealer_score == 0:
        break
      dealer_hand.append(deal_card())
      dealer_score = calculate_score(dealer_hand)
      display_hands_deal()
      if dealer_score > 21:
        print("Busted")
        is_winner = True
    is_winner = True

  def compare_scores(score_player, score_dealer):
    result = ""
    if score_player > 21:
      result = "Dealer wins!"
    elif score_dealer > 21:
      result = "Player Wins!"
    elif score_player == score_dealer:
      result = "Draw"
    elif score_player == 0:
      result = "Player wins with Blackjack!"
    elif score_dealer == 0:
      result = "Dealer wins with Blackjack!"
    elif score_player > score_dealer:
      result = "Player wins!"
    elif dealer_score > score_player:
      result = "Dealer wins!"
    return result
  player_score = sum(player_hand)
  dealer_score = sum(dealer_hand)
  print(compare_scores(player_score, dealer_score))
  print(f"Player hand is {player_hand}")
  print(f"Dealer hand is {dealer_hand}")
  play_again = input("Would you like to play again? y/n \n")
  if play_again =="y":
    os.system("clear")
    play_again = True
    continue
  else:
    break
