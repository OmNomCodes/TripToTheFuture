backpack = {
  "clothes": "",
  "phone": 0,
  "perk": 0,
  "robotname": "",
  "hoverboard": 0,
  "pet_points": 0, 
  "hunger": 3,
  "debt": 0,
  "present": 0,
  "future": 0
}

petPack = {
  "bed": 0,
  "toy": 0,
  "pet_food": 0
}

#Check if something exists in the bacpack:
#if "a" in dict_1:
#    print("Exists")
#else:
#    print("Does not exist")

#How to change all the values of a dictionary to the same number:
#   petPack = dict.fromkeys(petPack, 0)

 #How to add things to the backpacks:
    #thisdict["color"] = "red"
 #How to add things to the list:
    #backpack["pet_stuff"].extend(["bed, toy"])
 #How to change a number
    #backpack["debt"] += 200
# To tell a function do nothing write -->  pass (no parenthises)
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

def next():
  print("NEXT")

#PET POINT REDEMPTION
def petPrize():
  if backpack["pet_points"] >= 5:
    print("\nYou have " + str(backpack["pet_points"]) + " pet points now!  That's enough to choose a prize. What do you want to get?")
    print("1: New toy (5 pet points)")
    print("2: 1 bag of pet food (7 pet points)")
    print("3: New collar (5 pet points)")
    print("4: \"Grooming\" -> which is actually circuit maintenance (10 pet points)")
    print("5: I'll save my petpoints for later")
    answer = input(">")
    
    if answer == "1":
      backpack["pet_points"] -= 5
      petPack["toy"] += 1
      print("\nYou chose a toy!  A great item to keep your pet entertained.")
      print("You now have " + str(backpack["pet_points"]) + " pet points.")
      next()
    elif answer == "2":
      if backpack["pet_points"] >= 7:
        backpack["pet_points"] -= 7
        petPack["pet_food"] += 1
        print("\nYou chose to buy the pet food for 7 pet points!  You now have " + str(backpack["pet_points"]) + " pet points and " + str(petPack["pet_food"]) + " bags of pet food.")
        print("Remember: even though your pet is a robot, if you do not feed it regularly it may start to malfunction and that could turn into a very costly visit to the vet.")
        next()
      else:
        print("\nSorry, you don't have enough pet points for this option.  Please choose another option:")
        petPrize()
    elif answer == "3":
      backpack["pet_points"] -= 5
      if "collar" in petPack:
        petPack["collar"] += 1
        print("collar")
      else:
        petPack["collar"] = 1
        print("no collar")

      print("\nGood choice!  Your pet will look great with a collar.  You now have " + str(backpack["pet_points"]) + " pet points." )
      next()
    elif answer == "4":
      if backpack["pet_points"] >= 10:
        backpack["pet_points"] -= 10
        print("\nGreat choice!  Grooming your pet will keep it healthy and working properly. " + backpack["robotname"] + " is now sparkling clean.  Its carbon fiber body has never looked better!")
        next()
      else:
        print("\nSorry, you don't have enough pet points for this option.  Please choose another option:")
        petPrize()
    elif answer == "5":
      print("\nGood choice.  Saving up your pet points for later can allow you to buy " + backpack["robotname"] + " nothing but the best!")
      next()
    else:
      print("\nSorry, please choose a valid option: ")
      petPrize()
  else:
    pass
#FAST FOOD
def Fastfood(money):
  if money >= 10:
    money -= 10
    backpack["hunger"] += 0.5
    print(f"\nYou chose to get food for 10 microbucks.  You now have {money} microbucks left!")
    print("You also have "+str(backpack["hunger"])+" hunger points.  Fast food is unhealthy so it only counts for 0.5 hunger points.")
  else:
    print("\nSorry, you don't have enough money. Please choose another option.")
    dinner(money)

