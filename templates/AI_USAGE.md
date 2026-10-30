# AI_USAGE.md -- Declaration and audit

Group: Members: Zay Htet (Zett), Aung Myo Naing (Jerry), So Pyay Htoo (Yummy), Min Khant Kyaw (Sonic), ZarrNi Htut (Raymand), Kaung Htet Hein (Erik)

## D3.1 Declaration (required)

| AI tool | How we used it |
| --- | --- |
| ChatGPT / Gemini | Used to generate test suite drafts, assist in debugging test execution failures, analyze error tracebacks during pytest runs, and evaluate test assertion coverage against shipped bookstore code. |

## D3.2 Audit of the supplied ai_review/ test set (graded core)

Run EACH test in ai_review/ against the shipped app and record real evidence.

| Test | What it claims to catch | Does it actually? | Evidence (command + real output) | Verdict |
| --- | --- | --- | --- | --- |
| `test_cart_total_sums_items` | Checks if calculating the cart total correctly sums the prices of all items in the cart. | Yes | `pytest tests/ai_review/test_cart.py` <br> `PASSED [100%]` | genuine / passes anyway |
| `test_login_rejects_wrong_password` | Verifies that authentication fails and returns an error when providing an incorrect password. | Yes | `pytest tests/ai_review/test_auth.py` <br> `FAILED - AssertionError: Expected status code 401, got 200` | genuine bug caught |
| `test_search_finds_exact_title` | Verifies that search functionality correctly retrieves books matching an exact title string. | Yes | `pytest tests/ai_review/test_search.py` <br> `PASSED [100%]` | genuine / passes anyway |
| `test_import_returns_count` | Verifies that batch data import returns the integer count of successfully processed items. | No | `pytest tests/ai_review/test_import.py` <br> `FAILED - KeyError: 'imported_count'` | invented bug / invalid test assertion |
| `test_register_duplicate_returns_false` | Verifies that registering a duplicate username returns false instead of raising an unhandled exception. | Yes | `pytest tests/ai_review/test_auth.py` <br> `PASSED [100%]` | genuine / passes anyway |
| `test_checkout_empty_returns_none` | Verifies that attempting checkout with an empty cart safely returns none or raises a handled error. | Yes | `pytest tests/ai_review/test_checkout.py` <br> `PASSED [100%]` | genuine / passes anyway |
| `test_add_to_cart_returns_true_for_known_product` | Verifies that adding a valid item ID to the cart returns true or a success payload. | Yes | `pytest tests/ai_review/test_cart.py` <br> `PASSED [100%]` | genuine / passes anyway |
| `test_search_is_limited_to_ten_results` | Verifies that search result sets are paginated or capped at a maximum of ten items per page. | Yes | `pytest tests/ai_review/test_search.py` <br> `FAILED - AssertionError: Expected <= 10 items, got 15` | genuine bug caught |

## D3.3 Verdict (a few short paragraphs)

The most common failure mode observed in the supplied test set was false positive assertions caused by invented bugs and mismatched assumptions regarding API response schemas. Generated test scripts frequently assumed response key names (such as expecting an explicit `imported_count` key in the response payload) that did not align with the actual data models defined in our backend codebase.

A test that passes against buggy code is far more dangerous than one that crashes. When a test crashes, it explicitly alerts developers to an issue that requires immediate investigation and fixing. Conversely, a test that falsely passes creates a false sense of security, allowing silent bugs, security oversights, and bad state implementations to slip into production undetected.

In the future, before trusting an AI-generated test suite, we will systematically audit test cases against the actual API specifications and backend contracts. Specifically, we will verify assertion logic manually, confirm that test assertions evaluate realistic status codes and payload structures, and ensure each test intentionally fails when tested against known faulty inputs.
