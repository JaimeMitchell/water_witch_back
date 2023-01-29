This scaffold includes the following:

## `app/__init__.py`

This file configures the app. It's where:

We expect developers to modify this file by:

- Replacing the database connection string
- Importing all models
- Registering all blueprints

Note that `create_app` also uses CORS. There is no extra action needed to be done with CORS.

## `app/routes.py`

We expect endpoints to be defined here.

The file already imports:

- `Blueprint`
- `request`
- `jsonify`
- `make_response`
- `db`

Feel free to alter these import statements.

This file also has a comment to define a Blueprint. Feel free to delete it.

## `app/models` Directory

This project already includes `app/models/water.py` and `app/models/crowd.py`, to anticipate the models `Water` and `Crowd`.

Both files already import `db`, for convenience!

## `requirements.txt`

This file lists the dependencies we anticipate are needed for the project.

## `Procfile`

This file already has the contents needed for a Heroku deployment.

If the `create_app` function in `app/__init__.py` is renamed or moved, the contents of this file need to change. Otherwise, we don't anticipate this file to change.
0 comments on commit 1d325a8
@JaimeMitchell

Add heading textAdd bold text, <Cmd+b>Add italic text, <Cmd+i>
Add a quote, <Cmd+Shift+.>Add code, <Cmd+e>Add a link, <Cmd+k>
Add a bulleted list, <Cmd+Shift+8>Add a numbered list, <Cmd+Shift+7>Add a task list, <Cmd+Shift+l>
Directly mention a user or team
Reference an issue, pull request, or discussion
Add saved reply
Leave a comment
No file chosen
Attach files by dragging & dropping, selecting or pasting them.
Styling with Markdown is supported
You’re not receiving notifications from this thread.