def FamilyRestaurant(money):
  if money >= 30:
    money -= 30
    backpack["hunger"] += 1
    print("\nYou decided to go to the family restaurant for 30 dollars.  What would you like to get?")
    print("1: Fish and Chips (of course)")
    print("2: Waffles and Bacon because breakfast for dinner is cool")
    print("3: pierogies with sauerkraut because the polish do it right")
    print("4: Quit game")
    answer = input(">")

    if answer == "1":
      print("\nYou ate some delicious fish and chips and now have "+str(backpack["hunger"])+" hunger points.")
    elif answer == "2":
      print("\nNothing is better than breakfast, even at dinner time!  You now have "+str(backpack["hunger"])+" hunger points.")
    elif answer == "3":
      print("\nPierogies with sauerkraut might be the hardest thing on the menu to spell, but it sure is the best tasting!  You now have "+str(backpack["hunger"])+" hunger points.")
    elif answer == "4":
      game_over("")
    else:
      print("Sorry, please choose a valid option: ")
      FamilyRestaurant(money)

  else:
    print("\nSorry, you don't have enough money for this option.  Please choose another one.")
    dinner(money)

def Dogpark(money):
  backpack["pet_points"] += 1
  print("\nYou decided to go to the dog park with "+backpack["robotname"]+"!")
  print("A cute robot cat named Tuna played with "+backpack["robotname"]+".  When robotic animals were first attempted the dynamic between cats and dogs was maintained, but after a while people started asking for robotic animals that had the same traits as real animals but could remain peaceful together.")
  print("You now have " + str(backpack["pet_points"]) + " pet points.")
  petPrize()
  next()


def Pool(money):
  backpack["pet_points"] += 1
  print("\nYou decided to bring "+backpack["robotname"]+" to the pool.")
  print("Luckily robotic animals from the future happen to be waterproof.")
  print("After watching " + backpack["robotname"] + " swim for a while and cooling off in the water yourself, you realize it's already time for lunch!")
  print("Luckily, there are some food trucks nearby. ") #next(do foodtruck stuff selection and then lead into other functions for each)
  next()

#Breakfast
def Breakfast(money):
  print("\nTime for breakfast!  What will you get?")
  print("1: Jook, a common Asian breakfast food made from rice and water, topped with bacon, chicken, or other meats and sometimes eggs. (10 microbucks)")
  print("2: Pancakes with bacon and syrup. Served with a side of hashbrowns and coffee. (15 microbucks)")
  print("3: Chicken Lemon Rice Soup with toast and a salad. (10 microbucks)")
  print("4: Skip purchase")
  print("5: Quit Game (All progress will be lost)")
  next()
  

#coffee shop
def Coffee(money):
  print("\nYou chose to go to Asteroidbucks!  It seems to be a variation of Starbucks from the future.")
  print(f"What would you like to buy?  Keep in mind you have {money} microbucks.")
  print("1: Coffee, black. (5 microbucks)")
  print("2: Hot chocolate with whipped cream (6 microbucks)")
  print("3: Bagel sandwich and hot chocolate (15 microbucks)")
  print("4: Skip purchase")
  print("5: Quit Game (all progress will be lost)")
  next()

#shopping
def Shop(money):
  print("You chose to go shopping. Please choose what you want to buy:")
  print("1: Stuffed animal (10 microbucks)")
  next()



