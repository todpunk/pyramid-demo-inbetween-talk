### Behold, the demo! ###

This was written for and uploaded during the 2016 OpenWest talk "Pyramid: In Between Flask and Django"

The code is meant to be a demo of a simple end-to-end API for an sqlalchemy and cornice based workflow for a JSON API.  Obviously a lot of other things are possible with Pyramid and this is not meant in any way to be exhaustive in any approach.

To go through it you will need Cornice, SQLAlchemy, Pyramid (obviously), pyramid_debugtoolbar, and transaction (if others are required I'll try to update this, file an issue).  If you use postgres, psycopg2 is needed.  If you use sqlite, sqlite is needed.  These usually come with sqlalchemy.

To learn as we did in class (without this repo being uploaded), we did the following (no copying and pasting, type it out!)  You'll likely delete several files, that's ok.

```
# In the project base directory, with this file in it
pcreate -s alchemy -s cornice audience
cd audience
# Edit the development.ini file so the [app:main] section line is now: use = call:audience:main
# This will make it so you don't have to run setup.py, so don't do that, (or do that, it's your box, not mine, forge your path!)
# Keep in mind this will require the owdemo package to be on your python path (the owdemo/owdemo/ directory)
# Then edit the sqlalchemy.url to meet your database requirements

# If you use the InitializeDB script pyramid provides, more power to you, but I never do, so I don't know how.
# Instead, use the provided sql file, which I have only tested with postgres (change the options to your info, obviously)
psql.exe -f ../reinitdb.sql -h localhost -U dbuser -d demos

# You should have a db now.

pserve development.ini --reload

# Open an editor, start making the code be like you see it in the todref directory
# Start with views/__init__.py
# You may have to restart the 'pserve' line depending on your editor
```