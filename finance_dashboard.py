import json
import os
from typing import Dict, List, Any

def add_transaction(ledger: Dict[str, Any], transaction: Dict[str, Any]) -> Dict[str, Any]:
    """Updates the ledger with a new transaction."""
    ledger['transactions'].append(transaction)
    return ledger

def generate_report(ledger: Dict[str, Any]) -> Dict[str, Any]:
    """Returns a summary dict of income/expenses."""
    income = 0.0
    expenses = 0.0
    for t in ledger.get('transactions', []):
        if t.get('type') == 'income':
            income += t.get('amount', 0.0)
        elif t.get('type') == 'expense':
            expenses += t.get('amount', 0.0)
    return {
        'total_income': income,
        'total_expenses': expenses,
        'net': income - expenses,
        'transaction_count': len(ledger.get('transactions', []))
    }

def save_report(ledger: Dict[str, Any], filename: str) -> str:
    """Writes a report to a file."""
    report = generate_report(ledger)
    with open(filename, 'w') as f:
        json.dump(report, f)
    return filename
