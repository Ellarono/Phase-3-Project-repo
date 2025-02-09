import sqlite3

DATABASE = "movies.db"
from colorama import Fore, Back,Style, init

init(autoreset=True)

def display_menu():
    print(Fore.CYAN + Style.DIM + "=" * 30)
    print(Back.YELLOW + Fore.BLACK "My Movie Watchlist CLI")
    print(Fore.CYAN + "=" * 30 + Style.RESET_ALL)
    print(Fore.GREEN + "1. Add a Movie")
    print(Fore.GREEN + "2. View All Movies")
    print(Fore.GREEN + "3. Update a Movie")
    print(Fore.GREEN + "4. Mark as Watched")
    print(Fore.MAGENTA + "5. Delete a Movie")
    print(Fore.CYAN + "6. Exit")
    print(Fore.CYAN + "=" * 30)

def add_movie():
    """Add a new movie to the database."""
    title = input("Enter the movie title: ")
    genre = input("Enter the genre: ")
    release_year = input("Enter the release year: ")
    
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO movies (title, genre, release_year) 
            VALUES (?, ?, ?)
        ''', (title, genre, release_year))
        conn.commit()
        print(f"Movie '{title}' added successfully.")

def view_movies():
    """View all movies in the database."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM movies')
        movies = cursor.fetchall()
        if movies:
            print("\nMovies in your watchlist:")
            for movie in movies:
                watched_status = "Watched" if movie[4] else "Not Watched"
                print(f"ID: {movie[0]}, Title: {movie[1]}, Genre: {movie[2]}, Year: {movie[3]}, Status: {watched_status}")
        else:
            print("No movies found in the watchlist.")

def update_movie():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    
    try:
        movie_id = input("Enter the ID of the movie you want to update: ")
        
        # Check if the movie exists
        cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))
        movie = cursor.fetchone()
        if not movie:
            print("Movie not found. Please try again.")
            return
        
        # Get new details for the movie
        print("Leave a field blank to keep the current value.")
        new_title = input(f"New Title (current: {movie[1]}): ") or movie[1]
        new_genre = input(f"New Genre (current: {movie[2]}): ") or movie[2]
        new_release_year = input(f"New Release Year (current: {movie[3]}): ") or movie[3]
        new_watched = input(f"Watched? (yes/no, current: {'yes' if movie[4] else 'no'}): ").lower()
        
        # Convert watched status to boolean
        if new_watched == "":
            new_watched = movie[4]  # Keep current value
        elif new_watched in ["yes", "y"]:
            new_watched = True
        elif new_watched in ["no", "n"]:
            new_watched = False
        else:
            print("Invalid input for watched status. Keeping current value.")
            new_watched = movie[4]
        
        # Update the movie
        cursor.execute("""
            UPDATE movies
            SET title = ?, genre = ?, release_year = ?, watched = ?
            WHERE id = ?
        """, (new_title, new_genre, new_release_year, new_watched, movie_id))
        conn.commit()
        print("Movie updated successfully!")
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


def mark_movie_as_watched():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    
    try:
        movie_id = input("Enter the ID of the movie to mark as watched: ")
        
        # Check if the movie exists
        cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))
        movie = cursor.fetchone()
        if not movie:
            print("Movie not found. Please try again.")
            return
        
        # Update the watched status
        cursor.execute("""
            UPDATE movies
            SET watched = ?
            WHERE id = ?
        """, (True, movie_id))
        conn.commit()
        print(f"Movie '{movie[1]}' has been marked as watched!")
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()
def delete_movie():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    
    try:
        movie_id = input("Enter the ID of the movie to delete: ")
        
        # Check if the movie exists
        cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))
        movie = cursor.fetchone()
        if not movie:
            print("Movie not found. Please try again.")
            return
        
        # Confirm before deleting
        confirm = input(f"Are you sure you want to delete '{movie[1]}'? (yes/no): ").lower()
        if confirm in ['yes', 'y']:
            cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
            conn.commit()
            print(f"Movie '{movie[1]}' has been deleted.")
        else:
            print("Deletion cancelled.")
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

 
def main():
    """Main function to run the CLI application."""
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ")
        if choice == "1":
            add_movie()
        elif choice == "2":
            view_movies()
        elif choice == "3":
            update_movie()
        elif choice == "4":
            mark_movie_as_watched()
        elif choice == "5":
            delete_movie()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    print("Starting the CLI application...")
    main()
