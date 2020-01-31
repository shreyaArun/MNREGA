import sqlite3 as sq
import Utilities.Constants as ct
import logging

conn = sq.connect(ct.Database_Path)
cursor = conn.cursor()


def create_table(table_name, *args):
    """
    Method to create a table
    :param table_name: table name
    :param args: table arguments
    :return: null
    """
    try:
        value = ''
        for item in args:
            value += item + ','
        value = value[:-1]
        cursor.execute("CREATE TABLE IF NOT EXISTS {table_name} ({value});".format(table_name=table_name, value=value))
        logging.info("Table with {} name created".format(table_name))
    except Exception as e:
        print("Error is : {}".format(e))


def delete_gpm(table_name, asignee_id, email):
    """
    Method to delete a gpm
    :param table_name: table name for gpm
    :param asignee_id: bdo_id
    :param email: email of the gpm
    :return: null
    """
    try:
        cursor.execute(
            "SELECT {table_name}.id "
            "FROM {table_name} "
            "WHERE {table_name}.email = '{email}' "
            "AND {table_name}.asignee_id = {asignee_id};".format(
                table_name=table_name,
                email=email,
                asignee_id=asignee_id))

        result_data = cursor.fetchone()

        if result_data is not None:
            cursor.execute("DELETE from {table_name} "
                           "WHERE {table_name}.email = '{email}' "
                           "AND {table_name}.asignee_id = {asignee_id};".format(table_name=table_name,
                                                                                email=email,
                                                                                asignee_id=asignee_id))

            set_gpm_field_as_null(ct.PROJECT_MEMBER_DETAIL_TABLE, 'asignee_id', 'asignee_id', result_data[0])
            set_gpm_field_as_null(ct.MEMBER_TABLE, 'asignee_id', 'asignee_id', result_data[0])

            print("GPM successfully deleted")
        else:
            print("Not Authorized..! Please Try with valid details")

    except Exception as e:
        print("Error is : {}".format(e))


def insert_bdo_table(table_name,
                     name, email, password):
    """
    method to insert into the bdo table
    :param table_name: bdo table name
    :param name: name of the bdo
    :param email: email of the bdo
    :param password: password of the bdo
    :return: null
    """
    try:
        cursor.execute(
            "INSERT INTO {}(name, email, password) VALUES ('{}','{}',{});".format(table_name, name, email, password))
        conn.commit()
        logging.info("Item is inserted into table {}".format(table_name))

    except Exception as e:
        print("Error is {}".format(e))


def insert_gpm_table(table_name,
                     name, email, password, area, pincode, asignee_id):
    """
    Method to insert item into gpm table
    :param table_name: table name
    :param name: name of the gpm
    :param email: email of the gpm
    :param password: password of the gpm
    :param area: area of the gpm
    :param pincode: pincode of the gpm
    :param asignee_id: id of the bdo
    :return: null
    """
    try:
        # noinspection PyStringFormat
        cursor.execute(
            "INSERT INTO {}(name, email, password, area, pincode, asignee_id) "
            "VALUES ('{}','{}',{},'{}',{},{});".format(table_name,
                                                       name,
                                                       email,
                                                       password,
                                                       area,
                                                       pincode,
                                                       asignee_id))
        conn.commit()
    except Exception as e:
        print("Error is {}".format(e))


def insert_project_table(table_name, name, area, total_member, cost_estimate, project_type, start_date,
                         end_date, asignee_id):
    """
    Method to insert int othe project table
    :param table_name: project table name
    :param name: name of the project
    :param area: area of the project
    :param total_member: total memeber required by the project
    :param cost_estimate: cost estimate
    :param project_type: type of project
    :param start_date: start date of the project
    :param end_date: end date of the project
    :param asignee_id: id of the asignee
    :return: null
    """
    try:
        # noinspection PyStringFormat
        cursor.execute(
            "INSERT INTO "
            "{table_name}(name, area, total_member, cost_estimate, type, start_date, end_date, asignee_id) "
            "VALUES "
            "('{name}','{area}',{total_member}, {cost_estimate},'{type}','{start_date}','{end_date}',{asignee_id});".format(
                table_name=table_name,
                name=name,
                area=area,
                total_member=total_member,
                cost_estimate=cost_estimate,
                type=project_type,
                start_date=start_date,
                end_date=end_date,
                asignee_id=asignee_id))

        conn.commit()

    except Exception as e:
        print("Error is {}".format(e))


