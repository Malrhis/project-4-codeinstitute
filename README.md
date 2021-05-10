# Pampas Collective SG's Store

# <img style="height:150px" src="static/images/pampas-collective-logo.jpeg"> Aquarist's Resource (Freshwater Ver.)

# 1. Background & Objective
## Background / Problem Statement
-

## Objective
-


## Purpose and Value to users

1. 

<br>

# 2. Demo (Heroku)
Site is published via Heroku and can be viewed [here]()

<br>

# 3. Technologies Used
- HTML 
- CSS
- Bootstrap 4
- Django
- Django All Auth
- Django Cripsy Forms plugin
- Javascript
- [Toastr](https://github.com/CodeSeven/toastr) (JS notifications)
- Stripe (for Handling Checkout)
- [UploadCare](https://uploadcare.com/) (for image upload and cloud storage) 

## 3.1 Dependencies installed with pip (python's package manager)
- django
- django-allauth
- django-crispy-forms
- pyuploadcare
- python-dotenv
- stripe
- dj_database_url

## 3.1.1 For deployment to Heroku
- pip3 install gunicorn
- pip3 install psycopg2
- pip3 install Pillow
- pip3 install whitenoise 

## 3.2 Python Libraries used
```
from flask import Flask, render_template, request, redirect, url_for
```

<br>

# 4. The Goals: User Stories or (JTBD) Jobs-to-be-Done

The store administrator/owner is currently selling via South East Asia's largest e-commerce platform [Link to Shopee.sg store](https://shopee.sg/melodyamanda7?categoryId=11&itemId=3760378194)

For the small time e-commerce business store owner selling pampasgrass:

```
1. I want to...
```
<br>

# 5. Key Features
- 

## 5.1 Feature List
|# | Name          | Description   |     
| -| ------------- |-------------|
|1 |  || 

<br>

# 6. Database Design
insert here

## 6.1 Entity Relationship Diagram AKA ER Diagram
insert here

## 6.1 Logical Schema Diagram
insert here



# 6. Prototyping
Simple Prototyping was done directly using MS Powerpoint to mock-up the features of the website.

## 6.1 Front-End UI Mock-up
<img style="height:400px" src="" >

Reference was taken from
- insert sites which were used for inspiration

## 6.2 Actual Final Design
The final design aims to provide a solution to all user stories listed in `section 4 The Goals: User Stories or (JTBD) Jobs-to-be-Done` 

### 6.2.1 Search Section
<img style="height:300px" src="" >

```
1. Insert which user story was fulfilled by this feature
```

## 6.3 Colour
#
```
Color schemes if any
```
<br>

# 7. Detailed Features Write-up
## 7.1 Search Bar
- how as each implemented?

## 7.1.1 Search Bar Validation
- simple if function to prevent empty string from being processed


# 8. External Frameworks
## 8.1 Boostrap 4 Implemetation
- Bootstrap 4 was used for re-building the website in a responsive, mobile-first manner. You can access Boostrap 4 resouces [here](https://getbootstrap.com/docs/4.5/getting-started/introduction/)

The below `code snippets` were added to the HTML in `base.template.html` to invoke the boostrap framework
```
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">

<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>

<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>

<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
```

## 8.2 Toastr Implemetation
- insert information here

<br>

# 9. Environment setup

## 9.1
The following were used in the .env file
```
MONGO_URI
SECRET_KEY
```

MONGO_URI is to enable connection to mongoDB
SECRET_KEY is used to enable `flash` messages

# 10. Content Credits
## Pamspas Product 
- Insert here

## Images
- Credited to my deal wife melody amanda, and her furious photoshoots of her products in the basement of our marital home.
- Insert here


<br>

# 11. Non-relational Data Model Design of Fish and Plants Collection
Fish and plants collections are stored in mongoDB. Each document will essentially carry all the information required so that front end can render a card for each plant or fish

## 11.1 Relational database design philosophy:
1. Should encompass enough information about each fish and plant to allow users to find the information useful for their hobby
2. Front-end should display each document of fish or plant as a card
3. Card should have images
4. Images can be provided and stored as a string of text which in turn can be used as HTML `href`
5. Field related to numerical values has to have validation and checks: for instance: `Water's pH` cannot be negative: it has to be a `float` that is postiive
6. Field with restricted options should be restricted on the front end and stored as sting in the backend.
7. Determining of whether information is sufficient or not will draw on my personal knowledge of fish-keeping and aquascaping.


## 11.2 Input types for html
- Chosen based on logicality of the value required to be stored.
    - for instance: `Water's pH` cannot be negative: it has to be a `float` that is postiive
- If only a few options are available, fix the options via `dropdown` `select`
    - Diet: Carnivore, Herbivore, Omnivore

## 11.3 Importance of water parameters as data points
- the crux of all aquarium keeping is the water quality. 
- hence each card should have a separate section specially for water quality
```
water_temp_in_degc:"25.0"
pH:"6.0"
```

## 11.4 Importance of anecdotal evidence stored as string/text
```
tank_setup_text:"Can be maintained in a fully-decorated aquarium although many breeders..."
```
Much of the key information about fish-keeping and plant keeping is rooted in word of mouth. One of the key-value pairs has to be dedicated to allowing users to add as much text as possible to guide others to successful fish-keeping

<br>

# 12. Testing
## 12.1 Code Validation using Code Validators
- `style.css` was validated using the W3C Jigsaw validator ([Link](https://jigsaw.w3.org/css-validator/validator))
  - No issues were found with `style.css`
  
- all `.html` files in `templates` was validated using the W3 Nu HTML Validator ([Link](https://validator.w3.org/nu/#file))

## 12.2 PEP8 Style guide for Python
All code in `app.py` complies with `PEP8` [Style guide](https://www.python.org/dev/peps/pep-0008/) 

This is ensured by making sure no callouts from gitpod python linter are present in `app.py` and that no lines of code in `app.py` exceed 79 Characters

## 12.2 Testing and Bug Fixes (Test Case Table)

| # |Type| Test       | Result           | Fix/Expected Result  |
|-- |--|------------- |:-------------:| -----:|
|1  |Functionality| Search bar is supposed to display fish based on string entered | Displayed list fish that match the string | All OK |
|2  |Usability| Enter random string of text which doesn't match into search bar | returns no fish/plants | All OK |
|3  |Functionality| Display of all fields from mongo onto card in `show_all_fish` and `show_all_plants` | Show all fields from mongoDB in front end | Did not return `diet` element in `fish` template. was found that a wrong parameter was used (`plant` was used instead of `fish` and since plants don't have diets, front end was not displaying properly)
|5  |Functionality| Validation of empty input for `create` & `update` | flash message to alert user that input during `create` and `update` cannot be empty | All OK
|6  |Functionality| When error values are entered in `update`, supposed to merge `old values` and `error values` + display `flash` message so user knows which error occurred during validation and can edit their error | Only `old values` were showing | typo in `old values` and `error values` syntax. Was fixed quickly and now All OK
|7  |Usability| Page buttons should only show `next page` in the first to 2nd last page. should not show in last page. `Previous page` should only show in 2nd to last page | Button order did not work properly, and `next page` was shown in the last page even though there are no more documents to be displayed | created new variable to store `last_page` value. If `page != last page` then display `next button`. All OK now
|8  |Usability| style.css colour should be turquoise as that is the theme for the website | was stuck in black colour | Attempted to fix by moving file tree for `static`. Was found that `style.css` was being overwritted by the bootstrap class `navbar-dark`. Removed the class and the static file was synching |
|9  |Usability| favicon should be displayed | favicon could not be displayed | Attempted bugfix using different `url for` syntax. Was fixed by clearing cache using `ctrl + f5` |
|10 |Functionality| Delete document  | Document should be gone from fish/plant collection in mongo and on refresh, should not show in `show_all_fish` / `show_all_plants` | All Ok|
|11 |Functionality| url routing using `url_for` | navigate all links on navbar and site to ensure navigation are not broken | Navigation All Ok |
|12 |Responsiveness| Test screen size | Tested using Firefox to mock iPhone X, Samsung S9| Was found that cards were not `fluid` type. changed all cards to `fluid` so that they look better on mobile |
|13 |Functionality & Responsiveness| Deployment test to heroku | clicked on heroku link in mobile phone and tested if pages were working correctly and responsively | All Ok |
|14 |Usability| Browser Tab name should be correct | Found that browser tab name for plants create form was still named as fish create form | Changed  Jinja2 block and now All OK|
|15 |Usability| Could not click button to go back from create fish and create plant form | No back button | Added back button in create fish template |

<br>

# 14. Deployment

# 14.0 set `debug=False`!!! since we are going into production and no longer in development

## 14.1 Preparation
Before the site goes `live` the following elements are checked gitpod's native browser preview via open port `8000`. This is done by executing command in terminal `python3 app.py` to run the `flask app` in `app.py`
- Fulfillment of Learning objectives from 'Code Insitutes' Assessment Handbook`
- Check all code linters and validators are clear
- Check that all images src are not broken
- Test viewport dynamic resizing for android (Samsung S9) and iOS (iPhone X/XS)
- Check Create, Read, Display, Update, Delete functions from Fish to Plant
- Ensure all elements of the fish or plant are displayed, including images rendered from `picture html url string` key-value pair stored in mongoDB document
- Check navbar functionality and responsiveness
- Check pagination is working for `show_all_fish` and `show_all_plants`

## 14.2 Deployment Steps to Github
Deployment was done via github pages.

After ensuring that final commit and push via Visual Studio Code was done

1. Check if the contents have been successfully pushed to repository at https://github.com/Malrhis/project3

## 14.3 Deployment to Heroku
1. Login to `heroku` on terminal using `heroku login -i`
2. Check `remotes` using `git remote -v`
3. Ensure that `requirements.txt` is updated correctly
4. perform `git push heroku master`
5. Setup environment variables in heroku as follows
```
heroku config:set MONGO_URI= XXX
```
6. Check that environment variables can be seen in heroku app settings under `config vars`
5. Verify that site has been published to Heroku dashboard in Heroku ([Link](https://dashboard.heroku.com/apps/aquarist-resource))
7. Click on [Published URL](https://aquarist-resource.herokuapp.com/)
8. perform another round of validation based on `#14.1 Preparation` but this time in `heroku` instead of `gitpod browser preview`

## 14.3 Production
In the event that `#14.1`, `#14.2` & `#14.3`  are cleared, the site can then be considered to be in production. 
If not, repeat to ensure that deploying of code is error free and is working in `Github repo` and `heroku`.

<br>

# 15. Acknowledgements
- Mr Malcolm Yam - Bootrap instructor
- Mr Arif Rawi - HTML and CSS instructor
- Mr Paul Kunxin Chor - Who guided us on python, Jinja2, flask, mongo, pymongo
- Mr Ace Liang - Teaching assistant, who supported this project by holding consultation sessions.
- Ms Melody Amanda - Wife, content provider, entrepreneur