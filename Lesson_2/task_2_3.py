seasons = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
month = {1: 'январь',
         2: 'февраль',
         3: 'март',
         4: 'апрель',
         5: 'май',
         6: 'июнь',
         7: 'июль',
         8: 'август',
         9: 'сентябрь',
         10: 'октябрь',
         11: 'ноябрь',
         12: 'декабрь',
         }
month_season = {1: 'зима',
                2: 'зима',
                3: 'весна',
                4: 'весна',
                5: 'весна',
                6: 'лето',
                7: 'лето',
                8: 'лето',
                9: 'осень',
                10: 'осень',
                11: 'осень',
                12: 'зима',
                }
m = int(input('введите номер месяца в году:'))
print(f'введенный месяц "{month[m]}" относится к сезону: {seasons[m - 1]}')
print('')
print('Второй способ:')
print(f'введенный месяц "{month[m]}" относится к сезону: {month_season[m]}')
