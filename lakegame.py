


print("Welcome to my first game!")

name = input("What is your name? ")
print("Hello", name) 
age = int(input("How old are you? "))
health = 10

if age >= 18:
    print("You are old enough to play")
    consent = input("Do you want to play? (yes/no) ")
    if consent == "yes":
        print("You start the game with 10 points of health")
        first_move = input("Do you want to go left or right? (left/right) ")
        if first_move == "left": 
            print("Nice, you follow the path and reach a lake...")
            second_move = input("Do you swim across or go around? (across/around) ")
            if second_move == "across":
                print("You made it across but got bit by a big fish and you lost 5 points of health")
                health = health - 5
                print("When you walked out of the lake you notice a house and a river")
                third_move = input("Do you go to a house or cross the river? (house/river) ")
                if third_move == "house":
                    print("house")
                else:
                    print("river")
            else:
                print("You had to go through the bushes and got scratched. You lost 1 point of health")
                health = health - 1
        else:
            print("You didn't noticed the cliff and fell down. Your left arm and leg are broken and you can barely see anything. You lost 9 points of health")
            health = health - 9

else:
    print("You are not old enough to play this game")
