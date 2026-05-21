def add_transaction(ledger, description, amount, category='general'):
    ledger.append({
        'description': description,
        'amount': amount,
        'category': category,
        'type': 'income' if amount > 0 else 'expense'
    })
    return ledger

def generate_report(ledger):
    income = sum(tx['amount'] for tx in ledger if tx['type'] == 'income')
    expenses = sum(abs(tx['amount']) for tx in ledger if tx['type'] != 'income')
    return {
        'income': income,
        'expenses': expenses,
        'net_balance': income - expenses,
        'transaction_count': len(ledger)
    }

def save_report(report, filepath):
    import json
    with open(filepath, 'w') as f:
        json.dump(report, f, indent=2)
    return filepath
