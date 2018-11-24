periodic_table_elements.pkl is simply a dump of periodic table symbol and element names. 
This is extracted using [periodictable](https://github.com/pkienzle/periodictable)

To use this download periodic_table_elements.pkl and then:

```python
import pickle

elements = pickle.load(open('periodic_table_elements.pkl', 'rb'))
print(elements)
>>>> {'n': 'neutron', 'H': 'hydrogen', 'He': 'helium', 'Li': 'lithium', 
'Be': 'beryllium', 'B': 'boron', 'C': 'carbon', 'N': 'nitrogen', 'O': 'oxygen' ....}


```