import sys
sys.path.append("F:/Python/PythonLearning/DAY 9/PACK A")
sys.path.append("F:/Python/PythonLearning/DAY 9/PACK B")

# Approach 1
# import emp
# empobj=emp.Employee(101,"Scoot",50000)
# empobj.displayemp()

# import stu
# stuobj=stu.Student(101,"Naveen",5)
# stuobj.displaystu()

# Approach 2
from emp import Employee
empobj=Employee(1010,"John",30000)
empobj.displayemp()

from stu import Student
stuobj=Student(1010,"John",3)
stuobj.displaystu()