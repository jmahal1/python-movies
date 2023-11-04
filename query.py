from movies import Movies

movies = Movies('./movies.txt')

while True:

    print("1. Press q to quit program")
    print("2. Press 2 to list all movies")
    print("3. Press 3 to search for movie title")
    print("4. Press 4 to search for cast member")

    option = input()

    if(option == "q"):
        break
    elif(option == "2"):
        for film in movies._movies:
            print(film['name'])
    elif(option == "3"):
        title = input("Enter a movie name to search: ")
        for film in movies._movies:
            if(title.lower() in film['name'].lower()):      # lower() makes case insensitve
                print(film['name'])
    elif(option == "4"):
        person = input(" Enter the name of a cast member: ")
        for film in movies._movies:
            for index in range(len(film['cast'])):          # each film has different list length for cast values
                if (person.lower() in film['cast'][index].lower()):      
                    print(film['name'])
                    print(film['cast'][index])      