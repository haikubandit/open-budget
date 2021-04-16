"""Seed file to make sample data for db."""

from models import Department, Division, GeneralFund, RevenueSource, db
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
RevenueSource.query.delete()

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


mayor_gf_2019 = GeneralFund(id=1, dept_code='mayor', budget=1369316, year=2019, department=mayor)
council_gf_2019 = GeneralFund(id=2, dept_code='council', budget=1276072, year=2019, department=city_council)
clerk_gf_2019 = GeneralFund(id=3, dept_code='clerk', budget=829955, year=2019, department=city_clerk)
law_gf_2019 = GeneralFund(id=4, dept_code='law', budget=5053899, year=2019, department=law)
hr_gf_2019 = GeneralFund(id=5, dept_code='hr', budget=2902950, year=2019, department=hr)
hrr_gf_2019 = GeneralFund(id=6, dept_code='hrr', budget=1231708, year=2019, department=hrr)
finance_gf_2019 = GeneralFund(id=7, dept_code='fin', budget=4950497, year=2019, department=finance)
planning_gf_2019 = GeneralFund(id=8, dept_code='planning', budget=10534353, year=2019, department=planning)
police_gf_2019 = GeneralFund(id=9, dept_code='police', budget=154432279, year=2019, department=police)
fire_gf_2019 = GeneralFund(id=10, dept_code='fire', budget=107405531, year=2019, department=fire)
parks_gf_2019 = GeneralFund(id=11, dept_code='parks', budget=23105204, year=2019, department=parks)
conv_tour_gf_2019 = GeneralFund(id=12, dept_code='conv_tour', budget=1515000, year=2019, department=conv_tour)
pw_gf_2019 = GeneralFund(id=13, dept_code='pw', budget=22942203, year=2019, department=pw)
library_gf_2019 = GeneralFund(id=14, dept_code='lib', budget=13663971, year=2019, department=lib)
o_benefits_gf_2019 = GeneralFund(id=15, dept_code='o_benefits', budget=22051754, year=2019, department=o_benefits)
o_misc_gf_2019 = GeneralFund(id=16, dept_code='o_misc', budget=24465016, year=2019, department=o_misc)
o_debt_gf_2019 = GeneralFund(id=17, dept_code='o_debt', budget=3533536, year=2019, department=o_debt)

mayor_gf_2020 = GeneralFund(id=18, dept_code='mayor', budget=1411590, year=2020, department=mayor)
council_gf_2020 = GeneralFund(id=19, dept_code='council', budget=1300434, year=2020, department=city_council)
clerk_gf_2020 = GeneralFund(id=20, dept_code='clerk', budget=824646, year=2020, department=city_clerk)
law_gf_2020 = GeneralFund(id=21, dept_code='law', budget=5183399, year=2020, department=law)
hr_gf_2020 = GeneralFund(id=22, dept_code='hr', budget=2954730, year=2020, department=hr)
hrr_gf_2020 = GeneralFund(id=23, dept_code='hrr', budget=1258020, year=2020, department=hrr)
finance_gf_2020 = GeneralFund(id=24, dept_code='fin', budget=5050182, year=2020, department=finance)
planning_gf_2020 = GeneralFund(id=25, dept_code='planning', budget=10329825, year=2020, department=planning)
police_gf_2020 = GeneralFund(id=26, dept_code='police', budget=159362743, year=2020, department=police)
fire_gf_2020 = GeneralFund(id=27, dept_code='fire', budget=110173973, year=2020, department=fire)
parks_gf_2020 = GeneralFund(id=28, dept_code='parks', budget=22724140, year=2020, department=parks)
conv_tour_gf_2020 = GeneralFund(id=29, dept_code='conv_tour', budget=1600000, year=2020, department=conv_tour)
pw_gf_2020 = GeneralFund(id=30, dept_code='pw', budget=21441609, year=2020, department=pw)
library_gf_2020 = GeneralFund(id=31, dept_code='lib', budget=14512454, year=2020, department=lib)
o_benefits_gf_2020 = GeneralFund(id=32, dept_code='o_benefits', budget=20317000, year=2020, department=o_benefits)
o_misc_gf_2020 = GeneralFund(id=33, dept_code='o_misc', budget=32364342, year=2020, department=o_misc)
o_debt_gf_2020 = GeneralFund(id=34, dept_code='o_debt', budget=9148494, year=2020, department=o_debt)


