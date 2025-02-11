# Movie Watchlist CLI Application

### Overview
The Movie Watchlist CLI Application is a simple command-line tool that helps users manage their movie watchlist. With this app, users can add, view, update, mark as watched, and delete movies from their personal watchlist. The application uses an SQLite database to store the movie information.

### Features
- **Add a Movie:** Add a new movie to the watchlist with the title, genre, and release year.
- **View All Movies:** Display a list of all movies in the watchlist with their details, including watched status.
- **Update a Movie:** Update the details of an existing movie (title, genre, release year, or watched status).
- **Mark a Movie as Watched:** Mark a movie as watched without changing any other details.
- **Delete a Movie:** Remove a movie from the watchlist.
- **Exit the Application:** Exit the CLI application.
  
### Technologies Used
- **Python:** The primary language used to implement the CLI application.
- **SQLite:** A lightweight relational database to store movie data.
- **SQLite3:** Python library used to interact with the SQLite database.
  
### Prerequisites
Before using this application, ensure that you have Python installed on your system.
Installation
1. Clone the Repository:
```bash
git clone https://github.com/your-username/movie-watchlist-cli.git
cd movie-watchlist-cli
```
2. Install Python (if not already installed):

Download Python and follow the installation instructions for your platform.
3. Setup the Database:

- The initialize_db.py script is provided to create the required SQLite database (movies.db) and tables.
- Run the initialize_db.py script to initialize the database:
  
```bash
python initialize_db.py
```
4. Running the Application:
- After setting up the database, run the CLI application with the following command:
```bash
python movie_watchlist.py
```
# Usage
Once the application is running, you will be prompted with a menu of options. You can:

1. Add a Movie:
- Choose option 1 and provide the movie title, genre, and release year.

3. View All Movies:
- Choose option 2 to display all the movies in your watchlist, including their watched status.

4. Update a Movie:
- Choose option 3 and provide the movie ID to update the movie details. You can update the title, genre, release year, and watched status.

5. Mark a Movie as Watched:
- Choose option 4 and provide the movie ID to mark the movie as watched.

6.Delete a Movie:
- Choose option 5 and provide the movie ID to delete the movie from the watchlist.

7.Exit the Application:
- Choose option 6 to exit the CLI application.
Sample Menu Interaction
```bash
Movie Watchlist CLI
1. Add a movie
2. View all movies
3. Update a movie
4. Mark a movie as watched
5. Delete a movie
6. Exit

Enter your choice (1-6): 1
Enter the movie title: Inception
Enter the genre: Sci-Fi
Enter the release year: 2010
Movie 'Inception' added successfully.

Enter your choice (1-6): 2
Movies in your watchlist:
ID: 1, Title: Inception, Genre: Sci-Fi, Year: 2010, Status: Not Watched
```
### Live Demo
There is no live demo available for this CLI application, but you can try it locally by following the setup instructions above.
