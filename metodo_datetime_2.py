from datetime import datetime, date

mifecha = datetime(2022,8,15,13,2)
mifecha = mifecha.replace(month = 3)

print(mifecha)

nacimiento = date(1991,1,30)
muerte = date(2022,8,15)

vida = muerte - nacimiento

print(vida)