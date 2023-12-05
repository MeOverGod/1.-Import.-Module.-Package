from datetime import datetime
from application.db.people import get_employees
from application.salary import calculate_salary

if __name__ == '__main__':
    calculate_salary('func1')
    get_employees('func2')
    print(datetime.today().strftime('%d/%m/%Y'))