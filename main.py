import datetime as dt


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        if date is not None:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = dt.date.today()
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.records = []
        self.limit = limit

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.datetime.now().date()
        today_stats = sum(record.amount if record.date == today else 0 for record in self.records)
        return today_stats

    def get_week_stats(self):
        today = dt.datetime.now()
        week = today - dt.timedelta(7)
        week_stats = sum(record.amount for record in self.records)
        return week_stats

    def remained(self):
        return self.limit - self.get_today_stats()


class CaloriesCalculator(Calculator):

    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        calories_remained = self.limit - self.get_today_stats()
        if calories_remained <= 0:
            print("Достигнут дневной лимит")
        else:
            print(f"Для достижения сегодняшней нормы необходимо ещё {calories_remained} кКал")
        return calories_remained


class CashCalculator(Calculator):

    USD_RATE = 64.0
    EURO_RATE = 68.0
    RUB_RATE = 1.0

    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        cash_remained = self.remained()
        if cash_remained == 0:
            return 'Деньги закончились'
        currencies = {
            'eur': ('Euro', self.EURO_RATE),
            'usd': ('USD', self.USD_RATE),
            'rub': ('руб', self.RUB_RATE),
        }
        if currency not in currencies:
            return 'No such currency.'
        sign, rate = currencies.get(currency)
        cash_remained = round(cash_remained / rate, 2)
        if cash_remained > 0:
            return f'Остаток: {cash_remained} {sign}'
        cash_remained = abs(cash_remained)
        return f'Текущий долг: {cash_remained} {sign}'

