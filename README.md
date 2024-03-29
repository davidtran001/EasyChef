<h1 align="center">
  <strong>Easy Chef</strong>
</h1>

<p align="center">
  <img src="https://github.com/davidtran001/EasyChef/assets/46908974/9efe0eb8-d859-4925-b674-ff8aa7d6537f" width="50%" height="50%">
</p>

Easy Chef is a recipe sharing web application that allows users to create, view and share their recipes with each other. 

This application was built with Django REST framework and React.

## Backend Setup
Navigate to the directory:
```sh
cd EasyChef
```
Create an activate a virtual environment:
```sh
python3 -m venv .venv
source .venv/bin/activate
```
Install the required dependencies:
```sh
pip install -r requirements.txt
```
Navigate to backend directory:
```sh
cd Django-backend
```
Make migrations and migrate:
```sh
python3 manage.py makemgirations
python3 manage.py migrate
```
Launch backend server:
```sh
python3 manage.py runserver
```

## Frontend Setup
Navigate to the directory:
```sh
cd EasyChef
cd react-frontend
```
Install dependencies:
```sh
npm install
```
Launch frontend
```sh
npm start
```

## Features
### Home Page
![Screenshot 2023-12-17 at 5 00 28 PM](https://github.com/davidtran001/EasyChef/assets/46908974/aaba1038-c888-44d6-892f-ec4b16b4a1b0)
### Popular Recipes
![Screenshot 2023-12-17 at 5 02 00 PM](https://github.com/davidtran001/EasyChef/assets/46908974/db6cac1a-fc83-45a1-abe3-8ee2c22dd049)
### Recipe Filtering
![Screenshot 2023-12-17 at 5 02 33 PM](https://github.com/davidtran001/EasyChef/assets/46908974/9cd60be0-c2d6-40ff-899f-063e8e7b2370)
### Shopping List
![Screenshot 2023-12-17 at 5 04 56 PM](https://github.com/davidtran001/EasyChef/assets/46908974/6fee1636-8d6c-41ec-92b3-459383655366)
### Recipe Details
![Screenshot 2023-12-17 at 7 02 27 PM](https://github.com/davidtran001/EasyChef/assets/46908974/7ad83541-3481-48c3-aaeb-16f314cd1c5d)
### Create Recipes
![Screenshot 2023-12-17 at 7 02 43 PM](https://github.com/davidtran001/EasyChef/assets/46908974/e4a58e4b-2564-4d73-9398-e08c59e03b2b)

