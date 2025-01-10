class Customer:
    def __init__(self, customer_id, company_name, contact_name, country):
        self.customer_id = customer_id
        self.company_name = company_name
        self.contact_name = contact_name
        self.country = country


class CustomerRepository:
    def __init__(self, database):
        self.database = database

    def search_by_country(self, country_name: str):
        return self._search(
            lambda customer: self._contains(customer.country, country_name)
        )

    def search_by_company_name(self, company_name: str):
        return self._search(
            lambda customer: self._contains(customer.company_name, company_name)
        )

    def search_by_contact_name(self, contact_name: str):
        return self._search(
            lambda customer: self._contains(customer.contact_name, contact_name)
        )

    def _search(self, predicate):
        matching_customers = []
        for customer in self.database.customers:
            if predicate(customer):
                matching_customers.append(customer)
        return self._sort_customers(matching_customers)

    def _contains(self, source, target):
        source_length, target_length = len(source), len(target)
        for start_index in range(source_length - target_length + 1):
            if source[start_index : start_index + target_length] == target:
                return True
        return False

    def _sort_customers(self, customers):
        for outer_index in range(len(customers)):
            for inner_index in range(outer_index + 1, len(customers)):
                if (
                    customers[outer_index].customer_id
                    > customers[inner_index].customer_id
                ):
                    customers[outer_index], customers[inner_index] = (
                        customers[inner_index],
                        customers[outer_index],
                    )
        return customers


class CustomerExporter:
    @staticmethod
    def export_to_csv(customers):
        csv_output = ""
        for customer in customers:
            csv_output += (
                str(customer.customer_id)
                + ","
                + customer.company_name
                + ","
                + customer.contact_name
                + ","
                + customer.country
                + "\n"
            )
        return csv_output


if __name__ == "__main__":
    mock_database = type(
        "MockDB",
        (),
        {
            "customers": [
                Customer(1, "Company A", "John Doe", "USA"),
                Customer(2, "Company B", "Jane Smith", "Canada"),
            ]
        },
    )()

    repository = CustomerRepository(mock_database)
    exporter = CustomerExporter()

    search_results = repository.search_by_country("USA")
    print(exporter.export_to_csv(search_results))
