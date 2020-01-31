"""Utlities.Extras"""
import datetime
import Utilities.Constants as ct
import re


def decorate_break_message(message):
    """
    function to decorate a message
    :param message: message to be decorated
    :return: null
    """
    print("*" * 30 + message + "*" * 30)


def display_job_card(data):
    """
    Method to display the job card
    :param data: memeber info data
    :return: job id card
    """
    print("\n" + "-" * 30)
    print(ct.Name + str(data[0]))
    print(ct.Age + str(data[1]))
    print(ct.Gender + str(data[2]))
    print(ct.Area + str(data[3]))
    print(ct.Address + str(data[4]))
    print("-" * 30)


def convert_string_to_date(date_str):
    """
    Method to convert string into date time
    :param date_str: date string format
    :return: date in date format
    """
    format_str = '%d-%m-%Y'
    date_result = datetime.datetime.strptime(date_str, format_str)
    return date_result.date()


def validate_password(password):
    if isinstance(password, int) and 100 < password < 1000:
        return True
    else:
        return False


def validate_email(email):
    regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
    if re.search(regex, email):
        return True
    else:
        return False
