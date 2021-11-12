from flask import Flask, jsonify
from flask_restful import Resource, Api
from json import *
from flask_cors import CORS, cross_origin


app = Flask(__name__)


import mysql.connector as mysql


db = mysql.connect(host="localhost",
                   user="austin",
                   passwd="ThisIsMyPassword",
                   database="TestDB2")

cursor = db.cursor()


def check_user_position_foreman(first_name,last_name,Address,city,state,zipcode,position_name, job_site):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = ? AND STATE = ? AND ZIPCODE = ?", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= ? AND LAST_NAME = ? AND ADDRESS = ? AND  CITY_STATE_ZIP_ID = ? ", [first_name,last_name,Address,city_state_zip[0]])
    person = cursor.fetchone()
    cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = ?", [position_name])
    position = cursor.fetchone()
    cursor.execute("SELECT POSITION_ID FROM SALARIED_EMPLOYEE WHERE PERSON_ID = ? AND POSITION_ID=?", [person[0], position[0]])
    check_position= cursor.fetchone()
    if check_position[0] == position[0]:
        get_foreman_view()
    else:
        print("you are not a foreman and can't view that")

def check_user_position_project_manager(first_name,last_name,Address,city,state,zipcode,position_name):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = ? AND STATE = ? AND ZIPCODE = ?", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= ? AND LAST_NAME = ? AND ADDRESS = ? AND  CITY_STATE_ZIP_ID = ? ", [first_name,last_name,Address,city_state_zip[0]])
    person = cursor.fetchone()
    cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = ?", [position_name])
    position = cursor.fetchone()
    cursor.execute("SELECT POSITION_ID FROM SALARIED_EMPLOYEE WHERE PERSON_ID = ? AND POSITION_ID= ? ", [person[0], position[0]])
    check_position= cursor.fetchone()
    if check_position[0] == position[0]:
        get_project_manager_view()
    else:
        print("you are not a project manager and can't view that")

def check_user_position_general_manager(first_name,last_name,Address,city,state,zipcode,position_name):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = ? AND STATE = ? AND ZIPCODE = ?", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= ? AND LAST_NAME = ? AND ADDRESS = ? AND  CITY_STATE_ZIP_ID = ? ", [first_name,last_name,Address,city_state_zip[0]])
    person = cursor.fetchone()
    cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = ?", [position_name])
    position = cursor.fetchone()
    cursor.execute("SELECT POSITION_ID FROM SALARIED_EMPLOYEE WHERE PERSON_ID = ? AND POSITION_ID=?", [person[0], position[0]])
    check_position= cursor.fetchone()
    if check_position[0] == position[0]:
        get_general_manager_view()
    else:
        print("you are not a general manager and can't view that")


def change_hours_used_on_work_package(job_name, work_package_name, hours_used):
    cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME=?", [job_name])
    job_id = cursor.fetchone();
    cursor.execute("UPDATE WORK_PACKAGE SET HOURS_USED = ? WHERE WORK_PACKAGE_NAME = ? AND JOB_SITE_ID = ?", [hours_used,work_package_name, job_id[0]])
    db.commit()

def change_material_amount_used_in_work_package(work_package_name, job_site_name, inventory_name, amount_used):
    cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME = ?", [job_site_name])
    job_site = cursor.fetchone()
    cursor.execute("SELECT WORK_PACKAGE_ID FROM WORK_PACKAGE WHERE WORK_PACKAGE_NAME = ? AND JOB_SITE_ID = ?", [work_package_name,job_site])
    work_package = cursor.fetchone()
    cursor.execute("SELECT INVENTORY_ID FROM INVENTORY WHERE MATERIAL_NAME = ?", [inventory_name])
    inventory = cursor.fetchone()
    cursor.execute("UPDATE MATERIAL_IN_WORK_PACKAGE SET AMOUNT_USED =? WHERE INVENTORY_ID = ? AND WORK_PACKAGE_ID = ?", [amount_used, inventory[0],work_package[0]])
    db.commit()

def get_foreman_view(job_site_name):
    cursor.execute("SELECT * FROM FOREMAN WHERE JOB_SITE_NAME=?", [job_site_name])
    result = cursor.fetchall()
    columns = ["Work Package",  "Electrician First Name", "Electrician Last Name", "Individual Hours Given"]
    format_row = "{:>28}" * (len(result[0]) + 1)
    print(format_row.format("", *columns))
    for row in result:
        print(format_row.format(" ", *row))
    return jsonify(result)

