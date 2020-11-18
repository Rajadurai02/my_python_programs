import random

money = 100

#Write your game of chance functions here
def coin_flip(user_choice,bet_amount):
    choice = ['Heads','Tails']
    flip = random.choice(choice)
    if (flip == user_choice):
      return money + bet_amount
    else:
     return  money - bet_amount
    
print("Welcome to the coin flip game")
print("you can choose ethier heads or tails and bet your amount")
new_money = coin_flip('Heads',50)
print(new_money)
print("----------------------")
def cho_han(user_choice,bet_amount):
  dice1 = range(1,7)
  dice2 = range(1,7)
  num_dice1 = random.choice(list(dice1))
  num_dice2 = random.choice(list(dice2))
  total = num_dice1 + num_dice2
  if (total % 2 == 0):
    choice = "Even"
  else:
    choice = "Odd"
  if(user_choice == choice):
    return money + bet_amount
  else:
    return money - bet_amount
print("Welcome to the cho_han game")
print("you can choose ethier Odd or Even and bet your amount")
new_money1 = cho_han('Odd',50)
print(new_money1)
print("----------------------") 
def card(bet_amount):
  deck1 = range(1,11)
  deck2 = range(1,11)
  card1 = random.choice(list(deck1))
  card2 = random.choice(list(deck2))
  if (card1 > card2):
    return money + bet_amount
  elif (card1 < card2):
    return money - bet_amount
  else:
    return money + 0
print("Welcome to the deck of cards game")
print("you can choose one random card if the card value is higher than other one card you win and bet your amount")
new_money2 = card(50)
print(new_money2)
print("----------------------") 



#Call your game of chance functions here

