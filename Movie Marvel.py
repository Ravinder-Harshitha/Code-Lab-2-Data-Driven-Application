#import tkinter module and messagebox and other libraries
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image 
from tkinter import messagebox
import tkinter as tk
import requests
import random
import io

# Set the output window
root = Tk()
# name of the window
root.title('MovieMarvel')
# size of the output window
root.geometry('900x600')
# background color of the window
root.config(bg='#FAEF5D')
# code to disable the resizing of output window
root.resizable(0,0)

# Function to switch between frames
def show_frame(frame):
    frame.tkraise()

# Start frame
start_frame = Frame(root)
start_frame.place(x=10, y=10, height=580, width=880)

# Adding Background Image to start frame
bg_image = Image.open("1.png")
resize_image = bg_image.resize((880,580))
bg_img1 = ImageTk.PhotoImage(resize_image)
bg_image_label1 = Label(start_frame, image=bg_img1)
bg_image_label1.place(x=-2,y=-2)


# Instructions button
button = Button(start_frame, text="Instructions", fg="black", bg="#FFFB38", bd = 0, font=("Lucida Sans", 10, "bold"), command=lambda:show_frame(instruction_frame))
button.place(x=595, y=232, height=30, width=100)

# Enter button
button_1 = Button(start_frame, text="Enter", fg="black", bg="#FFFB38", font=("Lucida Sans", 10,"bold"), bd = 0, command=lambda:show_frame(main_frame))
button_1.place(x=595, y=326, height=30, width=100)



# instruction frame to display instructions
instruction_frame = Frame(root, bg="#181818")
instruction_frame.place(x=50, y=50, height=450, width=800)

# heading label
heading = Label(instruction_frame, text="INSTRUCTIONS", fg="#FFFB38", bg="#181818", font=("Lucida Sans", 15,"bold"))
heading.place(x=310, y=50)

# text labels
instructions_label1 = Label(instruction_frame, text=" This application primarily provides information about movies based on genre, \n popularity and user preferences.", fg="white", bg="#181818", font=("Lucida Sans", 10))
instructions_label1.place(x=140, y=100)

instructions_label2 = Label(instruction_frame, text="Using the buttons on the left navigation of the screen, you can navigate and search \n different movies according to what you are looking for.", fg="white", bg="#181818", font=("Lucida Sans", 10))
instructions_label2.place(x=170, y=150)

# image in instruction frame
pic_0 = Image.open("juliasart170500014-removebg-preview.png")
pic_1 = pic_0.resize((170,170))
img1 = ImageTk.PhotoImage(pic_1)
imgLabel1 = Label(instruction_frame, image=img1, bg="#181818")
imgLabel1.place(x=300, y=200)

# Place order button
enter_button = Button(instruction_frame, text="Enter", fg="black", bg="#FFFB38", font=("Lucida Sans", 10, "bold"), command=lambda:show_frame(main_frame))
enter_button.place(x=335, y=400, height=30, width=100)


# Menu frame to choose coffee options
main_frame = Frame(root, bg="black")
main_frame.place(x=10, y=10, height=580, width=880)

# background image to main page
bg_image_1 = Image.open("Purple Gradient Metaverse Desktop Prototype (2).png")
resize_image = bg_image_1.resize((880,580))
bg_img3 = ImageTk.PhotoImage(resize_image)
bg_image_label2 = Label(main_frame, image=bg_img3)
bg_image_label2.place(x=200,y=-2)

# Frame containing navigation bar/buttons
navigation_frame = Frame(main_frame, bg="#222222", width="200")
navigation_frame.place(x=0, y=0, height=580, width=200)

# image in navigation frame
pic_2 = Image.open("juliasart170500014-removebg-preview.png")
pic_3 = pic_2.resize((100,100))
img2 = ImageTk.PhotoImage(pic_3)
imgLabel3 = Label(navigation_frame, image=img2, bg="#222222")
imgLabel3.place(x=50, y=300)

