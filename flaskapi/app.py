from urllib import request
from datetime import datetime
import sys
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  sql
import os

app = Flask(__name__)
db = SQLAlchemy(app)


app.config['MYSQL_DATABASE_USER'] = 'austin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ThisIsMyPassword'
app.config['MYSQL_DATABASE_DB'] = 'TestDB2'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'


engine = create_engine()
conn = db.session
cursor = conn.execute("SELECT LOCATION_ID FROM JOB_SITE").cursor()

class JOB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'),
                            nullable=False)
    site_name = db.Column(db.String, unique=True, nullable=False)
    start_date = db.Column(db.datetime, unique = False, nullable=False)

    def __init__(self, site_name, start_date):
        self.site_name = site_name
        self.start_date = start_date

class EMPLOYEE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, unique=False, nullable=False)
    last_name = db.Column(db.String, unique=False, nullable=False)
    address = db.Column(db.String, unique=False, nullable=False)
    city = db.Column(db.String, unique=False, nullable=False)
    state = db.Column(db.String, unique=False, nullable=False)
    zip = db.Column(db.Integer, unique=False, nullable=False)
    position = db.Column(db.String, unique=False, nullable=False)
    pay_rate = db.Column(db.String, unique=False, nullable=False)
    years_employed = db.Column(db.Integer, unique=False, nullable=False)

class WORK_PACKAGE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String, unique=False, nullable=False)
    work_package_name = db.Column(db.String, unique=True, nullable=False)
    price_of_work = 0
    hours_alloted = 0
    hours_used = 0
class LOCATION(db.Model):
    id = db.Column(db.Integer, primary_key=True)




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
    db.connect.commit()

def change_material_amount_used_in_work_package(work_package_name, job_site_name, inventory_name, amount_used):
    cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME = ?", [job_site_name])
    job_site = cursor.fetchone()
    cursor.execute("SELECT WORK_PACKAGE_ID FROM WORK_PACKAGE WHERE WORK_PACKAGE_NAME = ? AND JOB_SITE_ID = ?", [work_package_name,job_site])
    work_package = cursor.fetchone()
    cursor.execute("SELECT INVENTORY_ID FROM INVENTORY WHERE MATERIAL_NAME = ?", [inventory_name])
    inventory = cursor.fetchone()
    cursor.execute("UPDATE MATERIAL_IN_WORK_PACKAGE SET AMOUNT_USED =? WHERE INVENTORY_ID = ? AND WORK_PACKAGE_ID = ?", [amount_used, inventory[0],work_package[0]])
    db.connect.commit()

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
    cursor.execute("SELECT LOCATION_ID FROM LOCATION WHERE LOCATION_NAME = %s", [location_name])
    location = cursor.fetchone()
    if location[0] != None:
        cursor.execute("INSERT INTO LOCATION (LOCATION_NAME) VALUES (?);", [location_name])
        db.connect.commit()

def delete_from_location(location_name):
    cursor.execute("DELETE FROM LOCATION WHERE LOCATION_NAME = ?;", [location_name])
    db.connect.commit()


def insert_into_city_state_zip(city,state,zipcode):
    cursor.execute("INSERT INTO CITY_STATE_ZIP (CITY,STATE,ZIPCODE) VALUES (?,?,?);", [city,state,zipcode])
    db.connect.commit()

def delete_from_city_state_zip(city,state,zipcode):
    cursor.execute("DELETE FROM CITY_STATE_ZIP WHERE CITY= ? AND STATE = ? AND ZIPCODE = ?);", [city,state,zipcode])
    db.connect.commit()



def insert_into_person(first_name,last_name,Address,city,state,zipcode):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = ? AND STATE = ? AND ZIPCODE = ?", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    cursor.execute("INSERT INTO PERSON (FIRST_NAME,LAST_NAME,ADDRESS, CITY_STATE_ZIP_ID) VALUES (?,?,?,?);", [first_name,last_name, Address, city_state_zip[0]])
    db.connect.commit()

