from us_visa.logger import logging
from us_visa.exception import error_message_detail
import sys

logging.info("Thank you Lord Jesus")


try:
    # Code that may raise an exception
    1 / 0
except ZeroDivisionError as e:
    error_msg = error_message_detail(e, sys)
    print(error_msg)
