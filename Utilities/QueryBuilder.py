import sqlite3 as sq
import Utilities.Constants as ct
import logging

conn = sq.connect(ct.Database_Path)
cursor = conn.cursor()


def create_table(table_name, *args):
    value = ''
    for item in args:
        value += item + ','
    value = value[:-1]
    cursor.execute("CREATE TABLE IF NOT EXISTS {table_name} ({value});".format(table_name=table_name, value=value))
    logging.info("Table with {} name created".format(table_name))


def delete_gpm(table_name, asignee_id, email):
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


def insert_bdo_table(table_name,
                     name, email, password):
    cursor.execute(
        "INSERT INTO {}(name, email, password) VALUES ('{}','{}',{});".format(table_name, name, email, password))
    conn.commit()
    logging.info("Item is inserted into table {}".format(table_name))


def insert_gpm_table(table_name,
                     name, email, password, area, pincode, asignee_id):
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
    logging.info("Item is inserted into table {}".format(table_name))


def insert_project_table(table_name, name, area, total_member, cost_estimate, project_type, start_date,
                         end_date, asignee_id):
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


def validate_credential(table_name, email, password):
    cursor.execute("SELECT {table_name}.password FROM {table_name} WHERE {table_name}.email = '{email}';".format(
        table_name=table_name, email=email))
    db_password = cursor.fetchone()
    if db_password is not None and db_password[0] == password:
        return True
    else:
        return False


def get_bdo_details(table_name, email, password):
    # noinspection PyStringFormat
    cursor.execute("SELECT {table_name}.id , {table_name}.name "
                   "FROM {table_name} "
                   "WHERE {table_name}.email = '{email}' AND {table_name}.password = {password};"
                   .format(table_name=table_name, email=email, password=password))
    return cursor.fetchone()


def get_gpm_or_member_details(table_name, email, password):
    cursor.execute("SELECT {table_name}.id , {table_name}.name, {table_name}.asignee_id "
                   "FROM {table_name} "
                   "WHERE {table_name}.email = '{email}' AND {table_name}.password = {password};"
                   .format(table_name=table_name, email=email, password=password))
    return cursor.fetchone()


def check_if_email_present(table_name, email):
    cursor.execute("SELECT {table_name}.email FROM {table_name} WHERE {table_name}.email = '{email}';".format(
        table_name=table_name, email=email))
    if cursor.fetchone() is not None:
        return True
    return False


def update_gpm_data(table_name, email, item_key, item_value, asignee_id):
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
                       "SET {item_key}={item_value}"
                       "WHERE {table_name}.email='{email}'".format(table_name=table_name,
                                                                   item_key=item_key,
                                                                   item_value=item_value,
                                                                   email=email))
        conn.commit()
        print("Data successfully Updated")
    else:
        print("Not Authorized..! Please Try with valid details")


def update_item_details(table_name, item_id, item_key, item_value):
    cursor.execute("UPDATE {table_name} "
                   "SET {item_key}={item_value} "
                   "WHERE {table_name}.id={item_id}".format(table_name=table_name,
                                                            item_key=item_key,
                                                            item_value=item_value,
                                                            item_id=item_id))
    conn.commit()
    print("Data successfully Updated")


def get_item_for_asignee(table_name, asignee_id):
    cursor.execute(
        "SELECT {table_name}.id , {table_name}.name "
        "FROM {table_name} "
        "WHERE {table_name}.asignee_id={asignee_id}".format(
            table_name=table_name,
            asignee_id=asignee_id))

    return cursor.fetchall()


def delete_item_from_table(table_name, item_id, key):
    cursor.execute("DELETE from {table_name} "
                   "WHERE {table_name}.{key} = {id};".format(table_name=table_name,
                                                             id=item_id,
                                                             key=key))
    conn.commit()
    print("Item Successfully deleted")


def insert_member_table(table_name, name, email, password, gender, age, address, area, pincode, gpm_id):
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


def fetch_job_id_data(table_name, item_id):
    cursor.execute("SELECT {table_name}.name , {table_name}.age, {table_name}.gender, {table_name}.area, "
                   "{table_name}.address "
                   "FROM {table_name} "
                   "WHERE {table_name}.id = {item_id};".format(table_name=table_name, item_id=item_id))
    return cursor.fetchone()


def get_project_details(table_name_project, project_id):
    cursor.execute("SELECT {table_name}.total_member , {table_name}.start_date, {table_name}.end_date "
                   "FROM {table_name} "
                   "WHERE {table_name}.id={project_id};".format(table_name=table_name_project,
                                                                project_id=project_id))
    return cursor.fetchone()