def delete_from_person(first_name,last_name,Address,city,state,zipcode):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = ? AND STATE = ? AND ZIPCODE = ?", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    cursor.execute("DELETE FROM PERSON WHERE FIRST_NAME = ? AND LAST_NAME = ? AND ADDRESS = ? AND CITY_STATE_ZIP_ID = ?;", [first_name,last_name, Address, city_state_zip[0]])
    db.connect.commit()



def insert_into_inventory(material_name, cost_per_unit, weight_per_unit):
    cursor.execute("INSERT INTO INVENTORY (MATERIAL_NAME,COST_PER_UNIT,WEIGHT_PER_UNIT) VALUES (?,?,?);", [material_name, cost_per_unit, weight_per_unit])
    db.connect.commit()

def delete_from_inventory(material_name, cost_per_unit, weight_per_unit):
    cursor.execute("DELETE FROM INVENTORY WHERE MATERIAL_NAME = ? AND COST_PER_UNIT = ? AND WEIGHT_PER_UNIT = ?;", [material_name, cost_per_unit, weight_per_unit])
    db.connect.commit()



def insert_into_position(position):
    cursor.execute(" INSERT INTO EMPLOYEE_POSITION (POSITION_NAME) VALUES (?);", [position])
    db.connect.commit()

def delete_from_position(position):
    cursor.execute(" DELETE FROM EMPLOYEE_POSITION WHERE POSITION_NAME = ?;", [position])
    db.connect.commit()



def insert_into_job_site(location_name, site_name, start_date):
    cursor.execute("SELECT LOCATION_ID FROM LOCATION WHERE LOCATION_NAME=?", [location_name])
    location = cursor.fetchone()
    cursor.execute("INSERT INTO JOB_SITE (SITE_NAME,LOCATION_ID,START_DATE) VALUES (?,?,?);", [site_name, location[0],start_date])
    db.connect.commit()

def delete_from_job_site(location_name, site_name, start_date):
    cursor.execute("SELECT LOCATION_ID FROM LOCATION WHERE LOCATION_NAME=?", [location_name])
    location = cursor.fetchone()
    cursor.execute("DELETE FROM JOB_SITE WHERE SITE_NAME = ? AND LOCATION_ID = ? AND START_DATE = ?;", [site_name, location[0],start_date])
    db.connect.commit()



def insert_into_work_package(job_site_name, work_package_name, price_of_work, hours_alloted):
    cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME = ?", [job_site_name])
    job_site = cursor.fetchone()
    cursor.execute("INSERT INTO WORK_PACKAGE (JOB_SITE_ID ,WORK_PACKAGE_NAME ,PRICE_OF_WORK, HOURS_ALLOTED,HOURS_USED) VALUES (?,?,?,?);", [job_site[0], work_package_name, price_of_work, hours_alloted,0])
    db.connect.commit()

def delete_from_work_package(job_site_name, work_package_name, price_of_work, hours_alloted):
    cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME = ?", [job_site_name])
    job_site = cursor.fetchone()
    cursor.execute("DELETE FROM WORK_PACKAGE WHERE JOB_SITE_ID = ? AND WORK_PACKAGE_NAME = ? AND PRICE_OF_WORK = ? AND  HOURS_ALLOTED,HOURS_USED = ?;", [job_site[0], work_package_name, price_of_work, hours_alloted,0])
    db.connect.commit()



