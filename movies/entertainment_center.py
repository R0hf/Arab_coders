import media 
import fresh_tomato
toy_story = media.Movie(
	"toy_story","story",
	"https://vignette.wikia.nocookie.net/marvelvscapcom/images/8/80/Spiderman.jpg/revision/latest?cb=20110729181501",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc") 
avatar = media.Movie(
	"avatar", "story_avatar",
	 "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
	  "https://www.youtube.com/watch?v=Ra-tiXq2jaE") 
hunger_games = media.Movie("hunger games" , "story" ,
	"https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg" ,
	"https://www.youtube.com/watch?v=RCDHJ6P_y0I")

midnight_in_paris = media.Movie("midnight in paris" , "story" , 
	"https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg" , 
	"https://www.youtube.com/watch?v=FAfR8omt-CY")

movies = [toy_story , avatar , hunger_games , midnight_in_paris]
#fresh_tomato.open_movies_page(movies)
print media.Movie.VALID_RATINGS


#avatar.show_trailer()