# Search button from the navigation bar
search_button = Button(navigation_frame, text="Search", border=0, bg="#222222", fg= "white", font=("Lucida Sans", 11), command=lambda:show_frame(search_frame))
search_button.place(x=55, y=50, height=30, width=90)


# Search Frame
search_frame = Frame(root, bg="gray")
search_frame.place(x=210, y=10, height=580, width=680)

# Sub-frame at the top with button and text
searchboxframe = Frame(search_frame, bg="#222222", width="200")
searchboxframe.place(x=5, y=5, height=80, width=670)

# label containing directionary text
text_label = Label(searchboxframe, text="Enter movie name", bg="#222222", fg="white", font=("Helvetica", 11))
text_label.place(x=70, y=30)


# Class to search movies 
class SearchMovies:
    def __init__(self, root, parent_frame):
        self.root = root
        self.parent_frame = parent_frame

        self.api_key = "8b127865f52e616a7772337e4ef916f6"

        self.display_frame = tk.Frame(self.parent_frame, bg="black")
        self.display_frame.place(x=5, y=90, height=485, width=670)

        self.plot_frame = tk.Frame(self.parent_frame, bg="#222222")
        self.plot_frame.place(x=20, y=365, height=200, width=640)

        self.movie_details_frame = tk.Frame(self.parent_frame, bg="#222222")
        self.movie_details_frame.place(x=230, y=105, height=250, width=430)

        self.movie_poster_label = tk.Label(self.display_frame)
        self.movie_poster_label.place(x=15, y=15, height=250, width=200)

        self.movie_title_label = tk.Label(self.movie_details_frame, text="", fg="white", bg="#222222", font=("Helvetica", 10, "bold"))
        self.movie_title_label.place(x=20, y=20)

        self.release_date_label = tk.Label(self.movie_details_frame, text="", fg="white", bg="#222222", font=("Helvetica", 10, "bold"))
        self.release_date_label.place(x=20, y=50)

        self.language_label = tk.Label(self.movie_details_frame, text="", fg="white", bg="#222222", font=("Helvetica", 10, "bold"))
        self.language_label.place(x=20, y=80)

        self.run_time_label = tk.Label(self.movie_details_frame, text="", fg="white", bg="#222222", font=("Helvetica", 10, "bold"))
        self.run_time_label.place(x=20, y=110)

        self.popularity_label = tk.Label(self.movie_details_frame, text="", fg="white", bg="#222222", font=("Helvetica", 10, "bold"))
        self.popularity_label.place(x=20, y=140)

        self.genre_label = tk.Label(self.movie_details_frame, text="", fg="white", bg="#222222", font=("Helvetica", 10, "bold"))
        self.genre_label.place(x=20, y=170)

        self.plot_label = tk.Label(self.plot_frame, text="", fg="white", bg="#222222", wraplength=550, font=("Helvetica", 10))
        self.plot_label.place(x=50, y=20)

        self.search_entry = tk.Entry(searchboxframe, width=20)
        self.search_entry.place(x= 210, y=30, width=250, height=25)

        self.search_button = tk.Button(search_frame, text="Search Movie", bg="#FAEF5D", fg= "black", command=self.search_movie)
        self.search_button.place(x=480, y=35)

    def get_movie_details(self, movie_id):
        # API request to get details of a specific movie
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={self.api_key}"
        response = requests.get(url)
        
        if response.status_code == 200:
            movie_data = response.json()
            return movie_data
        else:
            messagebox.showerror("Error",f"Failed to fetch details for movie ID {movie_id}.")
            return None

    # Function to display movie information
    def display_movie(self, movie_data):
        if movie_data:
            self.movie_title_label.config(text=f"Title: {movie_data['title']}")
            self.release_date_label.config(text=f"Release Date: {movie_data['release_date']}")
            self.language_label.config(text=f"Language: {movie_data['original_language']}")
            self.run_time_label.config(text=f"Run time: {movie_data['runtime']} minutes")
            self.popularity_label.config(text=f"Popularity score: {movie_data['popularity']}")
            genres = ", ".join([genre['name'] for genre in movie_data['genres']])
            self.genre_label.config(text=f"Genres: {genres}")
            self.plot_label.config(text=f"Overview \n \n {movie_data['overview']}")

            # Getting movie poster from API url
            poster_url = f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}"
            poster_data = requests.get(poster_url).content
            original_image = Image.open(io.BytesIO(poster_data))
            resized_image = original_image.resize((200, 250))
            
            # Converting the resized image to BytesIO
            resized_poster_data = io.BytesIO()
            resized_image.save(resized_poster_data, format="PNG")
            resized_poster_data.seek(0)

            # Displaying the resized image in poster label
            poster_image = ImageTk.PhotoImage(Image.open(resized_poster_data))
            self.movie_poster_label.config(image=poster_image)
            self.movie_poster_label.image = poster_image
        else:
            messagebox.showerror("Error","No movie data to display.")

    # Function to search movie information
    def search_movie(self):
        search_query = self.search_entry.get()
        if search_query:
            # API request to search for movie by title
            url = f"https://api.themoviedb.org/3/search/movie?api_key={self.api_key}&query={search_query}"
            response = requests.get(url)

            if response.status_code == 200:
                movie_list = response.json().get('results', [])
                if movie_list:
                    # Display the details of the first searched movie
                    details_data = self.get_movie_details(movie_list[0]['id'])
                    if details_data:
                        self.display_movie(details_data)
                else:
                    messagebox.showerror("Error","No results found.")
            else:
                messagebox.showerror("Error","Failed to fetch search results.")
        else:
            messagebox.showerror("Error","Please enter a search query.")

