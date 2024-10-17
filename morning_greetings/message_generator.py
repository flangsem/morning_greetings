from logger import log_error

import datetime

today = datetime.datetime.today().strftime("%A")

def generate_message(name: str, day: bool) ->str:
    try:
        if not isinstance(name, str):
            error_message = f"Expected 'name' to be a string, but got {type(name).__name__}."
            log_error(error_message, "generate_message()")
            raise TypeError(error_message)
        
        if not isinstance(day, bool):
            error_message = f"Expected 'day' to be a boolean, but got {type(day).__name__}."
            log_error(error_message, "generate_message()")
            raise TypeError(error_message)
        
        if day == False: 
            return f"Good Morning, {name}! Have a great day.....!"
        else:
            return f"Good Morning, {name}! Have a great {today}.....!"
    except TypeError as te:
        error_message  = str(te)
        log_error(error_message, "generate_message()")
        raise TypeError(error_message)
    
    except Exception as e:
        error_message = f"An unexpected error occurred: {e}"
        log_error(error_message, "generate_message()")
        raise Exception(error_message)