def saturday(money):
  if backpack["perk"] >= 1:
    print("\nIt is now Saturday, hooray!  You have today off of work.  Why don't you take "+backpack["robotname"]+" out today.  Where will you take it?")
    print("\n1: The dog park")
    print("2: The pool")
    print("3: Go to Asteroidbucks without your dog")
    print("4: Quit Game (All Progress Will Be Lost)")
    answer = input(">")

    if answer == "1":
      Dogpark(money)
    elif answer == "2":
      Pool(money)
    elif answer == "3":
      Coffee(money)
    elif answer == "4":
      game_over("")
    else:
      print("Please choose a valid option:")
      saturday(money)
  else: 
    print("\nIt's now Saturday and you get the day off from your job!")
    print("What would you like to do with your free day?")
    print("\n1: Grab a bite for breakfast")
    print("2: Go shopping and get something for yourself.")
    print("3: Rent a movie")
    print("4: Quit Game (all progress will be lost)")
    answer1 = input(">")

    if answer1 == "1":
      Breakfast(money)
    elif answer1 == "2":
      Shop(money)
    #elif answer1 == "3":
      #Movie(money)
    elif answer1 == "4": 
      game_over("")
    else:
      print("Sorry, please pick a valid option: ")
      saturday(money)


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
        petPack["bed"] += 1
        print("\nYou chose the pet bed for 15 microbucks.")
        print("\nBy buying your pet a bed, you earned one pet point.  You can get more pet points by doing different things for your pet.")
        print("These points once saved up can be used to redeem certain things for your pet.")
        print("You now have " + str(backpack["pet_points"]) + f" pet points and {money} microbucks.")
        saturday(money)

      else: 
        print("\nYou don't have enough microbucks.  Please choose another option.")
        pet_care(money)

    elif answer == "2":
      if money >= 5:
        money -=5
        petPack["toy"] += 1
        print("\nYou chose the dog toy for 5 microbucks. Good choice!")
        print(f"You now have {money} microbucks left.")
        saturday(money)
      else:
        print(f"\nYou only have {money} microbucks.  Please choose another option.")
        pet_care(money)

    elif answer == "3":
      if money >= 20:
        money -=20
        backpack["pet_points"] += 2
        petPack["toy"] += 1
        petPack["bed"] += 1
        print("\nYou chose to buy the pet bed and the toy, good choice!")
        print("This gives you 2 pet points, once you get more pet points you can redeem them for different things!")
        print("You now have " + str(backpack["pet_points"]) + f" pet points and {money} microbucks.")
        saturday(money)

      else:
        print(f"Sorry, you only have {money} microbucks.  Please choose another option.")
        pet_care(money)

    elif answer == "4":
      print("\nYou chose to skip buying anything for your pet.")
      print("In the future, you might consider buying your pet items as it gives you pet points which can later be redeemed to buy special items for your pet.")
      saturday(money)

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
    print("5) Quit Game")

    answer = input(">")

    if answer == "1":
      if money > 10:
        money -= 10
        backpack["hunger"] += 1
        print("\nYou chose the fast food for 10 microbucks.")
        print(f"You now have {money} microbucks left.")
        print("You also have " + str(backpack["hunger"]) + " hunger points left.")
        Fastfood(money)
        
      else:
        print(f"\nSorry, it seems you only have {money} microbucks.  Please choose again.")
        dinner(money)

    elif answer == "2":
      if money > 30:
        money -= 30
        backpack["hunger"] += 1
        print("\nYou chose the family diner for 30 microbucks.")
        print(f"You now have {money} microbucks left.")
        print("You also have " + str(backpack["hunger"]) + " hunger points.")
        FamilyRestaurant(money)
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
      if backpack["hunger"] <= 1:

        print("\nSorry, you need to eat. You don't have enough hunger points to skip it.  If you don't have enough money you can take out a small loan.")
        print("\n1) Take out a loan")
        print("\n2) Choose a different option")
        print("\n3) Quit Game")

        answer = input(">")
      
        if answer == "1":
          print("\nYou chose to take out a small loan of 100 dollars.  Keep in mind that you must repay the loan before you buy something else.")
          small_debt(money)
        elif answer == "2":
          dinner(money)
        elif answer == "3":
          game_over("\nYou chose to leave the game.  Come back soon!")

        else:
          print("Please choose a valid option: ")
          dinner(money)

      else:
        if backpack["hunger"] >= 2:
          backpack["hunger"] -= 1
          print("You chose to skip dinner tonight.")
          print("Your hunger level is now " + str(backpack["hunger"]) + ".  Keep in mind if it drops to zero you will faint and all items aqcuired will be lost.")
        else:
          print("\nSorry, you need to eat. You don't have enough hunger points to skip it.  If you don't have enough money you can take out a small loan.")
          print("\n1) Take out a loan")
          print("\n2) Choose a different option")
          print("\n3) Quit Game")

          answer = input(">")
      
          if answer == "1":
            print("\nYou chose to take out a small loan of 100 dollars.  Keep in mind that you must repay the loan before you buy something else.")
            small_debt(money)
          elif answer == "2":
            dinner(money)
          elif answer == "3":
            game_over("\nYou chose to leave the game.  Come back soon!")

          else:
            print("Please choose a valid option: ")
            dinner(money)

        
    elif answer == "5":
      game_over("\nYou chose to quit the game.  See you soon!")

    else:
      print("Sorry, please choose a valid answer: ")
      dinner(money)