movie_app_instance = SearchMovies(root, search_frame)

# back button to go back to home page                                 
back_button = Button(search_frame, text="Back", border=0, bg="grey", fg= "yellow", font=("Lucida Sans", 10), command=lambda:show_frame(main_frame))
back_button.place(x=560, y=525, height=30, width=90)



# About button from the navigation bar
about_button = Button(navigation_frame, text="About", border=0, bg="#222222", fg= "white", font=("Lucida Sans", 11), command=lambda:show_frame(about_frame))
about_button.place(x=55, y=100, height=30, width=90)

# Menu frame to choose coffee options
about_frame = Frame(root, bg="black")
about_frame.place(x=210, y=10, height=580, width=680)

# text labels
text_label = Label(about_frame, text="ABOUT", fg="#FAEF5D", bg="black", font=("Lucida Sans", 15, "bold"))
text_label.place(x= 20, y=30)

L1 = Label(about_frame, text="Movie Marvel is a movie database-based application that gives information about different movies ", fg="white", bg="black", font=("Lucida Sans", 10))
L1.place(x=20, y=80)

L1 = Label(about_frame, text="from across the world.", fg="white", bg="black", font=("Lucida Sans", 10))
L1.place(x=20, y=105)

L2 = Label(about_frame, text="The best application to search and surf for movies - popular, classics and of whatever genre you are a ", fg="white", bg="black", font=("Lucida Sans", 10))
L2.place(x=20, y=130)

L2 = Label(about_frame, text="fan of.", fg="white", bg="black", font=("Lucida Sans", 10))
L2.place(x=20, y=155)

L3 = Label(about_frame, text="Click on the various options to search and view movies based on the user, genre or popularity.", fg="white", bg="black", font=("Lucida Sans", 10))
L3.place(x= 20, y=180)

H2 = Label(about_frame, text="Browse for Movies", fg="#FAEF5D", bg="black", font=("Lucida Sans", 11, "bold"))
H2.place(x= 20, y=225)

L4 = Label(about_frame, text="Click on Search option and enter the name of the movie you want to search for. And click on  \n \n search to get the information about your movie.", fg="white", bg="black", font=("Lucida Sans", 10))
L4.place(x= 20, y=255)

H3 = Label(about_frame, text="Search for Movies based on Genres", fg="#FAEF5D", bg="black", font=("Lucida Sans", 11, "bold"))
H3.place(x= 20, y=330)

