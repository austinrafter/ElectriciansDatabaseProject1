from flask import request
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from models import Jobs, WorkPackages, Employees, Foreman, ProjectManager, GeneralManager, Inventory, MaterialInWorkPackage, ElectricianOnWorkPackage
from datetime import datetime



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://austin:ThisIsMyPassword@localhost/SJElectricDatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

cors = CORS()

engine = create_engine('mysql+mysqlconnector://austin:ThisIsMyPassword@localhost/SJElectricDatabase', echo = True)
conn = engine.raw_connection()
cursor = conn.cursor()

def check_user_position_foreman(first_name,last_name,Address,city,state,zipcode,position_name, job_to_view):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = %s AND STATE = %s AND ZIPCODE = %s", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    if city_state_zip == None:
        return [Foreman(1,"you are not a foreman and can't view that", "you are not a foreman and can't view that",
                        "you are not a foreman and can't view that", "you are not a foreman and can't view that", 0)]
    cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= %s AND LAST_NAME = %s AND ADDRESS = %s AND  CITY_STATE_ZIP_ID = %s ", [first_name,last_name,Address,city_state_zip[0]])
    person = cursor.fetchone()
    if person == None:
        return [Foreman(1,"you are not a foreman and can't view that", "you are not a foreman and can't view that",
                        "you are not a foreman and can't view that", "you are not a foreman and can't view that", 0)]
    cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = %s", [position_name])
    position = cursor.fetchone()
    cursor.execute("SELECT POSITION_ID FROM SALARIED_EMPLOYEE WHERE PERSON_ID = %s AND POSITION_ID=%s", [person[0], position[0]])
    check_position= cursor.fetchone()
    if check_position[0] == position[0]:
        return get_foreman_view(job_to_view)
    else:
        return [Foreman("you are not a foreman and can't view that","you are not a foreman and can't view that","you are not a foreman and can't view that","you are not a foreman and can't view that",0)]

def check_user_position_project_manager(first_name,last_name,Address,city,state,zipcode,position_name, job_to_view):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = %s AND STATE = %s AND ZIPCODE = %s", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    if city_state_zip == None:
        return [ProjectManager(1, "you are not a project manager and can't view that", 0, 0, 0, 0, 0, 0)]
    cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= %s AND LAST_NAME = %s AND ADDRESS = %s AND  CITY_STATE_ZIP_ID = %s", [first_name,last_name,Address,city_state_zip[0]])
    person = cursor.fetchone()
    if person == None:
        return [ProjectManager(1, "you are not a project manager and can't view that", 0, 0, 0, 0, 0, 0)]
    cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = %s", [position_name])
    position = cursor.fetchone()
    cursor.execute("SELECT POSITION_ID FROM SALARIED_EMPLOYEE WHERE PERSON_ID = %s AND POSITION_ID= %s", [person[0], position[0]])
    check_position= cursor.fetchone()
    if check_position[0] == position[0]:
        return get_project_manager_view(job_to_view)
    else:
        return [ProjectManager(1,"you are not a project manager and can't view that",0,0,0,0,0,0)]

def check_user_position_general_manager(first_name,last_name,Address,city,state,zipcode,position_name, job_to_view):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = %s AND STATE = %s AND ZIPCODE = %s", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    if city_state_zip == None:
        return [GeneralManager(1,"You arent an employee here", 0, 0, 0, 0)]
    cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= %s AND LAST_NAME = %s AND ADDRESS = %s AND  CITY_STATE_ZIP_ID = %s ", [first_name,last_name,Address,city_state_zip[0]])
    person = cursor.fetchone()
    if person == None:
        return [GeneralManager(1, "You arent an employee here",0, 0, 0, 0)]
    cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = %s", [position_name])
    position = cursor.fetchone()
    cursor.execute("SELECT POSITION_ID FROM SALARIED_EMPLOYEE WHERE PERSON_ID = %s AND POSITION_ID=%s", [person[0], position[0]])
    check_position = cursor.fetchone()
    if check_position[0] == position[0]:
        return get_general_manager_view(job_to_view)
    else:
        return [GeneralManager(1,"You arent a general manager and cannot view that",0,0,0,0)]

def position_check_fm(first_name,last_name,Address,city,state,zipcode,position_name):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = %s AND STATE = %s AND ZIPCODE = %s", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    if city_state_zip == None:
        return False
    cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= %s AND LAST_NAME = %s AND ADDRESS = %s AND  CITY_STATE_ZIP_ID = %s ", [first_name,last_name,Address,city_state_zip[0]])
    person = cursor.fetchone()
    if person == None:
        return False
    cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = %s", [position_name])
    position = cursor.fetchone()
    cursor.execute("SELECT POSITION_ID FROM SALARIED_EMPLOYEE WHERE PERSON_ID = %s AND POSITION_ID=%s", [person[0], position[0]])
    check_position= cursor.fetchone()
    if check_position[0] == position[0]:
        return True
    else:
        return False

def position_check_pm(first_name,last_name,Address,city,state,zipcode,position_name):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = %s AND STATE = %s AND ZIPCODE = %s", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    if city_state_zip == None:
        return False
    cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= %s AND LAST_NAME = %s AND ADDRESS = %s AND  CITY_STATE_ZIP_ID = %s", [first_name,last_name,Address,city_state_zip[0]])
    person = cursor.fetchone()
    if person == None:
        return False
    cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = %s", [position_name])
    position = cursor.fetchone()
    cursor.execute("SELECT POSITION_ID FROM SALARIED_EMPLOYEE WHERE PERSON_ID = %s AND POSITION_ID= %s", [person[0], position[0]])
    check_position= cursor.fetchone()
    if check_position[0] == position[0]:
        return True
    else:
        return False

def position_check_gm(first_name,last_name,Address,city,state,zipcode,position_name):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = %s AND STATE = %s AND ZIPCODE = %s", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    if city_state_zip == None:
        return False
    cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= %s AND LAST_NAME = %s AND ADDRESS = %s AND  CITY_STATE_ZIP_ID = %s ", [first_name,last_name,Address,city_state_zip[0]])
    person = cursor.fetchone()
    if person == None:
        return False
    cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = %s", [position_name])
    position = cursor.fetchone()
    cursor.execute("SELECT POSITION_ID FROM SALARIED_EMPLOYEE WHERE PERSON_ID = %s AND POSITION_ID=%s", [person[0], position[0]])
    check_position = cursor.fetchone()
    if check_position[0] == position[0]:
        return True
    else:
        return False

