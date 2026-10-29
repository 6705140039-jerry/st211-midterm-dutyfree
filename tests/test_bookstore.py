"""Your test suite. Write smoke, regression, and slow tests here.

Every test MUST carry exactly one marker (@pytest.mark.smoke / regression /
slow) and name its author in the docstring, e.g.:

    @pytest.mark.smoke
    def test_login_works():
        '''Author: <name>. Smoke test for login.'''

Run:  pytest            (all)     pytest -m smoke     pytest -m regression
"""
import pytest
from bookstore_app import Users, Catalog, Cart


@pytest.mark.smoke
def test_example_register():
    """Author: <example>. Smoke: a new user can register."""
    assert Users().register("newuser", "password123") is True


# ---- YOUR SMOKE TESTS (at least 5) ---- 

import pytest
from bookstore_app import Users, Catalog, Cart


@pytest.mark.smoke
def test_register_new_user():
    """Author: Zarr Ni Htut. Smoke test for registration."""
    users = Users()
    assert users.register("alice", "password123") is True
    assert "alice" in users.users


@pytest.mark.smoke
def test_login_with_correct_password():
    """Author: Zarr Ni Htut. Smoke test for login."""
    users = Users()
    users.register("bob", "password123")
    assert users.login("bob", "password123") is True


@pytest.mark.smoke
def test_add_product_to_catalog():
    """Author: Zarr Ni Htut. Smoke test for adding a product."""
    catalog = Catalog()
    catalog.add_product(1, "Python Basics", 250)
    assert 1 in catalog.products
    assert catalog.products[1]["title"] == "Python Basics"


@pytest.mark.smoke
def test_search_for_product():
    """Author: Zarr Ni Htut. Smoke test for product search."""
    catalog = Catalog()
    catalog.add_product(1, "Python Basics", 250)
    assert catalog.search("Python Basics") == [1]


@pytest.mark.smoke
def test_add_product_to_cart():
    """Author: Zarr Ni Htut. Smoke test for adding a product to cart."""
    catalog = Catalog()
    catalog.add_product(1, "Python Basics", 250)
    cart = Cart(catalog)
    assert cart.add(1) is True
    assert cart.items == [1]


@pytest.mark.smoke
def test_checkout_nonempty_cart():
    """Author: Zarr Ni Htut. Smoke test for checkout."""
    catalog = Catalog()
    catalog.add_product(1, "Python Basics", 250)
    cart = Cart(catalog)
    cart.add(1)

    assert cart.checkout() == [1]
    assert cart.items == []
    assert cart.history() == [[1]]


# ---- YOUR REGRESSION TESTS (the bug hunt) ---- 

@pytest.mark.regression
def test_login_preserves_symbols_in_password():
    """Author: Aung Myo Naing.
    Regression: login should compare the original password,
    not remove punctuation before checking it.
    """
    users = Users()
    users.register("alice_symbols", "p@ss-word!42")

    assert users.login("alice_symbols", "p@ss-word!42") is True


@pytest.mark.regression
def test_login_rejects_password_with_different_symbols():
    """Author: Aung Myo Naing.
    Regression: a password with different symbols must not be accepted.
    """
    users = Users()
    users.register("bob_symbols", "p@ssword")

    assert users.login("bob_symbols", "password") is False

@pytest.mark.regression
def test_catalog_search_ignores_letter_case():
    """Author: Min Khant Kyaw.
    Candidate regression: search should find a title regardless of case.
    Confirm this is an intended requirement before keeping the test.
    """
    catalog = Catalog()
    catalog.add_product(1, "Python Testing", 30)

    assert catalog.search("python") == [1]

@pytest.mark.regression
def test_catalog_search_with_empty_keyword():
    """Author: Min Khant Kyaw.
    Candidate regression: an empty search should return no results.
    Confirm this is an intended requirement before keeping the test.
    """
    catalog = Catalog()
    catalog.add_product(1, "Python Testing", 30)
    catalog.add_product(2, "Linux Basics", 25)

    assert catalog.search("") == []

@pytest.mark.regression
def test_cart_total_includes_last_item():
    """Author: Zay Htet.
    Regression: total must include every item in the cart.
    """
    catalog = Catalog()
    catalog.add_product(1, "Book A", 10)
    catalog.add_product(2, "Book B", 20)

    cart = Cart(catalog)
    cart.add(1)
    cart.add(2)

    assert cart.total() == 30


@pytest.mark.regression
def test_empty_checkout_returns_none_without_saving_order():
    """Author: Zay Htet.
    Regression: checking out an empty cart should not create an order.
    """
    cart = Cart(Catalog())

    result = cart.checkout()

    assert result is None
    assert cart.history() == []

# ---- YOUR SLOW TESTS (at least 2) ---- 
@pytest.mark.slow
def test_register_and_login_many_users():
    """Author: So Pyay Htoo
    Slow test: register and log in many different users.
    """
    users = Users()
    number_of_users = 10000

    for i in range(number_of_users):
        username = f"user_{i}"
        password = f"password_{i}"
        assert users.register(username, password) is True

    for i in range(number_of_users):
        username = f"user_{i}"
        password = f"password_{i}"
        assert users.login(username, password) is True

    assert len(users.users) == number_of_users