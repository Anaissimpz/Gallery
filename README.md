# Gallery

### By **Anais Simpenzwe**

## Description
The Gallery app is a simple photo gallery web application to showcase beautiful pictures and designs. Users get to view photos updated by the site admin. Users can see photos based on the location, by clicking on the listed locations in the menu. The search functionality will search photos based on the categories.

# BDD
### User
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| View photo of interest	| Click on the photo of interest| Displays the photo in a modal with the name, description and where it was taken|
| Search category | Enter the category in the search input | Shows all the photos in that category|
| View photo based on location | Click on the locations in the Menu | Displays all photos taken in that location |

# Setup and Installation

### Prerequisites

1. Ubuntu Software
2. Python3.6
3. Postgres
4. python virtual env

### Clone the Repo
 Run the following command on the terminal: git clone https://github.com/Anaissimpz/Gallery && cd Gallery

### Activate Virtual Environment

 Activate virtual environment using python3.6 as default handler:

 virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate

### Install dependancies

Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

### Create the Database

psql
CREATE DATABASE gallery;

### .env file

Create .env file and paste paste the following filling where appropriate:

SECRET_KEY = '<Secret_key>'
DBNAME = 'gallery'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

### Run initiall migrations

python3.6 manage.py makemigrations album
python3.6 manage.py migrate

### Run the app

python3.6 manage.py runserver

Open terminal on localhost:8000

### Technologies Used
- Python 3.6
- HTML
- Bootstrap 4
- JavaScript
- Heroku
- Postgresql
## Support and Contact Details
 * Email:anaissimpenzwe@gmail.com
 * Phone number: 0783711066
 
 ## License 
 Copyright (c) Anais Simpenzwe