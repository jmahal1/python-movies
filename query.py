from movies import Movies

movies = Movies('./movies.txt')

while True:

    print("1. Press q to quit program")

    option = input()

    if(option == "q"):
        break