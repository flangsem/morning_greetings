import sys
import os
import pandas as pd
import schedule
import time
import pkgutil

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import contacts
import message_generator
import message_sender

list_of_contacts_from_csv = pd.read_csv("morning_greetings/data/contact_list.csv")


list_of_contacts = contacts.Contacts()


def add_a_contact(name:str, contact_info: str,preferred_time: str, day:bool):
    """Adds a Contact"""
    list_of_contacts.add_contact(name, contact_info, preferred_time, day)
    contact_schedule(name, contact_info, preferred_time, day)

def remove_a_contact(contact_info:str):
    """Removes a contact based on the mailaddress"""
    list_of_contacts.remove_contact(contact_info)
    print(f"Contact with mail: {contact_info} is removed")
    endtask(contact_info)

def send_message_to_contact(name: str,contact_info:str, day:bool):
    """Generate and send a message to the contact"""
    message = message_generator.generate_message(name,day)
    message_sender.send_message(message, contact_info)


def contact_schedule(name: str,contact_info:str, preferred_time:str, day:bool):
    """Schedule when to send a message to the contact """
    jobtime = preferred_time
    schedule.every().day.at(jobtime,"Europe/Amsterdam").do(send_message_to_contact, name,contact_info,day ).tag(contact_info)


def endtask(contact_info:str):
    """Removes contact from message schedule"""
    schedule.clear(contact_info)

#Adds all contacts from file to the list
for index,row in list_of_contacts_from_csv.iterrows():
    add_a_contact(row["name"],row["mail"], row["preferred_time"], row["day"])

def start():
    firstime = True
    """Starts the prosess, will send messages when the given time comes around"""
    while True:
        if firstime== True:
            print("Schedule started")
            firstime = False
        schedule.run_pending()
        time.sleep(60)
        print("still running... press 'controll c' to stop program")

list_of_contacts.save_list
        
start()