#a theif
def theif(money):
    print("\nYou return to the capsule hotel to pick up your belongings to find they have all been stolen!")
    print("What will you do?")
    print("1) File a complaint to the local authorities")
    print("2) Let it go and go get some food")
    print("3) Quit Game")

    answer = input(">")

    if answer == "1":
      money += 100
      print("\nThe local authorities looked it over and agree to give you a 100 microbucks bonus.")
      print(f"Congratulations you now have {money} microbucks!")
      dinner(money)

    elif answer == "2":
      print("\nYour stuff might be stolen but you still have money, and need something to eat.")
      dinner(money)

    elif answer == "3":
      game_over("\nYou chose to leave the game.  Come back soon!")

    else:
      print("\nPlease Choose a Valid Selection:")
      theif(money)

#work()
def work(money):
    print("\n It's time to go to work to get some more mircrobucks.")
    print(f"You only have {money} microbucks left.")
    print("What would you like to do?")
    print("1) Work for 4 hours for 90 microbucks.")
    print("2) Work for 6 hours for 150 microbucks.")
    print("3) Leave the Game")

    answer = input(">")

    if answer == "1":
      money += 90
      print(f"\nYou chose to work for 4 hours and got 90 microbucks. You now have {money} microbucks.")
      theif(money)

    elif answer == "2":
      money += 150
      print(f"\nYou chose to work for 6 hours for 150 mcirobucks. You now have {money} microbucks.")
      theif(money)

    elif answer == "3":
      game_over("\nYou chose to leave the game.  Come back soon!")

    else:
      print("\nPlease pick a valid option:")
      work(money)


#hotel_options()
def hotel_options(money):
    print("What will you choose? (1 or 2)")
    print("1) 5 star hotel")
    print("2) Capsule hotel")
    print("3) Quit Game")

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

    elif answer == "3":
      game_over("\nYou chose to leave the game.  Come back soon!")

    else:
      print("\nYou really need to learn your number alphabet. Please choose a valid selection:")
      hotel_options(money)



#night_stay()
def night_stay(money):
    print("What will you do next? (1 or 2)")
    print("1)  find some place to stay for the night.")
    print("2)  Ask if there is somewhere to stay for free.")
    print("3)  Quit Game")

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

    elif answer == "3":
      game_over("Come back soon friend!")

    else:
      print("\nThat is not a valid selction.  Choose A VALID SelEcTIon!")
      night_stay(money)


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
    print("3) Quit Game")

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

    elif answer == "3":
      game_over("Game over.  Come back soon.")

    else:
        print("\nYou can't buy it if it doesn't exist. Choose another option:")
        clothes_shop(money)

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

#def after_debt(money):
  #print("Here is a test to see if this actually works.  Hoiya.  ")

#LOAN#
def small_debt(money):
  if backpack["debt"] == 0:
    backpack["debt"] += 100
    print("\nYou decided to take out a small loan of 100 dollars.  Don't forget to pay it back before you buy anything else!")
  else:
    print("Sorry, it seems you have a current loan out. You will have to repay that on first.")

