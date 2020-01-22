import Utilities.Constants as ct
import Utilities.Extras as extras
import Utilities.QueryBuilder as qb


def view_complaints(gpm_id):
    table_name = 'COMPLAINT'
    result_data = qb.fetch_complaints_by_authority(table_name, gpm_id, 'GPM')
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


class GPM:
    def __init__(self, gpm_id, gpm_name, asignee_bdo_id):
        self.id = gpm_id
        self.name = gpm_name
        self.asignee_bdo_id = asignee_bdo_id

    def welcome_screen(self):

        extras.decorate_break_message('Welcome {}'.format(self.name))
        print(ct.Choose_Action_For_GPM)
        choice = input(ct.Enter_choice)
        if int(choice) in [1, 2, 3, 4, 5, 6, 7]:
            if int(choice) == 1:
                create_member(self.id)
                self.welcome_screen()
            elif int(choice) == 2:
                delete_member(self.id)
                self.welcome_screen()
            elif int(choice) == 3:
                update_member(self.id)
                self.welcome_screen()
            elif int(choice) == 4:
                issue_job_card(self.id)
            elif int(choice) == 5:
                assign_project(self.id, self.asignee_bdo_id)
                self.welcome_screen()
            elif int(choice) == 6:
                raise_wage_request_for_all_members(self.id, self.asignee_bdo_id)
                self.welcome_screen()
            else:
                view_complaints(self.id)
                self.welcome_screen()
        else:
            print(ct.Wrong_choice)
            self.welcome_screen()


def create_member(gpm_id):
    table_name = 'MEMBER'
    name = input(ct.Enter_name)
    email = input(ct.Enter_email)
    password = input(ct.Enter_password)
    gender = input(ct.Enter_gender)
    while gender not in ['M', 'F']:
        print(ct.Warning_wrong_gender_entry)
        gender = input(ct.Enter_gender)
    address = input(ct.Enter_address)
    area = input(ct.Enter_area)
    age = input(ct.Enter_age)
    pincode = input(ct.Enter_pincode)


    qb.insert_member_table(table_name,
                           name,
                           email,
                           password,
                           gender,
                           age,
                           address,
                           area,
                           pincode,
                           gpm_id)


def delete_member(gpm_id):
    table_name = 'MEMBER'
    print(ct.Member_available_in_your_zone)
    member_list = qb.get_item_for_asignee(table_name, gpm_id)
    print("-" * 60)
    for item in member_list:
        print('Member Id : {}  |   Member Name :{}'.format(item[0], item[1]))
        print("-" * 60)

    item_id = input(ct.Enter_the_member_id_to_be_deleted)
    qb.delete_item_from_table(table_name, item_id, 'id')
    qb.delete_item_from_table(ct.PROJECT_MEMBER_DETAIL_TABLE, item_id, 'member_id')
    qb.delete_item_from_table(ct.WAGE_APPROVAL_TABLE, item_id, 'member_id')
    qb.delete_item_from_table(ct.COMPLAINT_TABLE, item_id, 'member_id')



def update_member(gpm_id):
    table_name = 'MEMBER'
    print(ct.Member_available_in_your_zone)
    member_list = qb.get_item_for_asignee(table_name, gpm_id)
    print("-" * 60)
    for item in member_list:
        print('Member Id : {}  |   Member Name :{}'.format(item[0], item[1]))
        print("-" * 60)

    item_id = input(ct.Enter_the_member_id_to_be_deleted)
    print(ct.Choose_Update_Option_For_Member)
    choice = input(ct.Enter_choice)

    if int(choice) in [1, 2, 3, 4, 5, 6]:
        if int(choice) == 1:
            updated_name = input(ct.Enter_new_name)
            qb.update_item_details(table_name, item_id, 'name', "'{}'".format(updated_name))
        elif int(choice) == 2:
            update_password = input(ct.Enter_new_password)
            qb.update_item_details(table_name, item_id, 'password', update_password)
        elif int(choice) == 3:
            updated_area = input(ct.Enter_new_area)
            qb.update_item_details(table_name, item_id, 'area', "'{}'".format(updated_area))
        elif int(choice) == 4:
            update_address = input(ct.Enter_new_address)
            qb.update_item_details(table_name, item_id, 'address', "'{}'".format(update_address))
        elif int(choice) == 5:
            updated_pincode = input(ct.Enter_new_pincode)
            qb.update_item_details(table_name, item_id, 'pincode', updated_pincode)
        else:
            updated_age = input(ct.Enter_new_age)
            qb.update_item_details(table_name, item_id, 'age', updated_age)
    else:
        print(ct.Wrong_choice)


