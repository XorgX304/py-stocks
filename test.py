from Stock import Stock

m = Stock('MSFT')

""" print('name', m.get_name())
print('current price', m.get_current_price())
print('52 week high', m.get_52week_high())
print('52 week low', m.get_52week_low())
print('address', m.get_address())
print('analyst recs', m.get_analyst_recs())
print('recent recs', m.get_most_recent_recs())
print('avg vol', m.get_average_volume())
print('day high', m.get_day_high())
print('day low', m.get_day_low())
print('div yield', m.get_dividend_yield())
print('employees', m.get_employees())
print('holders', m.get_holders())
print('industry', m.get_industry())
print('sector', m.get_sector())
print('sustainability info', m.get_sustainability_info())
print('volume', m.get_volume())
print('website', m.get_website())
print('summary', m.get_summary()) 
print('last month data', m.get_last_month_data())

"""

print(m.get_news())
