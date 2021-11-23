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
    foreman_id = 0
    site_name_foreman = ''
    package_name_foreman = ''
    worker_first_name = ''
    worker_last_name = ''
    individual_hours_alloted = 0

    def __init__(self, foreman_id, site_name_foreman,package_name_foreman, worker_first_name, worker_last_name, individual_hours_alloted):
        self.foreman_id = foreman_id
        self.site_name_foreman = site_name_foreman
        self.package_name_foreman = package_name_foreman
        self.worker_first_name = worker_first_name
        self.worker_last_name = worker_last_name
        self.individual_hours_alloted = individual_hours_alloted

    def serialize(self):
        return {
            'foreman_id' : self.foreman_id,
            'site_name_foreman': self.site_name_foreman,
            'package_name_foreman': self.package_name_foreman,
            'worker_first_name': self.worker_first_name,
            'worker_last_name': self.worker_last_name,
            'individual_hours_alloted': self.individual_hours_alloted,
        }

class ProjectManager():
    project_manager_id = 0
    work_package_name = ''
    hours_used = ''
    material_cost = 0.0
    work_package_cost = 0.0
    amount_made = 0.0
    total_profits = 0.0
    site_name = ''

    def __init__(self, project_manager_id, work_package_name, hours_used, material_cost, work_package_cost, amount_made, total_profits, site_name):
        self.project_manager_id = project_manager_id
        self.work_package_name = work_package_name
        self.hours_used = hours_used
        self.material_cost = material_cost
        self.work_package_cost = work_package_cost
        self.amount_made = amount_made
        self.total_profits = total_profits
        self.site_name = site_name

    def serialize(self):
        return {
            'project_manager_id' : self.project_manager_id,
            'work_package_name': self.work_package_name,
            'hours_used': self.hours_used,
            'material_cost': self.material_cost,
            'work_package_cost': self.work_package_cost,
            'amount_made': self.amount_made,
            'total_profits': self.total_profits,
            'site_name': self.site_name,
        }

class GeneralManager():
    general_manager_id = 0
    site_name = ''
    cost_of_project = 0.0
    amount_made = 0.0
    total_profits = 0.0
    number_of_days_on_project = 0.0


    def __init__(self, general_manager_id, site_name, cost_of_project, amount_made, total_profits, number_of_days_on_project):
        self.site_name = site_name
        self.cost_of_project = cost_of_project
        self.general_manager_id = general_manager_id
        self.amount_made = amount_made
        self.total_profits = total_profits
        self.number_of_days_on_project = number_of_days_on_project

    def serialize(self):
        return {
            'general_manager_id' : self.general_manager_id,
            'site_name': self.site_name,
            'cost_of_project': self.cost_of_project,
            'amount_made': self.amount_made,
            'total_profits': self.total_profits,
            'number_of_days_on_project': self.number_of_days_on_project,

        }

class Inventory():
    inventory_id = 0
    material_name = ''
    cost_per_unit = 0.0
    weight_per_unit = 0.0


    def __init__(self, inventory_id, material_name, cost_per_unit, weight_per_unit):
        self.inventory_id = inventory_id
        self.material_name = material_name
        self.cost_per_unit = cost_per_unit
        self.weight_per_unit = weight_per_unit


    def serialize(self):
        return {
            'inventory_id': self.inventory_id,
            'material_name': self.material_name,
            'cost_per_unit': self.cost_per_unit,
            'weight_per_unit': self.weight_per_unit,

        }

class Inventory():
    inventory_id = 0
    material_name = ''
    cost_per_unit = 0.0
    weight_per_unit = 0.0


    def __init__(self, inventory_id, material_name, cost_per_unit, weight_per_unit):
        self.inventory_id = inventory_id
        self.material_name = material_name
        self.cost_per_unit = cost_per_unit
        self.weight_per_unit = weight_per_unit


    def serialize(self):
        return {
            'inventory_id': self.inventory_id,
            'material_name': self.material_name,
            'cost_per_unit': self.cost_per_unit,
            'weight_per_unit': self.weight_per_unit,

        }

class MaterialInWorkPackage():
    material_in_work_package_id = 0
    material_name = ''
    amount_alloted = 0
    amount_used = 0
    work_package_name = ''
    site_name = ''


    def __init__(self, material_in_work_package_id, material_name, amount_alloted, amount_used, work_package_name, site_name):
        self.material_in_work_package_id = material_in_work_package_id
        self.material_name = material_name
        self.amount_alloted = amount_alloted
        self.amount_used = amount_used
        self.work_package_name = work_package_name
        self.site_name = site_name


    def serialize(self):
        return {
            'material_in_work_package_id': self.material_in_work_package_id,
            'material_name': self.material_name,
            'amount_alloted': self.amount_alloted,
            'amount_used': self.amount_used,
            "work_package_name": self.work_package_name,
            "site_name": self.site_name,

        }

class ElectricianOnWorkPackage():
    electrician_on_work_package_id = 0
    first_name = ''
    last_name = ''
    work_package_name = ''
    site_name = ''


    def __init__(self, electrician_on_work_package_id, first_name, last_name, work_package_name, site_name):
        self.electrician_on_work_package_id = electrician_on_work_package_id
        self.first_name = first_name
        self.last_name = last_name
        self.work_package_name = work_package_name
        self.site_name = site_name


    def serialize(self):
        return {
            'electrician_on_work_package_id': self.electrician_on_work_package_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            "work_package_name": self.work_package_name,
            "site_name": self.site_name,

        }