L5 = Label(about_frame, text="Click on Genre option and select the genre of the movie you want to search from the dropdown list. \n \n And click on search to get the information about the movie.", fg="white", bg="black", font=("Lucida Sans", 10))
L5.place(x= 20, y=360)

H4 = Label(about_frame, text="Browse for Popular Movies", fg="#FAEF5D", bg="black", font=("Lucida Sans", 11, "bold"))
H4.place(x= 20, y=435)

L6 = Label(about_frame, text="Click on Genre option and select the genre of the movie you want to search from the dropdown list. \n \n And click on search to get the information about the movie.", fg="white", bg="black", font=("Lucida Sans", 10))
L6.place(x= 20, y=465)

# back button to go back to home page
back_button = Button(about_frame, text="Back", border=0, bg="grey", fg= "yellow", font=("Lucida Sans", 10), command=lambda:show_frame(main_frame))
back_button.place(x=560, y=525, height=30, width=90)




# Genre button from the navigation bar
genre_button = Button(navigation_frame, text="Genre", border=0, bg="#222222", fg= "white", font=("Lucida Sans", 11), command=lambda:show_frame(genre_frame))
genre_button.place(x=55, y=150, height=30, width=90)

# Genre Frame
genre_frame = Frame(root, bg="grey")
genre_frame.place(x=210, y=10, height=580, width=680)

# Sub-frame at the top with button and text
findgenreframe = Frame(genre_frame, bg="#222222", width="200")
findgenreframe.place(x=5, y=5, height=80, width=670)

# label containing directionary text
text_label = Label(genre_frame, text="Select Genre", bg="#222222", fg="white", font=("Helvetica", 11))
text_label.place(x=110, y=35)