def get_project_manager_view():
    cursor.execute("SELECT * FROM PROJECT_MANAGER")
    result = cursor.fetchall()
    columns = ["Work Package",  "Hours Used", "Material Cost", "Cost of Work Package","Amount Made","Profits", "Site"]
    format_row = "{:>28}" * (len(result[0]) + 1)
    print(format_row.format("", *columns))
    for row in result:
        print(format_row.format(" ", *row))
    return jsonify(result)

def get_general_manager_view():
    cursor.execute("SELECT * FROM GENERAL_MANAGER")
    result = cursor.fetchall()
    columns = ["Project Cost",  "Project Price", "Profits", "Days On Project"]
    format_row = "{:>28}" * (len(result[0]) + 1)
    print(format_row.format("", *columns))
    for row in result:
        print(format_row.format(" ", *row))
    return jsonify(result)



def insert_into_location(location_name):
    cursor.execute("INSERT INTO LOCATION (LOCATION_NAME) VALUES (?);", [location_name])
    db.commit()

def delete_from_location(location_name):
    cursor.execute("DELETE FROM LOCATION WHERE LOCATION_NAME = ?;", [location_name])
    db.commit()


def insert_into_city_state_zip(city,state,zipcode):
    cursor.execute("INSERT INTO CITY_STATE_ZIP (CITY,STATE,ZIPCODE) VALUES (?,?,?);", [city,state,zipcode])
    db.commit()

def delete_from_city_state_zip(city,state,zipcode):
    cursor.execute("DELETE FROM CITY_STATE_ZIP WHERE CITY= ? AND STATE = ? AND ZIPCODE = ?);", [city,state,zipcode])
    db.commit()



def insert_into_person(first_name,last_name,Address,city,state,zipcode):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = ? AND STATE = ? AND ZIPCODE = ?", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    cursor.execute("INSERT INTO PERSON (FIRST_NAME,LAST_NAME,ADDRESS, CITY_STATE_ZIP_ID) VALUES (?,?,?,?);", [first_name,last_name, Address, city_state_zip[0]])
    db.commit()

def delete_from_person(first_name,last_name,Address,city,state,zipcode):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = ? AND STATE = ? AND ZIPCODE = ?", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    cursor.execute("DELETE FROM PERSON WHERE FIRST_NAME = ? AND LAST_NAME = ? AND ADDRESS = ? AND CITY_STATE_ZIP_ID = ?;", [first_name,last_name, Address, city_state_zip[0]])
    db.commit()



def insert_into_inventory(material_name, cost_per_unit, weight_per_unit):
    cursor.execute("INSERT INTO INVENTORY (MATERIAL_NAME,COST_PER_UNIT,WEIGHT_PER_UNIT) VALUES (?,?,?);", [material_name, cost_per_unit, weight_per_unit])
    db.commit()

def delete_from_inventory(material_name, cost_per_unit, weight_per_unit):
    cursor.execute("DELETE FROM INVENTORY WHERE MATERIAL_NAME = ? AND COST_PER_UNIT = ? AND WEIGHT_PER_UNIT = ?;", [material_name, cost_per_unit, weight_per_unit])
    db.commit()



def insert_into_position(position):
    cursor.execute(" INSERT INTO EMPLOYEE_POSITION (POSITION_NAME) VALUES (?);", [position])
    db.commit()

def delete_from_position(position):
    cursor.execute(" DELETE FROM EMPLOYEE_POSITION WHERE POSITION_NAME = ?;", [position])
    db.commit()



def insert_into_job_site(location_name, site_name, start_date):
    cursor.execute("SELECT LOCATION_ID FROM LOCATION WHERE LOCATION_NAME=?", [location_name])
    location = cursor.fetchone()
    cursor.execute("INSERT INTO JOB_SITE (SITE_NAME,LOCATION_ID,START_DATE) VALUES (?,?,?);", [site_name, location[0],start_date])
    db.commit()

def delete_from_job_site(location_name, site_name, start_date):
    cursor.execute("SELECT LOCATION_ID FROM LOCATION WHERE LOCATION_NAME=?", [location_name])
    location = cursor.fetchone()
    cursor.execute("DELETE FROM JOB_SITE WHERE SITE_NAME = ? AND LOCATION_ID = ? AND START_DATE = ?;", [site_name, location[0],start_date])
    db.commit()



