from periodictable import elements
import pickle

class Elements:

    def __init__(self, pickle_path='./periodic_table_elements.pkl'):
        self.pickle_path = pickle_path
        self.periodic_table_elements = {}

    def symbol_and_names(self):
        for el in elements._element:
            items = vars(elements._element[el])
            self.periodic_table_elements[items['symbol']] = items['name']
        return self.periodic_table_elements

    def save_table_as_pickle(self):
        try:
            pickle.dump(self.periodic_table_elements, open(self.pickle_path, 'wb'))
        except Exception as e:
            print(f"Got an exception while saving elements to pickle: {e}")
            raise e

    def symbol_and_names_from_pickle(self):
        try:
            self.periodic_table_elements = pickle.load(open(self.pickle_path, 'rb'))
            return self.periodic_table_elements
        except Exception as e:
            print(f"Failed to read symbols from pickle file. Its usually due to path. Check if file exists {e}")
            raise e



