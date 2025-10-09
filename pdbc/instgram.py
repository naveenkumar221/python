import mysql.connector
from instadata import inst

try:
    conn=mysql.connector.connect(**inst)
    print("connection sucessfuly: ")
except:
    print(" not able to connect: ")
    
cursor=conn.cursor()

## to create database:

query='create database if not exists inst_data'

cursor.execute(query)

cursor.execute('use inst_data')

#creating the instgram data base and table :

try:
    create_users = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(100),
        email VARCHAR(100) UNIQUE,
        joined_date DATE
    )
    """
    cursor.execute(create_users)
    print("Users table ready")
except Exception as e:
    print("Error creating users table:", e)


# Create POSTS table

try:
    create_posts = """
    CREATE TABLE IF NOT EXISTS posts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        content TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
    """
    cursor.execute(create_posts)
    print("Posts table ready")
except Exception as e:
    print("Error creating posts table:", e)




# CREATE USER

def create_user(username, email, joined_date):
    try:
        query = "INSERT INTO users (username, email, joined_date) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, email, joined_date))
        print(f"User {username} created successfully")
    except Exception as e:
        print("Error creating user:", e)

create_user("alice", "alice@gmail.com", "2025-09-20")
create_user("bob", "bob@gmail.com", "2025-09-21")

# CREATE POST

def create_post(user_id, content):
    try:
        query = "INSERT INTO posts (user_id, content) VALUES (%s, %s)"
        cursor.execute(query, (user_id, content))
        print("Post created successfully")
    except Exception as e:
        print("Error creating post:", e)

create_post(1, "Alice's first post!")
create_post(1, "Alice's second post!")
create_post(2, "Bob's first post!")




# READ USER + POSTS

def get_user_with_posts(user_id):
    try:
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        if not user:
            print("User not found")
            return
        print("User:", user)

        cursor.execute("SELECT * FROM posts WHERE user_id = %s", (user_id,))
        posts = cursor.fetchall()
        print("Posts:", posts)
    except Exception as e:
        print("Error fetching user:", e)

get_user_with_posts(1)
get_user_with_posts(2)


# UPDATE USER EMAIL

def update_user_email(user_id, new_email):
    try:
        query = "UPDATE users SET email = %s WHERE id = %s"
        cursor.execute(query, (new_email, user_id))
        print("User email updated")
    except Exception as e:
        print("Error updating email:", e)


update_user_email(1, "alice_new@gmail.com")

# UPDATE POST CONTENT

def update_post(post_id, new_content):
    try:
        query = "UPDATE posts SET content = %s WHERE id = %s"
        cursor.execute(query, (new_content, post_id))
        print("Post updated")
    except Exception as e:
        print("Error updating post:", e)

update_post(2, "Updated content of Alice's second post")

# DELETE USER


def delete_user(user_id):
    try:
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        print(f"User {user_id} deleted")
    except Exception as e:
        print("Error deleting user:", e)


delete_user(2)  


# DELETE POST

def delete_post(post_id):
    try:
        query = "DELETE FROM posts WHERE id = %s"
        cursor.execute(query, (post_id,))
        print(f"Post {post_id} deleted")
    except Exception as e:
        print("Error deleting post:", e)
        
delete_post(3)  















conn.commit()
cursor.close()
conn.close()


 
