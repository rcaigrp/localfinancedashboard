import json

_ledger = []

def add_transaction(amount, category, type='expense'):
    global _ledger
    _ledger.append({'amount': amount, 'category': category, 'type': type})

def generate_report():
    income = sum(t['amount'] for t in _ledger if t['type'] == 'income')
    expenses = sum(t['amount'] for t in _ledger if t['type'] == 'expense')
    return {'income': income, 'expenses': expenses, 'net_balance': income - expenses}

def save_report(filepath):
    report = generate_report()
    with open(filepath, 'w') as f:
        json.dump(report, f)
    return filepath