def validate_credential(table_name, email, password):
    """
    Function to validate the credentials
    :param table_name: table name of field to be validated
    :param email: email to be validated
    :param password: password to b e validated
    :return: null
    """
    try:
        cursor.execute("SELECT {table_name}.password FROM {table_name} WHERE {table_name}.email = '{email}';".format(
            table_name=table_name, email=email))
        db_password = cursor.fetchone()
        if db_password is not None and int(db_password[0]) == password:
            return True
        else:
            return False
    except Exception as e:
        print("Error is {}".format(e))


def get_bdo_details(table_name, email, password):
    """
    Function to get the bdo details
    :param table_name: table name
    :param email: email in the bdo table
    :param password: password in the bdo table
    :return: null
    """
    try:
        # noinspection PyStringFormat
        cursor.execute("SELECT {table_name}.id , {table_name}.name "
                       "FROM {table_name} "
                       "WHERE {table_name}.email = '{email}' AND {table_name}.password = {password};"
                       .format(table_name=table_name, email=email, password=password))
        return cursor.fetchone()
    except Exception as e:
        print("Error is {}".format(e))


def get_gpm_or_member_details(table_name, email, password):
    """
    Method to get the gpm or member details
    :param table_name: name of the table (GPM or MEMBER)
    :param email: email in particular table
    :param password: password in particular table
    :return:
    """
    try:
        cursor.execute("SELECT {table_name}.id , {table_name}.name, {table_name}.asignee_id "
                       "FROM {table_name} "
                       "WHERE {table_name}.email = '{email}' AND {table_name}.password = {password};"
                       .format(table_name=table_name, email=email, password=password))
        return cursor.fetchone()
    except Exception as e:
        print("Error is {}".format(e))


def update_gpm_data(table_name, email, item_key, item_value, asignee_id):
    """
    Method to update the gpm data
    :param table_name: gpm table name
    :param email: email of the gpm
    :param item_key: item key
    :param item_value: item value
    :param asignee_id: bdo id
    :return: null
    """
    try:
        cursor.execute(
            "SELECT {table_name}.email "
            "FROM {table_name} "
            "WHERE {table_name}.email='{email}' "
            "AND {table_name}.asignee_id={asignee_id}".format(
                table_name=table_name,
                email=email,
                asignee_id=asignee_id))

        if cursor.fetchone() is not None:
            cursor.execute("UPDATE {table_name} "
                           "SET {item_key}={item_value} "
                           "WHERE {table_name}.email='{email}'".format(table_name=table_name,
                                                                       item_key=item_key,
                                                                       item_value=item_value,
                                                                       email=email))
            conn.commit()
            print("Data successfully Updated")
        else:
            print("Not Authorized..! Please Try with valid details")

    except Exception as e:
        print("Error is {}".format(e))


def update_item_details(table_name, item_id, item_key, item_value):
    """
    MEthod to update the item details
    :param table_name: table name
    :param item_id: item id
    :param item_key: item key
    :param item_value: item value
    :return: null
    """
    cursor.execute("UPDATE {table_name} "
                   "SET {item_key}={item_value} "
                   "WHERE {table_name}.id={item_id}".format(table_name=table_name,
                                                            item_key=item_key,
                                                            item_value=item_value,
                                                            item_id=item_id))
    conn.commit()
    print("Data successfully Updated")


def get_item_for_asignee(table_name, asignee_id):
    """
    Method to get item details in the asignee
    :param table_name: table name
    :param asignee_id: asignee id
    :return: null
    """
    cursor.execute(
        "SELECT {table_name}.id , {table_name}.name "
        "FROM {table_name} "
        "WHERE {table_name}.asignee_id={asignee_id}".format(
            table_name=table_name,
            asignee_id=asignee_id))

    return cursor.fetchall()


