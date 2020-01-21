"""
Supports arithmetic operations and operations with dates in dd.mm.yyyy format.

For example:
2+(7-2)*3/5 ->5.0
28.11.2019+10 -> 08.12.2019
28.11.2019-50 -> 09.10.2019
25.10.2019-22.08.2019 -> 64 days
YYY
"""

from calcdigits import calculate_digits
from calcdates import date_delta, calculate_date, date_or_not

input_str=input('Введите выражение: ')

check_str=''
for x in input_str:
    if x.isdigit() or x=='.':
        check_str=check_str+x
    else:
        break
if date_or_not(check_str):
    if '-' in input_str:
        splt_str=input_str.split('-')
        if len(splt_str)==2:
            if date_or_not(splt_str[1]):
                print('Результат: ',date_delta(date1=splt_str[0],date2=splt_str[1]),'дней')
            else:
                try:
                    print('Результат: ',calculate_date(date1=splt_str[0],days=int(splt_str[1]),operation='-'))
                except:
                    print('Некорректный синтаксис')
        else:
            print('Некорректный синтаксис')
    elif '+' in input_str:
        splt_str=input_str.split('+')
        if len(splt_str)==2:
            try:
                print('Результат: ',calculate_date(date1=splt_str[0],days=int(splt_str[1]),operation='+'))
            except:
                print('Некорректный синтаксис')
        else:
            print('Некорректный синтаксис')
    else:
        print('Некорректный синтаксис')        
else:
    try:       
        print('Результат: ',calculate_digits(input_str))
    except ZeroDivisionError:
        print('Деление на 0 невозможно')
    except:
        print('Некорректный синтаксис')
