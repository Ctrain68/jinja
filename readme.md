Templating introduction - `https://www.youtube.com/watch?v=bxhXQG1qJPM&ab_channel=Mr.Rigden`
Flask-Jinja - `https://www.youtube.com/watch?v=QnDWIZuWYW0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=2&ab_channel=CoreySchafer`
Jinja cheat sheet - `https://dev.to/sm0ke/jinja-template-cheat-sheet-and-free-sample-28kh`

# Lets do this thing

Clone this repo: https://github.com/CoderAcademyEdu/ccc-03-16

First we need to setup our DB. Becasue I have the maturity of a 13 year old boy we will be using the below example.
Feel free to copy paste the commands below to get your DB up and running.

| Setting up the DB            | command                                                                          |
| ---------------------------- | -------------------------------------------------------------------------------- |
| Change user to postgres user | `psql postgres`                                                                  |
| Create the banazon db        | `CREATE DATABASE bamazon;`                                                       |
| Create the beff_heyzos user  | `CREATE USER beff_heyzos;`                                                       |
| Give beff_heyzos all access  | `grant all privileges on database bamazon to beff_heyzos;`                       |
| Give beff a password         | `ALTER USER beff_heyzos WITH ENCRYPTED PASSWORD 'taxisforsuckers'`               |
| Add this DB URI to .env      | `"postgresql+psycopg2://beff_heyzos:{'taxisforsuckers'}@localhost:5432/bamazon"` |
| Add dummy data for the rest  | `🦆`                                                                             |

Secondly we need to get our app running.
Copy paste the commands and we should have Bamazon up and running.

| Getting the app up and running          | command                            |
| --------------------------------------- | ---------------------------------- |
| Create your venv                        | `python3 -m venv venv`             |
| Activate the venv                       | `source venv/bin/activate`         |
| Install the requirements                | `pip3 install -r requirements.txt` |
| Set the app to main.py                  | `export FLASK_APP=main.py`         |
| Set the environment to development mode | `export FLASK_ENV=development`     |
| Make sure the .env has dummy data       | anything                           |
| Upgrade the db with the migrations      | `flask db upgrade`                 |
| Seed the DB                             | `flask db-custom seed`             |
| Run the app                             | `flask Run`                        |
| Check the index, go to this url ->      | `http://127.0.0.1:5000/books/`     |

1. Create a directory called templates on the same level as main.py
2. Add a html file inside templates called layout.html

Add the following code to it.
This is the html file that our template will be inheriting from.

```
<!doctype html>
<html>
    <head>
        <title> Bamazon </title>
    </head>

    <body>
    {% block content %}

    {% endblock %}
    </body>
</html>
```

3. Add a html file inside templates called books.html

add the following code to it.

```
{% extends "layout.html" %}

{% block content %}
    {% for book in books %}
        <div> {{book.title}} </div>
    {% endfor %}
{% endblock %}
```

6. Open our books controller

Include the import for render_template in the flask import so it looks like this `from flask import Blueprint, request, jsonify, abort, render_template`.

We will comment out the line that says `return jsonify(books_schema.dump(books))`.
and add in the line that says `return render_template("books_index.html", books=books)`

This simple change to the return statement now means that this controller will now respond to the request with a template of HTML instead of JSON.

```
@books.route("/", methods=["GET"])
def book_index():
    # Retrieve all books
    books = Book.query.options(joinedload("user")).all()
    # return jsonify(books_schema.dump(books))
    return render_template("books_index.html", books=books)
```

7. Lets take a look at the books controller and see what it looks like.

![]()

8. Lets add some styling to it so it looks a bit better.

Go to https://getbootstrap.com/docs/4.3/getting-started/introduction/ and have a look at the starter template. We will be extracting the links to the CSS and the JS and adding it to our app. We want all our pages to get access to this so we will add it to our layout template.

The layout template should look like this. We have added a container class to demosstrate how quick and easy it is to get something up and running with bootstrap.

```
<!doctype html>
<html>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <head>
        <title> Bamazon </title>
    </head>

    <body>
        <div class="container">
        {% block content %}

        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
        </div>
        {% endblock %}
    </body>
</html>

```

9. One last quick demo of templating and boostrap.

We will add a nav bar from these demos. `https://getbootstrap.com/docs/4.3/components/navbar/`
Your layout template should now look like this.

```
<!doctype html>
<html>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <head>
        <title> Bamazon </title>
    </head>

    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">Navbar</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Link</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Dropdown
              </a>
              <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                <a class="dropdown-item" href="#">Action</a>
                <a class="dropdown-item" href="#">Another action</a>
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" href="#">Something else here</a>
              </div>
            </li>
            <li class="nav-item">
              <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
            </li>
          </ul>
          <form class="form-inline my-2 my-lg-0">
            <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
          </form>
        </div>
      </nav>


    <body>
        <div class="container">
        {% block content %}

        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
        {% endblock %}
        </div>
    </body>
</html>

```

10. Okay so now that we have the layout sorted we can add some styling to our books.

Have a look at these different cards. You can choose which ever one you want but I would suggest a simple one

```

{% extends "layout.html" %}

{% block content %}
    {% for book in books %}
    <div class="col px-md-5"><div class="p-3 border bg-light">
                <div class="card" >
                    <div class="card-body">
                        <h5 class="card-title">{{book.title}}</h5>
                        <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                        <a href="#" class="card-link">Card link</a>
                        <a href="#" class="card-link">Another link</a>
                    </div>
                </div>
            </div>
    </div>
    {% endfor %}
{% endblock %}
```

#That is all you need to pass the front end criteria of this assessment.
