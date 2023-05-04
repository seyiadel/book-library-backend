# Book-library-backend
This API(Application Programming Interface) allows books and files in pdf format to be stored and accessed by authenticated users

<p>- Snapshot of Swagger Documentation <p/>

![Screenshot (234)](https://user-images.githubusercontent.com/95058684/235906639-92111fd8-f0aa-4255-bef6-2ed3707db118.png)

### Endpoints
 * GET `/books/`- Get all books added
 * GET `/book/{id}`- Get books added by id
 * POST `/book/`- Add new book
 * POST `/login/` - Logs in signed up user
 * POST `/logout/` - Deletes token in session of an authenticated user
 * POST `/logout-all/` - Deletes all tokens from previous sessions for an authenticated user
 * POST `/signup/` - Register user to database

### Run on your local machine
Open up your terminal, follow these steps below:
```
git clone https://github.com/seyiadel/book-library-backend.git
```
Change the directory to book-library-backend
```
cd book-library-backend
```
Install the dependecies from requirements.txt
```
pip install -r requirements.txt 
```
Run the development server 
```
python manage.py runserver
```

Voila!, You have the project running on your local machine, Check and test the documentation
```
127.0.0.1:8000/docs/
```
<sub> where `:8000` is your port number!<sub/>
