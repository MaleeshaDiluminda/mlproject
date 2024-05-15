import sys

def error_message_detail(error, error_detail:sys):
    # exc_info will give you 3 information about your error, exc_tb will give you where you can find the error ( which file , which line)
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in [{0}] line number [{1}] error measse [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message