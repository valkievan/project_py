from main import Record, CashCalculator

cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=100, comment='Латте'))

cash_calculator.add_record(Record(amount=250, comment='Долг за такси'))

cash_calculator.add_record(Record(amount=3500,comment='Ресторан', date='16.07.2021'))

print(cash_calculator.get_today_cash_remained('rub'))