# Failed... Well more like incomplete.

word, used = "root", []

while True:
    letter = input("")
    
    if not letter in word:
        print("Incorrect letter")
        continue
    elif letter in word and letter in used:
        print(f'Already used letter "{letter}"')

    used.append(letter)

    if all(letter in used for letter in word):
        print("\nYou win!")
        exit(0)

