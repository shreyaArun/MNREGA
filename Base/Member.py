import Utilities.Constants as ct
import Utilities.Extras as extras
import Utilities.QueryBuilder as qb


class MEMBER:
    def __init__(self, member_id, member_name, asignee_gpm_id, reviewer_bdo_id):
        self.id = member_id
        self.name = member_name
        self.asignee_gpm_id = asignee_gpm_id
        self.reviewer_bdo_id = reviewer_bdo_id

    def welcome_screen(self):
        extras.decorate_break_message('Welcome {}'.format(self.name))
        print(ct.Choose_Action_For_MEMBER)
        choice = input(ct.Enter_choice)
        if int(choice) in [1, 2]:
            if int(choice) == 1:
                check_wage(self.id)
                self.welcome_screen()
            else:
                raise_complaint(self.id, self.asignee_gpm_id, self.reviewer_bdo_id)
                self.welcome_screen()
        else:
            print(ct.Wrong_choice)
            self.welcome_screen()


def check_wage(member_id):
    """
    Function to check the wage of member
    :param member_id: member id
    :return: null
    """
    wage_data = int(qb.fetch_wage_for_member(member_id))
    print('WAGE FOR YOUR PROJECT TASK : {}'.format(wage_data))


def raise_complaint(member_id, asignee_gpm_id, reviewer_bdo_id):
    """
    Function to raise a complaint by the member
    :param member_id: member id
    :param asignee_gpm_id: gpm id
    :param reviewer_bdo_id: bdo id
    :return: null
    """
    table_name = 'COMPLAINT'

    print(ct.Raise_complaint_to)
    choice = input(ct.Enter_choice)
    message = input('Enter Complaint Message : ')
    complaint_date = input(ct.Enter_complaint_date)
    qb.raise_complaint(table_name, member_id, message, 'BDO' if int(choice) == 1 else 'GPM',
                       reviewer_bdo_id if int(choice) == 1 else asignee_gpm_id, complaint_date)
