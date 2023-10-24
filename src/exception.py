import sys
from src.logger import logging

def error_message_detail(error, error_detail:sys):
    exc_type, exc_value, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = 'Error occured in python script name [{0}] at line number [{1}] with error message [{2}]'.format(file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message

# if __name__ == "__main__":
#     # try: 
#     #     a=1/0
#     # except Exception as e:
#     #     print(e)
#     #     logging.info("Divide by zero")
#     #     raise CustomException("Divide by zero",sys)

#    val1 = 2
#    val2 = 5
#    try:
#      if val2 > val1:
#         raise CustomException("Something wrong", sys)
#    except CustomException as e:
#       logging.info("Invalid condition")
#       #raise CustomException("Invalid condition",sys)
#    except Exception as e:
#       logging.info("An unexpected error occurred: " + str(e))        