# Importing useful libraries and modules
import sys
from src.logger import logging

# Creating a function that gives us the error message
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() # Getting the error info
    file_name=exc_tb.tb_frame.f_code.co_filename # Getting the error name

    # Getting our custom error message
    error_message=f"Error occured \nin python script:[{file_name}] \
        \nline number:[{exc_tb.tb_lineno}] \nerror message:[{str(error)}]"

    return error_message

# Creating a class that will enable us to raise a custom exception and get the message
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message