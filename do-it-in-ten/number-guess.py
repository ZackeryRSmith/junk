while True:
    rnum = __import__("random").randint(1, nmax := int(input("Whats the range 0-?: ")))
    if not input(f"1-{nmax}? [Y, n] ").lower() == "n": break
while True:
    nofguess = int(input("Number of guesses: "))
    if not input(f"{nofguess} guesses? [Y, n] ").lower() == "n": break
while True:
    if nofguess == 0: print(f"You have run out of guess' :(\nCorrect number: {rnum}")
    elif int(input(": ")) == rnum: (print(f"Correct! (with {nofguess} guesses to spare)"), quit())
    else: [print(f"Incorrect! ({nofguess} more guesses left)"), nofguess := nofguess-1]
