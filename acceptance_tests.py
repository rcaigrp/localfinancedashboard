import pytest
import json
import os
import tempfile
from finance_dashboard import parse_transactions, calculate_totals, generate_report

def test_criterion_1_module_exists():
    import finance_dashboard
    assert hasattr(finance_dashboard, 'parse_transactions')
    assert hasattr(finance_dashboard, 'calculate_totals')
    assert hasattr(finance_dashboard, 'generate_report')

def test_criterion_2_parse_transactions():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write("date,category,amount\n2023-01-01,Income,500\n2023-01-02,Expense,200\n")
        temp_path = f.name
    try:
        transactions = parse_transactions(temp_path)
        assert isinstance(transactions, list)
        assert len(transactions) == 2
        assert 'date' in transactions[0]
        assert 'category' in transactions[0]
        assert 'amount' in transactions[0]
    finally:
        os.unlink(temp_path)

def test_criterion_3_calculate_totals():
    transactions = [
        {"date": "2023-01-01", "category": "Income", "amount": 500},
        {"date": "2023-01-02", "category": "Expense", "amount": 200}
    ]
    totals = calculate_totals(transactions)
    assert 'total_income' in totals
    assert 'total_expense' in totals
    assert 'net' in totals
    assert totals['total_income'] == 500
    assert totals['total_expense'] == 200
    assert totals['net'] == 300

def test_criterion_4_generate_report():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_path = f.name
    try:
        generate_report(temp_path)
        assert os.path.exists(temp_path)
        with open(temp_path, 'r') as f:
            report = json.load(f)
        assert 'total_income' in report
        assert 'total_expense' in report
        assert 'net' in report
    finally:
        os.unlink(temp_path)
