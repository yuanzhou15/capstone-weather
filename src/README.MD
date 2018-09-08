# Assumptions about data location:
An environment varaible 'weather' is assumed to point to a directory containing two Folders:  

satellite/  

radar/  

which contain the relevant data.

# How to use/import this module:
To import wdata and its utitlites, copy the following code depending on where your source-code file is:

cap-weath <br>
  ├── .gitignore <br>
  ├── README.md <br>
  ├── example1.py <br>
  ├── notebook1.ipynb <br>
  ├── src <br>
  │ &nbsp;&nbsp;&nbsp;&nbsp;├── \_\_init__.py <br>
  │ &nbsp;&nbsp;&nbsp;&nbsp;└── wdata.py <br>
  ├── siblingdir <br>
  │ &nbsp;&nbsp;&nbsp;&nbsp; ├── \_\_init__.py <br>
  │ &nbsp;&nbsp;&nbsp;&nbsp; ├── notebook2.ipynb <br>
  │ &nbsp;&nbsp;&nbsp;&nbsp; └── example2.py <br>


#### example1.py and notebook1.py:
```python
from src import wdata
```

#### notebook2.ipynb:
```python
import os, sys
nb_dir = os.path.split(os.getcwd())[0]
if nb_dir not in sys.path: sys.path.append(nb_dir)
from src import wdata
```

#### example2.py:
```python
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import wdata
```
