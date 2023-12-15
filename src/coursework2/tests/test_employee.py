# This file is deliberately badly written and does not conform to good practice for test case naming standards
import pytest

from src.coursework2.employee import Employee


def testemp1():
    e = Employee(name="A N Other", title="Manager", employee_id="12345", salary=45000)
    assert e.department == "HR"


def testemp2():
    e = Employee(name="A N Other", title="Manager", employee_id="12345", salary=45000)
    result = e.calculate_monthly_salary(hours_worked=155)
    assert result == 3875


def testemp3():
    e = Employee(name="A N Other", title="Manager", employee_id="12345", salary=45000)
    e.salary = 9000
    assert e.salary == 9000


def testemp4():
    e = Employee(name="A N Other", title="Manager", employee_id="12345", salary=45000)
    e.salary = 19575.67
    assert e.salary == 19575.67
    
def test_employee_assign_department():
    e = Employee(name="A N Other", title="Manager", employee_id="12345", salary=45000)
    e.assign_department("IT")
    assert e.department == "IT"

def test_employee_str_representation():
    e = Employee(name="A N Other", title="Manager", employee_id="12345", salary=45000)
    e.assign_department("HR")
    representation = str(e)
    assert "A N Other" in representation
    assert "12345" in representation
    assert "HR" in representation
    assert "Manager" in representation
    assert "45000" in representation

def test_employee_zero_hours_worked_monthly_salary():
    e = Employee(name="A N Other", title="Manager", employee_id="12345", salary=45000)
    monthly_salary = e.calculate_monthly_salary(0)  # Zero hours worked
    assert monthly_salary == pytest.approx(e.salary / 12, rel=1e-2)

def test_employee_overtime_calculation():
    e = Employee(name="A N Other", title="Manager", employee_id="12345", salary=45000)
    monthly_salary = e.calculate_monthly_salary(160)
    assert monthly_salary == pytest.approx(4750, rel=1e-2)

#Chatgpt was used to generate the four new tests but we chose what test to implement best for our case.
