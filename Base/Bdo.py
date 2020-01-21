import Utilities.Constants as ct
import Utilities.Extras as extras
import Utilities.QueryBuilder as qb


class BDO:
    def __init__(self, bdo_id, bdo_name):
        self.id = bdo_id
        self.name = bdo_name

    def welcome_screen(self):
        extras.decorate_break_message('Welcome {}'.format(self.name))
        print(ct.Choose_Action)
        choice = input(ct.Enter_choice)
        if int(choice) in [1, 2, 3, 4, 5, 6]:
            if int(choice) == 1:
                create_gpm(self.id)
                self.welcome_screen()
            elif int(choice) == 2:
                delete_gpm(self.id)
                self.welcome_screen()
            elif int(choice) == 3:
                update_gpm(self.id)
                self.welcome_screen()
            elif int(choice) == 4:
                create_project(self.id)
                self.welcome_screen()
                pass
            elif int(choice) == 5:
                delete_project(self.id)
                self.welcome_screen()
            else:
                update_project(self.id)
                self.welcome_screen()
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
                    'pincode integer',
                    'asignee_id integer')

    qb.insert_gpm_table(table_name, gpm_name, gpm_email, gpm_password, gpm_area, gpm_pincode, bdo_id)


def delete_gpm(bdo_id):
    print(ct.Enter_the_email_to_delete_gpm)
    gpm_email = input(ct.Enter_email)
    table_name = 'GPM'
    qb.delete_gpm(table_name, bdo_id, gpm_email)


def update_gpm(bdo_id):
    print(ct.Enter_the_email_to_update_gpm)
    gpm_email = input(ct.Enter_email)
    table_name = 'GPM'

    print(ct.Choose_Update_Option_For_GPM)
    choice = input(ct.Enter_choice)

    if int(choice) in [1, 2, 3, 4, 5]:
        if int(choice) == 1:
            updated_name = input(ct.Enter_new_name)
            qb.update_gpm_data(table_name, gpm_email, 'name', "'{}'".format(updated_name), bdo_id)
        elif int(choice) == 2:
            updated_password = input(ct.Enter_new_password)
            qb.update_gpm_data(table_name, gpm_email, 'password', updated_password, bdo_id)
        elif int(choice) == 3:
            updated_area = input(ct.Enter_new_area)
            qb.update_gpm_data(table_name, gpm_email, 'area', "'{}'".format(updated_area), bdo_id)
        else:
            updated_pincode = input(ct.Enter_new_pincode)
            qb.update_gpm_data(table_name, gpm_email, 'pincode', updated_pincode, bdo_id)
    else:
        print(ct.Wrong_choice)


def create_project(bdo_id):
    table_name = "PROJECT"
    project_name = input(ct.Enter_name)
    project_area = input(ct.Enter_area)
    member_count = input(ct.Enter_total_member_required)
    project_cost = input(ct.Enter_project_cost_estimate)
    project_type = input(ct.Enter_project_type)

    while project_type not in ["RC", "ST", "BC"]:
        print(ct.Warning_wrong_project_type)
        project_type = input(ct.Enter_project_type)

    project_start_date = extras.convert_string_to_date(input(ct.Enter_start_date))
    project_end_date = extras.convert_string_to_date(input(ct.Enter_end_date))
    while project_end_date < project_start_date:
        print(ct.Warning_wrong_end_date)
        project_end_date = extras.convert_string_to_date(input(ct.Enter_end_date))

    qb.create_table('PROJECT', 'id integer PRIMARY KEY AUTOINCREMENT',
                    'name varchar(50)',
                    'area varchar[50]',
                    'total_member integer',
                    'cost_estimate integer',
                    'type varchar[5]',
                    'start_date  Text',
                    'end_date Text',
                    'asignee_id integer')

    qb.insert_project_table(table_name,
                            project_name,
                            project_area,
                            member_count,
                            project_cost,
                            project_type,
                            project_start_date,
                            project_end_date,
                            bdo_id)


def delete_project(bdo_id):
    table_name = 'PROJECT'
    print(ct.Project_available_in_your_block)
    project_list = qb.get_project_for_bdo(table_name, bdo_id)
    print("-" * 60)
    for item in project_list:
        print('Project Id : {}  |   Project Name :{}'.format(item[0], item[1]))
        print("-" * 60)

    item_id = input(ct.Enter_the_project_id_to_be_deleted)
    qb.delete_project(table_name, item_id)


def update_project(bdo_id):
    table_name = 'PROJECT'
    print(ct.Project_available_in_your_block)
    project_list = qb.get_project_for_bdo(table_name, bdo_id)
    print("-" * 60)
    for item in project_list:
        print('Project Id : {}  |   Project Name :{}'.format(item[0], item[1]))
        print("-" * 60)

    item_id = input(ct.Enter_the_project_id_to_be_updated)
    print(ct.Choose_Update_Option_For_Project)
    choice = input(ct.Enter_choice)

    if int(choice) in [1, 2, 3, 4, 5]:
        if int(choice) == 1:
            updated_name = input(ct.Enter_new_name)
            # qb.update_gpm_data(table_name, gpm_email, 'name', "'{}'".format(updated_name), bdo_id)
            qb.update_project_details(table_name, item_id, 'name', "'{}'".format(updated_name))
        elif int(choice) == 2:
            updated_area = input(ct.Enter_new_area)
            qb.update_project_details(table_name, item_id, 'area', "'{}'".format(updated_area))
        elif int(choice) == 3:
            updated_member_count = input(ct.Enter_new_total_member_required)
            qb.update_project_details(table_name, item_id, 'total_member', updated_member_count)
        elif int(choice) == 4:
            updated_cost_estimate = input(ct.Enter_new_project_cost_estimate)
            qb.update_project_details(table_name, item_id, 'cost_estimate', updated_cost_estimate)
        else:
            updated_project_type = input(ct.Enter_new_project_type)
            while updated_project_type not in ["RC", "ST", "BC"]:
                print(ct.Warning_wrong_project_type)
                updated_project_type = input(ct.Enter_new_project_type)
            qb.update_project_details(table_name, item_id, 'type', "'{}'".format(updated_project_type))
    else:
        print(ct.Wrong_choice)
