backpack = {
  "clothes": "",
  "phone": 0,
  "perk": 0,
  "robotname": "",
  "hoverboard": 0,
  "pet_stuff": [],
  "pet_points": 0,
  "hunger": 3,
  "debt": 0
}

home_backpack = {

}
#test_subject()
# def test_subject(money):
#   if backpack["clothes"] == "purple":
#     print("purple clothes")
#   elif backpack["clothes"] == "blue":
#     print("blue clothes")
#   else:
#     game_over("error")



def pet_care(money):
  if backpack["perk"] >= 1:
    print("\nPart of being a responsible pet owner is taking care of your pet.")
    print("What will you buy your pet?")
    print("1) a bed (15 microbucks)")
    print("2) A toy (5 microbucks)")
    print("3) A bed and a toy (20 microbucks)")
    print("4) Skip purchase")
    print("5) Quit Game (All progress will be lost)")
    print(f"Keep in mind you have {money} microbucks.")
    #How to add things to the list:
    #backpack["pet_stuff"].extend(["bed, toy"])
    answer = input(">")

    if answer == "1":
      if money >= 15:
        money -= 15
        backpack["pet_points"] += 1
        backpack["pet_stuff"].extend(["bed"])
        print("\nYou chose the pet bed for 15 microbucks.")
        print("\nBy buying your pet a bed, you earned one pet point.  You can get more pet points by doing different things for your pet.")
        print("These points once saved up can be used to redeem certain things for your pet.")
        print("You now have " + str(backpack["pet_points"]) + f" pet points and {money} microbucks.")

      else: 
        print("\nYou don't have enough microbucks.  Please choose another option.")
        pet_care(money)

    elif answer == "2":
      if money >= 5:
        money -=5
        backpack["pet_stuff"].extend(["toy"])
        print("\nYou chose the dog toy for 5 microbucks. Good choice!")
        print(f"You now have {money} microbucks left.")
      else:
        print(f"\nYou only have {money} microbucks.  Please choose another option.")
        pet_care(money)

    elif answer == "3":
      if money >= 20:
        money -=20
        backpack["pet_points"] += 2
        backpack["pet_stuff"].extend(["bed, toy"])
        print("\nYou chose to buy the pet bed and the toy, good choice!")
        print("This gives you 2 pet points, once you get more pet points you can redeem them for different things!")
        print("You now have " + str(backpack["pet_points"]) + f" pet points and {money} microbucks.")

      else:
        print(f"Sorry, you only have {money} microbucks.  Please choose another option.")
        pet_care(money)

    elif answer == "4":
      print("\nYou chose to skip buying anything for your pet.")

    elif answer == "5":
      game_over("\nYou chose to quit the game.  Come back soon!")

    else:
      print("\nSorry, please make a valid selection.")
      pet_care(money)

      


#robot_name()
def robot_name(money):
  print("\nWhat will you name your robot?")
  backpack["robotname"] = input(">")
  print(backpack["robotname"] + " is now your pet!")
  pet_care(money)


#dinner()
def dinner(money):
    print("\nAfter a long day it's time to get some dinner.")
    print(f"You have {money} microbucks. Choose a restaurant:")
    print("1) Fast food for 10 microbucks")
    print("2) Family restaurant for 30 microbucks")
    print("3) 5 Star restaurant with free perks for 80 microbucks")
    print("4) Skip dinner")

    answer = input(">")

    if answer == "1":
      if money > 10:
        money -= 10
        backpack["hunger"] += 1
        print("\nYou chose the fast food for 10 microbucks.")
        print(f"You now have {money} microbucks left.")
        print("You also have " + str(backpack["hunger"]) + " hunger points left.")
        
      else:
        print(f"\nSorry, it seems you only have {money} microbucks.  Please choose again.")
        dinner(money)

    elif answer == "2":
      if money > 30:
        money -= 30
        backpack["hunger"] += 1
        print("\nYou chose the family diner for 30 microbucks.")
        print(f"You now have {money} microbucks left.")
        print("You also have " + str(backpack["hunger"]) + " hunger points left.")
      else:
        print(f"\nSorry, it seems you only have {money} microbucks.  Please choose again.")
        dinner(money)

    elif answer == "3":
      if money > 80:
        money -= 80
        backpack["hunger"] += 1
        print("\nYou chose the 5 star restaurant with perks for 80 microbucks.")
        print(f"You now have {money} microbucks left.")
        print("You also have " + str(backpack["hunger"]) + " hunger points left.")
        print("The waiter comes over and gives you something. It's a complimentary robot pet.")
        backpack["perk"] += 1
        robot_name(money)

      else:
        print(f"\nSorry, it seems you only have {money} microbucks.  Please choose again.")
        dinner(money)
    
    elif answer == "4":
      if backpack["hunger"] < 1:
        game_over("You ran out of hunger points.  Soon this will not be game over but start from home.")

      else:
        backpack["hunger"] -= 1
        print("You chose to skip dinner tonight.")
        print("Your hunger level is now " + str(backpack["hunger"]) + ".  Keep in mind if it drops to zero you will faint and all items aqcuired will be lost.")

    else:
      print("Sorry, please choose a valid answer: ")
      dinner(money)



