# YumBook !
## Recipe Book Django Application

## Table of Contents
- [About YumBook (The Recipe Book)](#about-yumbook-the-recipe-book)
- [Features](#features)
- [Getting Started](#getting-started)
- [About The Makefile](#about-the-makefile)

## About YumBook (The Recipe Book)
This is a simple Django application for storing and viewing recipes. The app features a homepage displaying the latest recipes, pages for browsing recipes by rating or category, and detailed recipe pages with ingredients and preparation steps. Only admin users can add, edit, or delete recipes. Clicking on a recipe opens a detailed view, showing the recipe name, image, ingredients, and preparation steps. The app does not come pre-loaded with recipes; instead, it is designed for you to add your own recipes and manage them on your local server.


## Features

- **YumBook - Home Page:** Links to the homepage. The home page displays the 3 most recently added recipes and bellow the 3 top-rated recipes.
- **All Recipes Page:** Displays all recipes sorted by rating.
- **Categories DropDown Menu:** A dropdown menu with cuisine types (e.g., Italian, Russian, Asian, Vegan). Selecting a category shows only recipes of that type.
- **Django Admin Page** to manage (add/edit/delete) recipes. The app dynamically displays updated content. Once a recipe is added, edited, or deleted in the database, the change will automatically reflect in the app without the need to modify HTML manually.


## Getting Started

### Prerequisites
Make sure you have Python 3 and pip installed on your system.

### Set Up the Aplication 
You can run the application in two ways, depending on your environment and needs:
**Option 1**: Run Locally (for development)
This is best if you're testing, developing, or making changes locally.<br>
**Option 2**: Run in Kubernetes Cluster.
If you want to deploy and run the app in a cluster using Argo CD and Helm, follow the instructions [Here](argocd/README.md).

### Here is the instruction on how to run application locally
1. Clone the repository and navigate to the project folder: <br>
```
git clone https://github.com/milangrahovac/yum_book.git
```

2. Navigate to yum_book folder and then set up a virtual environment. 
- Create the virtual environment: <br>
```
python3 -m venv venv
```
- Activate the Virtual Environment: <br>
```
source venv/bin/activate
```

3. Install dependencies: <br>
```
make requirements
```

4. Set Up the Database: <br>
- To store application data, you need to create a SQLite database file ***db.sqlite3*** in the root folder as its database and create the database shema. This command also creates admin user. You only need to run this once, when setting up the project for the first time.<br>
```
make db
```

5. Run the development server:<br>
```
make run
```


6. Open ```http://127.0.0.1:8000``` in your browser to start exploring the app.

## How to manage recepies

Only admin users can add, edit, or delete recipes. Follow these steps:

1. Log in as Admin. Run the YumBook app and go to the Django admin page: <br>
```http://127.0.0.1:8000/admin```

2. Log in with admin credentials.
- username: ***admin***
- password: ***yumpass***
3. Use the Django admin interface to manage (add/edit/delete) recipes.


## About The Makefile
Below are the available targets along with their descriptions and usage.

### Available targets
- ```make help``` - Lists all available targets in the Makefile along with short descriptions for each one. Run this command to get an overview of what you can do with the Makefile.
- ```make run``` - Stops the server on port 8000 if it's running and then starts the Django development server on port 8000. Run this command to ensure that you are starting the server fresh without any prior instances running. 
- ```make stop``` - Stops the Django development server if it’s currently running on port 8000. 
- ```make requirements``` - Installs the Python packages listed in requirements.txt. Run this command to ensure your environment has all the necessary dependencies installed. 
- ```make db``` - Applies database migrations to ensure the database schema is up-to-date with the Django models. Use this command whenever you have made changes to your models and need to update the database schema accordingly. It also creates an admin user if missing.
- ```make test``` - Run tests.

Once you have cloned the repository, installed the virtual environment, set up the database, and created a superuser with all the steps from the "Getting Started" section, you can easily run and stop the application using the Makefile.

### Using Makefile
Once you have cloned the repository, installed the virtual environment, set up the database, and created a superuser with all the steps from the [Getting Started](#getting-started) section, you can easily run and stop the application using the Makefile. 
1. Navigate to yum_book folder then Activate the virtual environment: <br>
```
source venv/bin/activate
```
2. Run the application: <br>
```
make run
```
3. Stop the aplication: <br>
```
make stop
```
