# gradiv
An open source API and interface that presents information about Graduate Programs

Choosing the right graduate programs to apply for isn’t easy when admissions data is murky, and is especially important given the cost and effort needed for every application. GradCafe is a great resource for admissions as is, enabling users to discuss admissions results and the application process; this project seeks to compile GradCafe data in slightly more accessible formats.

G - Graduate
A - Application
D - Data
I - Informatic
V - Visual

## Goals
Through the use of a visual medium, we hope to be able to present information scraped from GradCafe in a format that allows the user to easily access and visualize information about Graduate Admissions programs that might otherwise be hard to access and compare. Our primary goals are to:
 - Present data in a clean and sleek UI
 - Scrape and compile as much information as possible from various web-based sources

## Motivation

Being interested in Grad programs ourselves, we were presented with the challenge of trying to compare programs and our likely success rates with our applications. Though rankings and other such metrics exist, it was hard to find a single portal where we could access and compare information about Graduate programs that wasn’t otherwise locked behind a paywall or was spread out over an interface that was clunky and not user friendly. Being Engineers, and noticing this problem, we took it upon ourselves to come up with a solution that could not only help us, but can serve as a useful tool for all of our peers and those who come after us, as applying for higher education is a step and a decision that we would like to make armed with as much information as possible. 

## Requirements

To run the web scraping scripts, you'll need Python 2 and the following libraries:
- requests
- BeautifulSoup

To get these libraries, install pip, then run
```
pip install [library_name]
```

Coming soon will be a Dockerfile with all dependencies installed.

## Requirements for MongoDB Integration

Step 1: install MongoDB Community edition. I followed the steps here for version 4.2 using Homebrew on Mac (https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/).

Step 2: after following the installation + running steps, enter
```
mongo
```

to enter the Mongo shell. To create the same database/collection/data I'm currently using in the setup, do the following in the Mongo shell:
```
use bestdb
db.testCol.insert({"hello":"world"})
```
A database named bestdb with collection testCol should now have one entry.

Step 3:
In the virtual environment:
```
pip install Flask-PyMongo
```
Then boot up the server using flask run as you normally would. If this works, then on the "Hello World" page you will also see the following:
```
{'_id': ObjectId('5d55f92b702a9d1a0d00f55f'), 'hello': 'world'}
```
