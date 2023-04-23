import pandas as pd
from openpyxl import Workbook
from bs4 import BeautifulSoup

# Прочитать HTML-код страницы
with open('info1/templates/info1/all.html') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

# Получить таблицу в виде списка
table = []
for row in soup.select('table tr'):
    table.append([cell.text.strip() for cell in row.select('td')])

# Создать объект DataFrame
df = pd.DataFrame(table)

# Создать новый Excel-файл и сохранить таблицу в него
with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer:
    writer.workbook = Workbook()
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer._save()
