Getting started with slackbot

Step 1:
From the terminal (make sure you are in gyanbaba_app folder path) execute the following command

- source app_env/bin/activate

Then from terminal run:
pip install -r requirements.txt

    .flaskenv in your folder file will take care of the environment variables related to this command.

Step 2:
Slack app already created:
Please set the following environment variables. These variables are availabe from app's basic information and Oauth permissions tab.

```
$ export SLACK_BOT_TOKEN='xoxb-XXXXXXXXXXXX-xxxxxxxxxxxx-XXXXXXXXXXXXXXXXXXXXXXXX'
```

```
$ export SLACK_SIGNING_SECRET='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```

    Slack app not created:
        "https://api.slack.com/apps" - Please use this link to create a slack app. Once you receive the required variables, then you can start with above mentioned step,

Step 3:
From your terminal please execute the following command
flask run

    Now you have your server up and running. Please note down your port number. We will need it in a while

        E.g. "http://127.0.0.1:5000/" - Port number of this server address is 5000

Step 4:
While your server is running, please open a new terminal. Make sure you are in the gyanbaba_app folder path. Execute the following command with your port number

        $ ./ngrok http YOUR PORT NUMBER

    Now you can see ngrok serving its purpose. From the ngrok session status, we need the first forwarding url. This is the public url that help us to connect our local server to the internet

Step 5:
Now we should start subscribing for events in your slack app.

        1. Go to event subscriptions tab in your slack app webpage.

        2. Enable the events using the toggle button.

        3. Make sure ngrok and your server is running.

        4. Now we need to verify the request url. This is the combination of the forwarding url + '/slack/events/
            E.g ' http://1c8700530467.ngrok.io/slack/events'

            Note: Whenever you close the ngrok and start a new one, you get a new public url. When this happens we need to verify the request url once again.

        5. On pasting the url, you should get a verfied tick as long as the server is running.

        6. Once the verification is done, in the bottom of the page, please subscribe to the following events
            message.channels, pin_added, reaction_added, team_join

    In OAuth & Permissions:
        In Bot Token Scopes add:
            -channels:history
            -chat:write
            -im:write
            -pins:read
            -reactions:read
            -users:read

Step 6:
Now you can start using the app from the respective workspace.

    In which ever channel you have added the app, go to that particular channel and send the following message
        "start"
