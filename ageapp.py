movies = {'movie1': 0, 'movie2': 10, 'movie3': 13, 'movie4': 18}

name = input('What is your name? ')
age = int(input('What is your age? '))

while True:
    movieName = input(f"What movie do you want to watch, Mr {name}? ")
    
    if movieName in movies:
        age_data = int(movies[movieName])
        
        if age > age_data:
            print(f"Welcome {name}! YOu can watch movie")
        else:
            print("Koi aur movie dekh le bhai")

    else:
        print("Bhag ja nahi to laat khayega") 

