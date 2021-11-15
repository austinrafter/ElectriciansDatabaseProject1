class Jobs():
    job_id = 0
    start = ''
    site = ''
    location = ''
    def __init__(self, job_id,start,site,location):
        self.job_id = job_id
        self.start = start
        self.site = site
        self.location = location

class Employees():
    employee_id = 0
    first_name = ''
    last_name = ''
    address = ''
    city = ''
    state = ''
    zip = 0
    position = ''
    pay_rate = 0.0
    years_employed = 0

    def __init__(self, employee_id, first_name, last_name, address, city, state, zip, position, pay_rate, years_employed):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.position = position
        self.pay_rate = pay_rate
        self.years_employed = years_employed

class WorkPackages():
    work_package_id = 0
    job = ''
    work_package_name = ''
    price_of_work = 0
    hours_alloted = 0
    hours_used = 0

    def __init__(self, work_package_id,job, work_package_name, price_of_work, hours_alloted, hours_used):
        self.work_package_id = work_package_id
        self.job = job
        self.work_package_name = work_package_name
        self.price_of_work = price_of_work
        self.hours_alloted = hours_alloted
        self.hours_used = hours_used