@app.route("/foreman" , methods=["POST"], strict_slashes=False)
@cross_origin()
def foreman():
    first_name = request.json['first_name']
    print(first_name)
    last_name = request.json['last_name']
    position = request.json['position']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    zipcode = request.json['zip']
    years_employed = request.json['years_employed']
    print(years_employed)
    pay_rate = request.json['pay_rate']
    job_to_view = request.json['job_to_view']
    print(position)
    foreman = check_user_position_foreman(first_name,last_name,address,city,state,zipcode,position, job_to_view)
    print(foreman)
    return jsonify([e.serialize() for e in foreman])

@app.route("/project_manager" , methods=["POST"], strict_slashes=False)
@cross_origin()
def project_manager():
    first_name = request.json['first_name']
    print(first_name)
    last_name = request.json['last_name']
    position = request.json['position']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    zipcode = request.json['zip']
    years_employed = request.json['years_employed']
    print(years_employed)
    pay_rate = request.json['pay_rate']
    job_to_view = request.json['job_to_view']
    print(position)
    #employee = Employees(first_name, last_name, address, city, state, zipcode, position, pay_rate, years_employed,)

    project_manager = check_user_position_project_manager(first_name, last_name, address, city, state, zipcode, position, job_to_view)
    print(project_manager)
    return jsonify([e.serialize() for e in project_manager])


@app.route("/general_manager" , methods=["POST"], strict_slashes=False)
@cross_origin()
def general_manager():
    first_name = request.json['first_name']
    print(first_name)
    last_name = request.json['last_name']
    position = request.json['position']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    zipcode = request.json['zip']
    years_employed = request.json['years_employed']
    print(years_employed)
    pay_rate = request.json['pay_rate']
    job_to_view = request.json['job_to_view']
    print(position)

    general_manager = check_user_position_general_manager(first_name, last_name, address, city, state, zipcode, position, job_to_view)
    return jsonify([e.serialize() for e in general_manager])



@app.route("/hours_used" , methods=["POST"], strict_slashes=False)
@cross_origin()
def change_hours_used_on_work_package():
    job = request.json['job']
    work_package_name = request.json['work_package_name']
    hours_used = request.json['hours_used']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    position = request.json['position']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    zipcode = request.json['zip']
    years_employed = request.json['years_employed']
    foreman = position_check_fm(first_name,last_name,position,address,city,state,zipcode,years_employed)
    if foreman:
        cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME=?", [job])
        job_id = cursor.fetchone();
        cursor.execute("UPDATE WORK_PACKAGE SET HOURS_USED = ? WHERE WORK_PACKAGE_NAME = ? AND JOB_SITE_ID = ?", [hours_used,work_package_name, job_id[0]])
        conn.commit()
        return jsonify(hours_used)
    else:
        return False

@app.route("/material_amount_used" , methods=["POST"], strict_slashes=False)
@cross_origin()
def change_material_amount_used_in_work_package():
    work_package_name = request.json['work_package_name']
    job_site_name = request.json['job_site_name']
    inventory_name = request.json['inventory_name']
    amount_used = request.json['amount_used']
    cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME = %s", [job_site_name])
    job_site = cursor.fetchone()
    cursor.execute("SELECT WORK_PACKAGE_ID FROM WORK_PACKAGE WHERE WORK_PACKAGE_NAME = %s AND JOB_SITE_ID = %s", [work_package_name,job_site[0]])
    work_package = cursor.fetchone()
    cursor.execute("SELECT INVENTORY_ID FROM INVENTORY WHERE MATERIAL_NAME = %s", [inventory_name])
    inventory = cursor.fetchone()
    cursor.execute("UPDATE MATERIAL_IN_WORK_PACKAGE SET AMOUNT_USED =%s WHERE INVENTORY_ID = %s AND WORK_PACKAGE_ID = %s", [amount_used, inventory[0],work_package[0]])
    conn.commit()

@app.route("/add_inventory" , methods=["POST"], strict_slashes=False)
@cross_origin()
def add_inventory():
    material_name = request.json['material_name']
    cost_per_unit = request.json['cost_per_unit']
    weight_per_unit = request.json['weight_per_unit']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    position = request.json['position']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    zipcode = request.json['zipcode']
    years_employed = request.json['years_employed']
    if position == 'Project Manager':
        upper_management = position_check_pm(first_name, last_name, address, city, state, zipcode, position)
    elif position == 'Foreman':
        upper_management = position_check_fm(first_name, last_name, address, city, state, zipcode, position)
    if upper_management:
        cursor.execute("INSERT INTO INVENTORY (MATERIAL_NAME,COST_PER_UNIT,WEIGHT_PER_UNIT) VALUES (%s,%s,%s);",
                       [material_name, cost_per_unit, weight_per_unit])
        conn.commit()
        inventory = Inventory(1,material_name, cost_per_unit, weight_per_unit)
        inventorys = [inventory]

        return jsonify([e.serialize() for e in inventorys])
    else:
        inventory = Inventory(1, "You can't add inventory", 0, 0)
        inventorys = [inventory]
        return jsonify([e.serialize() for e in inventorys])

@app.route("/delete_inventory" , methods=["POST"], strict_slashes=False)
@cross_origin()
def delete_from_inventory():
    material_name = request.json['material_name']
    cost_per_unit = request.json['cost_per_unit']
    weight_per_unit = request.json['weight_per_unit']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    position = request.json['position']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    zipcode = request.json['zipcode']
    years_employed = request.json['years_employed']
    if position == 'Project Manager':
        upper_management = position_check_pm(first_name, last_name, address, city, state, zipcode, position)
    elif position == 'Foreman':
        upper_management = position_check_fm(first_name, last_name, address, city, state, zipcode, position)
    if upper_management:
        cursor.execute("SELECT MATERIAL_NAME FROM INVENTORY WHERE MATERIAL_NAME = %s", [material_name])
        material = cursor.fetchone()
        if material[0] == None:
            inventory = Inventory(1, "That inventory is not in our system to delete", 0, 0)
            inventorys = [inventory]
        else:
            cursor.execute("DELETE FROM INVENTORY WHERE MATERIAL_NAME = %s AND COST_PER_UNIT = %s AND WEIGHT_PER_UNIT = %s;",
                       [material_name, cost_per_unit, weight_per_unit])
            conn.commit()
            inventory = Inventory(1, material_name, cost_per_unit, weight_per_unit)
            inventorys = [inventory]

        return jsonify([e.serialize() for e in inventorys])
    else:
        inventory = Inventory(1, "You can't delete inventory", 0, 0)
        inventorys = [inventory]
        return jsonify([e.serialize() for e in inventorys])


def get_foreman_view(job_site_name):
    cursor.execute("SELECT * FROM FOREMAN WHERE SITE_NAME=%s", [job_site_name])
    result = cursor.fetchall()
    print(result)
    foremen = []
    i=0
    for x in result:
        foreman = Foreman(i+1, x[0], x[1], x[2], x[3], x[4])
        foremen.append(foreman)
    return foremen

