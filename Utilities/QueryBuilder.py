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
        "SELECT {table_name}.email "
        "FROM {table_name} "
        "WHERE {table_name}.email = '{email}' "
        "AND {table_name}.asignee_id = {asignee_id};".format(
            table_name=table_name,
            email=email,
            asignee_id=asignee_id))
    if cursor.fetchone() is not None:
        cursor.execute("DELETE from {table_name} "
                       "WHERE {table_name}.email = '{email}' "
                       "AND {table_name}.asignee_id = {asignee_id};".format(table_name=table_name,
                                                                            email=email,
                                                                            asignee_id=asignee_id))
        conn.commit()
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
        "INSERT INTO {}(name, email, password, area, pincode, asignee_id) VALUES ('{}','{}',{},'{}',{},{});"
            .format(table_name, name, email, password, area, pincode, asignee_id))
    conn.commit()
    logging.info("Item is inserted into table {}".format(table_name))
    # TODO : delete all the member data related to a particular gpm


def insert_project_table(table_name, name, area, total_member, cost_estimate, type, start_date, end_date, asignee_id):
    # noinspection PyStringFormat
    print(
        "INSERT INTO {table_name}(name, area, total_member, cost_estimate, start_date, end_date, asignee_id) "
        "VALUES ('{name}','{area}',{total_member}, {cost_estimate},'{type}',{start_date},{end_date},{asignee_id});".format(
            table_name=table_name,
            name=name,
            area=area,
            total_member=total_member,
            cost_estimate=cost_estimate,
            type=type,
            start_date=start_date,
            end_date=end_date,
            asignee_id=asignee_id))

    cursor.execute(
        "INSERT INTO {table_name}(name, area, total_member, cost_estimate, type, start_date, end_date, asignee_id) "
        "VALUES ('{name}','{area}',{total_member}, {cost_estimate},'{type}',{start_date},{end_date},{asignee_id});".format(
            table_name=table_name,
            name=name,
            area=area,
            total_member=total_member,
            cost_estimate=cost_estimate,
            type=type,
            start_date=start_date,
            end_date=end_date,
            asignee_id=asignee_id))

    conn.commit()


def validate_credential(table_name, email, password):
    cursor.execute("SELECT {table_name}.password FROM {table_name} WHERE {table_name}.email = '{email}';".format(
        table_name=table_name, email=email))
    db_password = cursor.fetchone()
    if db_password[0] == password:
        return True
    return False


def get_bdo_details(table_name, email, password):
    # noinspection PyStringFormat
    cursor.execute("SELECT {table_name}.id , {table_name}.name "
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


def update_project_details(table_name, item_id, item_key, item_value):
    cursor.execute("UPDATE {table_name} "
                   "SET {item_key}={item_value}"
                   "WHERE {table_name}.id='{item_id}'".format(table_name=table_name,
                                                              item_key=item_key,
                                                              item_value=item_value,
                                                              item_id=item_id))
    conn.commit()
    print("Data successfully Updated")


def get_project_for_bdo(table_name, asignee_id):
    cursor.execute(
        "SELECT {table_name}.id , {table_name}.name "
        "FROM {table_name} "
        "WHERE {table_name}.asignee_id={asignee_id}".format(
            table_name=table_name,
            asignee_id=asignee_id))

    return cursor.fetchall()


def delete_project(table_name, item_id):
    cursor.execute("DELETE from {table_name} "
                   "WHERE {table_name}.id = {id};".format(table_name=table_name,
                                                          id=item_id))
    conn.commit()
    print("Project Successfully deleted")
