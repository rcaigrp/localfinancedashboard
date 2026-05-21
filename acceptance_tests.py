import sys
import os
import json
import tempfile
import pytest

sys.path.insert(0, '/workspace')

def test_criterion_1_module_exists():
    import finance_dashboard
    assert hasattr(finance_dashboard, 'add_transaction')
    assert hasattr(finance_dashboard, 'generate_report')
    assert hasattr(finance_dashboard, 'save_report')

def test_criterion_2_add_transaction():
    import finance_dashboard
    ledger = []
    finance_dashboard.add_transaction(ledger, 'Test', 100, 'income')
    assert len(ledger) == 1
    assert ledger[0]['description'] == 'Test'
    assert ledger[0]['amount'] == 100
    assert ledger[0]['type'] == 'income'

def test_criterion_3_generate_report():
    import finance_dashboard
    ledger = [
        {'description': 'Salary', 'amount': 1000, 'category': 'income', 'type': 'income'},
        {'description': 'Food', 'amount': -100, 'category': 'expense', 'type': 'expense'}
    ]
    report = finance_dashboard.generate_report(ledger)
    assert report['income'] == 1000
    assert report['expenses'] == 100
    assert report['net_balance'] == 900
    assert report['transaction_count'] == 2

def test_criterion_4_save_report():
    import finance_dashboard
    report = {'income': 1000, 'expenses': 100, 'net_balance': 900}
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        f.write('')
        filepath = f.name
    finance_dashboard.save_report(report, filepath)
    with open(filepath, 'r') as f:
        saved_report = json.load(f)
    assert saved_report == report
