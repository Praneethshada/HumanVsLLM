from hypothesis import given, strategies as st
from profit_amount import profit_amount

@given(st.integers(min_value=0, max_value=5000), st.integers(min_value=0, max_value=5000))
def test_profit_logic(ac, sa):
    res = profit_amount(ac, sa)
    if ac < sa:
        assert res == sa - ac
    else:
        assert res is None

@given(st.floats(min_value=0, max_value=5000), st.floats(min_value=0, max_value=5000))
def test_profit_logic_floats(ac, sa):
    res = profit_amount(ac, sa)
    # if actual_cost > sale_amount -> function returns amount (bugged), else None
    if ac < sa:
        assert res == sa - ac
    else:
        assert res is None

@given(st.integers(min_value=-1000, max_value=0), st.integers(min_value=-1000, max_value=0))
def test_negative_costs(ac, sa):
    res = profit_amount(ac, sa)
    # if actual_cost > sale_amount -> function returns amount (bugged), else None
    if ac < sa:
        assert res == sa - ac
    else:
        assert res is None

@given(st.floats(min_value=-1000, max_value=0), st.floats(min_value=-1000, max_value=0))
def test_negative_costs_floats(ac, sa):
    res = profit_amount(ac, sa)
    # if actual_cost > sale_amount -> function returns amount (bugged), else None
    if ac < sa:
        assert res == sa - ac
    else:
        assert res is None

@given(st.integers(min_value=-1000, max_value=5000), st.integers(min_value=-1000, max_value=5000))
def test_mixed_costs(ac, sa):
    res = profit_amount(ac, sa)
    # if actual_cost > sale_amount -> function returns amount (bugged), else None
    if ac < sa:
        assert res == sa - ac
    else:
        assert res is None

@given(st.floats(min_value=-1000, max_value=5000), st.floats(min_value=-1000, max_value=5000))
def test_mixed_costs_floats(ac, sa):
    res = profit_amount(ac, sa)
    # if actual_cost > sale_amount -> function returns amount (bugged), else None
    if ac < sa:
        assert res == sa - ac
    else:
        assert res is None

@given(st.integers(min_value=0, max_value=10**6), st.integers(min_value=0, max_value=10**6))
def test_large_numbers(ac, sa):
    res = profit_amount(ac, sa)
    # if actual_cost > sale_amount -> function returns amount (bugged), else None
    if ac < sa:
        assert res == sa - ac
    else:
        assert res is None

@given(st.floats(min_value=0, max_value=10**6), st.floats(min_value=0, max_value=10**6))
def test_large_numbers_floats(ac, sa):
    res = profit_amount(ac, sa)
    # if actual_cost > sale_amount -> function returns amount (bugged), else None
    if ac < sa:
        assert res == sa - ac
    else:
        assert res is None

@given(st.one_of(st.integers(), st.floats()), st.one_of(st.integers(), st.floats()))
def test_mixed_types(ac, sa):
    res = profit_amount(ac, sa)
    # if actual_cost > sale_amount -> function returns amount (bugged), else None
    if ac < sa:
        assert res == sa - ac
    else:
        assert res is None

@given(st.integers(min_value=-1000, max_value=1000), st.integers(min_value=-1000, max_value=1000))
def test_edge_cases(ac, sa):
    res = profit_amount(ac, sa)
    # if actual_cost > sale_amount -> function returns amount (bugged), else None
    if ac < sa:
        assert res == sa - ac
    else:
        assert res is None

@given(st.floats(min_value=-1000, max_value=1000), st.floats(min_value=-1000, max_value=1000))
def test_edge_cases_floats(ac, sa):
    res = profit_amount(ac, sa)
    # if actual_cost > sale_amount -> function returns amount (bugged), else None
    if ac < sa:
        assert res == sa - ac
    else:
        assert res is None