def insert_into_work_package(job_site_name, work_package_name, price_of_work, hours_alloted):
    cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME = ?", [job_site_name])
    job_site = cursor.fetchone()
    cursor.execute("INSERT INTO WORK_PACKAGE (JOB_SITE_ID ,WORK_PACKAGE_NAME ,PRICE_OF_WORK, HOURS_ALLOTED,HOURS_USED) VALUES (?,?,?,?);", [job_site[0], work_package_name, price_of_work, hours_alloted,0])
    db.commit()

def delete_from_work_package(job_site_name, work_package_name, price_of_work, hours_alloted):
    cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME = ?", [job_site_name])
    job_site = cursor.fetchone()
    cursor.execute("DELETE FROM WORK_PACKAGE WHERE JOB_SITE_ID = ? AND WORK_PACKAGE_NAME = ? AND PRICE_OF_WORK = ? AND  HOURS_ALLOTED,HOURS_USED = ?;", [job_site[0], work_package_name, price_of_work, hours_alloted,0])
    db.commit()



def insert_into_electrician(first_name,last_name,Address,city,state,zipcode, years_employed, hourly_rate, position_name):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = ? AND STATE = ? AND ZIPCODE = ?", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= ? AND LAST_NAME = ? AND ADDRESS = ? AND  CITY_STATE_ZIP_ID = ? ", [first_name,last_name,Address,city_state_zip[0]])
    person = cursor.fetchone()
    cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = ?", [position_name])
    position = cursor.fetchone()
    cursor.execute("INSERT INTO ELECTRICIAN(PERSON_ID,POSITION_ID,YEARS_EMPLOYED, HOURLY_RATE) VALUES (?, ?, ?, ?);", [person[0],position[0],years_employed,hourly_rate])
    db.commit()

def delete_from_electrician(first_name,last_name,Address,city,state,zipcode, years_employed, hourly_rate, position_name):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = ? AND STATE = ? AND ZIPCODE = ?", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= ? AND LAST_NAME = ? AND ADDRESS = ? AND  CITY_STATE_ZIP_ID = ? ", [first_name,last_name,Address,city_state_zip[0]])
    person = cursor.fetchone()
    cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = ?", [position_name])
    position = cursor.fetchone()
    cursor.execute("DELETE FROM ELECTRICIAN WHERE PERSON_ID = ? AND POSITION_ID = ? AND YEARS_EMPLOYED = ? AND HOURLY_RATE = ?;", [person[0],position[0],years_employed,hourly_rate])
    db.commit()



def insert_into_electrician_on_work_package(first_name,last_name,position_name,address, work_package_name, job_site_name):
    cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = ?", [position_name])
    position = cursor.fetchone()
    cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= ? AND LAST_NAME = ? AND ADDRESS = ? ", [first_name,last_name,address])
    person = cursor.fetchone()
    cursor.execute("SELECT ELECTRICIAN_ID FROM ELECTRICIAN WHERE PERSON_ID = ? AND POSITION_ID = ?", [person,position[0]])
    electrician = cursor.fetchone()
    cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME = ?", [job_site_name])
    job_site = cursor.fetchone()
    cursor.execute("SELECT WORK_PACKAGE_ID FROM WORK_PACKAGE WHERE WORK_PACKAGE_NAME = ? AND JOB_SITE_ID = ?", [work_package_name,job_site[0]])
    work_package = cursor.fetchone()
    cursor.execute("INSERT INTO ELECTRICIAN_ON_WORK_PACKAGE(ELECTRICIAN_ID,WORK_PACKAGE_ID) VALUES (?,?);", [electrician[0],work_package[0]])
    db.commit()

