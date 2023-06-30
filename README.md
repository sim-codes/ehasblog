# Django Blog App

The Django News App is a web application built with Django framework that allows users to view and publish stories. It provides a user-friendly interface for reading the latest stories and allows registered users to submit their own stories.

## Features

- User Registration: Users can create accounts to access additional features such as submitting stories and commenting on stories.
- Story Submission: Registered users can submit their own news Stories by filling out a form with the necessary details.
- Story Commenting: Users can engage in discussions by commenting on news Stories.
- User Profile: Registered users have personalized profiles where they can update password and Stories
- Admin Panel: Administrators have access to an admin panel for managing users, Stories, and tags.

## Installation

1. Clone the repository:
   git clone https://github.com/sim-codes/ehasblog.git

2. Navigate to the project directory:

```
cd News-App
```

3. Create a virtual environment:

```
python -m venv env
```

4. Activate the virtual environment:

- For Windows:
  ```
  env\Scripts\activate
  ```
- For macOS and Linux:
  ```
  source env/bin/activate
  ```

5. Install the dependencies:

```
pip install -r requirements.txt
```

6. Perform database migrations:

```
python manage.py migrate
```

7. Create a superuser (admin account):

```
python manage.py createsuperuser
```

8. Start the development server:

```
python manage.py runserver
```

9. Open your browser and access the app at [http://localhost:8000](http://localhost:8000).

## Configuration

- Database: The default configuration uses Postgresql as the database backend. If you prefer to use a different database, update the `DATABASES` setting in the `settings.py` file.
- Static Files: The static files such as CSS and JavaScript are stored in the `static` directory. If you want to serve them from a different location, modify the `STATIC_URL` and `STATIC_ROOT` settings in the `settings.py` file.

## Usage

- Register a new account or log in with an existing account to access additional features.
- Click on a Story to view its details, including comments from other users.
- Registered users can submit their own Stories by clicking on the "+New" button to create post/sotries.
- Administrators can access the admin panel at [http://localhost:8000/admin](http://localhost:8000/admin) to manage users and Stories.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please create a new issue in the [issue tracker](https://github.com/sim-codes/ehasblog/issues) or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code as per your needs.

## Acknowledgements
My self
The Django App was created using the "Django for Beginners Build websites with Python Django 4.0 (William Vincent)".
Django 4 By Example: Build Powerful and Reliable Python Web Applications from Scratch
