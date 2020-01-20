import Utilities.Extras as extras
import Utilities.Constants as ct
import Utilities.QueryBuilder as qb


class BDO:
    def __init__(self, bdo_id, bdo_name):
        self.id = bdo_id
        self.name = bdo_name

    def welcome_screen(self):
        extras.decorate_break_message('Welcome {}'.format(self.name))
        print(ct.Choose_Action)
        choice = input(ct.Enter_choice)
        if int(choice) in [1, 2, 3]:
            if int(choice) == 1:
                create_gpm(self.id)
                self.welcome_screen()
            elif int(choice) == 2:
                delete_gpm(self.id)
            else:
                update_gpm()
        else:
            print(ct.Wrong_choice)
            self.welcome_screen()


def create_gpm(bdo_id):
    gpm_name = input(ct.Enter_name)
    gpm_email = input(ct.Enter_email)
    gpm_password = input(ct.Enter_password)
    gpm_area = input(ct.Enter_area)
    gpm_pincode = input(ct.Enter_pincode)
    table_name = 'GPM'

    qb.create_table('GPM', 'id integer PRIMARY KEY AUTOINCREMENT',
                    'name varchar(25)',
                    'email varchar(50)',
                    'password varchar(10)',
                    'area varchar[50]',
                    'pincode integet',
                    'asignee_id integer')

    qb.insert_gpm_table(table_name, gpm_name, gpm_email, gpm_password, gpm_area, gpm_pincode, bdo_id)


def delete_gpm(bdo_id):
    print('Enter the Email of GPM to be Deleted \n')
    gpm_email = input(ct.Enter_email)
    table_name = 'GPM'
    qb.delete_gpm(table_name, bdo_id, gpm_email)


def update_gpm():
    pass
