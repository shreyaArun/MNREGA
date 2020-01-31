""" base.login --> Login Page"""

import Utilities.Constants as ct
import Utilities.Extras as extras
import Utilities.QueryBuilder as qb
from Base.Bdo import BDO
from Base.Gpm import GPM
from Base.Member import MEMBER
import logging


def login_bdo():
    """
    Function for login through BDO
    :return: null
    """
    extras.decorate_break_message('Login For BDO')
    try:
        email = str(input(ct.Enter_email))
        while not extras.validate_email(email):
            print("Wrong Email Format. Please enter valid email \n")
            email = str(input(ct.Enter_email))

        password = int(input(ct.Enter_password))
        while not extras.validate_password(password):
            print("Wrong Password Format. Please enter numeric password between 101 and 999\n")
            password = int(input(ct.Enter_password))

        if qb.validate_credential(ct.BDO_TABLE, email, password):
            bdo_details = qb.get_bdo_details(ct.BDO_TABLE, email, password)
            bdo_id = int(bdo_details[0])
            bdo_name = str(bdo_details[1])
            bdo = BDO(bdo_id, bdo_name)
            bdo.welcome_screen()
            logging.info("Successfully logged in as BDO {}".format(bdo_name))
        else:
            print(ct.Wrong_credentials)
            login_bdo()
    except ValueError as e:
        print("Error is {}".format(e))
    finally:
        login_bdo()


def login_gpm():
    """
    Function for login through GPM
    :return: null
    """
    extras.decorate_break_message('Login For GPM')
    try:
        email = str(input(ct.Enter_email))
        while not extras.validate_email(email):
            print("Wrong Email Format. Please enter valid email \n")
            email = str(input(ct.Enter_email))

        password = int(input(ct.Enter_password))
        while not extras.validate_password(password):
            print("Wrong Password Format. Please enter numeric password between 101 and 999\n")
            password = int(input(ct.Enter_password))

        if qb.validate_credential(ct.GPM_TABLE, email, password):
            gpm_details = qb.get_gpm_or_member_details(ct.GPM_TABLE, email, password)
            gpm_id = int(gpm_details[0])
            gpm_name = str(gpm_details[1])
            asignee_bdo_id = int(gpm_details[2])
            gpm = GPM(gpm_id, gpm_name, asignee_bdo_id)
            gpm.welcome_screen()
        else:
            print(ct.Wrong_credentials)
            login_gpm()

    except ValueError as e:
        print("Error is {}".format(e))
    finally:
        login_gpm()


def login_member():
    """
    Function for login through Member
    :return:  null
    """
    extras.decorate_break_message('Login For MEMBER')
    try:
        email = str(input(ct.Enter_email))
        while not extras.validate_email(email):
            print("Wrong Email Format. Please enter valid email \n")
            email = str(input(ct.Enter_email))

        password = int(input(ct.Enter_password))
        while not extras.validate_password(password):
            print("Wrong Password Format. Please enter numeric password between 101 and 999\n")
            password = int(input(ct.Enter_password))
        if qb.validate_credential(ct.MEMBER_TABLE, email, password):
            member_details = qb.get_gpm_or_member_details(ct.MEMBER_TABLE, email, password)
            member_id = int(member_details[0])
            member_name = str(member_details[1])
            asignee_gpm_id = int(member_details[2])
            reviewer_bdo_id = int(qb.fetch_bdo_id(asignee_gpm_id))
            member = MEMBER(member_id, member_name, asignee_gpm_id, reviewer_bdo_id)
            member.welcome_screen()
        else:
            print(ct.Wrong_credentials)
            login_member()

    except ValueError as e:
        print("Error as {}".format(e))
    finally:
        login_member()


def start_application():
    """
    Function to start the application
    :return: null
    """
    print(ct.Choose_Role)
    try:
        choice = int(input(ct.Enter_choice))
        if int(choice) in [1, 2, 3]:
            if int(choice) == 1:
                login_bdo()
            elif int(choice) == 2:
                login_gpm()
            else:
                login_member()
        else:
            print(ct.Wrong_choice)
            start_application()
    except ValueError as e:
        print("Error is {}".format(e))
    finally:
        start_application()


def create_tables():
    """
    Fucntion to Create the table in database
    :return: null
    """
    qb.create_table(ct.BDO_TABLE,
                    'id integer PRIMARY KEY AUTOINCREMENT',
                    'name varchar(25)',
                    'email varchar(50)',
                    'password varchar(10)')

    qb.create_table(ct.GPM_TABLE,
                    'id integer PRIMARY KEY AUTOINCREMENT',
                    'name varchar(25)',
                    'email varchar(50)',
                    'password varchar(10)',
                    'area varchar[50]',
                    'pincode integer',
                    'asignee_id integer')

    qb.create_table(ct.MEMBER_TABLE,
                    'id integer PRIMARY KEY AUTOINCREMENT',
                    'name varchar(25)',
                    'email varchar(50)',
                    'password varchar(10)',
                    'gender varchar(5)',
                    'age integer',
                    'address varchar(50)',
                    'area varchar[50]',
                    'pincode integer',
                    'days_worked integer DEFAULT 0',
                    'wage integer DEFAULT 0',
                    'asignee_id integer')

    qb.create_table(ct.PROJECT_TABLE,
                    'id integer PRIMARY KEY AUTOINCREMENT',
                    'name varchar(50)',
                    'area varchar[50]',
                    'total_member integer',
                    'cost_estimate integer',
                    'type varchar(5)',
                    'start_date  varchar(15)',
                    'end_date varchar(15)',
                    'asignee_id integer')

    qb.create_table(ct.PROJECT_MEMBER_DETAIL_TABLE,
                    'member_id integer PRIMARY KEY',
                    'project_id integer',
                    'request_status integer DEFAULT 0',
                    'onboarding_date varchar(15)',
                    'end_date varchar(15)',
                    'asignee_id int',
                    'reviewer_id int')

    qb.create_table(ct.WAGE_APPROVAL_TABLE,
                    'member_id integer PRIMARY KEY',
                    'project_id integer',
                    'amount integer',
                    'days_worked integer',
                    'reviewer_id integer')

    qb.create_table(ct.COMPLAINT_TABLE,
                    'id integer PRIMARY KEY AUTOINCREMENT ',
                    'member_id integer',
                    'message varchar(255)',
                    'raise_to varchar(5)',
                    'authority_id integer',
                    'date varchar(15)')


if __name__ == '__main__':
    extras.decorate_break_message(ct.Welcome_to_Application)
    create_tables()
    start_application()
