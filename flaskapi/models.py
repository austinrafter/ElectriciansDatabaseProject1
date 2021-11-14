class JOB():
    location_name = ''
    site_name = ''
    start_date = ''

    def __init__(self, site_name, start_date, location_name):
        self.location_name = location_name
        self.site_name = site_name
        self.start_date = start_date

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

class WORK_PACKAGE():
    job = ''
    work_package_name = ''
    price_of_work = 0
    hours_alloted = 0
    hours_used = 0
