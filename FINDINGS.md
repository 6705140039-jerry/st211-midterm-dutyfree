FINDINGS.md -- Bug-hunt log
Group: Duty Free
Members: Zarr Ni Htut (Raymand), Zay Htet (Zett), Aung Myo Naing (Jerry), So Pyay Htoo (Yummy), Min Khant Kyaw (Sonic)

Included results: Only tests that failed in the initial run are listed below. The two tests that passed initially have been removed: test_login_rejects_password_with_different_symbols and test_add_and_search_large_catalog.

Part A -- Regression test findings
Bug 1 -- Login Fails with Special Characters in Password
Test: test_login_preserves_symbols_in_password
Author: Aung Myo Naing
Suspected: Login may remove punctuation or change a password before checking it.
Tried: Registered alice_symbols with p@ss-word!42, then attempted to log in with the exact same password.
Observed: In the initial test run, login returned False.
Expected: Login should return True when the exact registered password, including special characters, is entered.
Fix / result: The password-handling behavior was corrected. The test passed after the changes.
Bug 2 -- Case-Insensitive Catalog Search (Candidate Regression)
Test: test_catalog_search_ignores_letter_case
Author: Min Khant Kyaw
Suspected: Catalog search may be case-sensitive.
Tried: Added a product titled Python Testing, then searched for python.
Observed: In the initial regression run, search returned [].
Expected: The test expects search to return [1] regardless of letter case.
Fix / result: The test passed after the changes.
Finding: Candidate regression. The original test comment says to confirm that case-insensitive search is an intended requirement before keeping this test.
Bug 3 -- Empty Keyword Search Returns No Results (Candidate Regression)
Test: test_catalog_search_with_empty_keyword
Author: Min Khant Kyaw
Suspected: Searching with an empty keyword may return every product.
Tried: Added Python Testing and Linux Basics, then searched using an empty string ("").
Observed: In the initial regression run, search returned [1, 2].
Expected: The test expects an empty list ([]).
Fix / result: The test passed after the changes.
Finding: Candidate regression. The original test comment says to confirm the intended behavior before keeping this test.
Bug 4 -- Cart Total Excludes the Last Item
Test: test_cart_total_includes_last_item
Author: Zay Htet
Suspected: The cart total calculation may omit the last item.
Tried: Added Book A priced at 10 and Book B priced at 20, added both to the cart, and checked the total.
Observed: In the initial regression run, the total was 10.
Expected: The total should be 30.
Fix / result: The total calculation was corrected to include both items. The test passed after the changes.
Bug 5 -- Empty Checkout Returns an Empty List Instead of None
Test: test_empty_checkout_returns_none_without_saving_order
Author: Zay Htet
Suspected: Checkout may return an incorrect value or save an order when the cart is empty.
Tried: Created an empty cart, called checkout(), and checked the order history.
Observed: In the initial regression run, checkout returned [] instead of None.
Expected: Checkout should return None, and the order history should remain empty.
Fix / result: The empty-cart checkout behavior was corrected. The test passed after the changes.
Bug 6 -- Login After Registering 10,000 Users
Test: test_register_and_login_many_users
Author: So Pyay Htoo
Suspected: Registration and login may fail when the system handles many accounts.
Tried: Registered 10,000 users (user_0 through user_9999) with matching passwords (password_0 through password_9999), then attempted to log in each user.
Observed: The initial test failed on the first login: user_0 returned False.
Expected: All 10,000 users should register and log in successfully, and len(users.users) should equal 10,000.
Fix / result: The registration/login behavior was corrected. The test passed after the changes.
Bug 7 -- Bulk Import of 20,000 Products Returns an Incorrect Count
Test: test_bulk_import_many_products
Author: Zay Htet
Suspected: Bulk import may return an incorrect count or add an unexpected number of products.
Tried: Imported 20,000 products and checked the returned count, catalog size, first title, and last title.
Observed: In the initial slow-test run, the import function returned 20001 instead of 20000.
Expected: The returned count and catalog size should both be 20,000, with the first title Imported Book 0 and the last title Imported Book 19999.
Fix / result: The bulk-import count behavior was corrected. The test passed after the changes.
