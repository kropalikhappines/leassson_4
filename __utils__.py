import requests
import xml.etree.ElementTree as et
from datetime import datetime


response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

val_curs = et.XML(response.content)

def currency_rates(char_codes):
    result = {}
    date_now = val_curs.get('Date')

    for i in val_curs:
        #print(i)
        val = i.find('Value').text
        char_code = i.find('CharCode').text
        result[char_code] = {'val': val,}
    res = result.get(char_codes.upper(), {}).get('val')
    date_now = datetime.strptime(date_now, '%d.%m.%Y').date()
    if res == None:
        date_now = None
    return res, date_now