def get_project_allocated_strength(table_name_project_detail, project_id):
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
    cursor.execute("SELECT {table_name}.member_id "
                   "FROM {table_name} "
                   "WHERE {table_name}.member_id={member_id};".format(table_name=table_name_project_detail,
                                                                      member_id=item_id))
    if cursor.fetchone() is not None:
        return False
    else:
        return True


def assign_member_to_project(table_name_project_detail, item_id, project_id, gpm_id, bdo_id, onboarding_date,
                             end_date):
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
    cursor.execute("SELECT {table_name}.project_id "
                   "FROM {table_name} "
                   "WHERE {table_name}.project_id={project_id};".format(table_name=table_name,
                                                                        project_id=project_id))
    if cursor.fetchone() is not None:
        return False
    else:
        return True


def fetch_pending_request_for_project(table_name_project_details, project_id, asignee_id):
    cursor.execute("SELECT {table_name}.member_id, {table_name}.project_id, {table_name}.onboarding_date "
                   "FROM {table_name} "
                   "WHERE {table_name}.project_id={project_id} "
                   "AND {table_name}.request_status = 0 "
                   "AND {table_name}.asignee_id={asignee_id};".format(table_name=table_name_project_details,
                                                                      project_id=project_id,
                                                                      asignee_id=asignee_id))
    return cursor.fetchall()


def approve_pending_details_for_project(table_name, item_id, item_key, item_value):
    cursor.execute("UPDATE {table_name} "
                   "SET {item_key}={item_value} "
                   "WHERE {table_name}.member_id={item_id}".format(table_name=table_name,
                                                                   item_key=item_key,
                                                                   item_value=item_value,
                                                                   item_id=item_id))
    conn.commit()
    print("Data successfully Updated")


def delete_member_wage_data(table_name_wage_approval, member_id):
    cursor.execute("DELETE from {table_name} "
                   "WHERE {table_name}.member_id = {id};".format(table_name=table_name_wage_approval,
                                                                 id=member_id))
    conn.commit()


def fetch_wage_data_for_project(table_name_wage_approval, project_id, bdo_id):
    cursor.execute("SELECT {table_name}.member_id, {table_name}.amount, {table_name}.days_worked "
                   "FROM {table_name} "
                   "WHERE {table_name}.project_id={project_id} "
                   "AND {table_name}.reviewer_id={review_id};".format(table_name=table_name_wage_approval,
                                                                      project_id=project_id,
                                                                      review_id=bdo_id))
    return cursor.fetchall()


def fetch_bdo_id(asignee_gpm_id):
    cursor.execute("SELECT GPM.asignee_id  "
                   "FROM GPM "
                   "WHERE GPM.id={id};"
                   .format(id=asignee_gpm_id))
    return cursor.fetchone()[0]


def fetch_wage_for_member(member_id):
    cursor.execute("SELECT MEMBER.wage  "
                   "FROM MEMBER "
                   "WHERE MEMBER.id={id};"
                   .format(id=member_id))
    return cursor.fetchone()[0]


def raise_complaint(table_name, member_id, message, raise_to, raise_to_id, raise_date):
    cursor.execute("INSERT INTO {table_name}(member_id, message, raise_to, authority_id, date) "
                   "VALUES ({member_id},'{message}','{to}',{id},'{date}');".format(table_name=table_name,
                                                                                   member_id=member_id,
                                                                                   message=message,
                                                                                   to=raise_to,
                                                                                   id=raise_to_id,
                                                                                   date=raise_date))
    conn.commit()


def fetch_complaints_by_authority(table_name, authority_id, raise_to):
    cursor.execute("SELECT {table_name}.id, {table_name}.member_id, {table_name}.message, {table_name}.date "
                   "FROM {table_name} "
                   "WHERE {table_name}.authority_id={authority_id} "
                   "AND {table_name}.raise_to='{raise_to}';".format(table_name=table_name,
                                                                    authority_id=authority_id,
                                                                    raise_to=raise_to))
    return cursor.fetchall()


def set_gpm_field_as_null(table_name, key, field, gpm_id):
    print('UPDATE {table_name} SET {key}=NULL WHERE {table_name}.{field}={gpm_id}'.format(table_name=table_name,
                                                                                          key=key,
                                                                                          field=field,
                                                                                          gpm_id=gpm_id))
    cursor.execute(
        'UPDATE {table_name} SET {key}=NULL WHERE {table_name}.{field}={gpm_id}'.format(table_name=table_name,
                                                                                        key=key,
                                                                                        field=field,
                                                                                        gpm_id=gpm_id))
    conn.commit()
