from movies import Movies

movies = Movies('./movies.txt')

while True:

    print("1. Press q to quit program")
    print("2. Press 2 to list all movies")

    option = input()

    if(option == "q"):
        break
    elif(option == "2"):
        for film in movies._movies:
            print(film['name'])