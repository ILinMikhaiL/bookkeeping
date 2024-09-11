import application.salary
import application.db.people as people
import datetime

current_date = datetime.date.today().isoformat()
print(current_date)

if __name__ == '__main__':
        application.salary.calculate_salary()
        people.get_employees()