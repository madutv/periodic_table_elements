import pytest
from periodic_table_elements import Elements

@pytest.fixture
def default_period_table():
    return Elements()


def test_symbol_and_names(default_period_table):
    elements = default_period_table.symbol_and_names()
    default_period_table.save_table_as_pickle()
    assert(len(elements) > 115)
    assert(elements['H'] == 'hydrogen')

def test_symbol_and_names_from_pickle():
    elems2 = Elements()
    elems2.symbol_and_names_from_pickle()
    assert (len(elems2.periodic_table_elements) > 115)
    assert (elems2.periodic_table_elements['H'] == 'hydrogen')




