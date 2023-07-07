name = input("What is your name: ")
print("Welcome", name, "let's start the game")

answer = input(
    "You are on a dirt road, it has come to an end. Which way would you like to go? (right or left?)").lower()


if answer == "left":
    answer = input(
        "You come to a river. do you want to walk or swim accross? (swim / walk) "
    )
    if answer == "swim":
        print("Aaaaah...there is an alligator!!! You've been eaten!You lose.")
    elif answer == "walk":
        print("You walked for many miles. Now you are exhausted. Almost died. You lose.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input(
        "You come to a bridge, do you want to cross it or go back? (cross/back) "
        )
    if answer == "back":
        print("You go back and lose. Sad...")
    elif answer == "cross":
        answer = input("You've crossed the bridge and meet a stranger. Greet them? (yes/no) ")

        if answer == "yes":
            print("You talk to the stranger and they give you gold coin. Congratulation! You win!")
        elif answer == "no":
            print("You ignore the stranger and they are offended. You lose.")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")
