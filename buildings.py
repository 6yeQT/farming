

class chicken_coop(object):
    def __init__(self, farm_no, position, driver):
        self.position = position
        self.farm_no = farm_no

    def enter(self):
        print 'enter position'

    def collect_products(self):
        print 'collecting eggs'

    def start_production(self):
        print 'running production'

