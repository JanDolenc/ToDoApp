# ToDoApp by Jan

## Why did I make this app?
I wanted to improve my JavaScript knowledge by building a side project. I stumbled across a YouTube tutorial in which they build the UI - front-end for the to-do app. After I
finished building the UI following the tutorial the UI was looking interesting. My mentor saw the potential to level up this project by adding a back-end and this way get to 
know the concepts and tools used in back-end development.

## How did I improve this app?
* **I added a MySQL database.** In the tutorial the data - todo items were saved in the browser's local storage. I store data in the database.
* **I built REST API for querying and writing to the database.**  API was built using the FastAPI framework.
* **I containerized the app.** The app is running in Docker containers.

## How does it look like?
![image](https://user-images.githubusercontent.com/23385863/195825584-4ae8d6d8-eafd-4fef-b2f6-54b97f0b2c04.png)



## How do I want to improve the to-do app?
As you can see the app needs some more work. First off I want to address the most important problems:
* Install SSL certificate to ensure a secure connection
* Store passwords and sensitive information in ENV file and replace them in code with variables to follow best practices
* Fix the design on small screens
* Add support for multiple users
