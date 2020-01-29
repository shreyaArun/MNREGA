""" Contants """

Database_Path = r"/home/nineleaps/Desktop/MANREGA/Database/Application.db"

BDO_TABLE = 'BDO'
GPM_TABLE = 'GPM'
MEMBER_TABLE = 'MEMBER'
PROJECT_TABLE = 'PROJECT'
PROJECT_MEMBER_DETAIL_TABLE = "PROJECT_MEMBER_DETAIL"
WAGE_APPROVAL_TABLE = "WAGE_APPROVAL"
COMPLAINT_TABLE = 'COMPLAINT'

Choose_Role = 'Choose a Role : \n ' \
              '1 for BDO \n ' \
              '2 for GPM \n ' \
              '3 for MEMBER \n'
Choose_Action_For_Bdo = 'Choose a Action : \n ' \
                        '1 for Create GPM \n ' \
                        '2 for Delete GPM \n ' \
                        '3 for Update GPM \n ' \
                        '4 for Creating Project \n ' \
                        '5 for Deleting Project \n ' \
                        '6 for Updating Project \n ' \
                        '7 for Approving Projects \n ' \
                        '8 for Approving Wages \n ' \
                        '9 for View Complaints \n'
Choose_Action_For_GPM = 'Choose a Action : \n ' \
                        '1 for Create Member \n ' \
                        '2 for Delete Member \n ' \
                        '3 for Update Member \n ' \
                        '4 for Issue Job Card \n ' \
                        '5 for Assign Project \n ' \
                        '6 for Raise Wage Approval Request \n ' \
                        '7 for View Complaints \n'
Choose_Action_For_MEMBER = 'Choose a Action : \n ' \
                           '1 for Check Wage \n ' \
                           '2 for Raise Complaint \n '
Choose_Update_Option_For_GPM = 'Choose what to Update :\n ' \
                               '1 for Change Name \n ' \
                               '2 for Change Password\n ' \
                               '3 for Change Area\n ' \
                               '4 for Change Pincode\n'
Choose_Update_Option_For_Project = 'Choose what to Update :\n ' \
                                   '1 for Change Name \n ' \
                                   '2 for Change Area\n ' \
                                   '3 for Change Total Labour\n ' \
                                   '4 for Change Cost Estimate\n ' \
                                   '5 for Change Project Type\n '
Choose_Update_Option_For_Member = 'Choose what to Update :\n ' \
                                  '1 for Change Name \n ' \
                                  '2 for Change Password\n ' \
                                  '3 for Change Area\n ' \
                                  '4 for Change Address\n ' \
                                  '5 for Change Pincode\n ' \
                                  '6 for Change Age\n'
Name = 'Name : '
Age = 'Age : '
Gender = 'Gender : '
Area = 'Area : '
Address = "Address : "
Choose_complaint_that_has_been_resolved = 'Choose Complaint Id which has been resolved : '
Enter_choice = 'Enter your choice : '
Enter_name = 'Enter name : '
Enter_email = 'Enter email : '
Enter_password = 'Enter password : '
Enter_area = 'Enter area : '
Enter_age = 'Enter age : '
Enter_pincode = 'Enter pincode : '
Enter_gender = "Enter Gender (M : MALE , F : FEMALE) : "
Enter_address = 'Enter Member Address : '
Enter_total_member_required = "Enter Total Member Required : "
Enter_project_cost_estimate = "Enter Project Cost Estimate (in ₹) : "
Enter_project_type = "Enter Project Type Code (RC : Road Construction, ST : Sewage Treatment, " \
                     "BC : Building Construction) : "
Enter_complaint_date = 'Enter Complaint Date in (dd-mm-yyyy) : '
Enter_start_date = "Enter Start Date in (dd-mm-yyyy) : "
Enter_end_date = "Enter End Date in (dd-mm-yyyy) : "
Enter_his_wage = 'Enter his/her wage mentioned : '
Enter_days_worked = 'Enter his/her mentioned days worked : '
Enter_new_name = 'Enter New Name : '
Enter_new_password = 'Enter New Password : '
Enter_new_area = 'Enter New Area : '
Enter_new_age = 'Enter New Age : '
Enter_new_pincode = 'Enter New Pincode : '
Enter_new_address = 'Enter New Address : '
Enter_new_project_type = "Enter New Project Type Code (RC : Road Construction, ST : Sewage Treatment, BC : Building " \
                         "Construction) : "
Enter_new_project_cost_estimate = "Enter New Cost Estimate : "
Enter_new_total_member_required = "Enter New Total Member Required : "
Enter_the_email_to_update_gpm = 'Enter the Email of GPM to be Updated \n'
Enter_the_email_to_delete_gpm = 'Enter the Email of GPM to be Deleted \n'
Enter_the_project_id_to_be_deleted = "Enter the Project Id for the project to be Deleted : "
Enter_the_member_id_to_be_deleted = "Enter the Member Id of the member to be Deleted : "
Enter_the_project_id_to_be_updated = "Enter the Project Id for the project to be updated  : "
Enter_the_member_id_to_be_allotted = "Enter the Member Id of the member to be Allotted For Project : "
Enter_the_project_id_to_be_member_allotted = 'Enter the Project Id for the project to be allotted : '
Enter_the_project_id_to_view_pending_request = 'Enter the Project Id for the project to see pending requests : '
Enter_the_project_id_to_view_wage_request = 'Enter the Project Id for the project to see pending memeber wages : '
Enter_the_project_id_for_wage_update = 'Enter the Project Id for the wage to be updated : '
Enter_project_assigned_date = 'Enter Project Assigned Date (dd-mm-yyyy) : '
Member_available_in_your_zone = "Member Available in your Zone : \n"
Member_already_in_list = 'Member Already in Project Allotted/ Waitlist \n'
No_Request_for_the_project = 'No Request For this Project\n'
No_Complaint_present = "No Complaints Present"
Project_available_in_your_block = "Project Available in your Block : \n"
Project_slots_already_occupied = "Project Slots are already occupied.\n"
Raise_complaint_to = 'Raise Complaint to : \n ' \
                     '1 for BDO\n ' \
                     '2 for GPM '
Request_for_project_still_pending = "Request For Following Project Still Pending\n"
Welcome_to_Application = 'WELCOME TO MNREGA APPLICATION'
Wrong_choice = 'Wrong Option \n'
Wrong_credentials = 'Wrong Credentials \n'
Warning_wrong_end_date = "Warning : End Date must be greater than Start Date \n"
Warning_wrong_project_type = "Warning : Project Type Not Available. Please Try Again ..! \n"
Warning_wrong_gender_entry = 'Warning : Wrong Entry for Gender. Please Try Again'
Warning_invalid_onboarding_date = "Warning : Invalid Onboarding Date \n"
