This scaffold includes the following:

## `app/__init__.py`

This file configures the app.

Note that `create_app` also uses CORS. There is no extra action needed to be done with CORS.

## `app/routes.py`

Endpoints to be defined here:
Create & Read: /fountains
Create, Read, Update, Delete: /fountains/<id>


## `app/models` Directory

This project includes `app/models/fountain.py`

File already import `db`, for convenience!

## `requirements.txt`

This file lists the dependencies needed for the project.

## `Procfile`

This file already has the contents needed for a Heroku deployment.

If the `create_app` function in `app/__init__.py` is renamed or moved, the contents of this file need to change. Otherwise, I don't anticipate this file to change.

@JaimeMitchell