def delete_item_from_table(table_name, item_id, key):
    """
    Methos to delete item for a specific table
    :param table_name: table name
    :param item_id: item id
    :param key: key of the field to be deleted
    :return: null
    """
    try:
        cursor.execute("DELETE from {table_name} "
                       "WHERE {table_name}.{key} = {id};".format(table_name=table_name,
                                                                 id=item_id,
                                                                 key=key))
        conn.commit()
        print("Item Successfully deleted")

    except Exception as e:
        print("Error as {}".format(e))


def insert_member_table(table_name, name, email, password, gender, age, address, area, pincode, gpm_id):
    """
    Method to inser data into the member data
    :param table_name: table name for the member
    :param name: name of the member
    :param email: email of the member
    :param password: password of the member
    :param gender: gender of the member
    :param age: age of the member
    :param address: address of the member
    :param area: area of the member
    :param pincode: pincode of the member
    :param gpm_id: gpm id under whom the member lies
    :return: null
    """
    try:
        cursor.execute(
            "INSERT INTO {table_name}(name, email, password, gender, age, address, area, pincode, asignee_id) "
            "VALUES ('{name}','{email}',{password},'{gender}',{age},'{address}','{area}',{pincode},{asignee_id});".format(
                table_name=table_name,
                name=name,
                email=email,
                password=password,
                gender=gender,
                age=age,
                address=address,
                area=area,
                pincode=pincode,
                asignee_id=gpm_id))

        conn.commit()
    except Exception as e:
        print("Error as {}".format(e))


def fetch_job_id_data(table_name, item_id):
    """
    Method to fetch the job id of the member
    :param table_name: table name of member
    :param item_id: item id of the member requested
    :return: null
    """
    cursor.execute("SELECT {table_name}.name , {table_name}.age, {table_name}.gender, {table_name}.area, "
                   "{table_name}.address "
                   "FROM {table_name} "
                   "WHERE {table_name}.id = {item_id};".format(table_name=table_name, item_id=item_id))
    return cursor.fetchone()


def get_project_details(table_name_project, project_id):
    """
    Method to get the project details
    :param table_name_project: project table name
    :param project_id: id of te project
    :return: null
    """
    cursor.execute("SELECT {table_name}.total_member , {table_name}.start_date, {table_name}.end_date "
                   "FROM {table_name} "
                   "WHERE {table_name}.id={project_id};".format(table_name=table_name_project,
                                                                project_id=project_id))
    return cursor.fetchone()


def get_project_allocated_strength(table_name_project_detail, project_id):
    """
    Method to get the allocated strength of members in the project
    :param table_name_project_detail: project details table name
    :param project_id: id of the project
    :return: null
    """
    cursor.execute('SELECT {table_name}.member_id '
                   'FROM {table_name} '
                   'WHERE {table_name}.project_id={project_id};'.format(table_name=table_name_project_detail,
                                                                        project_id=project_id))
    result_data = cursor.fetchall()
    if result_data is not None:
        return len(result_data)
    else:
        return 0


def check_member_not_present(table_name_project_detail, item_id):
    """
    Method to check if the member is present or not in the database
    :param table_name_project_detail: table name for project name details
    :param item_id: item id
    :return: null
    """
    try:
        cursor.execute("SELECT {table_name}.member_id "
                       "FROM {table_name} "
                       "WHERE {table_name}.member_id={member_id};".format(table_name=table_name_project_detail,
                                                                          member_id=item_id))
        if cursor.fetchone() is not None:
            return False
        else:
            return True
    except Exception as e:
        print("Error as {}".format(e))