#a theif
def theif(money):
    print("\nYou return to the capsule hotel to pick up your belongings to find they have all been stolen!")
    print("What will you do?")
    print("1) File a complaint to the local authorities")
    print("2) Let it go and go get some food")

    answer = input(">")

    if answer == "1":
      money += 100
      print("\nThe local authorities looked it over and agree to give you a 100 microbucks bonus.")
      print(f"Congratulations you now have {money} microbucks!")
      dinner(money)

    elif answer == "2":
      print("\nYour stuff might be stolen but you still have money, and need something to eat.")
      dinner(money)

    else:
      game_over("YOU TYPED IT WRONGGGGGG!!!")


#work()
def work(money):
    print("\n It's time to go to work to get some more mircrobucks.")
    print(f"You only have {money} microbucks left.")
    print("What would you like to do?")
    print("1) Work for 4 hours for 90 microbucks.")
    print("2) Work for 6 hours for 150 microbucks.")

    answer = input(">")

    if answer == "1":
      money += 90
      print(f"\nYou chose to work for 4 hours and got 90 microbucks. You now have {money} microbucks.")
      theif(money)

    elif answer == "2":
      money += 150
      print(f"\nYou chose to work for 6 hours for 150 mcirobucks. You now have {money} microbucks.")
      theif(money)

    else:
      game_over("That's not an option.  Gosh, and you got so far.")


#hotel_options()
def hotel_options(money):
    print("What will you choose? (1 or 2)")
    print("1) 5 star hotel")
    print("2) Capsule hotel")

    answer = input(">")

    if answer == "1":
      if money > 90:
        money -= 90
        print("\nYou chose the more expensive 5 star hotel.")
        print(f"You now have {money} microbucks left.")
        work(money)
      else:
        print(f"\nSorry, it seems you only have {money} microbucks.  Please choose another option.")
        hotel_options(money)

    elif answer == "2":
      if money > 30:
        money -= 30
        print("\nYou chose the cheeper capsule hotel.  Good choice!")
        print(f"You now have {money} microbucks left.")
        work(money)
      else:
        print(f"\nSorry, it seems you only have {money} microbucks. Please choose another option.")
        hotel_options(money)

    else:
      game_over("You really need to learn your number alphabet.")



#night_stay()
def night_stay(money):
    print("What will you do next? (1 or 2)")
    print("1)  find some place to stay for the night.")
    print("2)  Ask if there is somewhere to stay for free.")

    answer = input(">")

    if answer == "1":
      print(f"There are a couple of options.  Keep in mind you have {money} microbucks left.")
      print("You can buy a premium night stay for 90 microbucks at an exclusive 5 star hotel.")
      print("Or for cheeper, you can stay at the local capsule hotel for 30 microbucks.")
      hotel_options(money)
      
    elif answer == "2":
      print("Sadly, there are no open spots at the library's shelter tonight.  You will have to buy a place to stay.")
      print(f"There are a couple of options.  Keep in mind you have {money} microbucks left.")
      print("You can buy a premium night stay for 90 microbucks at an exclusive 5 star hotel.")
      print("Or for cheeper, you can stay at the local capsule hotel for 30 microbucks.")
      hotel_options(money)

    else:
      game_over("You've been doing it for so long, how hard is it to press one number?")


#money_left()
def money_left(money):
    print(f"\nYou now have {money} microbucks left.")
    print("What would you like to do with it? (1 or 2)")
    print("1) Save the rest up to buy a house later")
    print("2) Buy a hoverboard")

    answer = input(">")

    if answer == "1":
        print("Good idea, this will be a good investment.")
        print(f"You still have {money} microbucks left.")
        night_stay(money)


    elif answer == "2":
        money -= 50
        backpack["hoverboard"] += 1
        print(" You decided to buy the cheapest hoverboard you can find.")
        print("You buy a hoverboard for 50 microbucks.  It says it can hold 2 people.")
        print(f"You have {money} microbucks left.")
        night_stay(money)

    elif answer == "3":
      print("\nYou chose to leave the game. Come back soon.")

    else:
      print("\nPlease choose a valid option:")
      money_left(money_left)


