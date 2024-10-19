# BLOG APPLICATION

## INTRODUCTION

A simple blog application to showcase basic skills in Django Development.

## Setup Instructions

1. **Clone the Repository**
   - Clone the repository to your local machine using the provided URL.
   ```
   git clone https://gitlab.com/MCKY0822/task_2-simple-blog-application.git
   ```

2. **Navigate to the Project Directory**
   - Change into the project directory after cloning.
   ```
   cd task_2-simple-blog-application
   ```

3. **Set Up the Environment**
   - Create and activate a virtual environment for the project.
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Dependencies**
   - Install all necessary packages and dependencies.
   ```
   pip install -r requirements.txt
   ```

5. **Apply Migrations**
   - Set up the database by applying the migrations.
   ```
   python manage.py migrate
   ```

6. **Create a Superuser**
   - Create a superuser to access the admin panel for managing posts and users.
   ```
   python manage.py createsuperuser
   ```

7. **Create Another User (Non-Admin)**
   - Create a non-admin user to test authentication. This user can be created through the admin panel.
   ```
   http://127.0.0.1:8000/admin/
   ```

8. **Run the Server**
   - Start the Django development server to run the application.
   ```
   python manage.py runserver
   ```

9. **Access the Application**
   - Open your browser and navigate to the specified local URL to access the blog application.
   ```
   http://127.0.0.1:8000/
   ```

10. **Log In**
    - Log in using your credentials on the login page. Use the credentials of the non-admin user to test authentication.

11. **View Blog Posts**
    - After logging in, the home page will display recent blog posts.
    
12. **Create a Blog Post**
    - Authenticated users can create new blog posts using the available form and/or to the Blog Create page.
    ```
    http://127.0.0.1:8000/blogs/create/
    ```

13. **View All Blog Posts**
    - Navigate to see a list of all blog posts.
    ```
    http://127.0.0.1:8000/blogs/
    ```

14. **Delete a Blog Post (Admin Only)**
    - Admin users can delete posts from the specific blog page.
    ```
    http://127.0.0.1:8000/blogs/(blog id no.) -> http://127.0.0.1:8000/blogs/1
    ```

## REFERENCES

- [Python](https://www.python.org)
- [Django Documentation](https://docs.djangoproject.com/en/5.1/)
- [Django REST Framework](https://www.django-rest-framework.org)
- [w3schools](https://www.w3schools.com/django/index.php)
- [freeCodeCamp](https://www.freecodecamp.org)
- [YouTube/Dave Gray](https://www.youtube.com/@DaveGrayTeachesCode)
- [YouTube/Programming with Mosh](https://www.youtube.com/@programmingwithmosh)


## Michael R. Montaña
michaelmontana@me.com
