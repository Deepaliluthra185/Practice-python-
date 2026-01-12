def guess_the_number():
    high=100
    low=1
    attempts=0
    print("Hey ! , Guess a number between 1-100")
    while True:
        guess = (high+low )//2
        attempts += 1
        print("my guess is :", guess)
        feedback=input("choose : high,low,right")

        if feedback=="right":
            print("I guessed it")
            print("number of attempts :",attempts)
            break
        elif feedback =="high":
            high=guess-1
        elif feedback=="low":
            low=guess+1
        else:
            print("invalid operator")     

guess_the_number()


    