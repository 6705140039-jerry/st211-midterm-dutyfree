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
| `test_cart_total_sums_items` | Checks if calculating the cart total correctly sums the prices of all items in the cart. | Yes | `python -m pytest ai_review/test_ai_generated.py::test_cart_total_sums_items -v` <br> `PASSED` | genuine / passes anyway |
| `test_login_rejects_wrong_password` | Verifies that authentication fails and returns an error when providing an incorrect password. | Yes | `python -m pytest ai_review/test_ai_generated.py::test_login_rejects_wrong_password -v` <br> `PASSED` | genuine / passes anyway |
| `test_search_finds_exact_title` | Verifies that search functionality correctly retrieves books matching an exact title string. | Yes | `python -m pytest ai_review/test_ai_generated.py::test_search_finds_exact_title -v` <br> `PASSED` | genuine / passes anyway |
| `test_import_returns_count` | Verifies that bulk-import returns the integer count of successfully processed items. | Yes | `python -m pytest ai_review/test_ai_generated.py::test_import_returns_count -v` <br> `PASSED` | genuine / passes anyway |
| `test_register_duplicate_returns_false` | Verifies that registering a duplicate username returns false instead of raising an unhandled exception. | Yes | `python -m pytest ai_review/test_ai_generated.py::test_register_duplicate_returns_false -v` <br> `PASSED` | genuine / passes anyway |
| `test_checkout_empty_returns_none` | Verifies that checking out an empty cart returns None without saving an order. | Yes | `python -m pytest ai_review/test_ai_generated.py::test_checkout_empty_returns_none -v` <br> `PASSED` | genuine / passes anyway |
| `test_add_to_cart_returns_true_for_known_product` | Verifies that adding a valid item ID to the cart returns true or a success payload. | Yes | `python -m pytest ai_review/test_ai_generated.py::test_add_to_cart_returns_true_for_known_product -v` <br> `PASSED` | genuine / passes anyway |
| `test_search_is_limited_to_ten_results` | Claims the catalogue search returns at most ten results. | No | `python -m pytest ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results -v` <br> `FAILED - AssertionError: assert 20 <= 10` | invented bug / invalid test assertion |

## D3.3 Verdict (a few short paragraphs)

The most common failure mode observed in the supplied test set was invalid assertion bounds and unrealistic expectations regarding search pagination limits, such as `test_search_is_limited_to_ten_results` asserting a hard cap of 10 items when the catalog search method returns all matches without built-in truncation[cite: 2]. 

A test that passes against buggy code is far more dangerous than one that crashes. When a test fails or crashes, it immediately signals developers to investigate a potential code defect or logic flaw. Conversely, a test that falsely passes or asserts incorrect assumptions creates a false sense of security, allowing underlying issues or bad business logic to pass unnoticed into production.

In the future, before trusting an AI-generated test suite, we will systematically audit every assertion against the functional specification and actual code implementation. Specifically, we will verify boundary conditions, cross-check expected return types, and ensure that test constraints accurately match the implemented behavior of the application modules.