def delete_from_electrician_on_work_package(first_name,last_name,position_name,address, work_package_name, job_site_name):
    cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = ?", [position_name])
    position = cursor.fetchone()
    cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= ? AND LAST_NAME = ? AND ADDRESS = ? ", [first_name,last_name,address])
    person = cursor.fetchone()
    cursor.execute("SELECT ELECTRICIAN_ID FROM ELECTRICIAN WHERE PERSON_ID = ? AND POSITION_ID = ?", [person,position[0]])
    electrician = cursor.fetchone()
    cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME = ?", [job_site_name])
    job_site = cursor.fetchone()
    cursor.execute("SELECT WORK_PACKAGE_ID FROM WORK_PACKAGE WHERE WORK_PACKAGE_NAME = ? AND JOB_SITE_ID = ?", [work_package_name,job_site[0]])
    work_package = cursor.fetchone()
    cursor.execute("DELETE FROM ELECTRICIAN_ON_WORK_PACKAGE WHERE ELECTRICIAN_ID = ? AND WORK_PACKAGE_ID = ?;", [electrician[0],work_package[0]])
    db.commit()



def insert_into_material_in_work_package(inventory_name, work_package_name, job_site_name, material_amount_issued,material_amount_used):
    cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME = ?", [job_site_name])
    job_site = cursor.fetchone()
    cursor.execute("SELECT WORK_PACKAGE_ID FROM WORK_PACKAGE WHERE WORK_PACKAGE_NAME = ? AND JOB_SITE_ID = ?", [work_package_name,job_site])
    work_package = cursor.fetchone()
    cursor.execute("SELECT INVENTORY_ID FROM INVENTORY WHERE MATERIAL_NAME = ?", [inventory_name])
    inventory = cursor.fetchone()
    cursor.execute("INSERT INTO MATERIAL_IN_WORK_PACKAGE(WORK_PACKAGE_ID,INVENTORY_ID,AMOUNT_ALLOTED,AMOUNT_USED) VALUES (?, ?, ?, ?);", [inventory[0], work_package[0], material_amount_issued, material_amount_used])
    db.commit()

def delete_from_material_in_work_package(inventory_name, work_package_name, job_site_name, material_amount_issued,material_amount_used):
    cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME = ?", [job_site_name])
    job_site = cursor.fetchone()
    cursor.execute("SELECT WORK_PACKAGE_ID FROM WORK_PACKAGE WHERE WORK_PACKAGE_NAME = ? AND JOB_SITE_ID = ?", [work_package_name,job_site])
    work_package = cursor.fetchone()
    cursor.execute("SELECT INVENTORY_ID FROM INVENTORY WHERE MATERIAL_NAME = ?", [inventory_name])
    inventory = cursor.fetchone()
    cursor.execute("DELETE FROM MATERIAL_IN_WORK_PACKAGE WHERE WORK_PACKAGE_ID = ? AND INVENTORY_ID = ? AND AMOUNT_ALLOTED = ? AND AMOUNT_USED = ?;", [inventory[0], work_package[0], material_amount_issued, material_amount_used])
    db.commit()

@app.route('/')
@cross_origin()
def get_all_jobs():
    locations = []
    cursor.execute("SELECT SITE_NAME FROM JOB_SITE")
    jobs = cursor.fetchall()
    cursor.execute("SELECT LOCATION_ID FROM JOB_SITE")
    location_id = cursor.fetchall()
    return jsonify(jobs)


def get_work_packages_on_job(job_site_name):
    cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME = %s", [job_site_name])
    job_site = cursor.fetchone()
    cursor.execute("SELECT WORK_PACKAGE_NAME, PRICE_OF_WORK, HOURS_ALLOTED, HOURS_USED FROM WORK_PACKAGE WHERE JOB_SITE_ID = %s", [job_site[0]])
    work_packages = cursor.fetchall()
    for x in work_packages:
        print("Work package name: " + x[0] + "\nJob site of work package: " + job_site_name +"\nPrice charged to customer: " + str(x[1]) + "\nHours alloted for work: " + str(x[2]) +"\nHours used for work: " + str(x[3]) + '\n\n')

def get_jobs_by_location(location_name):
    val = [location_name]
    cursor.execute("SELECT * FROM LOCATION")
    location = cursor.fetchall()
    for x in location:
        if x[1] == location_name:
            val = x[0]
    cursor.execute("SELECT SITE_NAME,START_DATE FROM JOB_SITE WHERE LOCATION_ID=%s", [val])
    jobs = cursor.fetchall()
    for job in jobs:
        print("Job Name: " +job[0] + "\nLocation: " + location_name +  "\nStart date: " + str(job[1]) + "\n\n")






if __name__ == '__main__':
    app.run(debug=True)