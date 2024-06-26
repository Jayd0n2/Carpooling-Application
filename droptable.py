import sqlite3

def drop_table(table_name):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('instance/database.db')  # Replace 'your_database.db' with your database file path
        cursor = conn.cursor()

        # Drop the table
        cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
        conn.commit()
        print(f"Table '{table_name}' dropped successfully.")

    except sqlite3.Error as e:
        print("Error:", e)

    finally:
        # Close the connection
        if conn:
            conn.close()

# Call the function with the name of the table you want to drop
drop_table('offered_scheduled_ride')