def insert_into_electrician(first_name,last_name,Address,city,state,zipcode, years_employed, hourly_rate, position_name):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = ? AND STATE = ? AND ZIPCODE = ?", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    if city_state_zip == None:
        cursor.execute("INSERT INTO CITY_STATE_ZIP (CITY,STATE,ZIPCODE) VALUES (?,?,?);", [city,state,zipcode])
        db.connect.commit()
    cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= ? AND LAST_NAME = ? AND ADDRESS = ? AND  CITY_STATE_ZIP_ID = ? ", [first_name,last_name,Address,city_state_zip[0]])
    person = cursor.fetchone()
    if person == None:
        cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = ? AND STATE = ? AND ZIPCODE = ?", [city,state,zipcode])
        city_state_zip = cursor.fetchone()
        cursor.execute("INSERT INTO PERSON (FIRST_NAME,LAST_NAME,ADDRESS, CITY_STATE_ZIP_ID) VALUES (?,?,?,?);", [first_name,last_name, Address, city_state_zip[0]])
        db.connect.commit()
    cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = ?", [position_name])
    position = cursor.fetchone()
    cursor.execute("INSERT INTO ELECTRICIAN(PERSON_ID,POSITION_ID,YEARS_EMPLOYED, HOURLY_RATE) VALUES (?, ?, ?, ?);", [person[0],position[0],years_employed,hourly_rate])
    db.connect.commit()

def insert_into_salaried_employee(first_name,last_name,Address,city,state,zipcode, years_employed, salary_rate, position_name):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = ? AND STATE = ? AND ZIPCODE = ?", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    if city_state_zip == None:
        cursor.execute("INSERT INTO CITY_STATE_ZIP (CITY,STATE,ZIPCODE) VALUES (?,?,?);", [city,state,zipcode])
        db.connect.commit()
    cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= ? AND LAST_NAME = ? AND ADDRESS = ? AND  CITY_STATE_ZIP_ID = ? ", [first_name,last_name,Address,city_state_zip[0]])
    person = cursor.fetchone()
    if person == None:
        cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = ? AND STATE = ? AND ZIPCODE = ?", [city,state,zipcode])
        city_state_zip = cursor.fetchone()
        cursor.execute("INSERT INTO PERSON (FIRST_NAME,LAST_NAME,ADDRESS, CITY_STATE_ZIP_ID) VALUES (?,?,?,?);", [first_name,last_name, Address, city_state_zip[0]])
        db.connect.commit()
    cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = ?", [position_name])
    position = cursor.fetchone()
    cursor.execute("INSERT INTO SALARIED_EMPLOYEE(PERSON_ID,POSITION_ID,YEARS_EMPLOYED, SALARY_RATE) VALUES (?, ?, ?, ?);", [person[0],position[0],years_employed,salary_rate])
    db.connect.commit()

def delete_from_electrician(first_name,last_name,Address,city,state,zipcode, years_employed, hourly_rate, position_name):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = ? AND STATE = ? AND ZIPCODE = ?", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= ? AND LAST_NAME = ? AND ADDRESS = ? AND  CITY_STATE_ZIP_ID = ? ", [first_name,last_name,Address,city_state_zip[0]])
    person = cursor.fetchone()
    cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = ?", [position_name])
    position = cursor.fetchone()
    cursor.execute("DELETE FROM ELECTRICIAN WHERE PERSON_ID = ? AND POSITION_ID = ? AND YEARS_EMPLOYED = ? AND HOURLY_RATE = ?;", [person[0],position[0],years_employed,hourly_rate])
    db.connect.commit()



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
    db.connect.commit()

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
    db.connect.commit()



def insert_into_material_in_work_package(inventory_name, work_package_name, job_site_name, material_amount_issued,material_amount_used):
    cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME = ?", [job_site_name])
    job_site = cursor.fetchone()
    cursor.execute("SELECT WORK_PACKAGE_ID FROM WORK_PACKAGE WHERE WORK_PACKAGE_NAME = ? AND JOB_SITE_ID = ?", [work_package_name,job_site])
    work_package = cursor.fetchone()
    cursor.execute("SELECT INVENTORY_ID FROM INVENTORY WHERE MATERIAL_NAME = ?", [inventory_name])
    inventory = cursor.fetchone()
    cursor.execute("INSERT INTO MATERIAL_IN_WORK_PACKAGE(WORK_PACKAGE_ID,INVENTORY_ID,AMOUNT_ALLOTED,AMOUNT_USED) VALUES (?, ?, ?, ?);", [inventory[0], work_package[0], material_amount_issued, material_amount_used])
    db.connect.commit()