def issue_job_card(gpm_id):
    table_name = 'MEMBER'
    print(ct.Member_available_in_your_zone)
    member_list = qb.get_item_for_asignee(table_name, gpm_id)
    print("-" * 60)
    for item in member_list:
        print('Member Id : {}  |   Member Name :{}'.format(item[0], item[1]))
        print("-" * 60)
    item_id = input(ct.Enter_the_member_id_to_be_deleted)
    member_job_data = qb.fetch_job_id_data(table_name, item_id)
    extras.display_job_card(member_job_data)


def assign_project(gpm_id, bdo_id):
    table_name_project_detail = 'PROJECT_MEMBER_DETAIL'
    table_name_project = "PROJECT"
    table_name_member = 'MEMBER'



    print(ct.Project_available_in_your_block)
    project_list = qb.get_item_for_asignee(table_name_project, bdo_id)
    print("-" * 60)
    for item in project_list:
        print('Project Id : {}  |   Project Name :{}'.format(item[0], item[1]))
        print("-" * 60)

    project_id = input(ct.Enter_the_project_id_to_be_member_allotted)
    project_data = qb.get_project_details(table_name_project, project_id)
    total_strength = project_data[0]
    start_date = str(project_data[1])
    end_date = str(project_data[2])
    current_strength = qb.get_project_allocated_strength(table_name_project_detail, project_id)

    if current_strength < total_strength:
        print(ct.Member_available_in_your_zone)
        member_list = qb.get_item_for_asignee(table_name_member, gpm_id)
        print("-" * 60)
        for item in member_list:
            print('Member Id : {}  |   Member Name :{}'.format(item[0], item[1]))
            print("-" * 60)

        item_id = input(ct.Enter_the_member_id_to_be_allotted)
        if qb.check_member_not_present(table_name_project_detail, item_id):
            onboarding_date = input(ct.Enter_project_assigned_date)
            while extras.convert_string_to_date(start_date) > extras.convert_string_to_date(str(onboarding_date)) \
                    or extras.convert_string_to_date(end_date) < extras.convert_string_to_date(str(onboarding_date)):
                print(ct.Warning_invalid_onboarding_date)
                onboarding_date = input(ct.Enter_project_assigned_date)
            qb.assign_member_to_project(table_name_project_detail,
                                        item_id,
                                        project_id,
                                        gpm_id,
                                        bdo_id,
                                        onboarding_date,
                                        end_date)
        else:
            print(ct.Member_already_in_list)
    else:
        print(ct.Project_slots_already_occupied)


def raise_wage_request_for_all_members(gpm_id, bdo_id):
    table_name_wage_approval = 'WAGE_APPROVAL'
    table_name_project_details = "PROJECT_MEMBER_DETAIL"
    table_name_project = 'PROJECT'



    print(ct.Project_available_in_your_block)
    project_list = qb.get_item_for_asignee(table_name_project, bdo_id)
    print("-" * 60)
    for item in project_list:
        print('Project Id : {}  |   Project Name :{}'.format(item[0], item[1]))
        print("-" * 60)

    project_id = input(ct.Enter_the_project_id_for_wage_update)
    if qb.is_project_wage_not_pending(table_name_wage_approval, project_id):
        member_detail_list = qb.get_member_project_details(table_name_project_details, project_id, gpm_id)
        for item in member_detail_list:
            number_of_days_worked = int((extras.convert_string_to_date(item[3]) -
                                         extras.convert_string_to_date(item[2])).days)
            amount = number_of_days_worked * 100
            qb.insert_wage_table(table_name_wage_approval, item[0], item[1], amount, number_of_days_worked, bdo_id)
    else:
        print(ct.Request_for_project_still_pending)