#clothes_shop
def clothes_shop(money):
    print("\nYou enter the clothes shop and are given 2 options.")
    print("You can either buy a blue suit with one pocket and minimal tech for 30 microbucks.")
    print("Or you can buy a purple suit with 4 pockets and a fair amount of tech for 45 microbucks.")
    print("What will you do? (1 or 2)")
    print("1) Blue suit, 30 microbucks")
    print("2) Purple suit, 45 microbucks")

    answer = input(">")

    if answer == "1":
        money -=30
        backpack["clothes"] = "blue"
        print("\nYou chose the blue suit with minimal tech and saved some money.")
        print(f"You now have {money} microbucks.")
        money_left(money)

    elif answer == "2":
        money -= 45
        backpack["clothes"] = "purple"
        print("\nYou chose the purple suit with a fair amount of tech.  Good choice.")
        print(f"You now have {money} microbucks.")
        money_left(money)

    else:
        game_over("\nYou can't buy it if it doesn't exist.")

#Bakery
def bakery(money):
    print("\nYou enter the bakery looking for some food.")
    print("\nThere is a large selection of food.")
    print("\nWhat will you choose? (1 or 2)")
    print("1) Donut and coffee: 5 microbucks")
    print("2) Bagel and hot cocoa 5 microbucks")

    answer = input(">")
    if answer == "1":
        money -= 5
        backpack["hunger"] += 1
        print("\nYou buy a donut and coffee for 5 microbucks.")
        print(f"You now have {money} microbucks.")
        money_left(money)

    elif answer == "2":
        money -= 5
        backpack["hunger"] += 1
        print("\nYou buy the bagel and hot cocao for 5 microbucks.")
        print(f"You now have {money} microbucks.")
        money_left(money)

    else:
        print("\nPlease choose a valid selection:")
        bakery(money)


# pay day
def pay_day(money):
    print("\nYou worked for 8 hours.  The sun is down now. ")
    print("You earned 120 microbucks for a hard day of work.")
    print("You were also given a virtual bank for free which they put on a little handheld device.")
    print("It seems to work like a credit card, and everyone gets one when they get their first job.")
    print("\nWhat will you do next? (1 or 2)")
    print("1) Buy some clothes to fit in")
    print("2) Buy some food to eat")

    answer = input(">")

    if answer == "1":
        print("\nYou need clothes.  You set out for the clothes shop.")
        clothes_shop(money)

    elif answer == "2":
        print("\nYou have to buy some food to eat.  You set out for the local bakery.")
        bakery(money)

    else:
        print("\n Please choose a valid selection: ")
        pay_day(money)


# book store
def book_store(money):
    print("\nYou suddenly see a book store.")
    print("The window shows a display, Hiring Humans, 15 microbucks an hour.")
    print("What will you do? (1 or 2)")
    print("1) Apply for the job")
    print("2) Quit Game")

    answer = input(">")

    if answer == "1":
        print("\n Your application is accepted and you start the job.")
        print("Your job is to program the robots to retrieve the books and interact with customers.")
        pay_day(money)

    elif answer == "2":
        game_over("Goodbye for now, come back soon.")

    else:
        print("\nThat is not a valid selection.  Try again.")
        book_store(money)

#Coffee Shop
def coffee_shop(money):
    print("\n It suddenly occurs to you you don't have any money.")
    print("You see a flyer, human help needed 15 microbucks an hour, no experience necessary.")
    print("What will you do? (1 or 2)")
    print("1) Apply for the job")
    print("2) Explore the future")

    answer = input(">")

    if answer == "1":
        print("\nYour application is accepted and you start the job.")
        print("Your job is to program the robots to make coffee and interact with customers.")
        pay_day(money)

    elif answer == "2":
        print("\nThe city has tall buildings and sleek futuristic technology.")
        print("\nThe city is bustling with people and you notice that everyone is wearing the same kind of clothes.")
        print("You want to fit in, but you don't have money to get clothes.")
        book_store(money)

    else:
        print("\nPlease choose a valid selection.")
        coffee_shop(money)


# function to ask play again or not
def play_again():
  print("\nDo you want to play again? (y or n)")
  
  # convert the player's input to lower_case
  answer = input(">").lower()

  if "y" in answer:
    # if player typed "yes" or "y" start the game from the beginning
    start()
  else:
    # if user types anything besides "yes" or "y", exit() the program
    exit()


# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  print("\n" + reason)
  print("Game Over!")
  # ask player to play again or not by activating play_again() function
  play_again()

#bad google interview
def bad_google(money):
  print("\nYou don't have time to finish getting ready, your interview is starting!")
  print("\nYour interview is with Google, you want to apply for the position of a software engineer.")
  print("Your interviewer thinks you look a little too proffesional for the position.")
  print("They ask you some questions: ")
  print("1) Do you work well in groups?")
  


