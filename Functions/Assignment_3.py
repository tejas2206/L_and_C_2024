class Customer:
    def __init__(self, customer_id, company_name, contact_name, country):
        self.customer_id = customer_id
        self.company_name = company_name
        self.contact_name = contact_name
        self.country = country

class CustomerRepository:
    def __init__(self, db):
        self.db = db

    def search_by_country(self, country: str):
        return self._search(lambda c: self._contains(c.country, country))

    def search_by_company_name(self, company: str):
        return self._search(lambda c: self._contains(c.company_name, company))

    def search_by_contact(self, contact: str):
        return self._search(lambda c: self._contains(c.contact_name, contact))

    def _search(self, predicate):
        result = []
        for customer in self.db.customers:
            if predicate(customer):
                result.append(customer)
        return self._sort(result)

    def _contains(self, source, target):
        n, m = len(source), len(target)
        for i in range(n - m + 1):
            if source[i:i + m] == target:
                return True
        return False

    def _sort(self, customers):
        for i in range(len(customers)):
            for j in range(i + 1, len(customers)):
                if customers[i].customer_id > customers[j].customer_id:
                    customers[i], customers[j] = customers[j], customers[i]
        return customers

class CustomerExporter:
    @staticmethod
    def export_to_csv(customers):
        output = ""
        for customer in customers:
            output += (str(customer.customer_id) + "," + customer.company_name + "," + 
                       customer.contact_name + "," + customer.country + "\n")
        return output

if __name__ == "__main__":
    db = type('MockDB', (), {"customers": [
        Customer(1, "Company A", "John Doe", "USA"),
        Customer(2, "Company B", "Jane Smith", "Canada")
    ]})()

    repository = CustomerRepository(db)
    exporter = CustomerExporter()

    results = repository.search_by_country("USA")
    print(exporter.export_to_csv(results))