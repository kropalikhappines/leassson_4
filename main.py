from __utils__ import currency_rates

if __name__ == '__main__':
    valu, dt = currency_rates('UsD')
    print(f"Курс доллара {valu}, дата {dt}")
    valu, dt = currency_rates('UsD')

    print(f"Курс евро {valu}, дата {dt}")
    #print(f"Курс Фунт стерлингов Соединенного королевства {currency_rates('gBp')}")
    valu, dt = currency_rates('sd')
    print(f"Курс  {valu}, дата {dt}")