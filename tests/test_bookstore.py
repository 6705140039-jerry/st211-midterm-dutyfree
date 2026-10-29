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
    """Author: Aung Myo Naing - Replace with name.
    Regression: login should compare the original password,
    not remove punctuation before checking it.
    """
    users = Users()
    users.register("alice_symbols", "p@ss-word!42")

    assert users.login("alice_symbols", "p@ss-word!42") is True


@pytest.mark.regression
def test_login_rejects_password_with_different_symbols():
    """Author: Aung Myo Naing - Replace with name.
    Regression: a password with different symbols must not be accepted.
    """
    users = Users()
    users.register("bob_symbols", "p@ssword")

    assert users.login("bob_symbols", "password") is False





# ---- YOUR SLOW TESTS (at least 2) ---- 
