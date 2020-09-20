### Installation
- If it's not already on your PC or Mac, install python3.6 and pip (pip should come with it) \* Note: Python 3.7.x is not yet supported

- Create a virtual environment with python 3.6 and activate it:
  - Using virtualenv
    - run `pip install virtualenv`
    - run `virtualenv -p python3 venv`
  - Using venv
    - run `python3 -m venv venv`
  - run `source ./venv/bin/activate` in the same location as the above command

The following should happen in a terminal with `venv` activated (often this means you can see the `venv` name in the beginning of the terminal prompt):

- run `pip install -r requirements.txt` (make sure you're on the root folder of the repo where requirement.txt is)

- run `python manage.py migrate`

- run `python manage.py populate_db` to populate your db with seed data.

- run `python manage.py createsuperuser` to create an account for the admin.

- run `python manage.py runserver`.
  This should start up the server and show output about which IP/Port it's running on (usually 127.0.0.1:8000)
  You can view the admin dashboard here: `127.0.0.1:8000/admin`

- Open a browser on 127.0.0.1:8000 or localhost:8000 as the URL (or whatever URL the previous command displayed)


#### React App
In your terminal, navigate to the `react-app` directory and run the follow commands:
- Using NPM:
  - `npm install`
  - `npm run build`
  - `npm run start`

- Using Yarn
  - `yarn install`
  - `yarn build`
  - `yarn start`

Reload the page at `127.0.0.1:8000`, you should see the seed data showing.

If you run into any issues, check `react-app/readme.md` which provides more details about the react app installation.

### Quick start
Backend
- `account/views.py` - create new API endpoints handlers (code blocks) here.
- `account/models.py` - define behaviors or update data fields here. Read more [here](https://docs.djangoproject.com/en/3.1/topics/db/models/)
- `main-project/urls.py` - add new API endpoint URL here.
- `init_data` - this is where you'd find the seed data.

Frontend
- Check `react-app/src/App.js` to get started with the frontend code. 
- Be sure to always run `npm run build` or `yarn build` every time you make changes to the react app codebase. 

### API endpoints

| Route | Description |
| ------ | ------ |
| 127.0.0.1:8000/api/accounts/ | Get all accounts |


### Assignment
