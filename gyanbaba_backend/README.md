Getting started with slackbot

Step 1:
From the terminal (make sure you are in gyanbaba_app folder path) execute the following command
source app_env/bin/activate

Then from terminal run:
pip install -r requirements.txt

    .flaskenv in your folder file will take care of the environment variables related to this command.

Step 2:
Create a mysql database name bot_db
After this in instance/config.py

change: `SQL_ALCHEMY_DATABASE_URI='mysql+pymysql://<username>:<password>@localhost/bot_db`

Step 3:
In terminal run the following commands(make sure you are in the gyanbaba_backend route):

- export FLASK_APP=run.py
- flask db init
- flask db migrate
- flask db upgrade

Step 4:
From your terminal please execute the following command
flask run

    Now you have your server up and running. Please note down your port number. We will need it in a while

        E.g. "http://127.0.0.1:5000/" - Port number of this server address is 5000

Step 5:
While your server is running, please open a new terminal. Make sure you are in the gyanbaba_app folder path. Execute the following command with your port number

        $ ./ngrok http YOUR PORT NUMBER

    Now you can see ngrok serving its purpose. From the ngrok session status, we need the first forwarding url. This is the public url that help us to connect our local server to the internet
