# Overview
The math flashcards project provides a web page where users can review basic math facts. It is my first project written using Django, and I chose this project because a flashcard program is fairly straightforward. Thus, it gave me the opportunity to focus on understanding and implementing Django's unique project development style rather than getting bogged down in the details of any complex coding procedures or complicated database systems. 

This program can be run from VS Code onto a computer's localhost server by typing the 'python manage.py runserver' command in the terminal. The coomand will not work unless the virtual environment is active and the command is being run from the project's root directory.

Upon opening the program's home page, a menu is shown which provides the user with 5 options to practice either addition, subtraction, multiplication, division, or a random mix of all the operations. Once an option is clicked, the first flashcard out of 15 is shown for the user to enter their answer. Once an answer is submitted, the result will be shown along with an indication of whether the user's entered answer was correct. This process continues until the final card has been attempted by the user. Afterwards, it displays the total number of correct answers, and the user is able to navigate back to the main menu so they may choose a new operation to practice.

I chose a project that felt very complementary to Django's model-view-template design pattern, and I made a conscious effort to apply that design pattern to it. For instance, a flashcard program does not need a database to store its mathematical expressions, but I chose to implement one so my project could rely on interacting with a model in order to render data onto a template.


[Software Demo Video](https://youtu.be/xIeNJt9R9rg)

# Web Pages

{Describe each of the web pages you created and how the web app transitions between each of them.  Also describe what is dynamically created on each page.}

# Development Environment
This program was developed on VS Code using Python 3.9.4 and Django 4.2.6. 
A small amount of Bootstrap was also used.

Django is a Python web framework used to build web applications quickly with
its model-view-template (MVT) design pattern. It uses database models to
store/retrieve data, views to handle logic that ultimately determines the
content shown to viewers, and templates to design the actual web page layouts.

This program utilizes many of Django's built-in features, including its 
URL routing, object-relational mapping of databases, and re-use of code
using templates.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* ['Try Django 3.2' Youtube Playlist, by CodingEntreprenuers' ](https://www.youtube.com/watch?v=SlHBNXW1rTk&list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL)
* [Django Documentation](https://docs.djangoproject.com/en/4.2/)

# Future Work

* Allow user to select the amount of cards to be included in one practice round.
* Record the amount of time it takes for a user to complete one practice round.
* Create user accounts to track a user's progress.
* Create flashcard tables organized based on difficulty levels so user can 
  exclude flashcard sets that they've already mastered.
* Implement a point system to unlock higher flashcard difficulty levels.
* Let user explicitly include or exclude certain