#google_interview()
def google_interview(money):
  print("\nYou don't have time to finish getting ready, your interview is starting!")
  print("\nYour interview is with Google, you want to apply for the position of a software engineer.")
  print("Your interviewer loves your outfit and thinks you will do well with the Google atmosphere.")
  print("They test your skills and let you start the next day.  Congratulations!")

#present_life()
def present_life(money):
  print("\nYou decide to stay with your friends and family.")
  print("You walk back through the door that got you here, but instead of returning to the dark room you started in, you wake up.")
  print("You realize it was a dream and get ready for the day.")
  print("You have a job interview today.")
  print("You only have 120 dollars in savings and would like to make some more.")
  print("What will you do first?")
  print("1) Put on a suit and tie")
  print("2) Style your hair")
  print("3) Quit game")

  answer = input(">")

  if answer == "1":
    print("\nYou choose to put on a suit and tie.")
    print("Your outfit is professional but not very fun.")
    bad_google(money)

  elif answer == "2":
    print("\nYou chose to put on some socks.")
    print("Your socks are very fun, today you have little computers drinking coffee on them.")
    print("They're so high that you can see them even with your shoes on.")
    print("Your outfit is very fun, but not the most professional.")
    google_interview(money)

  elif answer == "3":
    print("\nYou chose to style your hair.  You brush it out and dye it purple. ")
    print("Super fun, but not the most professional hairstyle.")
    google_interview(money)

  elif answer == "4":
    game_over("\nYou left the game.  Come back soon!")

  else:
    print("\nSorry, please pick a listed option.")
    present_life(money)


# future room
def future_room(money):
  # some prompts
  print("\nYou realize ")
  print("\nYou could stay in the future and build a life for yourself!")
  print("But that would mean leaving your friends and family back home.")
  print("What would you do? (1 or 2)")
  print("1). Go to the future")
  print("2). Stay in the present")

  # take input()
  answer = input(">")
  
  if answer == "1":
    # the player is dead, call game_over() function with the "reason"
    print("\nThe future is really cool.")
    coffee_shop(money)
  elif answer == "2":
    # the player won the game
    print("\nYou decide to stay with your friends and family, and have a nice life.")
    # activate play_again() function
    present_life(money)
  else:
    # call game_over() with "reason"
    game_over("Go and learn how to type a number.")


# cookie room
def cookie_room(money):
  # some prompts
  # '\n' is to print the line in a new line
  print("\nYou enter a room full of cookies!")
  print("Behind the cookies you find a futuristic looking keycard")
  print("You notice a door with a keycard reader")
  print("What would you do? (1 or 2)")
  print("1). Eat all the cookies.")
  print("2). Open the door.")

  # take input()
  answer = input(">")

  if answer == "1":
    # dead()
    game_over("The cookies were poisoned!  You die instantly.")
  elif answer == "2":
    # go to future_room()
    print("\nYou open the door and cool air rushes in, the floor is smooth concrete and a flying car zooms by.")
    future_room(money)
  else:
    # game_over() with "reason"
    game_over("Go and learn how to type a number.")


# bear room
def cake_room(money):
  # give some prompts
  # '\n' is to print the line in a new line
  print("\nThere is an unlimited supply of cake!")
  print("But what's this? Behind the cake you find a futuristic looking keycard.")
  print("You notice a door with keycard reader.")
  print("What would you do? (1 or 2)")
  print("1). Eat all the cake")
  print("2). Open the door")

  # take input()
  answer = input(">")
  
  if answer == "1":
    # the player is dead!
    game_over("The cake was poisoned you died instantly.")
  elif answer == "2":
    # future
    print("\nYou open the door and cool air rushes in, the floor is smooth concrete and a flying car zooms by.")
    future_room(money)
  else:
    # else call game_over() function with the "reason" argument
    game_over("Don't you know how to type a number?")


#START HERE#


def start():
  money = int(120)
  # give some prompts.
  print("\nDisclaimer: Part of this code was based off of a coding tutorial by thecodingpie from thecodingpie.com")
  print("\nYou are standing in a dark room.")
  print("There is a door to your left and right, which one do you take? (l or r)")
  print("You can also type 's' to skip intro or 'quit' to quit the game.")
  
  # convert the player's input() to lower_case
  answer = input(">").lower()

  if "l" in answer:
    # if player typed "left" or "l" lead player to cake room)
    cake_room(money)
  elif "r" in answer:
    # else if player typed "right" or "r" lead him to monster_room()
    cookie_room(money)
  elif "s" in answer:
    future_room(money)
  else:
    # else call game_over() function with the "reason" argument
    game_over("You quit the game or mistyped.  Come back soon.")


# start the game
start()