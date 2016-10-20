import fresh_tomatoes
import media

# Initialize the project with movie data
batman_begins = media.Movie(
    "Batman Begins",
    "First Movie of Batman: Dark Knight Trilogy",
    "https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",
    "https://www.youtube.com/watch?v=neY2xVmOfUM")

dark_knight = media.Movie(
    "The Dark Knight",
    "Second Movie of Batman: Dark Knight Trilogy",
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
    "https://www.youtube.com/watch?v=yrJL5JxEYIw")

dark_knight_rises = media.Movie(
    "The Dark Knight Rises",
    "Third Movie of Batman: Dark Knight Trilogy",
    "https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.\
jpg",
    "https://www.youtube.com/watch?v=J9DlV9qwtF0")

toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that become real",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "An epic science fiction Movie which showed alien life on pandora",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

avengers = media.Movie(
    "Avengers",
    "A superhero movie based on Marvels comics",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
    "https://www.youtube.com/watch?v=eOrNdBpGMv8")

the_proposal = media.Movie(
    "The Proposal",
    "Here comes the bride",
    "https://upload.wikimedia.org/wikipedia/en/0/02/The_Proposal.jpg",
    "https://www.youtube.com/watch?v=RFL8b1p1ELY")

titanic = media.Movie(
    "Titanic",
    "Story of Love",
    "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
    "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

# Creating the array of movie data
movies = [batman_begins, dark_knight, dark_knight_rises, toy_story, avatar,
          avengers, the_proposal, titanic]
# Creating the web page
fresh_tomatoes.create_movie_tiles_content(movies)
fresh_tomatoes.open_movies_page(movies)