#FAINT#
def faint(money):
  money == 0
  backpack["phone"] == 0
  petPack = dict.fromkeys(petPack, 0)
  backpack["hunger"] == 3
  print("\nYou fainted and lost all your stuff!")
  print("\n(some of these may include your phone, money, and pet items.")
  print(f"You now have {money} microbucks and no phone or pet items (if aquired)")
  print("You now have "+str(backpack["hunger"])+" hunger points.")

#WORK#
def workday(money):
  money += 40
  print("\nIt's time for work.  You go to Google and have a successful day. You get a free dinner there and leave to go home.")
  print(f"\nYou now have {money} dollars.")

  


def dinner_present(money):
  print("Whether you passed or not, you have to eat!  It's time to get some food.  Where would you like to eat?")
  print(f"Keep in mind you have {money} dollars and " + str(backpack["hunger"]) + " hunger points.")
  print("\n1) Get groceries from Whole Foods for 15 dollars")
  print("\n2) Go to a chain restaurant for 30 dollars")
  print("\n3) Go to a fancy restaurant for 50 dollars (includes free gift)")
  print("\n4) Skip Dinner (-2 hunger points)")
  print("\n5) Quit Game")

  answer = input(">")

  if answer == "1":
    if money >= 15:
      money -= 15
      backpack["hunger"] += 1
      print("You chose to get a meal from Whole Foods.")
      print(f"\nYou now have {money} dollars left and " + str(backpack["hunger"]) + " hunger points.")
      workday(money)
      
    else:
      print("\nSorry, you don't have enough money for this option.  Please choose another.")
      dinner_present(money)

  elif answer == "2":
    if money >= 30:
      money -= 30
      backpack["hunger"] += 2
      print("\n You chose to eat out at a chain restaurant.  You are glad you didn't waste your time shopping.")
      print(f"\nYou now have {money} dollars and " + str(backpack["hunger"]) + " hunger points.")
      workday(money)

    else:
      print("\nSorry, you don't have enough money for this option.  Please choose another.")
      dinner_present(money)

  elif answer == "3":
    if money >= 50:
      money -= 50
      backpack["hunger"] += 2
      backpack["perk"] += 1
      print("\n You chose to eat out at a fancy restaurant for $50 with an free gift.")
      print(f"\nYou now have {money} dollars left and " + str(backpack["hunger"]) + " hunger points.")
      print("\nYour gift was a raffle ticket where the prizes are different things.  ")
      print("\nYou enter in your ticket and win a computer! This will be great for your new job at Google.")
      workday(money)

    else:
      print("\nSorry, you don't have enough money for this option.  Please choose another.")
      dinner_present(money)

  elif answer == "4":
    if backpack["hunger"] > 2:
      backpack["hunger"] -= 1
      print("\nYou chose to skip dinner.  You now have " + str(backpack["hunger"]) + " hunger points left.")
      workday(money)

    else:
      print("\nSorry, you need to eat. You don't have enough hunger points to skip it.  If you don't have enough money you can take out a small loan.")
      print("\n1) Take out a loan")
      print("\n2) Choose a different option")
      print("\n3) Quit Game")
      answer = input(">")
      if answer == "1":
        if backpack["debt"] <= 0:
          print("\nYou chose to take out a small loan of 100 dollars.  Keep in mind that you must repay the loan before you buy something else.")
          small_debt(money)

        else:
          print("\nSorry, you already have an outstanding loan. Please pay off the loan or skip dinner anyway.")
          print("\n1) Pay off loan")
          print("\n2) Skip dinner anyway")
          print("\n3) Quit Game")
          answer = input(">")
          if answer == "1":
            if money >= backpack["debt"]:
              money -= backpack["debt"]
              backpack["debt"] = 0
              print(f"\nYou paid off your loan and now have {money} dollars left.")

            elif answer == "2":
              faint(money)

            elif answer == "3":
              game_over("You decided to leave the game.  Please come back soon!")

            else:
              print("\n Please choose a valid answer")
              dinner_present(money)  

          elif answer == "2":
            faint(money)

          elif answer == "3":
            game_over("You chose to leave the game.  Come back soon!")

          else:
            print("\nPlease choose a valid option.")
            dinner_present(money)

  elif answer == "5":
    game_over("\nYou chose to leave the game.  Come back soon!")

  else:
    print("\nSorry, please choose a valid option: ")
    dinner_present(money)