def delete_from_material_in_work_package(inventory_name, work_package_name, job_site_name, material_amount_issued,material_amount_used):
    cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME = ?", [job_site_name])
    job_site = cursor.fetchone()
    cursor.execute("SELECT WORK_PACKAGE_ID FROM WORK_PACKAGE WHERE WORK_PACKAGE_NAME = ? AND JOB_SITE_ID = ?", [work_package_name,job_site])
    work_package = cursor.fetchone()
    cursor.execute("SELECT INVENTORY_ID FROM INVENTORY WHERE MATERIAL_NAME = ?", [inventory_name])
    inventory = cursor.fetchone()
    cursor.execute("DELETE FROM MATERIAL_IN_WORK_PACKAGE WHERE WORK_PACKAGE_ID = ? AND INVENTORY_ID = ? AND AMOUNT_ALLOTED = ? AND AMOUNT_USED = ?;", [inventory[0], work_package[0], material_amount_issued, material_amount_used])
    db.connect.commit()

@app.route('/')
@cross_origin()
def get_all_jobs():
    locations = []
    cursor.execute("SELECT SITE_NAME FROM JOB_SITE")
    jobs = cursor.fetchall()
    cursor.execute("SELECT LOCATION_ID FROM JOB_SITE")
    location_id = cursor.fetchall()
    return jsonify(jobs)

@app.route("/jobs", methods=["GET"], strict_slashes=False)
@cross_origin()
def jobs():
    locations = []
    cursor.execute("SELECT SITE_NAME FROM JOB_SITE")
    jobs_name = cursor.fetchall()
    cursor.execute("SELECT LOCATION_ID FROM JOB_SITE")
    location_id = cursor.fetchall()
    cursor.execute("SELECT START_DATE FROM JOB_SITE")
    start_dates = cursor.fetchall()
    location_names = []
    jobs = JOB.query.all()
    for x in location_id:
        cursor.execute("SELECT LOCATION_NAME FROM LOCATION WHERE LOCATION_ID = %s", [x])
        id = cursor.fetchone()
        location_names.append(id[0])
    job_info = [[]]
    for x,y,z in zip(jobs_name,location_names,start_dates):
        job_info.append([x,y,z])
    jobs_array = []
    for x in job_info:
        job = JOB(site_name = x[0],
                  location = x[1],
                  start_date = x[2])
        jobs_array.append(job)
        print(jobs_array)

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

@app.route("/add_job", methods=["POST"], strict_slashes=False)
@cross_origin()
def add_jobs():
    location = request.json['location']
    site_name = request.json['site_name']
    start_date = request.join['start_date']
    insert_into_location(location)
    insert_into_job_site(location, site_name, start_date)
    job = JOB(location = location,
              site_name = site_name,
              start_date = start_date)

@app.route("/add_work_package", methods=["POST"], strict_slashes=False)
@cross_origin()
def add_work_package():
    job = request.json['job']
    work_package_name = request.json['work_package_name']
    price_of_work = request.json['price_of_work']
    hours_alloted = request.json['hours_alloted']
    hours_used = request.json['hours_used']
    insert_into_work_package(job, work_package_name, price_of_work, hours_alloted)
    work_package = WORK_PACKAGE()

@app.route("/add_employee", methods=["POST"], strict_slashes=False)
@cross_origin()
def add_employee():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    position = request.json['position']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    zipcode = request.json['zipcode']
    years_employed = request.json['years_employed']
    pay_rate = request.json['pay_rate']
    if (position == "Inside Wireman") or (position == "Residential Wireman"):
        insert_into_electrician(first_name,last_name,address,city,state,zipcode, years_employed, pay_rate, position)
    else:
        insert_into_salaried_employee(first_name,last_name,address,city,state,zipcode, years_employed, pay_rate, position)
    employee = EMPLOYEE(
    first_name = first_name,
    last_name = last_name,
    address = address,
    city = city,
    state = state,
    zip = zip,
    position = position,
    pay_rate = pay_rate,
    years_employed = years_employed)







if __name__ == '__main__':
    app.run(debug=True)