def get_project_manager_view(job_site_name):
    cursor.execute("SELECT * FROM PROJECT_MANAGER WHERE SITE_NAME=%s", [job_site_name])
    result = cursor.fetchall()
    project_managers = []
    i = 0
    for x in result:
        project_manager = ProjectManager(i+1, x[0], x[1], x[2], x[3], x[4], x[5], x[6])
        project_managers.append(project_manager)
    return project_managers

def get_general_manager_view(job_site_name):
    cursor.execute("SELECT * FROM GENERAL_MANAGER WHERE SITE_NAME= %s",[job_site_name])
    result = cursor.fetchall()
    general_managers = []
    i = 0
    for x in result:
        general_manager = GeneralManager(i+1, x[0], x[1], x[2], x[3], x[4])
        general_managers.append(general_manager)
    return general_managers



def insert_into_location(location_name):
    cursor.execute("SELECT LOCATION_ID FROM LOCATION WHERE LOCATION_NAME = %s", [location_name])
    location = cursor.fetchone()
    if location == None:
        cursor.execute("INSERT INTO LOCATION (LOCATION_NAME) VALUES (%s);", [location_name])
        conn.commit()

def delete_from_location(location_name):
    cursor.execute("DELETE FROM LOCATION WHERE LOCATION_NAME = ?;", [location_name])
    conn.commit()


def insert_into_city_state_zip(city,state,zipcode):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = %s AND STATE = %s AND ZIPCODE = %s;", [city, state, zipcode])
    id = cursor.fetchone()
    if id == None:
        cursor.execute("INSERT INTO CITY_STATE_ZIP (CITY,STATE,ZIPCODE) VALUES (%s,%s,%s);", [city,state,zipcode])
        conn.commit()

def delete_from_city_state_zip(city,state,zipcode):
    cursor.execute("DELETE FROM CITY_STATE_ZIP WHERE CITY= %s AND STATE = %s AND ZIPCODE = %s);", [city,state,zipcode])
    conn.commit()



def insert_into_person(first_name,last_name,Address,city,state,zipcode):
    insert_into_city_state_zip(city,state,zipcode)
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = %s AND STATE = %s AND ZIPCODE = %s", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME = %s AND LAST_NAME = %s AND ADDRESS = %s AND CITY_STATE_ZIP_ID = %s;",[first_name, last_name, Address, city_state_zip[0]])
    person = cursor.fetchone()
    if person == None:
        cursor.execute("INSERT INTO PERSON (FIRST_NAME,LAST_NAME,ADDRESS, CITY_STATE_ZIP_ID) VALUES (%s,%s,%s,%s);", [first_name,last_name, Address, city_state_zip[0]])
        conn.commit()

def delete_from_person(first_name,last_name,Address,city,state,zipcode):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = %s AND STATE = %s AND ZIPCODE = %s", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    cursor.execute("DELETE FROM PERSON WHERE FIRST_NAME = %s AND LAST_NAME = %s AND ADDRESS = %s AND CITY_STATE_ZIP_ID = %s;", [first_name,last_name, Address, city_state_zip[0]])
    conn.commit()

def insert_into_position(position):
    cursor.execute(" SELECT POSITION_ID FROM  EMPLOYEE_POSITION WHERE POSITION_NAME = %s;", [position])
    position_here = cursor.fetchone()
    if position_here == None:
        cursor.execute(" INSERT INTO EMPLOYEE_POSITION (POSITION_NAME) VALUES (%s);", [position])
        conn.commit()

def delete_from_position(position):
    cursor.execute(" DELETE FROM EMPLOYEE_POSITION WHERE POSITION_NAME = %s;", [position])
    conn.commit()



def insert_into_job_site(location_name, site_name, start_date):
    cursor.execute("SELECT LOCATION_ID FROM LOCATION WHERE LOCATION_NAME=%s", [location_name])
    location = cursor.fetchone()
    cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME = %s AND LOCATION_ID = %s AND START_DATE = %s;", [site_name, location[0], start_date])
    job = cursor.fetchone()
    if job == None:
        cursor.execute("INSERT INTO JOB_SITE (SITE_NAME,LOCATION_ID,START_DATE) VALUES (%s,%s,%s);", [site_name, location[0],start_date])
        conn.commit()

def delete_from_job_site(location_name, site_name, start_date):
    cursor.execute("SELECT LOCATION_ID FROM LOCATION WHERE LOCATION_NAME=%s", [location_name])
    location = cursor.fetchone()
    if location == None:
        return False
    else:
        cursor.execute("DELETE FROM JOB_SITE WHERE SITE_NAME = %s AND LOCATION_ID = %s AND START_DATE = %s;", [site_name, location[0],start_date])
        conn.commit()
        return True



def insert_into_work_package(job_site_name, work_package_name, price_of_work, hours_alloted, hours_used):
    cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME = %s", [job_site_name])
    job_site = cursor.fetchone()
    if job_site == None:
        return False;
    cursor.execute("INSERT INTO WORK_PACKAGE (JOB_SITE_ID ,WORK_PACKAGE_NAME ,PRICE_OF_WORK, HOURS_ALLOTED,HOURS_USED) VALUES (%s,%s,%s,%s,%s);", [job_site[0], work_package_name, price_of_work, hours_alloted,hours_used])
    conn.commit()
    return True;

def delete_from_work_package(job_site_name, work_package_name, price_of_work, hours_alloted, hours_used):
    cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME = %s", [job_site_name])
    job_site = cursor.fetchone()
    if job_site == None:
        return False
    cursor.execute("DELETE FROM WORK_PACKAGE WHERE JOB_SITE_ID = %s AND WORK_PACKAGE_NAME = %s AND PRICE_OF_WORK = %s AND  HOURS_ALLOTED = %s AND HOURS_USED = %s;", [job_site[0], work_package_name, price_of_work, hours_alloted,hours_used])
    conn.commit()
    return True



def insert_into_electrician(first_name,last_name,Address,city,state,zipcode, years_employed, hourly_rate, position_name):
    insert_into_city_state_zip(city, state, zipcode)
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = %s AND STATE = %s AND ZIPCODE = %s", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    insert_into_person(first_name,last_name,Address,city,state,zipcode)
    cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= %s AND LAST_NAME = %s AND ADDRESS = %s AND  CITY_STATE_ZIP_ID = %s ", [first_name,last_name,Address,city_state_zip[0]])
    person = cursor.fetchone()
    insert_into_position(position_name)
    cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = ?", [position_name])
    position = cursor.fetchone()
    cursor.execute("SELECT ELECTRICIAN_ID FROM ELECTRICIAN WHERE PERSON_ID = %s AND POSITION_ID = %s AND YEARS_EMPLOYED = %s AND HOURLY_RATE = %s;",[person[0], position[0], years_employed, hourly_rate])
    electrician = cursor.fetchone()
    if electrician[0] == None:
        cursor.execute("INSERT INTO ELECTRICIAN(PERSON_ID,POSITION_ID,YEARS_EMPLOYED, HOURLY_RATE) VALUES (%s, %s, %s, %s);", [person[0],position[0],years_employed,hourly_rate])
        conn.commit()

