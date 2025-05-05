import sys
import os
'my_package'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"my_package")))

import my_package.list1 as l
import my_package.set2 as s
import my_package.dict3 as d

l.append1(1)
s.adds2(10)
d.add3("name,lio")