import Utilities.Constants as ct
import Utilities.Extras as extras
import Utilities.QueryBuilder as qb


def view_complaints(bdo_id):
    table_name = 'COMPLAINT'
    result_data = qb.fetch_complaints_by_authority(table_name, bdo_id, 'BDO')
    if len(result_data) != 0:
        print("-" * 140)
        for item in result_data:
            print('Complaint Id : {complaint_id} |  Member Id : {member_id} | '
                  'Message : {message} | Complaint Date : {date}'.format(complaint_id=item[0],
                                                                         member_id=item[1],
                                                                         message=item[2],
                                                                         date=item[3]))
            print("-" * 140)
        complaint_id = input(ct.Choose_complaint_that_has_been_resolved)
        qb.delete_item_from_table(table_name, complaint_id, 'id')
    else:
        print(ct.No_Complaint_present)


class BDO:
    def __init__(self, bdo_id, bdo_name):
        self.id = bdo_id
        self.name = bdo_name

    def welcome_screen(self):
        extras.decorate_break_message('Welcome {}'.format(self.name))
        print(ct.Choose_Action_For_Bdo)
        choice = input(ct.Enter_choice)
        if int(choice) in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
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
            elif int(choice) == 5:
                delete_project(self.id)
                self.welcome_screen()
            elif int(choice) == 6:
                update_project(self.id)
                self.welcome_screen()
            elif int(choice) == 7:
                approving_projects(self.id)
                self.welcome_screen()
            elif int(choice) == 8:
                approving_wages(self.id)
                self.welcome_screen()
            else:
                view_complaints(self.id)
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

    start_date = input(ct.Enter_start_date)
    end_date = input(ct.Enter_end_date)
    project_start_date = extras.convert_string_to_date(start_date)
    project_end_date = extras.convert_string_to_date(end_date)

    while project_end_date < project_start_date:
        print(ct.Warning_wrong_end_date)
        end_date = input(ct.Enter_end_date)
        project_end_date = extras.convert_string_to_date(end_date)

    qb.insert_project_table(table_name,
                            project_name,
                            project_area,
                            member_count,
                            project_cost,
                            project_type,
                            start_date,
                            end_date,
                            bdo_id)


def delete_project(bdo_id):
    table_name = 'PROJECT'
    print(ct.Project_available_in_your_block)
    project_list = qb.get_item_for_asignee(table_name, bdo_id)
    print("-" * 60)
    for item in project_list:
        print('Project Id : {}  |   Project Name :{}'.format(item[0], item[1]))
        print("-" * 60)

    item_id = input(ct.Enter_the_project_id_to_be_deleted)
    qb.delete_item_from_table(table_name, item_id, 'id')
    qb.delete_item_from_table(ct.PROJECT_MEMBER_DETAIL_TABLE, item_id, 'project_id')


def update_project(bdo_id):
    table_name = 'PROJECT'
    print(ct.Project_available_in_your_block)
    project_list = qb.get_item_for_asignee(table_name, bdo_id)
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
            qb.update_item_details(table_name, item_id, 'name', "'{}'".format(updated_name))
        elif int(choice) == 2:
            updated_area = input(ct.Enter_new_area)
            qb.update_item_details(table_name, item_id, 'area', "'{}'".format(updated_area))
        elif int(choice) == 3:
            updated_member_count = input(ct.Enter_new_total_member_required)
            qb.update_item_details(table_name, item_id, 'total_member', updated_member_count)
        elif int(choice) == 4:
            updated_cost_estimate = input(ct.Enter_new_project_cost_estimate)
            qb.update_item_details(table_name, item_id, 'cost_estimate', updated_cost_estimate)
        else:
            updated_project_type = input(ct.Enter_new_project_type)
            while updated_project_type not in ["RC", "ST", "BC"]:
                print(ct.Warning_wrong_project_type)
                updated_project_type = input(ct.Enter_new_project_type)
            qb.update_item_details(table_name, item_id, 'type', "'{}'".format(updated_project_type))
    else:
        print(ct.Wrong_choice)


def approving_projects(bdo_id):
    table_name_project = "PROJECT"
    table_name_project_details = "PROJECT_MEMBER_DETAIL"
    print(ct.Project_available_in_your_block)
    project_list = qb.get_item_for_asignee(table_name_project, bdo_id)
    print("-" * 60)
    for item in project_list:
        print('Project Id : {}  |   Project Name :{}'.format(item[0], item[1]))
        print("-" * 60)

    project_id = input(ct.Enter_the_project_id_to_view_pending_request)
    result_data = qb.fetch_pending_request_for_project(table_name_project_details,
                                                       project_id,
                                                       bdo_id)
    print('Choose the member id whom you wanna approve\n')
    print('Member Id\t\tProject Id\t\tOnboarding Date\n')
    for item in result_data:
        print('\t\t{member_id}\t\t\t{project_id}\t\t\t{onboarding_date}'.format(member_id=item[0],
                                                                                project_id=item[1],
                                                                                onboarding_date=item[2]))
    member_id = input(ct.Enter_the_member_id_to_be_allotted)
    qb.approve_pending_details_for_project(table_name_project_details, member_id, 'request_status', 1)


def approving_wages(bdo_id):
    table_name_project = "PROJECT"
    table_name_wage_approval = "WAGE_APPROVAL"
    table_name_member = 'MEMBER'
    print(ct.Project_available_in_your_block)
    project_list = qb.get_item_for_asignee(table_name_project, bdo_id)
    print("-" * 60)
    for item in project_list:
        print('Project Id : {}  |   Project Name :{}'.format(item[0], item[1]))
        print("-" * 60)

    project_id = input(ct.Enter_the_project_id_to_view_wage_request)
    member_wage_data = qb.fetch_wage_data_for_project(table_name_wage_approval, project_id, bdo_id)
    if len(member_wage_data) != 0:
        print('\t\t\t WAGE DATA FOR MEMBER \t\t\t')
        print('Member Id\t\tAmount\t\tDays Worked')
        for item in member_wage_data:
            print('\t\t{member_id}\t\t{amount}\t\t{days_worked}'.format(member_id=item[0],
                                                                        amount=item[1],
                                                                        days_worked=item[2]))

        member_id = input(ct.Enter_the_member_id_to_be_allotted)
        wage = input(ct.Enter_his_wage)
        days_worked = input(ct.Enter_days_worked)
        qb.delete_member_wage_data(table_name_wage_approval, member_id)
        qb.update_item_details(table_name_member, member_id, 'wage', wage)
        qb.update_item_details(table_name_member, member_id, 'days_worked', days_worked)
    else:
        print()