def insert_into_salaried_employee(first_name,last_name,Address,city,state,zipcode, years_employed, salary_rate, position_name):
    insert_into_city_state_zip(city,state,zipcode)
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = %s AND STATE = %s AND ZIPCODE = %s", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    insert_into_person(first_name,last_name,Address,city,state,zipcode)
    cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= %s AND LAST_NAME = %s AND ADDRESS = %s AND  CITY_STATE_ZIP_ID = %s ", [first_name,last_name,Address,city_state_zip[0]])
    person = cursor.fetchone()
    insert_into_position(position_name)
    cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = %s", [position_name])
    position = cursor.fetchone()
    cursor.execute("SELECT SALARIED_EMPLOYEE_ID FROM SALARIED_EMPLOYEE WHERE PERSON_ID=%s AND POSITION_ID=%s AND YEARS_EMPLOYED=%s AND SALARY_RATE=%s;",[person[0], position[0], years_employed, salary_rate])
    salary = cursor.fetchone()
    if salary == None:
        cursor.execute("INSERT INTO SALARIED_EMPLOYEE(PERSON_ID,POSITION_ID,YEARS_EMPLOYED, SALARY_RATE) VALUES (%s, %s, %s, %s);", [person[0],position[0],years_employed,salary_rate])
        conn.commit()

def delete_from_electrician(first_name,last_name,Address,city,state,zipcode, years_employed, hourly_rate, position_name):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = %s AND STATE = %s AND ZIPCODE = %s", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    if city_state_zip == None:
        return False
    cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= %s AND LAST_NAME = %s AND ADDRESS = %s AND  CITY_STATE_ZIP_ID = %s ", [first_name,last_name,Address,city_state_zip[0]])
    person = cursor.fetchone()
    if person == None:
        return False
    cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = %s", [position_name])
    position = cursor.fetchone()
    if position == None:
        return False
    cursor.execute("DELETE FROM ELECTRICIAN WHERE PERSON_ID = %s AND POSITION_ID = %s AND YEARS_EMPLOYED = %s AND HOURLY_RATE = %s;", [person[0],position[0],years_employed,hourly_rate])
    conn.commit()
    return True

def delete_from_salaried_employee(first_name,last_name,Address,city,state,zipcode, years_employed, salary_rate, position_name):
    cursor.execute("SELECT CITY_STATE_ZIP_ID FROM CITY_STATE_ZIP WHERE CITY = %s AND STATE = %s AND ZIPCODE = %s", [city,state,zipcode])
    city_state_zip = cursor.fetchone()
    if city_state_zip == None:
        return False
    cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= %s AND LAST_NAME = %s AND ADDRESS = %s AND  CITY_STATE_ZIP_ID = %s", [first_name,last_name,Address,city_state_zip[0]])
    person = cursor.fetchone()
    if person == None:
        return False
    cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = %s", [position_name])
    position = cursor.fetchone()
    if position == None:
        return False
    cursor.execute("DELETE FROM SALARIED_EMPLOYEE WHERE PERSON_ID = %s AND POSITION_ID = %s AND YEARS_EMPLOYED = %s AND SALARY_RATE = %s;", [person[0],position[0],years_employed,salary_rate])
    conn.commit()
    return True


@app.route("/add_electrician_to_work_package" , methods=["POST"], strict_slashes=False)
@cross_origin()
def add_electrician_to_work_package():
    electricians_first_name = request.json['electricians_first_name']
    electricians_last_name = request.json['electricians_last_name']
    electricians_position = request.json['electricians_position']
    electricians_address = request.json['electricians_address']
    work_package_name = request.json['work_package_name']
    site_name = request.json['site_name']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    position = request.json['position']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    zipcode = request.json['zipcode']
    if position == 'Project Manager':
        upper_management = position_check_pm(first_name, last_name, address, city, state, zipcode, position)
    elif position == 'Foreman':
        upper_management = position_check_fm(first_name, last_name, address, city, state, zipcode, position)
    if upper_management:
        insert_into_position(electricians_position)
        cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = %s", [electricians_position])
        position = cursor.fetchone()
        if position == None:
            inventory = ElectricianOnWorkPackage(1, "This position is not in our system",
                                                 "This position is not in our system",
                                                 "This position is not in our system",
                                                 "This position is not in our system")
            inventorys = [inventory]
            return jsonify([e.serialize() for e in inventorys])
        cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= %s AND LAST_NAME = %s AND ADDRESS = %s", [electricians_first_name,electricians_last_name,electricians_address])
        person = cursor.fetchone()
        if person == None:
            inventory = ElectricianOnWorkPackage(1, "This person is not in our system",
                                                 "This person is not in our system",
                                                 "This person is not in our system",
                                                "This person is not in our system")
            inventorys = [inventory]
            return jsonify([e.serialize() for e in inventorys])
        cursor.execute("SELECT ELECTRICIAN_ID FROM ELECTRICIAN WHERE PERSON_ID = %s AND POSITION_ID = %s", [person[0],position[0]])
        electrician = cursor.fetchone()
        if electrician == None:
            inventory = ElectricianOnWorkPackage(1, "This electrician is not in our system",
                                                 "This electrician is not in our system",
                                                 "This electrician is not in our system",
                                                 "This electrician is not in our system")
            inventorys = [inventory]
            return jsonify([e.serialize() for e in inventorys])
        cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME = %s", [site_name])
        job_site = cursor.fetchone()
        if job_site == None:
            inventory = ElectricianOnWorkPackage(1, "This job is not in our system",
                                                 "This job is not in our system",
                                                 "This job is not in our system",
                                                 "This job is not in our system")
            inventorys = [inventory]
            return jsonify([e.serialize() for e in inventorys])
        cursor.execute("SELECT WORK_PACKAGE_ID FROM WORK_PACKAGE WHERE WORK_PACKAGE_NAME = %s AND JOB_SITE_ID = %s", [work_package_name,job_site[0]])
        work_package = cursor.fetchone()
        if work_package == None:
            inventory = ElectricianOnWorkPackage(1, "This work package is not in our system",
                                                 "This work package is not in our system",
                                                 "This work package is not in our system",
                                                 "This work package is not in our system")
            inventorys = [inventory]
            return jsonify([e.serialize() for e in inventorys])
        cursor.execute("INSERT INTO ELECTRICIAN_ON_WORK_PACKAGE(ELECTRICIAN_ID,WORK_PACKAGE_ID) VALUES (%s,%s);", [electrician[0],work_package[0]])
        conn.commit()
        inventory = ElectricianOnWorkPackage(1, electricians_first_name,
                                             electricians_last_name,
                                             work_package_name,
                                             site_name)
        inventorys = [inventory]
        return jsonify([e.serialize() for e in inventorys])
    else:
        inventory = ElectricianOnWorkPackage(1, "You can't add electricians to work packages","You can't add material to work packages","You can't add material to work packages","You can't add material to work packages")
        inventorys = [inventory]
        return jsonify([e.serialize() for e in inventorys])

