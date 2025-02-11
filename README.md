# 🎥 Movie Watchlist CLI

A Python-based Command Line Interface (CLI) application to manage your personal movie watchlist. This application helps you add movies, update details, mark them as watched, and remove them from the list.

---

## 🛠 Features

- **Add Movies**: Add new movies to your watchlist with a title, genre, and release year.
- **View All Movies**: Display all movies in your watchlist, including watched/unwatched status.
- **Update Movie Details**: Edit the title, genre, release year, or status of a movie.
- **Mark as Watched**: Keep track of movies you’ve watched.
- **Delete Movies**: Remove movies from your watchlist permanently.

---

## 📋 Requirements

- Python 3.6+
- SQLite (pre-installed with Python)

---

## 🚀 Getting Started

Follow these steps to set up and run the Movie Watchlist CLI:

### Step 1: Clone the Repository

Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/movie-watchlist-cli.git
cd movie-watchlist-cli
```
### Step 2: Initialize the Database

Before running the application, set up the database using the provided script:

``` bash
python initialize_db.py
```
This script will create an SQLite database (movies.db) and set up the required table structure.

### Step 3: Run the Application
Start the CLI application by running:
```bash
python watchlist.py
```
### Usage Guide
After launching the application, you’ll see a menu with the following options:

Menu Options
Add a Movie
Add a new movie to your watchlist by providing the following details:

Title (required)
Genre (optional)
Release Year (optional)
View All Movies
View a complete list of movies in your watchlist. Movies are displayed with their ID, title, genre, release year, and watched status.

Update a Movie
Edit the details of an existing movie by selecting its ID from the list.

Mark a Movie as Watched
Quickly update the watched status of a movie to "watched."

Delete a Movie
Remove a movie permanently by selecting its ID.

Exit the Application
Quit the CLI application

### Example Workflow
Add a Movie:
Select option 1 and enter the movie details when prompted.
Example:
``` yaml
Enter movie title: The Matrix
Enter movie genre: Sci-Fi
Enter release year: 1999
Movie added successfully!
```
View Movies:
Select option 2 to see the updated list:

ID | Title         | Genre  | Release Year | Watched
----------------------------------------------------
1  | The Matrix    | Sci-Fi | 1999         | No

Mark as Watched:
Select option 4, enter the movie ID, and confirm:
```
Enter movie ID to mark as watched: 1
Movie marked as watched successfully!
```
Delete a Movie:
Select option 5, enter the movie ID, and confirm:
```
Enter movie ID to delete: 1
Movie deleted successfully!
```
### Files in This Project
initialize_db.py: Script to set up the SQLite database.
watchlist.py: Main CLI application script.
movies.db: SQLite database file to store movie data.

### Future Enhancements
Add search functionality to find movies by title, genre, or year.
Include sorting options for viewing movies.
Add genre-based filtering.
Export the watchlist to a CSV or text file.

### Technologies Used
Python: For building the CLI application.
SQLite: Lightweight database to store movie information.



