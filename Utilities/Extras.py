"""Utlities.Extras"""
import datetime


def decorate_break_message(message):
    print("*" * 30 + message + "*" * 30)


def convert_string_to_date(date_str):
    format_str = '%d-%m-%Y'
    date_result = datetime.datetime.strptime(date_str, format_str)
    return date_result.date()