# gradiv
An open source API and interface that presents information about Graduate Programs

Choosing the right graduate programs to apply for isn’t easy when admissions data is murky, and is especially important given the cost and effort needed for every application. GradCafe is a great resource for admissions as is, enabling users to discuss admissions results and the application process; this project seeks to compile GradCafe data in slightly more accessible formats.

G - Graduate
A - Application
D - Data
I - Informatic
V - Visual

Goals:
Through the use of a visual medium, we hope to be able to present information scraped from GradCafe in a format that allows the user to easily access and visualize information about Graduate Admissions programs that might otherwise be hard to access and compare. 
Present data in a clean and sleek UI
Scrape as much data as possible from Grad Cafe

Motivation:
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