def assign_member_to_project(table_name_project_detail, item_id, project_id, gpm_id, bdo_id, onboarding_date,
                             end_date):
    """
    Method to assign member to a project
    :param table_name_project_detail: project detail table name
    :param item_id: item id
    :param project_id: project id
    :param gpm_id: gpm id
    :param bdo_id: bdo id
    :param onboarding_date: onboarding date
    :param end_date: end date of the project
    :return: null
    """
    cursor.execute(
        "INSERT INTO {table_name}(member_id, project_id, onboarding_date, end_date, asignee_id, reviewer_id) "
        "VALUES ({member_id},{project_id},'{onboarding_date}','{end_date}',{asignee_id},{reviewer_id});".format(
            table_name=table_name_project_detail,
            member_id=item_id,
            project_id=project_id,
            onboarding_date=onboarding_date,
            end_date=end_date,
            asignee_id=gpm_id,
            reviewer_id=bdo_id))

    conn.commit()


def get_member_project_details(table_name_project_details, project_id, asignee_id):
    cursor.execute("SELECT {table_name}.member_id, {table_name}.project_id, {table_name}.onboarding_date, "
                   "{table_name}.end_date "
                   "FROM {table_name} "
                   "WHERE {table_name}.project_id={project_id} "
                   "AND {table_name}.request_status = 1 "
                   "AND {table_name}.asignee_id={asignee_id};".format(table_name=table_name_project_details,
                                                                      project_id=project_id,
                                                                      asignee_id=asignee_id))
    return cursor.fetchall()


def insert_wage_table(table_name_wage_approval, member_id, project_id, amount, number_of_days_worked, bdo_id):
    """
    Method ot insert calculated data int othe wage table
    :param table_name_wage_approval: wage approval table name
    :param member_id: member id
    :param project_id: project id
    :param amount: amount
    :param number_of_days_worked: total days worked
    :param bdo_id: bdo id
    :return: null
    """
    cursor.execute("INSERT INTO {table_name}(member_id, project_id, amount, days_worked, reviewer_id) "
                   "VALUES ({member_id},{project_id},{amount},"
                   "{days_worked},{reviewer_id});".format(table_name=table_name_wage_approval,
                                                          member_id=member_id,
                                                          project_id=project_id,
                                                          amount=amount,
                                                          days_worked=number_of_days_worked,
                                                          reviewer_id=bdo_id))
    conn.commit()


def is_project_wage_not_pending(table_name, project_id):
    """
    Method to check if the project has pending wages or not
    :param table_name: table name for the project
    :param project_id: project id
    :return: null
    """
    cursor.execute("SELECT {table_name}.project_id "
                   "FROM {table_name} "
                   "WHERE {table_name}.project_id={project_id};".format(table_name=table_name,
                                                                        project_id=project_id))
    if cursor.fetchone() is not None:
        return False
    else:
        return True


def fetch_pending_request_for_project(table_name_project_details, project_id, reviewer_id):
    """ Method to fetch the pending request for a given project"""
    cursor.execute("SELECT {table_name}.member_id, {table_name}.project_id, {table_name}.onboarding_date "
                   "FROM {table_name} "
                   "WHERE {table_name}.project_id={project_id} "
                   "AND {table_name}.request_status=0 "
                   "AND {table_name}.reviewer_id={reviewer_id};".format(table_name=table_name_project_details,
                                                                        project_id=project_id,
                                                                        reviewer_id=reviewer_id))
    print("SELECT {table_name}.member_id, {table_name}.project_id, {table_name}.onboarding_date "
          "FROM {table_name} "
          "WHERE {table_name}.project_id={project_id} "
          "AND {table_name}.request_status=0 "
          "AND {table_name}.reviewer_id={reviewer_id};".format(table_name=table_name_project_details,
                                                               project_id=project_id,
                                                               reviewer_id=reviewer_id))
    return cursor.fetchall()


def approve_pending_details_for_project(table_name, item_id, item_key, item_value):
    """ Method to approve the pending request for member in the project"""
    cursor.execute("UPDATE {table_name} "
                   "SET {item_key}={item_value} "
                   "WHERE {table_name}.member_id={item_id}".format(table_name=table_name,
                                                                   item_key=item_key,
                                                                   item_value=item_value,
                                                                   item_id=item_id))
    conn.commit()
    print("Data successfully Updated")


