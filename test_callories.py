from main import CaloriesCalculator, Record

def test_caloriest_calculator():
    calories_calculator = CaloriesCalculator(1000)
    calories_calculator.add_record(Record(amount=150, comment='Чай с сушками'))

    calories_calculator.add_record(Record(amount=400, comment='Обед'))

    calories_calculator.add_record(Record(amount=300, comment='Сэндвич', date='16.05.2021'))

    calories_remained = 1000 - 150 - 400
    assert calories_remained == calories_calculator.get_calories_remained()