@app.route("/delete_electrician_from_work_package" , methods=["POST"], strict_slashes=False)
@cross_origin()
def delete_electrician_from_work_package():
    electricians_first_name = request.json['electricians_first_name']
    electricians_last_name = request.json['electricians_last_name']
    electricians_position = request.json['electricians_position']
    electricians_address = request.json['electricians_address']
    work_package_name = request.json['work_package_name']
    site_name = request.json['site_name']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    position = request.json['position']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    zipcode = request.json['zipcode']
    if position == 'Project Manager':
        upper_management = position_check_pm(first_name, last_name, address, city, state, zipcode, position)
    elif position == 'Foreman':
        upper_management = position_check_fm(first_name, last_name, address, city, state, zipcode, position)
    if upper_management:
        insert_into_position(electricians_position)
        cursor.execute("SELECT POSITION_ID FROM EMPLOYEE_POSITION WHERE POSITION_NAME = %s", [electricians_position])
        position = cursor.fetchone()
        if position == None:
            inventory = ElectricianOnWorkPackage(1, "This position is not in our system",
                                                 "This position is not in our system",
                                                 "This position is not in our system",
                                                 "This position is not in our system")
            inventorys = [inventory]
            return jsonify([e.serialize() for e in inventorys])
        cursor.execute("SELECT PERSON_ID FROM PERSON WHERE FIRST_NAME= %s AND LAST_NAME = %s AND ADDRESS = %s",
                       [electricians_first_name, electricians_last_name, electricians_address])
        person = cursor.fetchone()
        if person == None:
            inventory = ElectricianOnWorkPackage(1, "This person is not in our system",
                                                 "This person is not in our system",
                                                 "This person is not in our system",
                                                 "This person is not in our system")
            inventorys = [inventory]
            return jsonify([e.serialize() for e in inventorys])
        cursor.execute("SELECT ELECTRICIAN_ID FROM ELECTRICIAN WHERE PERSON_ID = %s AND POSITION_ID = %s",
                       [person[0], position[0]])
        electrician = cursor.fetchone()
        if electrician == None:
            inventory = ElectricianOnWorkPackage(1, "This electrician is not in our system",
                                                 "This electrician is not in our system",
                                                 "This electrician is not in our system",
                                                 "This electrician is not in our system")
            inventorys = [inventory]
            return jsonify([e.serialize() for e in inventorys])
        cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME = %s", [site_name])
        job_site = cursor.fetchone()
        if job_site == None:
            inventory = ElectricianOnWorkPackage(1, "This job is not in our system",
                                                 "This job is not in our system",
                                                 "This job is not in our system",
                                                 "This job is not in our system")
            inventorys = [inventory]
            return jsonify([e.serialize() for e in inventorys])
        cursor.execute("SELECT WORK_PACKAGE_ID FROM WORK_PACKAGE WHERE WORK_PACKAGE_NAME = %s AND JOB_SITE_ID = %s",
                       [work_package_name, job_site[0]])
        work_package = cursor.fetchone()
        if work_package == None:
            inventory = ElectricianOnWorkPackage(1, "This work package is not in our system",
                                                 "This work package is not in our system",
                                                 "This work package is not in our system",
                                                 "This work package is not in our system")
            inventorys = [inventory]
            return jsonify([e.serialize() for e in inventorys])
        cursor.execute("DELETE FROM ELECTRICIAN_ON_WORK_PACKAGE WHERE ELECTRICIAN_ID = %s AND WORK_PACKAGE_ID = %s;",
                       [electrician[0], work_package[0]])
        conn.commit()
        inventory = ElectricianOnWorkPackage(1, electricians_first_name,
                                             electricians_last_name,
                                             work_package_name,
                                             site_name)
        inventorys = [inventory]
        return jsonify([e.serialize() for e in inventorys])
    else:
        inventory = ElectricianOnWorkPackage(1, "You can't add electricians to work packages",
                                             "You can't add material to work packages",
                                             "You can't add material to work packages",
                                             "You can't add material to work packages")
        inventorys = [inventory]
        return jsonify([e.serialize() for e in inventorys])



@app.route("/insert_material_in_work_package" , methods=["POST"], strict_slashes=False)
@cross_origin()
def insert_material_in_work_package():
    material_name = request.json['material_name']
    work_package_name = request.json['work_package_name']
    site_name = request.json['site_name']
    amount_alloted = request.json['amount_alloted']
    amount_used = request.json['amount_used']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    position = request.json['position']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    zipcode = request.json['zipcode']
    if position == 'Project Manager':
        upper_management = position_check_pm(first_name, last_name, address, city, state, zipcode, position)
    elif position == 'Foreman':
        upper_management = position_check_fm(first_name, last_name, address, city, state, zipcode, position)
    if upper_management:
        cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME = %s", [site_name])
        job_site = cursor.fetchone()
        print(job_site)
        if job_site == None:
            inventory = MaterialInWorkPackage(1, "That job site does not exist", 0, 0,
                                              "That job site does not exist",
                                              "That job site does not exist")
            inventorys = [inventory]
            return jsonify([e.serialize() for e in inventorys])
        cursor.execute("SELECT WORK_PACKAGE_ID FROM WORK_PACKAGE WHERE WORK_PACKAGE_NAME = %s AND JOB_SITE_ID = %s",
                       [work_package_name, job_site[0]])
        work_package = cursor.fetchone()
        if work_package == None:
            inventory = MaterialInWorkPackage(1, "That work package does not exist", 0, 0,
                                              "That work package does not exist",
                                              "That work package does not exist")
            inventorys = [inventory]
            return jsonify([e.serialize() for e in inventorys])
        cursor.execute("SELECT INVENTORY_ID FROM INVENTORY WHERE MATERIAL_NAME = %s", [material_name])
        inventory_id = cursor.fetchone()
        if inventory_id == None:
            inventory = MaterialInWorkPackage(1, "That item does not exist in our system", 0, 0,
                                              "That item does not exist in our system",
                                              "That item does not exist in our system")
            inventorys = [inventory]
            return jsonify([e.serialize() for e in inventorys])
        print(inventory_id)
        print(work_package)
        cursor.execute(
            "INSERT INTO MATERIAL_IN_WORK_PACKAGE(WORK_PACKAGE_ID,INVENTORY_ID,AMOUNT_ALLOTED,AMOUNT_USED) VALUES (%s, %s, %s, %s);",
            [work_package[0], inventory_id[0], amount_alloted, amount_used])
        conn.commit()
        inventory = MaterialInWorkPackage(1,material_name, amount_alloted, amount_used, work_package_name, site_name)
        inventorys = [inventory]

        return jsonify([e.serialize() for e in inventorys])
    else:
        inventory = MaterialInWorkPackage(1, "You can't add material to work packages", 0, 0,"You can't add material to work packages","You can't add material to work packages")
        inventorys = [inventory]
        return jsonify([e.serialize() for e in inventorys])