def delete_member_wage_data(table_name_wage_approval, member_id):
    """
    Metohd ot delete wage data for a member once approved
    :param table_name_wage_approval: wage approval table name
    :param member_id: member id to be deleted
    :return: null
    """
    try:
        cursor.execute("DELETE from {table_name} "
                       "WHERE {table_name}.member_id = {id};".format(table_name=table_name_wage_approval,
                                                                     id=member_id))
        conn.commit()
    except Exception as e:
        print("Error as {}".format(e))


def fetch_wage_data_for_project(table_name_wage_approval, project_id, bdo_id):
    """
    Metthod to fetch all the wage data for the project
    :param table_name_wage_approval: wage approval table
    :param project_id: project id
    :param bdo_id: author or bdo id
    :return:
    """
    try:
        cursor.execute("SELECT {table_name}.member_id, {table_name}.amount, {table_name}.days_worked "
                       "FROM {table_name} "
                       "WHERE {table_name}.project_id={project_id} "
                       "AND {table_name}.reviewer_id={review_id};".format(table_name=table_name_wage_approval,
                                                                          project_id=project_id,
                                                                          review_id=bdo_id))
        return cursor.fetchall()
    except Exception as e:
        print("Error as {}".format(e))


def fetch_bdo_id(asignee_gpm_id):
    """
    Method to get the author id or bdo id
    :param asignee_gpm_id: gpm id
    :return: null
    """
    cursor.execute("SELECT GPM.asignee_id  "
                   "FROM GPM "
                   "WHERE GPM.id={id};"
                   .format(id=asignee_gpm_id))
    return cursor.fetchone()[0]


def fetch_wage_for_member(member_id):
    """
    Method to get wage for a member
    :param member_id: member id
    :return: null
    """
    cursor.execute("SELECT MEMBER.wage  "
                   "FROM MEMBER "
                   "WHERE MEMBER.id={id};"
                   .format(id=member_id))
    return cursor.fetchone()[0]


def raise_complaint(table_name, member_id, message, raise_to, raise_to_id, raise_date):
    """
    Method for the member to raise the compalain
    :param table_name: table name
    :param member_id: memeber id
    :param message: message raised by the member
    :param raise_to: raise to gpm or bdo
    :param raise_to_id: raise to id
    :param raise_date: raise date
    :return: null
    """
    cursor.execute("INSERT INTO {table_name}(member_id, message, raise_to, authority_id, date) "
                   "VALUES ({member_id},'{message}','{to}',{id},'{date}');".format(table_name=table_name,
                                                                                   member_id=member_id,
                                                                                   message=message,
                                                                                   to=raise_to,
                                                                                   id=raise_to_id,
                                                                                   date=raise_date))
    conn.commit()


def fetch_complaints_by_authority(table_name, authority_id, raise_to):
    """
    Metohd to fetch complains by authority i.e BDO or GPM
    :param table_name: table name as per authority
    :param authority_id: authority id
    :param raise_to: raise to field
    :return: null
    """
    try:
        cursor.execute("SELECT {table_name}.id, {table_name}.member_id, {table_name}.message, {table_name}.date "
                       "FROM {table_name} "
                       "WHERE {table_name}.authority_id={authority_id} "
                       "AND {table_name}.raise_to='{raise_to}';".format(table_name=table_name,
                                                                        authority_id=authority_id,
                                                                        raise_to=raise_to))
        return cursor.fetchall()

    except Exception as e:
        print("Error as {}".format(e))


def set_gpm_field_as_null(table_name, key, field, gpm_id):
    """
    Function to set gpm field as null when a gpm is deleted
    :param table_name: table name
    :param key: key for the gpm details
    :param field: data for the field
    :param gpm_id: gpm id
    :return:
    """
    try:
        cursor.execute(
            'UPDATE {table_name} SET {key}=NULL WHERE {table_name}.{field}={gpm_id}'.format(table_name=table_name,
                                                                                            key=key,
                                                                                            field=field,
                                                                                            gpm_id=gpm_id))
        conn.commit()
    except Exception as e:
        print("Error as {}".format(e))
