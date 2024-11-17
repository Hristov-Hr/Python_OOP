from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:

    LOAN_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    CLIENT_TYPES = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.LOAN_TYPES.keys():
            raise Exception("Invalid loan type!")

        self.loans.append(self.LOAN_TYPES[loan_type]())

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENT_TYPES.keys():
            raise Exception("Invalid client type!")

        if self.capacity <= len(self.clients):
            return "Not enough bank capacity."

        self.clients.append(self.CLIENT_TYPES[client_type](client_name, client_id, income))

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        is_match = [("Student", "StudentLoan"), ("Adult", "MortgageLoan")]
        loan = [l for l in self.loans if loan_type == l.__class__.__name__][0]
        client = [c for c in self.clients if client_id == c.client_id][0]

        if (client.__class__.__name__, loan.__class__.__name__) not in is_match:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        try:
            client = next(filter(lambda x: x.client_id == client_id, self.clients))
            if len(client.loans) > 0:
                raise Exception("The client has loans! Removal is impossible!")

            self.clients.remove(client)
            return f"Successfully removed {client.name} with ID {client_id}."

        except StopIteration:
            raise Exception("No such client!")

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = [lo.increase_interest_rate() for lo in self.loans if lo.__class__.__name__ == loan_type]

        return f"Successfully changed {len(number_of_changed_loans)} loans."

    def increase_clients_interest(self, min_rate: float):

        changed_client_rates_number = [cl.increase_clients_interest() for cl in self.clients if cl.interest < min_rate]

        return f"Number of clients affected: {len(changed_client_rates_number)}."

    def get_statistics(self):
        loans_count_granted_to_clients = 0
        granted_sum = 0
        client_interest_rate = 0

        for client in self.clients:
            loans_count_granted_to_clients += len(client.loans)
            granted_sum += sum(lo.amount for lo in client.loans)
            client_interest_rate += client.interest

        avg_client_interest_rate = client_interest_rate / len(self.clients) if self.clients else 0

        result = [f"Active Clients: {len(self.clients)}", f"Total Income: {sum(i.income for i in self.clients):.2f}",
                  f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}",
                  f"Available Loans: {len(self.loans)}, Total Sum: {sum(l.amount for l in self.loans):.2f}",
                  f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"]

        return "\n".join(result)