@app.route("/delete_material_in_work_package" , methods=["POST"], strict_slashes=False)
@cross_origin()
def delete_material_in_work_package():
    material_name = request.json['material_name']
    work_package_name = request.json['work_package_name']
    site_name = request.json['site_name']
    amount_alloted = request.json['amount_alloted']
    amount_used = request.json['amount_used']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    position = request.json['position']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    zipcode = request.json['zipcode']
    if position == 'Project Manager':
        upper_management = position_check_pm(first_name, last_name, address, city, state, zipcode, position)
    elif position == 'Foreman':
        upper_management = position_check_fm(first_name, last_name, address, city, state, zipcode, position)
    if upper_management:
        cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME = %s", [site_name])
        job_site = cursor.fetchone()
        if job_site == None:
            inventory = MaterialInWorkPackage(1, "That job site does not exist", 0, 0,
                                              "That job site does not exist",
                                              "That job site does not exist")
            inventorys = [inventory]
            return jsonify([e.serialize() for e in inventorys])
        cursor.execute("SELECT WORK_PACKAGE_ID FROM WORK_PACKAGE WHERE WORK_PACKAGE_NAME = %s AND JOB_SITE_ID = %s",
                       [work_package_name, job_site[0]])
        work_package = cursor.fetchone()
        if work_package == None:
            inventory = MaterialInWorkPackage(1, "That work package does not exist", 0, 0,
                                              "That work package does not exist",
                                              "That work package does not exist")
            inventorys = [inventory]
            return jsonify([e.serialize() for e in inventorys])
        cursor.execute("SELECT INVENTORY_ID FROM INVENTORY WHERE MATERIAL_NAME = %s", [material_name])
        inventory = cursor.fetchone()
        if inventory == None:
            inventory = MaterialInWorkPackage(1, "That item does not exist in our system", 0, 0,
                                              "That item does not exist in our system",
                                              "That item does not exist in our system")
            inventorys = [inventory]
            return jsonify([e.serialize() for e in inventorys])
        cursor.execute(
            "DELETE FROM MATERIAL_IN_WORK_PACKAGE WHERE WORK_PACKAGE_ID = %s AND INVENTORY_ID = %s AND AMOUNT_ALLOTED = %s AND AMOUNT_USED = %s;",
            [work_package[0], inventory[0], amount_alloted, amount_used])
        conn.commit()
        inventory = MaterialInWorkPackage(1, material_name, amount_alloted, amount_used, work_package_name, site_name)
        inventorys = [inventory]

        return jsonify([e.serialize() for e in inventorys])
    else:
        inventory = MaterialInWorkPackage(1, "You can't add material to work packages", 0, 0,
                                          "You can't add material to work packages",
                                          "You can't add material to work packages")
        inventorys = [inventory]
        return jsonify([e.serialize() for e in inventorys])


@app.route("/")
@cross_origin()
def get_all_jobs():
    locations = []
    cursor.execute("SELECT SITE_NAME FROM JOB_SITE")
    jobs = cursor.fetchall()
    cursor.execute("SELECT LOCATION_ID FROM JOB_SITE")
    location_id = cursor.fetchall()
    return jsonify(jobs)

@app.route("/jobs" , methods=["GET"], strict_slashes=False)
@cross_origin()
def jobs():
    locations = []
    cursor.execute("SELECT JOB_SITE_ID FROM JOB_SITE")
    jobs_id = cursor.fetchall()
    cursor.execute("SELECT SITE_NAME FROM JOB_SITE")
    jobs_name = cursor.fetchall()
    cursor.execute("SELECT LOCATION_ID FROM JOB_SITE")
    location_id = cursor.fetchall()
    cursor.execute("SELECT START_DATE FROM JOB_SITE")
    start_dates = cursor.fetchall()
    location_names = []
    for x in location_id:
        cursor.execute("SELECT LOCATION_NAME FROM LOCATION WHERE LOCATION_ID = %s", [x[0]])
        name = cursor.fetchone()
        location_names.append(name[0])
    job_info = []
    for x in range(len(jobs_name)):
        job_info.append([jobs_id[x],datetime.strptime(('%s' % start_dates[x]), '%Y-%m-%d'),jobs_name[x],location_names[x]])
    jobs = []
    for x in job_info:
        job = Jobs(x[0],x[1],x[2],x[3])
        jobs.append(job)
    return jsonify([e.serialize() for e in jobs])

@app.route("/inventory" , methods=["GET"], strict_slashes=False)
@cross_origin()
def inventory():
    locations = []
    cursor.execute("SELECT INVENTORY_ID FROM INVENTORY")
    inventory_id = cursor.fetchall()
    cursor.execute("SELECT MATERIAL_NAME FROM INVENTORY")
    material_name = cursor.fetchall()
    cursor.execute("SELECT COST_PER_UNIT FROM INVENTORY")
    cost_per_unit = cursor.fetchall()
    cursor.execute("SELECT WEIGHT_PER_UNIT FROM INVENTORY")
    weight_per_unit = cursor.fetchall()
    location_names = []
    job_info = []
    for x in range(len(inventory_id)):
        job_info.append([inventory_id[x],material_name[x],cost_per_unit[x],weight_per_unit[x]])
    jobs = []
    for x in job_info:
        job = Inventory(x[0],x[1],x[2],x[3])
        jobs.append(job)
    return jsonify([e.serialize() for e in jobs])

