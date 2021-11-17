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

    def serialize(self):
        return {
            'job_id': self.job_id,
            'start': self.start,
            'site': self.site,
            'location': self.location,
        }

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

    def serialize(self):
        return {
            'employee_id': self.employee_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip': self.zip,
            'position': self.position,
            'pay_rate': self.pay_rate,
            'years_employed': self.years_employed,
        }

class WorkPackages():
    work_package_id = 0
    job_site = ''
    work_package_name = ''
    price_of_work = 0
    hours_alloted = 0
    hours_used = 0

    def __init__(self, work_package_id,job_site, work_package_name, price_of_work, hours_alloted, hours_used):
        self.work_package_id = work_package_id
        self.job_site = job_site
        self.work_package_name = work_package_name
        self.price_of_work = price_of_work
        self.hours_alloted = hours_alloted
        self.hours_used = hours_used

    def serialize(self):
        return {
            'work_package_id': self.work_package_id,
            'job_site': self.job_site,
            'work_package_name': self.work_package_name,
            'price_of_work': self.price_of_work,
            'hours_alloted': self.hours_alloted,
            'hours_used': self.hours_used,
        }

class Foreman():
    site_name = ''
    work_package_name = ''
    worker_first_name = ''
    worker_last_name = ''
    individual_hours_alloted = 0

    def __init__(self, site_name,work_package_name, worker_first_name, worker_last_name, individual_hours_alloted):
        self.site_name = site_name
        self.work_package_name = work_package_name
        self.worker_first_name = worker_first_name
        self.worker_last_name = worker_last_name
        self.individual_hours_alloted = individual_hours_alloted

    def serialize(self):
        return {
            'site_name': self.site_name,
            'work_package_name': self.work_package_name,
            'worker_first_name': self.worker_first_name,
            'worker_last_name': self.worker_last_name,
            'individual_hours_alloted': self.individual_hours_alloted,
        }

class ProjectManager():
    work_package_name = ''
    hours_used = ''
    material_cost = 0.0
    work_package_cost = 0.0
    amount_made = 0.0
    total_profits = 0.0
    site_name = ''

    def __init__(self, work_package_name, hours_used, work_package_cost, amount_made, total_profits, site_name):
        self.work_package_name = work_package_name
        self.hours_used = hours_used
        self.work_package_cost = work_package_cost
        self.amount_made = amount_made
        self.total_profits = total_profits
        self.site_name = site_name

    def serialize(self):
        return {
            'work_package_name': self.work_package_name,
            'hours_used': self.hours_used,
            'work_package_cost': self.work_package_cost,
            'amount_made': self.amount_made,
            'total_profits': self.total_profits,
            'site_name': self.site_name,
        }

class GeneralManager():
    cost_of_project = 0.0
    amount_made = 0.0
    total_profits = 0.0
    number_of_days_on_project = 0.0

    def __init__(self, cost_of_project, amount_made, total_profits, number_of_days_on_project):
        self.cost_of_project = cost_of_project
        self.amount_made = amount_made
        self.total_profits = total_profits
        self.number_of_days_on_project = number_of_days_on_project

    def serialize(self):
        return {
            'cost_of_project': self.cost_of_project,
            'amount_made': self.amount_made,
            'total_profits': self.total_profits,
            'number_of_days_on_project': self.number_of_days_on_project,
        }





