movies = [
  {"Title": "Wakanda Forever", 
   "Year": 2022 ,
   "Producer":"Marvel" },
  
  {"Title" : "Avatar way of water",
   "Year": 2022 ,
   "Producer" : "Fox Century"},
  
  {"Title" : "Enola Holmes", 
   "Year" : 2022 , 
   "Producer" : "Netflix"},
]

Menu_prompt = "n\Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movied by title or 'q' to quit: "

def add_movie():
  title = input("Enter the movie title: ")
  year = input("Enter movie release year: ")
  producer = input("Enter movie producer: ")
  
  movies.append({
    "Title" : title,
    "Year" : year,
    "Producer" : producer
  })


def show_movies():
  for movie in movies:
    print_movie(movie)


def print_movie(movie):
  print(f"Title: {movie['Title']}")
  print(f"Year:{movie['Year']}")
  print(f"Producer:{movie['Producer']}")                

def find_movie():
  search_title = input("Enter movie you are looking for: ")
  
  for movie in movies:
    if movie["Title"] ==search_title:
      print_movie(movie)


user_option = {
  "a": add_movie,
  "l": show_movies,
  "f": find_movie
}

def Menu() :
  selection = input(Menu_prompt)
  while selection != 'q':
      if selection in user_option:
        selected_function =user_option[selection]
        selected_function()
       
      else :
        print('unknown command.plea\se try again')

      selection = input(Menu_prompt)




Menu()