gf_carryover_rs_2019 = RevenueSource(id=1, revenue_code='gf_carryover', revenue_name='General Fund Carryover', budget=11347628, year=2019)
citysales_use_tax_rs_2019 = RevenueSource(id=2, revenue_code='citysales_use_tax', revenue_name='City Sales and Use Tax', budget=168615330, year=2019)
property_tax_rs_2019 = RevenueSource(id=3, revenue_code='property_tax', revenue_name='Property Tax', budget=170091626, year=2019)
restaurant_tax_rs_2019 = RevenueSource(id=4, revenue_code='restaurant_tax', revenue_name='Restaurant Tax', budget=34007711, year=2019)
other_taxes_rs_2019 = RevenueSource(id=5, revenue_code='other_taxes', revenue_name='Other Taxes', budget=73054448, year=2019)
licenses_permits_rs_2019 = RevenueSource(id=6, revenue_code='licenses_permits', revenue_name='Licenses and Permits', budget=13343776, year=2019)
intergovernmental_rs_2019 = RevenueSource(id=7, revenue_code='intergovernmental', revenue_name='Intergovernmental', budget=57248649, year=2019)
investment_income_rs_2019 = RevenueSource(id=8, revenue_code='investment_income', revenue_name='Investment Income', budget=1839543, year=2019)
sewer_use_fee_rs_2019 = RevenueSource(id=9, revenue_code='sewer_use_fee', revenue_name='Sewer Use Fee', budget=170599595, year=2019)
wheel_tax_rs_2019 = RevenueSource(id=10, revenue_code='wheel_tax', revenue_name='Motor Vehicle Wheel Fee', budget=23698450, year=2019)
service_charges_rs_2019 = RevenueSource(id=11, revenue_code='service_charges', revenue_name='Charges for services', budget=61075788, year=2019)
rents_royalties_other_rs_2019 = RevenueSource(id=12, revenue_code='rents_royalties_other', revenue_name='Rents, Royalties, & Other', budget=1445513, year=2019)
contributions_grants_rs_2019 = RevenueSource(id=13, revenue_code='contributions_grants', revenue_name='Contributions and Grants', budget=85319990, year=2019)
salesbond_proceeds_rs_2019 = RevenueSource(id=14, revenue_code='salesbond_proceeds', revenue_name='Proceeds From Sale of Bonds', budget=169988000, year=2019)
transfers_rs_2019 = RevenueSource(id=15, revenue_code='transfers', revenue_name='Transfers', budget=0, year=2019)

gf_carryover_rs_2020 = RevenueSource(id=16, revenue_code='gf_carryover', revenue_name='General Fund Carryover', budget=5750227, year=2020)
citysales_use_tax_rs_2020 = RevenueSource(id=17, revenue_code='citysales_use_tax', revenue_name='City Sales and Use Tax', budget=172110849, year=2020)
property_tax_rs_2020 = RevenueSource(id=18, revenue_code='property_tax', revenue_name='Property Tax', budget=182111391, year=2020)
restaurant_tax_rs_2020 = RevenueSource(id=19, revenue_code='restaurant_tax', revenue_name='Restaurant Tax', budget=34597640, year=2020)
other_taxes_rs_2020 = RevenueSource(id=20, revenue_code='other_taxes', revenue_name='Other Taxes', budget=72633908, year=2020)
licenses_permits_rs_2020 = RevenueSource(id=21, revenue_code='licenses_permits', revenue_name='Licenses and Permits', budget=12917170, year=2020)
intergovernmental_rs_2020 = RevenueSource(id=22, revenue_code='intergovernmental', revenue_name='Intergovernmental', budget=58775055, year=2020)
investment_income_rs_2020 = RevenueSource(id=23, revenue_code='investment_income', revenue_name='Investment Income', budget=1958310, year=2020)
sewer_use_fee_rs_2020 = RevenueSource(id=24, revenue_code='sewer_use_fee', revenue_name='Sewer Use Fee', budget=179556073, year=2020)
wheel_tax_rs_2020 = RevenueSource(id=25, revenue_code='wheel_tax', revenue_name='Motor Vehicle Wheel Fee', budget=23439226, year=2020)
service_charges_rs_2020 = RevenueSource(id=26, revenue_code='service_charges', revenue_name='Charges for services', budget=53243119, year=2020)
rents_royalties_other_rs_2020 = RevenueSource(id=27, revenue_code='rents_royalties_other', revenue_name='Rents, Royalties, & Other', budget=5755030, year=2020)
contributions_grants_rs_2020 = RevenueSource(id=28, revenue_code='contributions_grants', revenue_name='Contributions and Grants', budget=87183697, year=2020)
salesbond_proceeds_rs_2020 = RevenueSource(id=29, revenue_code='salesbond_proceeds', revenue_name='Proceeds From Sale of Bonds', budget=238043000, year=2020)
transfers_rs_2020 = RevenueSource(id=30, revenue_code='transfers', revenue_name='Transfers', budget=1555000, year=2020)

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
    o_debt_gf_2020,
    gf_carryover_rs_2019,
    citysales_use_tax_rs_2019,
    property_tax_rs_2019,
    restaurant_tax_rs_2019,
    other_taxes_rs_2019,
    licenses_permits_rs_2019,
    intergovernmental_rs_2019,
    investment_income_rs_2019,
    sewer_use_fee_rs_2019,
    wheel_tax_rs_2019,
    service_charges_rs_2019,
    rents_royalties_other_rs_2019,
    contributions_grants_rs_2019,
    salesbond_proceeds_rs_2019,
    transfers_rs_2019,
    gf_carryover_rs_2020,
    citysales_use_tax_rs_2020,
    property_tax_rs_2020,
    restaurant_tax_rs_2020,
    other_taxes_rs_2020,
    licenses_permits_rs_2020,
    intergovernmental_rs_2020,
    investment_income_rs_2020,
    sewer_use_fee_rs_2020,
    wheel_tax_rs_2020,
    service_charges_rs_2020,
    rents_royalties_other_rs_2020,
    contributions_grants_rs_2020,
    salesbond_proceeds_rs_2020,
    transfers_rs_2020
])
db.session.commit()