# Class to get movies based on genre
class MovieGenre:
    def __init__(self, root, parent_frame):
        self.root = root
        self.parent_frame = parent_frame

        self.api_key = "8b127865f52e616a7772337e4ef916f6"

        self.display_frame = tk.Frame(self.parent_frame, bg="black")
        self.display_frame.place(x=5, y=90, height=485, width=670)

        self.plot_frame = tk.Frame(self.parent_frame, bg="#222222")
        self.plot_frame.place(x=20, y=365, height=200, width=640)

        self.movie_details_frame = tk.Frame(self.parent_frame, bg="#222222")
        self.movie_details_frame.place(x=230, y=105, height=250, width=430)

        self.movie_poster_label = tk.Label(self.display_frame)
        self.movie_poster_label.place(x=15, y=15, height=250, width=200)

        self.movie_title_label = tk.Label(self.movie_details_frame, text="", fg="white", bg="#222222", font=("Helvetica", 10, "bold"))
        self.movie_title_label.place(x=20, y=20)

        self.release_date_label = tk.Label(self.movie_details_frame, text="", fg="white", bg="#222222", font=("Helvetica", 10, "bold"))
        self.release_date_label.place(x=20, y=50)

        self.language_label = tk.Label(self.movie_details_frame, text="", fg="white", bg="#222222", font=("Helvetica", 10, "bold"))
        self.language_label.place(x=20, y=80)

        self.run_time_label = tk.Label(self.movie_details_frame, text="", fg="white", bg="#222222", font=("Helvetica", 10, "bold"))
        self.run_time_label.place(x=20, y=110)

        self.popularity_label = tk.Label(self.movie_details_frame, text="", fg="white", bg="#222222", font=("Helvetica", 10, "bold"))
        self.popularity_label.place(x=20, y=140)

        self.genre_label = tk.Label(self.movie_details_frame, text="", fg="white", bg="#222222", font=("Helvetica", 10, "bold"))
        self.genre_label.place(x=20, y=170)

        self.plot_label = tk.Label(self.plot_frame, text="", fg="white", bg="#222222", wraplength=550, font=("Helvetica", 10))
        self.plot_label.place(x=50, y=20)

        # Dropdown for selecting genres
        self.genres = [
            {"id": 28, "name": "Action"},
            {"id": 12, "name": "Adventure"},
            {"id": 878, "name": "Science Fiction"},
            {"id": 53, "name": "Thriller"},
            {"id": 27, "name": "Horror"},
            {"id": 9648, "name": "Mystery"},
            {"id": 36, "name": "History"},
            {"id": 14, "name": "Fantasy"},
            {"id": 18, "name": "Drama"},
            {"id": 35, "name": "Comedy"},
            {"id": 80, "name": "Crime"},
            {"id": 10749, "name": "Romance"},
        ]

        self.genre_combobox = ttk.Combobox(findgenreframe, values=[genre["name"] for genre in self.genres])  # Corrected
        self.genre_combobox.set("Select Genre")
        self.genre_combobox.place(x=210, y=30, width=250, height=25)

        # button to get the movie based on genre
        self.fetch_button = tk.Button(findgenreframe, text="Get Any Movie", bg="#FAEF5D", fg= "black", command=self.get_and_display_movie)
        self.fetch_button.place(x=475, y=30)

    def get_movie_by_genre(self, genre_id):
        # API request to discover random movies of a selected genre
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={self.api_key}&sort_by=popularity.desc&with_genres={genre_id}"
        response = requests.get(url)
        
        if response.status_code == 200:
            movie_list = response.json().get('results', [])
            return random.choice(movie_list) if movie_list else None
        else:
            messagebox.showerror("Error","Failed to fetch random movie of genre ID {genre_id}.")
            return None

    # Function to get movie details and display
    def get_and_display_movie(self):
        selected_genre_name = self.genre_combobox.get()  
        selected_genre = next((genre for genre in self.genres if genre["name"] == selected_genre_name), None)

        if selected_genre:
            genre_id = selected_genre["id"]
            movie_data = self.get_movie_by_genre(genre_id)
            self.display_movie(movie_data)
        else:
            messagebox.showerror("Error","Invalid genre selected.")

    # Function to get movie details
    def get_movie_details(self, movie_id):
        # API request to get details of a specific movie
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={self.api_key}"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            messagebox.showerror("Error",f"Failed to fetch details for movie ID {movie_id}.")
            return None    

    # Function to display movie information
    def display_movie(self, movie_data):
        if movie_data:
            movie_id = movie_data['id']
            details_data = self.get_movie_details(movie_id)

            if details_data:
                self.movie_title_label.config(text=f"Title: {details_data['title']}")
                self.release_date_label.config(text=f"Release Date: {details_data['release_date']}")
                self.language_label.config(text=f"Language: {details_data['original_language']}")
                self.run_time_label.config(text=f"Run time: {details_data['runtime']} minutes")
                self.popularity_label.config(text=f"Popularity score: {details_data['popularity']}")
                genres = ", ".join([genre['name'] for genre in details_data['genres']])
                self.genre_label.config(text=f"Genres: {genres}")
                self.plot_label.config(text=f"Overview \n \n{details_data['overview']}")

                # Getting movie poster from API url 
                poster_url = f"https://image.tmdb.org/t/p/w500{details_data['poster_path']}"
                poster_data = requests.get(poster_url).content
                original_image = Image.open(io.BytesIO(poster_data))
                resized_image = original_image.resize((200, 250))
                
                # Converting the resized image to BytesIO
                resized_poster_data = io.BytesIO()
                resized_image.save(resized_poster_data, format="PNG")
                resized_poster_data.seek(0)

                # Displaying the resized image in poster label
                poster_image = ImageTk.PhotoImage(Image.open(resized_poster_data))
                self.movie_poster_label.config(image=poster_image)
                self.movie_poster_label.image = poster_image
            else:
                messagebox.showerror("Error","No details data to display.")
        else:
            messagebox.showerror("Error","No movie data to display.")

# Creating an instance of the MovieApp within the popular frame
movie_app_instance = MovieGenre(root, genre_frame)

