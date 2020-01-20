""" base.login --> Login Page"""
import Utilities.Constants as ct
import Utilities.Extras as extras
import Utilities.QueryBuilder as qb
from Base.Bdo import BDO
import logging


def login_bdo():
    qb.create_table('BDO', 'id integer PRIMARY KEY AUTOINCREMENT',
                    'name varchar(25)',
                    'email varchar(50)',
                    'password varchar(10)')

    extras.decorate_break_message('Login For BDO')
    email = input(ct.Enter_email)
    table_name = 'BDO'

    if qb.check_if_email_present(table_name, email):
        password = input(ct.Enter_password)
        if qb.validate_credential(table_name, email, password):
            bdo_details = qb.get_bdo_details(table_name,email,password)
            bdo_id = int(bdo_details[0])
            bdo_name = str(bdo_details[1])
            bdo = BDO(bdo_id, bdo_name)
            bdo.welcome_screen()
            logging.info("Successfully logged in as BDO {}".format(bdo_name))
        else:
            print(ct.Wrong_credentials)
            login_bdo()
    else:
        print("Please Enter the following Details")
        name = input(ct.Enter_name)
        password = input(ct.Enter_password)
        qb.insert_bdo_table(table_name, str(name), str(email), password)
        login_bdo()


def login_gpm():
    extras.decorate_break_message('Login For GPM')
    table_name = 'GPM'
    email = input(ct.Enter_email)
    password = input(ct.Enter_password)
    if qb.validate_credential(table_name, email, password):
        pass


def start_application():
    print(ct.Choose_Role)
    choice = input(ct.Enter_choice)
    if int(choice) in [1, 2, 3]:
        # TODO : Write the logic for selected choice
        if int(choice) == 1:
            login_bdo()
        elif int(choice) == 2:
            login_gpm()
        else:
            pass
    else:
        print(ct.Wrong_choice)
        start_application()


if __name__ == '__main__':
    extras.decorate_break_message(ct.Welcome_to_Application)
    start_application()
