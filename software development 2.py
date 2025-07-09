def add_post():
    title = input("Title: ")
    content = input("Content: ")
    with open("blog.txt", "a") as f:
        f.write(f"{title}\n{content}\n---\n")
    print("Post added.")

def view_posts():
    try:
        with open("blog.txt", "r") as f:
            print("\n--- All Posts ---")
            print(f.read())
    except FileNotFoundError:
        print("No posts yet.")

def delete_all():
    open("blog.txt", "w").close()
    print("All posts deleted.")

while True:
    print("\n1. Add Post  2. View Posts  3. Delete All  4. Exit")
    ch = input("Choose: ")
    if ch == "1":
        add_post()
    elif ch == "2":
        view_posts()
    elif ch == "3":
        delete_all()
    elif ch == "4":
        break
    else:
        print("Invalid choice.")
