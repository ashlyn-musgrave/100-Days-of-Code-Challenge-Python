name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()


if answer == 'left':
    answer = input("You come across an abandonded house, would you like to avoid it or go inside? Enter avoid to avoid the house or inside to go inside: ")

    if answer == 'avoid':
        answer = input("Good call. You keep walking but are getting thirsty. It looks like there is a river ahead but there is a family of tigers drinking out of it. If you want to go the river, enter river. If you want to keep walking, enter walking: ")

        if answer == 'river':
            answer = input("The tigers took a liking to you and want to bring you back to their den. If you want to go with the tigers, enter proceed. If you want to decline the tigers offer, enter decline: ")

            if answer == 'proceed':
                answer = input("While walking with the tigers, you stumble and fall off into a pit. The tigers don't see a point in saving you so they leave. A gypse woman comes along and will help you out only if you give her a lock of your hair in return. Enter yes or no: ")

                if answer == 'Yes':
                    print("The gypse woman used your hair to cast a paralysis spell on you. The tigers came back and ate you. Game over.")

                elif answer == 'No':
                    print("Good call. An unexpected tornado from the east blew the tail end of a rope into your pit and you were able to crawl out. Upon crawling out, you see a distant campfire. If you want to explore the campfire, enter explore. If you want to keep walking, enter walk: ")

                else:
                    print('Not a valid option. You lose.')

                    if answer == 'explore':
                        print("The campfire was a decoy for cannables to lure people to their camp. Sorry, but you were eaten. Game over.")
                                               
                    elif answer == 'walk':
                        print("You walked into a jungle where a pack of angry gorillas mistook you for their derranged brother and killed you. Game over.")

                    else:
                        print('Not a valid option. You lose.')                  
                            
            elif answer == 'decline':
                answer = input("The tigers didn't appreciate your disrespect, they pushed you into the river where the killer croc lurks. You're struggling to keep your head above the rushing water and see what looks like a log ahead. If you want to swim towards the log, enter log. If you want to keep struggling, enter struggle: ")

                if answer == 'log':
                    print("The log turned out to be killer croc! You tried to reason with him, but he ate you! Game over.")
                               
                elif answer == 'struggle':
                    print("A merman came from underneath you and swam you to safety. You made such an impression on him that he invited you to be king of Atlantis. Congratualions, you won!")

                else:
                    print('Not a valid option. You lose.')

            else:
                print('Not a valid option. You lose.')

        elif answer == 'walking':
            answer = input("Avoiding the river caused you to pass out from dehydration. While passed out, you had a dream that your wife ate all your snacks. It motivated you to keep going so that you could eat all of her snacks. If you're petty like that, enter petty. If not, type onward: ")

            if answer == 'petty':
                print("You found out that your wife wasn't the one who ate your snacks, but becasue you accused her, she ate your snacks any way. You lose.")

            elif answer == 'onward':
                answer = input("You came across a bridge that required you to either answer a question correctly or pay the troll toll. If you want to answer the question, enter question. If you would like to pay the toll, enter toll: ")

            else:
                print('Not a valid option. You lose.')
                
                if answer == 'question':
                    answer = input("The troll asks you where the Marvel Movie franchise went wrong. If you think it's becasue the movies are too righteous, enter righteous. If you think the movies are too kiddish, enter kiddish: ")

                    if answer == 'righteous':
                        print("The troll completely agreed and granted you passage. Batman came out of nowhere, congratualated you on your answer, and asked if you wanted to be his partner in serving justice. You humbly agree. Game over.")

                    elif answer == 'kiddish':
                        print("The troll completely agreed, but Iron Man swooped out of nowhere and dropped you in the ocean to drown because he can't take an ego hit. Game over.")

                    else:
                        print('Not a valid option. You lose.')
                            
                elif answer == 'toll':
                    print("The toll was your heart. Game over.")

                else:
                    print('Not a valid option. You lose.')

        else:
            print('Not a valid option. You lose.')

    elif answer == 'inside':
        answer = input("Your closest friends were cooking hamburger helper and it was almost ready. But all of the sudden, the kool aid guy jumps through the wall and demands to eat all of the hamburger helper. If you want to fight the kool aid guy, enter fight. If you want to let him take the hamburger helper, enter take: ")

        if answer == 'fight':
            print("You stood up to kool aid guy and he backed down immediately, saying he struggles with making new friends. You invite him to join you and your friends and proceed to watch 13 Going on 30.")

        elif answer == 'take':
            print("You never let anyone take your hamburger helper. Game over.")
            
        else:
            print('Not a valid option. You lose.')

    else:
        print('Not a valid option. You lose.')

elif answer == 'right':

    print("As soon as you turned right, a mysterious car pulled up, someone jumped out and pushed you inside. 30 minutes later, they let you out of the car and let you pick any cat your wanted at the pet shop. Life is good. Game over.")

else:
    print('Not a valid option. You lose.')

