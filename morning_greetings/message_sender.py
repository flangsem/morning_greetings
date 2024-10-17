from logger import *

def send_message(message:str, mail:str):
    try:
        if not message and not mail:
            error_message = "Error: No message and mail address provided"
            log_error(error_message," send_message()" )
            raise ValueError(error_message)
        
        elif not message: 
            error_message = "Error: No message provided", "send_message" 
            log_error(error_message," send_message()" )
            raise ValueError(error_message)
        
        elif not mail:
            error_message = "Error: No mail address provided"
            log_error(error_message," send_message()" )
            raise ValueError(error_message)
        
        else:
            log_message(mail, message)
            print(f"Sending message to {mail}: {message}")

    except ValueError as ve:
        error_message = str(ve)
        log_error(error_message, "send_message()")
        raise ValueError(error_message)
    
    except Exception as e:
        error_message = f"An unexpected error occurred while sending the message: {e}"
        log_error(error_message, "send_message()")
        raise Exception(error_message)