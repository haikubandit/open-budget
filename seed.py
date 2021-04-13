"""Seed file to make sample data for db."""

from models import Department, Division, GeneralFund, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Make a bunch of departments
# d1 = Department(dept_code="mktg", dept_name="Marketing")
# d2 = Department(dept_code="acct", dept_name="Accounting")
# d3 = Department(dept_code="r&d",
#                 dept_name="Research and Development", phone="908-7878")
# d4 = Department(dept_code="sales", dept_name="Sales", phone="225-6912")
# d5 = Department(
#     dept_code="it", dept_name="Information Technology", phone="888-4562")

# db.session.add_all([d1, d2, d3, d4, d5])

# db.session.commit()

# # Make a bunch of employees

# river = Employee(name="River Bottom", state="NY", dept_code="mktg")
# summer = Employee(name="Summer Winter", state="OR", dept_code="mktg")
# joaquin = Employee(name="Joaquin Phoenix", dept_code="acct")
# octavia = Employee(name="Octavia Spencer", dept_code="r&d")
# larry = Employee(name="Larry David", dept_code="r&d", state="NY")
# kurt = Employee(name="Kurt Cobain", dept_code="it", state="WA")
# rain = Employee(name="Rain Phoenix", dept_code="it")

# db.session.add_all([river, summer, joaquin, octavia, larry, kurt, rain])

# db.session.commit()

Department.query.delete()
Division.query.delete()
GeneralFund.query.delete()

# Add sample employees and departments
mayor = Department(dept_code='mayor', dept_name=f"Mayor's Office", description='555-1000')
city_council = Department(dept_code='council', dept_name='City Council', description='555-2222')
city_clerk = Department(dept_code='clerk', dept_name='City Clerk', description='555-9999')
law = Department(dept_code='law', dept_name='Law', description='555-1000')
hr = Department(dept_code='hr', dept_name='Human Resources', description='555-2222')
hrr = Department(dept_code='hrr', dept_name='Human Rights & Relations', description='555-9999')
finance = Department(dept_code='fin', dept_name='Finance', description='555-1000')
planning = Department(dept_code='planning', dept_name='Planning', description='555-2222')
police = Department(dept_code='police', dept_name='Police', description='555-9999')
fire = Department(dept_code='fire', dept_name='Fire', description='555-9999')
parks = Department(dept_code='parks', dept_name='Parks', description='555-9999')
conv_tour = Department(dept_code='conv_tour', dept_name='Convention and Tourism', description='555-9999')
pw = Department(dept_code='pw', dept_name='Public Works', description='555-9999')
lib = Department(dept_code='lib', dept_name='Library', description='555-9999')
o_benefits = Department(dept_code='o_benefits', dept_name='Other Budgetary Accounts - Benefits', description='555-9999')
o_misc = Department(dept_code='o_misc', dept_name='Other Budgetary Accounts - Misc', description='555-9999')
o_debt = Department(dept_code='o_debt', dept_name='Other Budgetary Accounts - Debt Service', description='555-9999')


mayor_gf_2019 = GeneralFund(id=1, dept_code='mayor', allocation=1369316, year=2019, department=mayor)
council_gf_2019 = GeneralFund(id=2, dept_code='council', allocation=1276072, year=2019, department=city_council)
clerk_gf_2019 = GeneralFund(id=3, dept_code='clerk', allocation=829955, year=2019, department=city_clerk)
law_gf_2019 = GeneralFund(id=4, dept_code='law', allocation=5053899, year=2019, department=law)
hr_gf_2019 = GeneralFund(id=5, dept_code='hr', allocation=2902950, year=2019, department=hr)
hrr_gf_2019 = GeneralFund(id=6, dept_code='hrr', allocation=1231708, year=2019, department=hrr)
finance_gf_2019 = GeneralFund(id=7, dept_code='fin', allocation=4950497, year=2019, department=finance)
planning_gf_2019 = GeneralFund(id=8, dept_code='planning', allocation=10534353, year=2019, department=planning)
police_gf_2019 = GeneralFund(id=9, dept_code='police', allocation=154432279, year=2019, department=police)
fire_gf_2019 = GeneralFund(id=10, dept_code='fire', allocation=107405531, year=2019, department=fire)
parks_gf_2019 = GeneralFund(id=11, dept_code='parks', allocation=23105204, year=2019, department=parks)
conv_tour_gf_2019 = GeneralFund(id=12, dept_code='conv_tour', allocation=1515000, year=2019, department=conv_tour)
pw_gf_2019 = GeneralFund(id=13, dept_code='pw', allocation=22942203, year=2019, department=pw)
library_gf_2019 = GeneralFund(id=14, dept_code='lib', allocation=13663971, year=2019, department=lib)
o_benefits_gf_2019 = GeneralFund(id=15, dept_code='o_benefits', allocation=22051754, year=2019, department=o_benefits)
o_misc_gf_2019 = GeneralFund(id=16, dept_code='o_misc', allocation=24465016, year=2019, department=o_misc)
o_debt_gf_2019 = GeneralFund(id=17, dept_code='o_debt', allocation=3533536, year=2019, department=o_debt)

