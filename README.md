# 	****JobSearchMonitoring****


> This App is a personal follow-up on your job research.
>
> Find a job on your favorites web pages, save it in your database and enjoy the clarity of the organization.
>
> Log in  into your personal account 
>
> create a category 
>
> create a job offer:
>
> - ***\*category (choose one of the category you created)\****
> - ***\*title (job offer name)\****
> - ***\*company_name\****
> - ***\*URL (link to the job offer from where you fin it (ex: linked-in, monster, indeed...))\****
> - ***\*date (auto implement at the creation)\**** 
> - ***\*salary (in Euro)\****
> - ***\*comments\**** 
> - ***\*upload a motivation letter\**** 
> - ***\*upload you CV\****
> - ***\*status (select one)\****
> - ***\*style (choose a style of job)\****
> - ***\*type (choose a type of job)\****

---------------------------------------------------------------------------------------------

[]()**RUN THE APP:**

`Installation required:`

- ```
  Install Virtual Environment : python -m pip install --user virtualenv
  ```

- ```
  pip install -r requirements.txt
  ```



`Installation database:`

- ```
  python manage.py makemigrations
  ```

- ```
  python manage.py migrate
  ```

- ```
  python manage.py create_db
  ```

  

`Launch:`

- ```
  env\Scripts\activate
  ```

- ```
  python manage.py runserver
  ```


----------------------------------------------------------------------------------------------

[]()**FEATURES:**

`Encoding:`

- Python 3

- HTML 5

- CSS

- Bootstrap 4

- Javascript (Jquery)

- Django 3

- AWS S3

- PostgreSQL

  

`Launched:`
Django 3



`Fork:`
https://github.com/MyBhive/JobSearchMonitoring.git

-----------------------------------------------------------------------------------------------

[]()**DESCRIPTION:**

`framework`

| Django 3 |      |
| -------- | ---- |
|          |      |

`Back-end files and folders`

| ROOT[]()            | --------------------------------------------------------------------- |
| ------------------- | ------------------------------------------------------------ |
| **requirement.txt** | File to install “requirement.txt                             |
|                     |                                                              |
|                     | **---------------------------------------------------------------------** |
| **dashboard**       | settings                                                     |
| **useraccount**     | account feature                                              |
| **jobsearch**       | products feature                                             |
| **static**          | CSS / Javascript/ asset-img                                  |
| **templates**       | html pages/userpages                                         |
| **manage.py**       | main file                                                    |

`Front-end files`

| **TEMPLATES FOLDER**[]() | --------------------------------------------------------------------- |
| ------------------------ | ------------------------------------------------------------ |
| **page**s                | templates of the products thema                              |
| **userpages**            | templates of the user acount thema                           |
| **STATIC FOLDER**[]()    | **---------------------------------------------------------------------** |
| **script.js**            | File containing all the Javascript coding                    |
| **style.css**            | File containing all the CSS coding                           |
| **asset/img**            | folder containing all the picture used on the homepage       |

`Text files`

| **Requirement.txt**      |      |
| ------------------------ | ---- |
| packages used to the app |      |

​	`Installation files`

| **.gitignore** | to filter what should be visible |
| -------------- | -------------------------------- |
| **Procfile**   | to connect with **heroku**       |
|                |                                  |

​	



----------------------------------------------------------------------------------------------

[]()**TO CONTRIBUTE:** 

> You need to respect PEP8 !!!  

- Fork it 

- Create your feature branch

- Commit your changes

- Push to your branch 

- Create a pull request

-----------------------------------------------------------------------------------------------

##### []()**WRITTEN BY:**

> MyBhive 

https://fast-jobresearch.herokuapp.com