# back button to go back to home page
back_button = Button(genre_frame, text="Back", border=0, bg="grey", fg= "yellow", font=("Lucida Sans", 10), command=lambda:show_frame(main_frame))
back_button.place(x=560, y=525, height=30, width=90)




# Popular button from the navigation bar
back_button = Button(navigation_frame, text="Popular", border=0, bg="#222222", fg= "white", font=("Lucida Sans", 11),command=lambda:show_frame(popular_frame))
back_button.place(x=56, y=200, height=30, width=90)

# Popular Frame
popular_frame = tk.Frame(root, bg="grey")
popular_frame.place(x=210, y=10, height=580, width=680)

# Sub-frame at the top with button and text
getmovieframe = Frame(popular_frame, bg="#222222", width="200")
getmovieframe.place(x=5, y=5, height=80, width=670)

# label containing directionary text
text_label = Label(getmovieframe, text="Press the button to get the popular movies right now!", bg="#222222", fg="white", font=("Helvetica", 11))
text_label.place(x=40, y=30)

# Class to get popular movies
class PopularMovie:
    def __init__(self, root, parent_frame):
        self.root = root
        self.parent_frame = parent_frame

        self.api_key = "8b127865f52e616a7772337e4ef916f6"

        self.display_frame = tk.Frame(self.parent_frame, bg="black")
        self.display_frame.place(x=5, y=90, height=485, width=670)

        self.plot_frame = tk.Frame(self.parent_frame, bg="#222222")
        self.plot_frame.place(x=20, y=365, height=200, width=640)

        self.movie_details_frame = tk.Frame(self.parent_frame, bg="#222222")
        self.movie_details_frame.place(x=230, y=105, height=250, width=430)

        self.movie_poster_label = tk.Label(self.display_frame)
        self.movie_poster_label.place(x=15, y=15, height=250, width=200)

        self.movie_title_label = tk.Label(self.movie_details_frame, text="", fg="white", bg="#222222", font=("Helvetica", 10, "bold"))
        self.movie_title_label.place(x=20, y=20)

        self.release_date_label = tk.Label(self.movie_details_frame, text="", fg="white", bg="#222222", font=("Helvetica", 10, "bold"))
        self.release_date_label.place(x=20, y=50)

        self.language_label = tk.Label(self.movie_details_frame, text="", fg="white", bg="#222222", font=("Helvetica", 10, "bold"))
        self.language_label.place(x=20, y=80)

        self.run_time_label = tk.Label(self.movie_details_frame, text="", fg="white", bg="#222222", font=("Helvetica", 10, "bold"))
        self.run_time_label.place(x=20, y=110)

        self.popularity_label = tk.Label(self.movie_details_frame, text="", fg="white", bg="#222222", font=("Helvetica", 10, "bold"))
        self.popularity_label.place(x=20, y=140)

        self.genre_label = tk.Label(self.movie_details_frame, text="", fg="white", bg="#222222", font=("Helvetica", 10, "bold"))
        self.genre_label.place(x=20, y=170)

        self.plot_label = tk.Label(self.plot_frame, text="", fg="white", bg="#222222", wraplength=550, font=("Helvetica", 10))
        self.plot_label.place(x=50, y=20)

        self.fetch_button = tk.Button(getmovieframe, text="Get Popular Movies", bg="#FAEF5D", fg= "black", command=self.display_movie)
        self.fetch_button.place(x=520, y=29)

    # Function to get a random movie based on popularity
    def get_random_movie(self):
        # API request to get random movies
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={self.api_key}&sort_by=popularity.desc"
        response = requests.get(url)
        
        if response.status_code == 200:
            movie_list = response.json().get('results', [])
            return random.choice(movie_list) if movie_list else None
        else:
            messagebox.showerror("Error","Failed to fetch random movie.")
            return None

    # Function to get movie details
    def get_movie_details(self, movie_id):
        # API request to get details of a specific movie
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={self.api_key}"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            messagebox.showerror("Error",f"Failed to fetch details for movie ID {movie_id}.")
            return None

    # Function to display movie information
    def display_movie(self):
        movie_data = self.get_random_movie()
        if movie_data:
            movie_id = movie_data['id']
            details_data = self.get_movie_details(movie_id)

            if details_data:
                self.movie_title_label.config(text=f"Title: {details_data['title']}")
                self.release_date_label.config(text=f"Release Date: {details_data['release_date']}")
                self.language_label.config(text=f"Language: {details_data['original_language']}")
                self.run_time_label.config(text=f"Run time: {details_data['runtime']} minutes")
                self.popularity_label.config(text=f"Popularity score: {details_data['popularity']}")
                genres = ", ".join([genre['name'] for genre in details_data['genres']])
                self.genre_label.config(text=f"Genres: {genres}")
                self.plot_label.config(text=f"Overview \n \n {details_data['overview']}")

                # Getting movie poster from API url 
                poster_url = f"https://image.tmdb.org/t/p/w500{details_data['poster_path']}"
                poster_data = requests.get(poster_url).content
                original_image = Image.open(io.BytesIO(poster_data))
                resized_image = original_image.resize((200, 250))
                
                # Converting the resized image to BytesIO
                resized_poster_data = io.BytesIO()
                resized_image.save(resized_poster_data, format="PNG")
                resized_poster_data.seek(0)

                # Displaying the resized image in poster label
                poster_image = ImageTk.PhotoImage(Image.open(resized_poster_data))
                self.movie_poster_label.config(image=poster_image)
                self.movie_poster_label.image = poster_image
            else:
                #print("No details data to display.")
                messagebox.showerror("Error", "No details data to display.")
        else:
            #print("No movie data to display.")
            messagebox.showerror("Error", "No movie data to display.")

