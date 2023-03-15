# TelegramTool 

## Install dependencies

You'd need python3 and pip3 installed and available in your PATH.

Run `pip3 install telethon` from the projects root directory.

### Telegram Configuration

1. To run it you need to generate API credentials for your Telegram user, you can do it [here](https://my.telegram.org), and access your already created ones [here](https://my.telegram.org)
2. Replace your credentials in the script
    ```python
    id = 000000        # YOUR API_ID
    hash = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'        # YOUR API_HASH
    phone = '+34000000000'        # YOUR PHONE NUMBER, INCLUDING COUNTRY CODE
    ```

### Export users
Just follow the instructions in the script after running it from your the shell.

> No headers are expected in the CSV files

Once you have your CSV prepared, just follow the instructions in the script.

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
                                   STEP BY STEP PROCEDURE 
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-


# Telegram-Scraper & DM Sender


PROCEDURE:-


apt update && upgrade


pkg install python


pkg install python -y


pkg install git -y


pkg install -y git python


cd TeleAdder

ls


To Get the Group User Data

 python3 GetGroupUserData.py

( members.csv is default if you changed name use it )


Send Bulk Message To all the members in the CSV file

python3 SendMessageToAll.py members.csv