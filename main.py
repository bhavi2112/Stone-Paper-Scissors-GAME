import time
i = 0
computer_score = 0
your_score = 0
draw = 0
print("Welcome to the game which is known by every one !!STONE PAPER SCISSORS!!")
time.sleep(1)
class hi():
    print("Hi")
hi()
while (1):
    i = i + 1
    if 6 == i:
        break


    def swg():
        """
        Whole game of snake water gun
        """
        import random
        options_computer_have = ["stone", "paper", "scissors"]
        a = random.choice(options_computer_have)

        options_you_have = str.lower(input())
        if a == "stone" and options_you_have == "scissors":
            def cs_yw():
                """
                when computer takes snake and I take water than computer win
                :return:
                """
                print("I choose", a)
                time.sleep(0.5)
                print("1 point to me")
                time.sleep(0.5)
                global computer_score
                global your_score
                global draw
                computer_score = computer_score + 1
                print("My total", computer_score)
                time.sleep(0.5)
                print("Your total", your_score)
                time.sleep(0.5)
                print("Draw", draw)
                time.sleep(0.5)

            cs_yw()
        elif a == "stone" and options_you_have == "paper":
            def cs_yg():
                """
                when computer takes snake and I take gun than I win
                :return:
                """
                print("I choose", a)
                time.sleep(0.5)
                print("1 point to you")
                time.sleep(0.5)
                global computer_score
                global your_score
                global draw
                your_score = your_score + 1
                print("My total", computer_score)
                time.sleep(0.5)
                print("Your total", your_score)
                time.sleep(0.5)
                print("Draw", draw)
                time.sleep(0.5)

            cs_yg()
        elif a == "stone" and options_you_have == "stone":
            def cs_ys():
                """
                when computer takes snake and I take snake than draw
                :return:
                """
                print("I choose", a)
                time.sleep(0.5)
                print("Its a draw")
                time.sleep(0.5)
                global draw
                draw = draw + 1
                print("My total", computer_score)
                time.sleep(0.5)
                print("Your total", your_score)
                time.sleep(0.5)
                print("Draw", draw)
                time.sleep(0.5)

            cs_ys()
        elif a == "paper" and options_you_have == "scissors":
            def cw_ys():
                """
                when computer take water and I take snake than I win
                :return:
                """
                print("I choose", a)
                time.sleep(0.5)
                print("1 point to you")
                time.sleep(0.5)
                global computer_score
                global your_score
                global draw
                your_score = your_score + 1
                print("My total", computer_score)
                time.sleep(0.5)
                print("Your total", your_score)
                time.sleep(0.5)
                print("Draw", draw)
                time.sleep(0.5)

            cw_ys()
        elif a == "paper" and options_you_have == "stone":
            def cw_yg():
                """
                when computer takes water and I take gun than computer win
                :return:
                """
                print("I choose", a)
                time.sleep(0.5)
                print("1 point to me")
                time.sleep(0.5)
                global computer_score
                global your_score
                global draw
                computer_score = computer_score + 1
                print("My total", computer_score)
                time.sleep(0.5)
                print("Your total", your_score)
                time.sleep(0.5)
                print("Draw", draw)
                time.sleep(0.5)

            cw_yg()
        elif a == "paper" and options_you_have == "paper":
            def cw_yw():
                """
                when computer takes water and I take water than draw
                :return:
                """
                print("I choose", a)
                time.sleep(0.5)
                print("Its a draw")
                time.sleep(0.5)
                global draw
                draw = draw + 1
                print("My total", computer_score)
                time.sleep(0.5)
                print("Your total", your_score)
                time.sleep(0.5)
                print("Draw", draw)
                time.sleep(0.5)

            cw_yw()
        elif a == "scissors" and options_you_have == "paper":
            def cg_ys():
                """
                when computer takes gun and I take snake than computer win
                :return:
                """
                print("I choose", a)
                time.sleep(0.5)
                print("1 point to me")
                time.sleep(0.5)
                global computer_score
                global your_score
                global draw
                computer_score = computer_score + 1
                print("My total", computer_score)
                time.sleep(0.5)
                print("Your total", your_score)
                time.sleep(0.5)
                print("Draw", draw)
                time.sleep(0.5)

            cg_ys()
        elif a == "scissors" and options_you_have == "stone":
            def cg_yw():
                """
                when computer takes gun and I take water than I win
                :return:
                """
                print("I choose", a)
                time.sleep(0.5)
                print("1 point to you")
                time.sleep(0.5)
                global computer_score
                global your_score
                global draw
                your_score = your_score + 1
                print("My total", computer_score)
                time.sleep(0.5)
                print("Your total", your_score)
                time.sleep(0.5)
                print("Draw", draw)
                time.sleep(0.5)

            cg_yw()
        elif a == "scissors" and options_you_have == "scissors":
            def cg_yg():
                """
                If computer takes gun and I take gun than draw
                :return:
                """
                print("I choose", a)
                time.sleep(0.5)
                print("Its a draw")
                time.sleep(0.5)
                global draw
                draw = draw + 1
                print("My total", computer_score)
                time.sleep(0.5)
                print("Your total", your_score)
                time.sleep(0.5)
                print("Draw", draw)
                time.sleep(0.5)

            cg_yg()
        else:
            print("Please enter a valid option(stone, paper, scissors)")


    print("(", i, ")", "Choose one the following:\nstone\npaper\nscissors")
    swg()
if computer_score > your_score:
    print("-----------------------------")
    print("*****************************")
    time.sleep(0.5)
    print("RESULT'S ARE:")
    time.sleep(0.5)
    print("Your total:", your_score)
    time.sleep(0.5)
    print("My total:", computer_score)
    time.sleep(0.5)
    print("Draw:", draw)
    time.sleep(0.5)
    print("My score is more than you")
    print("I win  😜  👍  😎  🥳  ")
    print("*****************************")
    print("-----------------------------")
    print("*this game is developed by bhavyang bhatt*")
elif computer_score == your_score:
    print("-----------------------------")
    print("*****************************")
    time.sleep(0.5)
    print("RESULT'S ARE:")
    time.sleep(0.5)
    print("Your total:", your_score)
    time.sleep(0.5)
    print("My total:", computer_score)
    time.sleep(0.5)
    print("Draw:", draw)
    time.sleep(0.5)
    print("Both score are equal")
    print("Its a tie")
    print("*****************************")
    print("-----------------------------")
    print("*this game is developed by bhavyang bhatt*")
else:
    print("-----------------------------")
    print("*****************************")
    print("RESULT'S ARE:")
    time.sleep(0.5)
    print("Your total:", your_score)
    time.sleep(0.5)
    print("My total:", computer_score)
    time.sleep(0.5)
    print("Draw:", draw)
    time.sleep(0.5)
    print("Your score is more than me")
    print("you win  😜  👍  😎  🥳  ")
    print("*****************************")
    print("-----------------------------")
    print("*this game is developed by bhavyang bhatt*")

