class JOB():
    location = ''
    site = ''
    start = ''

    def __init__(self, site, start, location):
        self.location_name = location_name
        self.site = site
        self.start = start

class EMPLOYEE():
    first_name = ''
    last_name = ''
    address = ''
    city = ''
    state = ''
    zip = 0
    position = ''
    pay_rate = 0.0
    years_employed = 0

    def __init__(self, first_name, last_name, address, city, state, zip, position, pay_rate, years_employed):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.position = position
        self.pay_rate = pay_rate
        self.years_employed = years_employed

class WORK_PACKAGE():
    job = ''
    work_package_name = ''
    price_of_work = 0
    hours_alloted = 0
    hours_used = 0

    def __init__(self, job, work_package_name, price_of_work, hours_alloted, hours_used):
        self.job = job
        self.work_package_name = work_package_name
        self.price_of_work = price_of_work
        self.hours_alloted = hours_alloted
        self.hours_used = hours_used