# Creating an instance of the MovieApp within the popular frame
movie_app_instance = PopularMovie(root, popular_frame)

# back button to go back to home page
back_button = tk.Button(popular_frame, text="Back", border=0, bg="grey", fg= "yellow", font=("Lucida Sans", 10), command=lambda: show_frame(main_frame))
back_button.place(x=560, y=525, height=30, width=90)


# Exit button located in under navigation bar to leave the app
b6 = Button(navigation_frame, text="Exit", border=0, bg="grey", fg= "yellow", font=("Lucida Sans", 11), command=lambda:show_frame(end_frame))
b6.place(x=56, y=530, height=30, width=90)

# End/Last Frame
end_frame = Frame(root)
end_frame.place(x=10, y=10, height=580, width=880)

# background image to enf frame
bg_image = Image.open("Purple Gradient Metaverse Desktop Prototype (1).png")
resize_image = bg_image.resize((880,580))
bg_img2 = ImageTk.PhotoImage(resize_image)
bg_image_label3 = Label(end_frame, image=bg_img2)
bg_image_label3.place(x=-2,y=-2)

# frame to display text and logo
last_frame = Frame(end_frame, bg="#181818")
last_frame.place(x=40, y=50, height=350, width=800)

# text label
end_label = Label(last_frame, text="You Exited the Application \n \n Movie Marvel - Your go-to destination for movie surfing!", fg="white", bg="#181818", font=("Lucida Sans", 12))
end_label.place(x=200, y=205)

# logo image
pic_4 = Image.open("Black Orange Modern Star Entertainment Studio Logo (1).png")
pic_5 = pic_4.resize((200,200))
img3 = ImageTk.PhotoImage(pic_5)
imgLabel4 = Label(last_frame, image=img3, bg="#181818")
imgLabel4.place(x=300, y=5)

# Function for message box
def msg():
    message = "This app is made using MovieDB API and Python Tkinter. \n \n Made by Ravinder Harshitha Egudur"
    messagebox.showinfo("Submission",message)

# Exit button located in under navigation bar to leave the app
b6 = Button(last_frame, text="Click Me", border=0, bg="grey", fg= "yellow", font=("Lucida Sans", 11), command=msg)
b6.place(x=350, y=290, height=30, width=90)

# run the loop
start_frame.tkraise()
root.mainloop()