@app.route("/electricians" , methods=["GET"], strict_slashes=False)
@cross_origin()
def electricians():
    locations = []
    cursor.execute("SELECT ELECTRICIAN_ID FROM ELECTRICIAN")
    electrician_id = cursor.fetchall()
    cursor.execute("SELECT PERSON_ID FROM ELECTRICIAN")
    person_id = cursor.fetchall()
    first_names = []
    last_names = []
    addresses = []
    cityStateZips = []
    for x in person_id:
        cursor.execute("SELECT FIRST_NAME FROM PERSON WHERE PERSON_ID = %s", [x[0]])
        first_name = cursor.fetchone()
        first_names.append(first_name[0])
        cursor.execute("SELECT LAST_NAME FROM PERSON WHERE PERSON_ID = %s", [x[0]])
        last_name = cursor.fetchone()
        last_names.append(last_name[0])
        cursor.execute("SELECT ADDRESS FROM PERSON WHERE PERSON_ID = %s", [x[0]])
        address = cursor.fetchone()
        addresses.append(address[0])
        cursor.execute("SELECT CITY_STATE_ZIP_ID FROM PERSON WHERE PERSON_ID = %s", [x[0]])
        city_state_zip_id = cursor.fetchone()
        cityStateZips.append(city_state_zip_id[0])
    citys = []
    states = []
    zips = []
    for x in cityStateZips:
        cursor.execute("SELECT CITY FROM CITY_STATE_ZIP WHERE CITY_STATE_ZIP_ID = %s", [x])
        city = cursor.fetchone()
        citys.append(city[0])
        cursor.execute("SELECT STATE FROM CITY_STATE_ZIP WHERE CITY_STATE_ZIP_ID = %s", [x])
        state = cursor.fetchone()
        states.append(state[0])
        cursor.execute("SELECT ZIPCODE FROM CITY_STATE_ZIP WHERE CITY_STATE_ZIP_ID = %s", [x])
        zipcode = cursor.fetchone()
        zips.append(zipcode[0])
    cursor.execute("SELECT POSITION_ID FROM ELECTRICIAN")
    position_id = cursor.fetchall()
    position_names = []
    for x in position_id:
        cursor.execute("SELECT POSITION_NAME FROM EMPLOYEE_POSITION WHERE POSITION_ID = %s", [x[0]])
        name = cursor.fetchone()
        position_names.append(name[0])
    cursor.execute("SELECT YEARS_EMPLOYED FROM ELECTRICIAN")
    years_employed = cursor.fetchall()
    cursor.execute("SELECT HOURLY_RATE FROM ELECTRICIAN")
    hourly_rate = cursor.fetchall()
    location_names = []
    job_info = []
    for x in range(len(electrician_id)):
        job_info.append([electrician_id[x],first_names[x],last_names[x],addresses[x], citys[x], states[x], zips[x], position_names[x], hourly_rate[x], years_employed[x] ])
    jobs = []
    for x in job_info:
        job = Employees(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9])
        jobs.append(job)
    return jsonify([e.serialize() for e in jobs])

def convertTuple(tup):
    # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str

@app.route("/work_packages" , methods=["POST"], strict_slashes=False)
@cross_origin()
def work_packages():
    work_packages = []
    if request.method == 'POST':
        jobSite = request.get_json()
        jobSite = jobSite.get('jobSite')
        jobSite = str(jobSite.get('job_site'))
        fixedJob = convertTuple(jobSite)
        sql_starter = """SELECT JOB_SITE_ID FROM JOB_SITE WHERE SITE_NAME= (%s);"""
        locations = []
        cursor.execute(sql_starter, [fixedJob])
        job_id = cursor.fetchone()
        cursor.execute("SELECT WORK_PACKAGE_ID FROM WORK_PACKAGE WHERE JOB_SITE_ID = %s;", [job_id[0]])
        ids = cursor.fetchall()
        cursor.execute("SELECT WORK_PACKAGE_NAME FROM WORK_PACKAGE WHERE JOB_SITE_ID=%s;", [job_id[0]])
        work_package_names = cursor.fetchall()
        cursor.execute("SELECT PRICE_OF_WORK FROM WORK_PACKAGE WHERE JOB_SITE_ID=%s;", [job_id[0]])
        prices_of_work = cursor.fetchall()
        cursor.execute("SELECT HOURS_ALLOTED FROM WORK_PACKAGE WHERE JOB_SITE_ID=%s;", [job_id[0]])
        hours_alloted_for_each = cursor.fetchall()
        cursor.execute("SELECT HOURS_USED FROM WORK_PACKAGE WHERE JOB_SITE_ID=%s;", [job_id[0]])
        hours_used_for_each = cursor.fetchall()
        work_package_info = []
        for x in range(len(work_package_names)):
            work_package_info.append([ ids[x], jobSite, work_package_names[x], prices_of_work[x], hours_alloted_for_each[x], hours_used_for_each[x] ])
        for x in work_package_info:
            work_package = WorkPackages(x[0], x[1], x[2], x[3], x[4], x[5])
            work_packages.append(work_package)
        print(work_packages)
        return jsonify([e.serialize() for e in work_packages])


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

@app.route("/delete_job", methods=["POST"], strict_slashes=False)
@cross_origin()
def delete_job():
    location = request.json['location']
    site_name = request.json['site_name']
    start_date = request.json['start_date']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    position = request.json['position']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    zipcode = request.json['zipcode']

    general_manager = position_check_pm(first_name, last_name, address, city, state, zipcode, position)
    if general_manager:
        delete = delete_from_job_site(location, site_name, start_date)
        if delete:
            job = Jobs(1,start_date,site_name,location)
            jobs = [job]
            return jsonify([e.serialize() for e in jobs])
        else:
            job = Jobs(1, "Job does not exist", "Job does not exist", start_date)
            jobs = [job]
            return jsonify([e.serialize() for e in jobs])
    else:
        job = Jobs(1, "You are not a general manager and may not add new jobs", "You are not a general manager and may not add new jobs", start_date)
        jobs = [job]
        return jsonify([e.serialize() for e in jobs])

@app.route("/add_job", methods=["POST"], strict_slashes=False)
@cross_origin()
def add_job():
    location = request.json['location']
    site_name = request.json['site_name']
    start_date = request.json['start_date']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    position = request.json['position']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    zipcode = request.json['zipcode']

    general_manager = position_check_pm(first_name, last_name, address, city, state, zipcode, position)
    if general_manager:
        insert_into_location(location)
        insert_into_job_site(location, site_name, start_date)
        job = Jobs(1,start_date,site_name,location)
        jobs = [job]
        return jsonify([e.serialize() for e in jobs])
    else:
        job = Jobs(1, "You are not a general manager and may not add new jobs", "You are not a general manager and may not add new jobs", start_date)
        jobs = [job]
        return jsonify([e.serialize() for e in jobs])

