
import analyzer
from operations import square_calc, time_transformer, visualizer   
import pandas as pd

amount = int(input('Введите количество эксперименотов: '))
max_epochs = int(input('Введите максимальное количество эпох: '))

extra_data = {}
extra_data['Размер деления'] = float(input('Введите размер деления в микрометрах: '))

extra_data['Частота записи'] = int(input('Введите частоту записи в Гц: '))

min_,max_ = map(float,input('Введите интервал для анализа в секундах, через дефис: ').split('-'))

experiments = {}
for i in range(amount):
    print('___'*10)
    name = input('Введите название: ')
    experiments[name] = {}

    dim = float(input('Введите диаметр в делениях: '))
    experiments[name]['dim'] = dim

    epochs = int(input('Введите количество эпох для этого протопласта: '))
    experiments[name]['epochs'] = epochs

min_,max_ = time_transformer.transform(min_,max_,extra_data['Частота записи'])
extra_data['начало'] = min_
extra_data['конец'] = max_

square_calc.calculation(experiments,extra_data['Размер деления'])
table_I, table_V = analyzer.generate_tables(experiments,amount, max_epochs,min_,max_)

with pd.ExcelWriter('results/data.xlsx') as writer:  
    table_I.to_excel(writer, sheet_name='table_I')
    table_V.to_excel(writer, sheet_name='table_V')

stat_data = analyzer.statistics_calc(table_I, table_V)

with pd.ExcelWriter('results/stat.xlsx') as writer:
    stat_data.to_excel(writer, sheet_name='statistics')
visualizer.plot(stat_data)







