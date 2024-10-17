from logger import log_error
import csv

class Contacts:
    def __init__(self):
        """initiate an empty list"""
        self.contacts = []

    def add_contact(self,name: str, contact_info: str, preferred_time: str, day: bool):
        """Add a Conctact"""
        try:
            if not all([name, contact_info, preferred_time, isinstance(day, bool)]):
                error_message = "Invalid input: name, contact_info, and preferred_time must be non-empty strings, and 'day' must be a boolean."
                log_error(error_message," add_contact()")
                raise ValueError(error_message)
            
            contact = {
                'name': name,
                'contact_info': contact_info,
                'preferred_time': preferred_time,
                'day':day
                }
            self.contacts.append(contact)

            print(f"Contact {name} added")

        except ValueError as ve:
            error_message = f"Failed to add contact: {ve}"
            log_error(error_message, "add_contact()")
            raise ValueError(f"Failed to add contact: {ve}")
        except Exception as e:
            error_message =f"An unexpected error : {e}, occurred while adding the contact."
            log_error(error_message, "add_contact()")
            raise Exception(error_message)
                  
        
    def remove_contact(self, contact_info: str):
        """Removes contact with the matching email"""
        try:
            #Verifies that contactinfo is a string
            if not isinstance(contact_info, str):
                error_message = "contact_info must be a string."
                log_error(error_message, "remove_contact()")
                raise TypeError(error_message)
            
            initial_length = len(self.contacts)
            self.contacts = [c for c in self.contacts if c['contact_info'] != contact_info]

            #if the lenght of the list doesnt change, none was removed
            if len(self.contacts) == initial_length:
                error_message = f"Contact with info '{contact_info}' not found."
                log_error(error_message, "remove_contact")
                raise ValueError(error_message)
            else:
                print(f"Contact with info '{contact_info}' removed.")

        except TypeError as te:
            error_message = f"Failed to remove contact: {te}"
            log_error(error_message, "remove_contact()")
            raise TypeError(error_message)

        except ValueError as ve:
            error_message = f"Failed to remove contact: {ve}"
            log_error(error_message, "remove_contact()")
            raise ValueError(error_message)

        except Exception as e:
            error_message = f"An unexpected error: {e}, occurred while removing the contact."
            log_error(error_message, "remove_contact()")
            raise Exception(error_message)
  

    def get_contacts(self)-> list:
        return self.contacts
    
    def save_list(self, path = "data/contact_list.csv"):
        """Save the list to file(data/contact_list.csv)"""
        try:
            #Enusres that there is a list
            if not self.contacts:
                error_message = "No contacts available to save."
                log_error(error_message, "save_list()")
                raise ValueError(error_message)
            
            with open(path, 'w') as f:
                write = csv.writer(f)
                write.writerow(["name","mail","preferred_time", "day"])
                for person in self.get_contacts():
                    write.writerow([person.get("name"), 
                                    person.get("contact_info"), 
                                    person.get("preferred_time"), 
                                    person.get("day")])

            print("Contacts saved to data/contact_list.csv")
        except FileNotFoundError:
            error_message = "The directory 'data' does not exist. Please ensure the directory is created."
            log_error(error_message, "save_list()")
            raise FileNotFoundError(error_message)
        except PermissionError:
            error_message = "Permission denied when trying to save the file."
            log_error(error_message, "save_list()")
            raise PermissionError(error_message)
        except Exception as e:
            error_message = f"An unexpected error: {e}, occurred while saving the contacts."
            log_error(error_message, "save_list()")
            raise Exception(error_message)