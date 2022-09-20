#DAY TRIP GENERATOR


reservation_list = ["destination", "restaurant", "transportation", "entertainment\n"]
print(reservation_list)




print()

destination = ["Paris", "Italy", "Germany", "Ireland"]
print(destination)
restaurant = ["Jaques Bistro", "Brunos Olive Garden", "Schnetzels Place", "Leprechauns Pot of Gold"]
print(restaurant)
transportation = ["vehicle rentals", "train", "plane", "cruise liner"]
print(transportation)
entertainment = ["dancing", "theater", "museum","excursion"]
print(entertainment)


print()

print("RANDOM SELECTIONS")

print()
#destitnation_list = ["Paris", "Italy", "Germany", "Ireland"]
import random
destination_list = ["Paris", "Italy", "Germany", "Ireland"]
print(random.choice(destination_list))

print()
#restaurant_list = ["Jaques Bistro", "Brunos Olive Garden", "Schnetzels Place", "Leprechauns GoldPot"]
import random
restaurant_list = ["Jaques Bistro", "Brunos Olive Garden", "Schnetzels Place", "Leprechauns GoldPot"]
print(random.choice(restaurant_list))

print()
#transportation_list = ["vehicle rentals", "train", "plane", "cruise liner"]
import random
transportation_list = ["vehicle rentals", "train", "plane", "cruise liner"]
print(random.choice(transportation_list))

print()
#entertainment = ["dancing", "theater", "museum","excursion"]
import random
entertainment_list = ["dancing", "theater", "museum","excursion"]
print(random.choice(entertainment_list))


print()


#DESTINATION SETUP FOR USER
# # 15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of 
# #transportation, and/or form of entertainment if I don’t like one or more of those things. 
#DESTINATION:
destination_list = ["Paris", "Italy", "Germany", "Ireland"]
print("PLACES To Go: We chose four of our top places you may fine interesting")
for destiny in destination_list:
     print("")     
     print(f" Try {destiny}")
Another_location = input("Enter another place you would like to go?\n")


print()
#RESTAURANT:
restaurant_list = ["Jaques Bistro", "Brunos Olive Garden", "Schnetzels Place", "Leprechauns GoldPot"]
print("FINE DINING: Please try one of our fine dining places.")
for dining in restaurant_list:
     print("")     
     print(f" We have {dining}")
Another_location = input("Otherwise, please enter another place you would like to dine?\n")


print()
#TRANSPORTATION:
transportation = ["vehicle rentals", "train", "plane", "cruise liner"]
print("TRANSPORTING METHODS: We offer four wonderful methods of transportaion.")
for transporting in transportation:
     print("")     
     print(f" {transporting}")
Other_transporting_methods = input("Please enter your choice of transportation.\n")


print()
#ENTERTAINMENT:
entertainment = ["dancing", "theater", "museum","excursion"]
print("ENTERTAINMENT EXCITEMENTS: For your pleasure we have a variety of interesting entertainments")
for amusement in entertainment:
     print("")     
     print(f" {amusement}")
Enjoyment = input("Please select your idea of fun.\n")



print("Just to confirm your selections lets go over your request.")


Paris = input("You have chosen to go to Paris. Enter yes or no.\n")
Restaurant = input("You have chosen to go to Jaques Bistro? Enter yes or no\n")
Transportation = input("You have chosen to take the Cruise liner? Enter yes or no\n")
Entertainment = input("You have chosen to go to the excurions Enter yes or no.\n" )

print("CONGRATULATIONS!!")
print("You are now set to to go on that fabulous Day Trip to Paris; enjoying Jaques Bistro on that nice cruise liner hitting the excursions.\n")


