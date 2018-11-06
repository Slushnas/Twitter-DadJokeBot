# Twitter-DadJokeBot

This project is my solution to the first Serverless Framework 2018 #noServerNovember Intermediate/Advanced track (fun version) challenge.

To use:
1. Create or use an existing Twitter account and Twitter application and update your Twitter application keys in **_secrets.py_** 
2. Deploy this code to AWS Lambda with the Serverless Framework **`serverless deploy`** and it should post a random "Dad Joke" from the icanhazdadjoke.com website to the Twitter account specified every day. You can adjust the Tweet posting time in the **_serverless.yml_** file: `- schedule: cron(30 22 * * ? *)`