#bad google interview
def bad_google(money):
  print("\nYou don't have time to finish getting ready, your interview is starting!")
  print("\nYour interview is with Google, you want to apply for the position of a software engineer.")
  print("Your interviewer thinks you look a little too proffesional for the position.")
  print("They ask you one important question: ")
  print("What is your favourite colour?")
  print("1) A warm colour")
  print("2) A cool colour")
  print("3) Quit Game")

  answer = input(">")
  
  if answer == "1":
    print("\nCongratulations you passed the test! (You would have passed it no matter what, but that doesn't matter).  You are set to start tomorrow.")
    dinner_present(money)

  elif answer == "2":
    print("\nCongratulations you passed the test! (You would have passed it no matter what, but that doesn't matter).  You are set to start tomorrow.")
    dinner_present(money)

  elif answer == "3":
    game_over("\nYou chose to leave the game.  Come back soon!")

  else:
    print("\nSorry, please choose a valid selection.")
    bad_google(money)

#google_interview()
def google_interview(money):
  print("\nYou don't have time to finish getting ready, your interview is starting!")
  print("\nYour interview is with Google, you want to apply for the position of a software engineer.")
  print("Your interviewer loves your outfit and thinks you will do well with the Google atmosphere.")
  print("They test your skills and let you start the next day.  Congratulations!")
  dinner_present(money)

#present_life()
def present_life(money):
  print("\nYou decide to stay with your friends and family.")
  print("You walk back through the door that got you here, but instead of returning to the dark room you started in, you wake up.")
  print("You realize it was a dream and get ready for the day.")
  print("You have a job interview today.")
  print("You only have 120 dollars in savings and would like to make some more.")
  print("What will you do first?")
  print("1) Put on a suit and tie")
  print("2) Put on Some Socks")
  print("3) Style Your Hair")
  print("4) Quit Game")

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
  print("3). Quit Game")

  # take input()
  answer = input(">")
  
  if answer == "1":
    backpack["future"] += 1
    print("\nThe future is really cool.")
    coffee_shop(money)

  elif answer == "2":
    backpack["present"] += 1
    print("\nYou decide to stay with your friends and family, and have a nice life.")
    present_life(money)

  elif answer == "3":
    game_over("\nYou chose to leave the game.  Come back soon friend!")

  else:
    print("\nPlease choose a valid selection:")
    future_room(money)


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
  print("3). Quit Game")

  # take input()
  answer = input(">")

  if answer == "1":
    # dead()
    game_over("The cookies were poisoned!  You die instantly.")
  elif answer == "2":
    # go to future_room()
    print("\nYou open the door and cool air rushes in, the floor is smooth concrete and a flying car zooms by.")
    future_room(money)
  elif answer == "3":
    game_over("\nYou chose to leave the game come back soon!")
  else:
    # game_over() with "reason"
    print("\nPlease choose a valid answer.")
    cookie_room(money)


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
  print("3). Leave Game")

  # take input()
  answer = input(">")
  
  if answer == "1":
    # the player is dead!
    game_over("The cake was poisoned you died instantly.")
  elif answer == "2":
    # future
    print("\nYou open the door and cool air rushes in, the floor is smooth concrete and a flying car zooms by.")
    future_room(money)
  elif answer == "3":
    game_over("You chose to leave the game. Come back soon!")
  else:
    # else call game_over() function with the "reason" argument
    print("\nPlease choose a REAL selection this time:")
    cake_room(money)


#START HERE#


def start():
  #STARTING MONEY 120
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
  elif "q" in answer:
    game_over("You chose to leave the game.  See you soon!")
  else:
    # else call game_over() function with the "reason" argument
    print("\nPlease choose a valid selection:")
    start()


# start the game
start()

# Look for anything with the function next() to start working on