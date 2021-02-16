class RetailItem:
    def __init__(self, description, invenunit, price):
        self.description = description
        self.invenunit = invenunit
        self.price = price

    def get_description(self):
        return self.description

    def get_invenunit(self):
        return self.invenunit

    def get_price(self):
        return self.price
