import os
import json
from datetime import datetime

class FinanceDashboard:
    def __init__(self):
        self.ledger = []

    def add_transaction(self, amount, category, date=None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        self.ledger.append({
            "amount": amount,
            "category": category,
            "date": date
        })

    def generate_report(self):
        income = 0
        expenses = 0
        for t in self.ledger:
            if t["category"].startswith("income"):
                income += abs(t["amount"])
            else:
                expenses += abs(t["amount"])
        return {
            "income": income,
            "expenses": expenses,
            "balance": income - expenses,
            "transactions": self.ledger
        }

    def save_report(self, filepath):
        report = self.generate_report()
        with open(filepath, "w") as f:
            json.dump(report, f, indent=2)