@app.route("/add_work_package", methods=["POST"], strict_slashes=False)
@cross_origin()
def add_work_package():
    job = request.json['job']
    work_package_name = request.json['work_package_name']
    price_of_work = request.json['price_of_work']
    hours_alloted = request.json['hours_alloted']
    hours_used = request.json['hours_used']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    position = request.json['position']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    zipcode = request.json['zipcode']
    years_employed = request.json['years_employed']
    if position == 'Project Manager':
      upper_management =  position_check_pm(first_name,last_name,address,city,state,zipcode, position)
    elif position == 'Foreman':
        upper_management = position_check_fm(first_name, last_name, address, city, state, zipcode, position)
    if upper_management:
        work_p = insert_into_work_package(job, work_package_name, price_of_work, hours_alloted, hours_used)
        if work_p == False:
            work_package = WorkPackages(1, "that is not a job to add to", "that is not a job to add to", 1, 1, 1)
        else:
            work_package = WorkPackages(1,job,work_package_name,price_of_work,hours_alloted,hours_used)
        work_packages = [work_package]
        return jsonify([e.serialize() for e in work_packages])
    else:
        work_package = WorkPackages(1, "You can't add work packages", "You can't add work packages", price_of_work, hours_alloted, hours_used)
        work_packages = [work_package]
        return jsonify([e.serialize() for e in work_packages])

@app.route("/delete_work_package", methods=["POST"], strict_slashes=False)
@cross_origin()
def delete_work_package():
    job = request.json['job']
    work_package_name = request.json['work_package_name']
    price_of_work = request.json['price_of_work']
    hours_alloted = request.json['hours_alloted']
    hours_used = request.json['hours_used']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    position = request.json['position']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    zipcode = request.json['zipcode']
    years_employed = request.json['years_employed']
    if position == 'Project Manager':
      upper_management =  position_check_pm(first_name,last_name,address,city,state,zipcode, position)
    elif position == 'Foreman':
        upper_management = position_check_fm(first_name, last_name, address, city, state, zipcode, position)
    if upper_management:
        work = delete_from_work_package(job, work_package_name, price_of_work, hours_alloted, hours_used)
        if work == False:
            work_package = WorkPackages(1,"that is not a work package for this job","that is not a work package for this job",price_of_work,hours_alloted,hours_used)
            work_packages = [work_package]
            return jsonify([e.serialize() for e in work_packages])
        else:
            work_package = WorkPackages(1,job,work_package_name,price_of_work,hours_alloted,hours_used)
            work_packages = [work_package]
            return jsonify([e.serialize() for e in work_packages])
    else:
        work_package = WorkPackages(1, "You can't add work packages", "You can't add work packages", price_of_work, hours_alloted, hours_used)
        work_packages = [work_package]
        return jsonify([e.serialize() for e in work_packages])


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
    first_name_gm = request.json['first_name_gm']
    last_name_gm = request.json['last_name_gm']
    position_gm = request.json['position_gm']
    address_gm = request.json['address_gm']
    city_gm = request.json['city_gm']
    state_gm = request.json['state_gm']
    zipcode_gm = request.json['zipcode_gm']
    general_man = position_check_gm(first_name_gm,last_name_gm,address_gm,city_gm,state_gm,zipcode_gm,position_gm)
    if general_man:
        if (position == "Inside Wireman") or (position == "Residential Wireman"):
          insert_into_electrician(first_name,last_name,address,city,state,zipcode, years_employed, pay_rate, position)
        else:
            insert_into_salaried_employee(first_name,last_name,address,city,state,zipcode, years_employed, pay_rate, position)
        employee = Employees(1, first_name,last_name,address,city,state,zipcode,position,pay_rate,years_employed)
        employees = [employee]
        return jsonify([e.serialize() for e in employees])
    else:
        employee = Employees(1, "You are not a general manager and may not add new employees", "You are not a general manager and may not add new employees", "You are not a general manager and may not add new employees","You are not a general manager and may not add new employees","You are not a general manager and may not add new employees",0,"You are not a general manager and may not add new employees",0,0)
        employees = [employee]
        return jsonify([e.serialize() for e in employees])

@app.route("/delete_employee", methods=["POST"], strict_slashes=False)
@cross_origin()
def delete_employee():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    position = request.json['position']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    zipcode = request.json['zipcode']
    years_employed = request.json['years_employed']
    pay_rate = request.json['pay_rate']
    first_name_gm = request.json['first_name_gm']
    last_name_gm = request.json['last_name_gm']
    position_gm = request.json['position_gm']
    address_gm = request.json['address_gm']
    city_gm = request.json['city_gm']
    state_gm = request.json['state_gm']
    zipcode_gm = request.json['zipcode_gm']
    general_man = position_check_gm(first_name_gm,last_name_gm,address_gm,city_gm,state_gm,zipcode_gm,position_gm)
    if general_man:
        if (position == "Inside Wireman") or (position == "Residential Wireman"):
          electrician = delete_from_electrician(first_name,last_name,address,city,state,zipcode, years_employed, pay_rate, position)
          if electrician == False:
              employee = Employees(1, "that is not an electrician in this company","that is not an electrician in this company","that is not an electrician in this company","that is not an electrician in this company","that is not an electrician in this company",zipcode,"that is not an electrician in this company",pay_rate,years_employed)
              employees = [employee]
              return jsonify([e.serialize() for e in employees])
          else:
              employee = Employees(1, first_name, last_name, address, city, state, zipcode, position, pay_rate, years_employed)
              employees = [employee]
              return jsonify([e.serialize() for e in employees])
        else:
            salaried = delete_from_salaried_employee(first_name,last_name,address,city,state,zipcode, years_employed, pay_rate, position)
            if salaried == False:
                employee = Employees(1, "that is not an employee in this company",
                                     "that is not an employee in this company",
                                     "that is not an employee in this company",
                                     "that is not an employee in this company",
                                     "that is not an employee in this company", zipcode,
                                     "that is not an employee in this company", pay_rate, years_employed)
                employees = [employee]
                return jsonify([e.serialize() for e in employees])
            else:
                employee = Employees(1, first_name,last_name,address,city,state,zipcode,position,pay_rate,years_employed)
                employees = [employee]
                return jsonify([e.serialize() for e in employees])
    else:
        employee = Employees(1, "You are not a general manager and may not add new employees", "You are not a general manager and may not add new employees", "You are not a general manager and may not add new employees","You are not a general manager and may not add new employees","You are not a general manager and may not add new employees",0,"You are not a general manager and may not add new employees",0,0)
        employees = [employee]
        return jsonify([e.serialize() for e in employees])






if __name__ == '__main__':
    app.run(debug=True)