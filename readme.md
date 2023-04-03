# How to Django

### Using the virtual environment

In order to ensure that all developers working on this project have the same dependencies, we have created a virtual
environment. <br> This virtual environment contains all of the necessary packages and libraries required for the project to
run smoothly.

To activate the virtual environment, you must use the following command:

`source env/bin/activate`

This command will activate the virtual environment, allowing you to work with the correct dependencies in place. <br> Once
you have finished working on the project, it is important to deactivate the virtual environment. This will help prevent
conflicts with other projects that you may be working on.

To deactivate the virtual environment, simply enter the following command:

`deactivate`

By using a virtual environment, we can ensure consistency across all project contributors, making it easier to
collaborate and share code. <br> Please make sure to activate and deactivate the virtual environment as needed to ensure a
smooth development experience.

### Installing dependencies

Now that we know how to activate and deactivate the virtual environment, we can install the Python dependencies.

First, activate the virtual environment using the command shown earlier. <br> Then, type the following command in your
terminal:

`pip install -r requirements.txt`

### update dependencies

If necessary, new dependencies can be added to the requirements.txt file using the command:

`pip freeze > requirements.txt`

This will add new dependencies and update existing ones if necessary.
### Note: Make sure to execute this command while inside the virtual environment (venv).

### login details for admin page

**email:** lesBoss@django.com

**username:** lesBoss

**password:** popcorn06