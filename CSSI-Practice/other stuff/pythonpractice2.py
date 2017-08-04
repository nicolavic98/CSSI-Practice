# from random import randint
#
# def num_game():
#     game_num = randint(0, 100)
#     for i in range(100):
#         user_num = int(raw_input("What is your guess from 0-100?: "))
#         if user_num == game_num:
#             print "Congrats!"
#         elif user_num > game_num:
#             print "Try a lower number!"
#         elif user_num < game_num:
#             print "Try a higher number!"
# num_game()


from random import randint
game_num = randint(0, 100)
user_num = int(raw_input("What is your guess from 0-100?: "))

def num_game2():
    while (game_num != user_num):
        if user_num == game_num:
            print "Congrats!"
        elif user_num > game_num:
            print "Try a lower number!"
        elif user_num < game_num:
            print "Try a higher number!"

num_game2()
