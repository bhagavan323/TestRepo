# Approach 1
# import sys
# sys.path.append("F:/Python/PythonLearning/DAY 9/package1")
# sys.path.append("F:/Python/PythonLearning/DAY 9/package1/package2")
#
# import module1
# import module2
# module1.display()
# module2.show()

# Approach 2 from keyword

import sys
sys.path.append("F:/Python/PythonLearning/DAY 9/package1")
sys.path.append("F:/Python/PythonLearning/DAY 9/package1/package2")
from module1 import *
from module2 import *
display()
show()