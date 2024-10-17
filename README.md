# Contacts Manager

Contacts Manager is a Python package that allows you to manage a list of contacts. You can add, remove, retrieve, and save contacts, as well as schedule and send messages with built-in error handling and logging for robust usage.
Features

Add Contacts: Add a contact with details such as name, contact info, preferred time, and a boolean value to indicate if the message is to tell what day it is.
Remove Contacts: Remove a contact by providing their contact info.
Retrieve Contacts: Get a list of all stored contacts.
Save Contacts: Save the contacts list to a CSV file, ensuring that the data is preserved.
Logging: The package provides detailed logging of messages and errors for tracking purposes.
Message Generation: Generate personalized messages based on user input.
Message Scheduling: Schedule messages to be sent at a preferred time.
Message Sending: Send messages to contacts.

## Installation
Clone the repository:

    git clone https://github.com/flangsem/morning_greetings


Navigate to the directory:

    cd contacts-manager


Install dependencies:

    pip install -r requirements.txt
    
## Package structure
```
morning_greetings/
│
├── setup.py                    # Installation script
├── README.md                   # Documentation for the package
├── requirements.txt            # Reqired external libraries
├── LICENSE
   morning_greetings/
   │
   ├── __init__.py              # Marks the directory as a package
   ├── contacts.py              # Manage contacts list
   ├── logger.py                # Log errors and simulated messages
   ├── main.py                  # Main script to run task
   ├── message_generator.py     # Generate messages
   ├── message_sender.py        # Simulate sending messages
       data/
      │
      ├── contact_list.csv         # Log file for contacts
      logs/
      │
      ├── error_log.txt            # Log file for messages sent
      ├── message_log.txt          # Log file for sent messages
```

## Usage
Once everything is installed you have 3 options

1. Run automated script
Run the script
     ```bash
    python -m morning_greetings.main
     ```
This will run the script with the contacts saved in morning_greetings/data/contactlist.csv

2. Add contacts in morning_greetings/data/contactlist.csv:

    Add a contact direcly into the csv file like this:
   
    ```bash
    Anna,exampleemail@example.com,09:00,False
   ```
    This will result in a message being sent(simulated), to exampleemail@example.com at 09:00.
    The format for adding time is 24:00.
    Change "False" to "True" if you want the message to include what day it is.

    then run the script
    ```bash
   python -m morning_greetings.main
   ```

3. Add contacts in main

    In main.py, add a contact like this:
    ```bash
    add_a_contact("Peter","petersMail@mail.ex", "07:30", True)
    ```
    above start()
    The format for adding time is 24:00.
    Change "True" to "False" if you dont want the message to include what day it is.
    Then run the script
    ```bash
    python -m morning_greetings.main
    ```

If you dont want to wait until 07:30 to see the message meing sent(simulated)

## Logging

The logger.py module is used to log messages and errors:

Message Logs: Logs are saved in logs/message_log.txt.
Error Logs: Errors are logged in logs/error_log.txt.

## Dependencies

Ensure the following packages are installed:

    pandas
    schedule
    csv (standard Python library)
    datetime (standard Python library)
    logger (custom logging module)


## License

This project is licensed under the MIT License.
Author

    Fredrik Andersen Langsem