mayor_gf_2020 = GeneralFund(id=18, dept_code='mayor', allocation=1411590, year=2020, department=mayor)
council_gf_2020 = GeneralFund(id=19, dept_code='council', allocation=1300434, year=2020, department=city_council)
clerk_gf_2020 = GeneralFund(id=20, dept_code='clerk', allocation=824646, year=2020, department=city_clerk)
law_gf_2020 = GeneralFund(id=21, dept_code='law', allocation=5183399, year=2020, department=law)
hr_gf_2020 = GeneralFund(id=22, dept_code='hr', allocation=2954730, year=2020, department=hr)
hrr_gf_2020 = GeneralFund(id=23, dept_code='hrr', allocation=1258020, year=2020, department=hrr)
finance_gf_2020 = GeneralFund(id=24, dept_code='fin', allocation=5050182, year=2020, department=finance)
planning_gf_2020 = GeneralFund(id=25, dept_code='planning', allocation=10329825, year=2020, department=planning)
police_gf_2020 = GeneralFund(id=26, dept_code='police', allocation=159362743, year=2020, department=police)
fire_gf_2020 = GeneralFund(id=27, dept_code='fire', allocation=110173973, year=2020, department=fire)
parks_gf_2020 = GeneralFund(id=28, dept_code='parks', allocation=22724140, year=2020, department=parks)
conv_tour_gf_2020 = GeneralFund(id=29, dept_code='conv_tour', allocation=1600000, year=2020, department=conv_tour)
pw_gf_2020 = GeneralFund(id=30, dept_code='pw', allocation=21441609, year=2020, department=pw)
library_gf_2020 = GeneralFund(id=31, dept_code='lib', allocation=14512454, year=2020, department=lib)
o_benefits_gf_2020 = GeneralFund(id=32, dept_code='o_benefits', allocation=20317000, year=2020, department=o_benefits)
o_misc_gf_2020 = GeneralFund(id=33, dept_code='o_misc', allocation=32364342, year=2020, department=o_misc)
o_debt_gf_2020 = GeneralFund(id=34, dept_code='o_debt', allocation=9148494, year=2020, department=o_debt)

# leonard = Employee(name='Leonard', dept=dl)
# liz = Employee(name='Liz', dept=dl)
# maggie = Employee(name='Maggie', state='DC', dept=dm)
# nadine = Employee(name='Nadine')

# db.session.add_all([df, dl, dm, leonard, liz, maggie, nadine])
# db.session.commit()

# pc = Project(proj_code='car', proj_name='Design Car',
#              assignments=[EmployeeProject(emp_id=liz.id, role='Chair'),
#                           EmployeeProject(emp_id=maggie.id)])
# ps = Project(proj_code='server', proj_name='Deploy Server',
#              assignments=[EmployeeProject(emp_id=liz.id),
#                           EmployeeProject(emp_id=leonard.id, role='Auditor')])

db.session.add_all([
    mayor, 
    city_council,
    city_clerk,
    law,
    hr,
    hrr,
    finance,
    planning,
    police,
    fire,
    parks,
    conv_tour,
    pw,
    lib,
    o_benefits,
    o_misc,
    o_debt,
    mayor_gf_2019, 
    council_gf_2019,
    clerk_gf_2019,
    law_gf_2019,
    hr_gf_2019,
    hrr_gf_2019,
    finance_gf_2019,
    planning_gf_2019,
    police_gf_2019,
    fire_gf_2019,
    parks_gf_2019,
    conv_tour_gf_2019,
    pw_gf_2019,
    library_gf_2019,
    o_benefits_gf_2019,
    o_misc_gf_2019,
    o_debt_gf_2019,
    mayor_gf_2020,
    council_gf_2020,
    clerk_gf_2020,
    law_gf_2020,
    hr_gf_2020,
    hrr_gf_2020,
    finance_gf_2020,
    planning_gf_2020,
    police_gf_2020,
    fire_gf_2020,
    parks_gf_2020,
    conv_tour_gf_2020,
    pw_gf_2020,
    library_gf_2020,
    o_benefits_gf_2020,
    o_misc_gf_2020,
    o_debt_gf_2020
])
db.session.commit()
