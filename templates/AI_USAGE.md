# AI Usage Declaration and Audit

**Group:** Duty Free\
**Members:** Zarr Ni Htut (Raymand), Zay Htet (Zett), Aung Myo Naing
(Jerry), So Pyay Htoo (Yummy), Min Khant Kyaw (Sonic)

------------------------------------------------------------------------

## Part 1 --- AI Usage Declaration (required, unmarked)

Every AI tool any member used anywhere in this project should be declared. Using AI is allowed. Not declaring it is not.

| Tool | What we used it for | Where in the project | How we checked it before relying on it |
|---|---|---|---|
| ChatGPT | Helped discuss test ideas, explain pytest failures and tracebacks, review test behaviour, troubleshoot code, and organize the test-audit documentation. | Test/debugging discussions and documentation, including `FINDINGS.md`, `REPORT.md`, and `AI_USAGE.md`. | Reviewed suggestions manually, compared them with the application behaviour, and checked relevant results by running pytest against the original and fixed versions. |
| Gemini | Helped explore test ideas, analyse test behaviour, and support test-suite and audit-documentation discussions. | Test-suite drafts and audit documentation, including `AI_USAGE.md` and related project files where Gemini suggestions were used. | Reviewed suggestions and checked relevant behaviour against the application and pytest results. |

If any AI tools were used but are not listed here, add them before submission.

------------------------------------------------------------------------

## Part 2 --- Audit of the Supplied Test Set

The repository test run confirms that all eight supplied tests are
present in `ai_review/test_ai_generated.py`. The initial full run was
against the shipped code; the final full run was after the group's
fixes.

### 2.1 Classification Rules

  -----------------------------------------------------------------------
  Shipped code            Fixed code              Verdict
  ----------------------- ----------------------- -----------------------
  FAIL                    PASS                    Genuine detection

  PASS                    PASS                    Detects nothing

  PASS                    FAIL                    Locks in the bug

  FAIL                    FAIL                    Invented requirement,
                                                  if the expected
                                                  behaviour is not a
                                                  documented requirement
  -----------------------------------------------------------------------

### 2.2 Summary Table

| # | Test | What it claims to catch | Shipped code | Fixed code | Verdict | Auditor |
|---:|---|---|---|---|---|---|
| 1 | `test_cart_total_sums_items` | Checks whether the cart total includes all item prices. | FAIL | PASS | Genuine detection | Zarr Ni Htut |
| 2 | `test_login_rejects_wrong_password` | Checks whether login rejects an incorrect password. | PASS | PASS | Detects nothing | Zarr Ni Htut |
| 3 | `test_search_finds_exact_title` | Checks whether exact-title search returns the matching product. | PASS | PASS | Detects nothing | Aung Myo Naing |
| 4 | `test_import_returns_count` | Checks whether bulk import returns the number of imported products. | FAIL | PASS | Genuine detection | Aung Myo Naing |
| 5 | `test_register_duplicate_returns_false` | Checks whether registering a duplicate username returns `False`. | PASS | PASS | Detects nothing | Min Khant Kyaw |
| 6 | `test_checkout_empty_returns_none` | Checks whether empty-cart checkout returns `None`. | FAIL | PASS | Genuine detection | Zay Htet |
| 7 | `test_add_to_cart_returns_true_for_known_product` | Checks whether adding a known product returns a successful result. | PASS | PASS | Detects nothing | So Pyay Htoo |
| 8 | `test_search_is_limited_to_ten_results` | Claims catalogue search should return no more than ten results. | FAIL | FAIL | Invented requirement (provisional; verify specification) | So Pyay Htoo |

*The auditor names follow the earlier group audit assignment draft. Each named member must confirm that they personally performed the audit; authorship of related group tests does not independently establish who audited these AI-supplied tests.*

### 2.3 Individual Test Analysis and Evidence

The actual repository test file shown in the terminal output is
`ai_review/test_ai_generated.py` (not the template's example path
`ai_review/test_ai_suggested.py`). The evidence below uses the actual
pytest output supplied by the group. Each test entry follows the five
required detail points.

#### Test: `test_cart_total_sums_items` (`ai_review/test_ai_generated.py`)

**Audited by:** Zarr Ni Htut --- confirm that you personally performed
this audit.

**1. What it claims to catch.**\
The test checks whether a cart containing two products priced at 10 and
20 returns a total of 30. It is intended to catch a cart-total
calculation that omits an item's price.

**2. Evidence --- against the shipped code**

``` text
ai_review/test_ai_generated.py::test_cart_total_sums_items FAILED
E       assert 10 == 30
```

**3. Evidence --- against your fixed code**

``` text
ai_review/test_ai_generated.py::test_cart_total_sums_items PASSED
```

**4. What that pair proves.**\
This is **Genuine detection --- FAIL then PASS**. The shipped code
returned 10 instead of 30, while the fixed code passed the same test.
The assertion `assert c.total() == 30` correctly checks the total of
both products.

**5. Verdict (tick one)**

-   [x] Genuine detection --- FAIL then PASS
-   [ ] Detects nothing --- PASS then PASS
-   [ ] Locks in the bug --- PASS then FAIL
-   [ ] Invented requirement --- FAIL then FAIL

#### Test: `test_login_rejects_wrong_password` (`ai_review/test_ai_generated.py`)

**Audited by:** Zarr Ni Htut --- confirm that you personally performed
this audit.

**1. What it claims to catch.**\
The test checks whether the login system rejects an incorrect password.
It does not specifically test the group's special-character password
defect.

**2. Evidence --- against the shipped code**

``` text
ai_review/test_ai_generated.py::test_login_rejects_wrong_password PASSED
```

**3. Evidence --- against your fixed code**

``` text
ai_review/test_ai_generated.py::test_login_rejects_wrong_password PASSED
```

**4. What that pair proves.**\
This is **Detects nothing --- PASS then PASS**. The wrong-password
rejection assertion passes in both versions, so it does not reveal a
defect fixed by the group. To test the special-character login defect,
the test would need to register a user with a password containing
symbols and assert that login with that exact password succeeds.

**5. Verdict (tick one)**

-   [ ] Genuine detection --- FAIL then PASS
-   [x] Detects nothing --- PASS then PASS
-   [ ] Locks in the bug --- PASS then FAIL
-   [ ] Invented requirement --- FAIL then FAIL

#### Test: `test_search_finds_exact_title` (`ai_review/test_ai_generated.py`)

**Audited by:** Aung Myo Naing --- confirm that you personally performed
this audit.

**1. What it claims to catch.**\
The test checks whether searching for an exact product title returns the
matching product. It does not specifically establish that search is
case-insensitive.

**2. Evidence --- against the shipped code**

``` text
ai_review/test_ai_generated.py::test_search_finds_exact_title PASSED
```

**3. Evidence --- against your fixed code**

``` text
ai_review/test_ai_generated.py::test_search_finds_exact_title PASSED
```

**4. What that pair proves.**\
This is **Detects nothing --- PASS then PASS**. The exact-title search
assertion passes in both versions. To test the group's case-insensitive
search finding, the search assertion would need to use a different
letter case from the stored product title, for example store
`Python Testing` and search for `python`.

**5. Verdict (tick one)**

-   [ ] Genuine detection --- FAIL then PASS
-   [x] Detects nothing --- PASS then PASS
-   [ ] Locks in the bug --- PASS then FAIL
-   [ ] Invented requirement --- FAIL then FAIL

#### Test: `test_import_returns_count` (`ai_review/test_ai_generated.py`)

**Audited by:** Aung Myo Naing --- confirm that you personally performed
this audit.

**1. What it claims to catch.**\
The test checks whether importing two products returns an
imported-product count of 2. It is intended to catch an incorrect count
from the bulk-import function.

**2. Evidence --- against the shipped code**

``` text
ai_review/test_ai_generated.py::test_import_returns_count FAILED
E       AssertionError: assert 3 == 2
```

**3. Evidence --- against your fixed code**

``` text
ai_review/test_ai_generated.py::test_import_returns_count PASSED
```

**4. What that pair proves.**\
This is **Genuine detection --- FAIL then PASS**. The shipped function
returned 3 when the test expected 2, and the fixed version passed. The
assertion compares the import return value with the number of products
supplied.

**5. Verdict (tick one)**

-   [x] Genuine detection --- FAIL then PASS
-   [ ] Detects nothing --- PASS then PASS
-   [ ] Locks in the bug --- PASS then FAIL
-   [ ] Invented requirement --- FAIL then FAIL

#### Test: `test_register_duplicate_returns_false` (`ai_review/test_ai_generated.py`)

**Audited by:** Min Khant Kyaw --- confirm that you personally performed
this audit.

**1. What it claims to catch.**\
The test checks whether trying to register a username that already
exists returns `False`. This is a duplicate-registration behaviour
check.

**2. Evidence --- against the shipped code**

``` text
ai_review/test_ai_generated.py::test_register_duplicate_returns_false PASSED
```

**3. Evidence --- against your fixed code**

``` text
ai_review/test_ai_generated.py::test_register_duplicate_returns_false PASSED
```

**4. What that pair proves.**\
This is **Detects nothing --- PASS then PASS**. The
duplicate-registration assertion passes in both versions, so this test
does not identify a defect changed by the group's fixes. It is not a
test for the special-character login, search, cart-total,
empty-checkout, or bulk-import defects recorded by the group.

**5. Verdict (tick one)**

-   [ ] Genuine detection --- FAIL then PASS
-   [x] Detects nothing --- PASS then PASS
-   [ ] Locks in the bug --- PASS then FAIL
-   [ ] Invented requirement --- FAIL then FAIL

#### Test: `test_checkout_empty_returns_none` (`ai_review/test_ai_generated.py`)

**Audited by:** Zay Htet --- confirm that you personally performed this
audit.

**1. What it claims to catch.**\
The test checks whether checking out with an empty cart returns `None`.
It is intended to catch empty checkout returning an unexpected value.

**2. Evidence --- against the shipped code**

``` text
ai_review/test_ai_generated.py::test_checkout_empty_returns_none FAILED
E       assert [] is None
```

**3. Evidence --- against your fixed code**

``` text
ai_review/test_ai_generated.py::test_checkout_empty_returns_none PASSED
```

**4. What that pair proves.**\
This is **Genuine detection --- FAIL then PASS**. The shipped code
returned an empty list instead of `None`, while the fixed code passed
the test.

**5. Verdict (tick one)**

-   [x] Genuine detection --- FAIL then PASS
-   [ ] Detects nothing --- PASS then PASS
-   [ ] Locks in the bug --- PASS then FAIL
-   [ ] Invented requirement --- FAIL then FAIL

#### Test: `test_add_to_cart_returns_true_for_known_product` (`ai_review/test_ai_generated.py`)

**Audited by:** So Pyay Htoo --- confirm that you personally performed
this audit.

**1. What it claims to catch.**\
The test checks whether adding a known product to the cart returns a
successful result. It checks the normal add-to-cart operation.

**2. Evidence --- against the shipped code**

``` text
ai_review/test_ai_generated.py::test_add_to_cart_returns_true_for_known_product PASSED
```

**3. Evidence --- against your fixed code**

``` text
ai_review/test_ai_generated.py::test_add_to_cart_returns_true_for_known_product PASSED
```

**4. What that pair proves.**\
This is **Detects nothing --- PASS then PASS**. The known-product
add-to-cart assertion passes in both versions, so it does not detect a
defect fixed by the group. It does not test the cart-total calculation;
to detect that bug, the assertion must check that the total includes the
prices of every item added.

**5. Verdict (tick one)**

-   [ ] Genuine detection --- FAIL then PASS
-   [x] Detects nothing --- PASS then PASS
-   [ ] Locks in the bug --- PASS then FAIL
-   [ ] Invented requirement --- FAIL then FAIL

#### Test: `test_search_is_limited_to_ten_results` (`ai_review/test_ai_generated.py`)

**Audited by:** So Pyay Htoo --- confirm that you personally performed
this audit.

**1. What it claims to catch.**\
The test claims that catalogue search must return no more than ten
results. It creates 20 matching products and asserts that the search
result count is at most 10.

**2. Evidence --- against the shipped code**\
Command used for the full shipped-code run: `python -m pytest -v`

``` text
ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results FAILED
E       AssertionError: assert 20 <= 10
E       + where 20 = len([0, 1, 2, 3, 4, 5, ...])
```

**3. Evidence --- against your fixed code**\
Command used for the final full run: `python -m pytest -v`

``` text
ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results FAILED
E       AssertionError: assert 20 <= 10
E       + where 20 = len([0, 1, 2, 3, 4, 5, ...])
```

**4. What that pair proves.**\
This is **FAIL then FAIL** in our own project's runs. The catalogue
returned 20 matching products before and after the group's fixes. The
other group's screenshot shows a different group's fixed-code run passing;
that is not evidence for our repository and must not replace our result.
Our two outputs establish that this test did not pass after our fixes.
They do not, by themselves, establish whether a ten-result cap is an
actual application requirement. Check the assignment specification or
other authoritative project requirements. If no cap is specified, the
test assumes an unsupported requirement and should be classified as an
invented requirement. Until that check is made, keep the classification
provisional and do not claim this test found a confirmed bug.

**5. Verdict (tick one)**

-   [ ] Genuine detection --- FAIL then PASS
-   [ ] Detects nothing --- PASS then PASS
-   [ ] Locks in the bug --- PASS then FAIL
-   [x] Invented requirement --- FAIL then FAIL (provisional; confirm
    against the specification)

### 2.4 Full Test-Run Evidence Summary

The following results are transcribed from the group's terminal output.
The initial full run used Python 3.12.10 and pytest 9.2.0. The later
smoke, regression, and slow runs used pytest 9.1.1. The environment
versions differ, so the commands and results are reported as they were
run.

**A. Initial full run against shipped code**  
Command: `python -m pytest -v`

```text
collected 10 items

ai_review/test_ai_generated.py::test_cart_total_sums_items FAILED
ai_review/test_ai_generated.py::test_login_rejects_wrong_password PASSED
ai_review/test_ai_generated.py::test_search_finds_exact_title PASSED
ai_review/test_ai_generated.py::test_import_returns_count FAILED
ai_review/test_ai_generated.py::test_register_duplicate_returns_false PASSED
ai_review/test_ai_generated.py::test_checkout_empty_returns_none FAILED
ai_review/test_ai_generated.py::test_add_to_cart_returns_true_for_known_product PASSED
ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results FAILED
tests/test_bookstore.py::test_example_register PASSED
worked_example/test_notes.py::test_word_count_counts_words_not_characters FAILED

5 failed, 5 passed in 0.29s
```

The five failures were:
- `test_cart_total_sums_items`: returned 10 instead of 30.
- `test_import_returns_count`: returned 3 instead of 2.
- `test_checkout_empty_returns_none`: returned `[]` instead of `None`.
- `test_search_is_limited_to_ten_results`: returned 20 results instead of no more than 10.
- `test_word_count_counts_words_not_characters`: returned 18 instead of 3.

The last failure belongs to `worked_example/test_notes.py`, not to the
eight AI-generated tests.

**B. Smoke tests**  
Command: `python -m pytest -m smoke -v`

```text
collected 16 items / 9 deselected / 7 selected
7 passed, 9 deselected in 0.06s
```

The seven selected smoke tests all passed: example registration, new
user registration, correct-password login, adding a catalog product,
searching for a product, adding a product to the cart, and non-empty
checkout.

**C. Regression tests against shipped code**  
Command: `python -m pytest -m regression -v`

```text
collected 22 items / 16 deselected / 6 selected
5 failed, 1 passed, 16 deselected in 0.20s
```

The five failures were:
- `test_login_preserves_symbols_in_password`: login returned `False`
  for the registered password `p@ss-word!42`.
- `test_catalog_search_ignores_letter_case`: searching for `python`
  returned `[]` instead of `[1]`.
- `test_catalog_search_with_empty_keyword`: searching with an empty
  keyword returned `[1, 2]` instead of `[]`.
- `test_cart_total_includes_last_item`: returned 10 instead of 30.
- `test_empty_checkout_returns_none_without_saving_order`: returned
  `[]` instead of `None`.

`test_login_rejects_password_with_different_symbols` passed.

**D. Regression tests against fixed code**  
Command: `python -m pytest -m regression -v`

```text
collected 25 items / 19 deselected / 6 selected
6 passed, 19 deselected in 0.06s
```

All six selected regression tests passed after the group's fixes.

**E. Slow tests against shipped code**  
Command: `python -m pytest -m slow -v`

```text
collected 25 items / 22 deselected / 3 selected
2 failed, 1 passed, 22 deselected in 0.19s
```

The 10,000-user registration/login test failed when login for
`user_0` returned `False`. The 20,000-product bulk-import test returned
20,001 instead of 20,000. The large-catalog search test passed.

**F. Slow tests against fixed code**  
Command: `python -m pytest -m slow -v`

```text
collected 25 items / 22 deselected / 3 selected
3 passed, 22 deselected in 0.08s
```

All three selected slow tests passed after the group's fixes.

**G. Full run after bookstore fixes, before the notes fix**  
Command: `python -m pytest -v`

```text
collected 25 items
2 failed, 23 passed in 0.23s
```

The remaining failures were `test_search_is_limited_to_ten_results` and
`test_word_count_counts_words_not_characters`. The group then changed
`worked_example/notes.py` to use `.split()` and committed that change as
`a5871d0` (`add the split method to countthe words correctly`).

The separate bookstore-only command was:

```powershell
python -m pytest tests/test_bookstore.py
```

Actual result:

```text
16 passed in 0.15s
```

**H. Final full run after the notes fix**  
Command: `python -m pytest -v`

```text
collected 25 items

ai_review/test_ai_generated.py::test_cart_total_sums_items PASSED
ai_review/test_ai_generated.py::test_login_rejects_wrong_password PASSED
ai_review/test_ai_generated.py::test_search_finds_exact_title PASSED
ai_review/test_ai_generated.py::test_import_returns_count PASSED
ai_review/test_ai_generated.py::test_register_duplicate_returns_false PASSED
ai_review/test_ai_generated.py::test_checkout_empty_returns_none PASSED
ai_review/test_ai_generated.py::test_add_to_cart_returns_true_for_known_product PASSED
ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results FAILED
tests/test_bookstore.py — all 16 tests PASSED
worked_example/test_notes.py::test_word_count_counts_words_not_characters PASSED

1 failed, 24 passed in 0.22s
```

The final run shows that all 24 other tests passed, including all
bookstore tests and the worked-example word-count test. The only
remaining failure was `test_search_is_limited_to_ten_results`, which
returned 20 results.

**I. Individual command for the remaining search-limit test**

To run the remaining test by itself, use:

```powershell
py -m pytest -q --tb=short ai_review\test_ai_generated.py::test_search_is_limited_to_ten_results
```

No isolated output or elapsed time for this command was included in the
supplied terminal logs. Run the command and record its actual result.
Do not use the full-suite runtime of 0.22s as the individual test time.

**Timing clarification:** The times above (0.29s, 0.06s, 0.20s,
0.06s, 0.19s, 0.08s, 0.23s, 0.15s, and 0.22s) are runtimes for the
complete pytest commands shown. They are not individual test durations.

**Evidence limitation:** The supplied terminal logs do not show the
original shipped-code commit hash or an isolated checkout command. Do not
add a commit ID for the shipped-code run unless the group independently
verifies it.

### 2.5 Classification Summary

| Verdict | Number of tests |
|---|---:|
| Genuine detection | 3 |
| Detects nothing | 4 |
| Locks in the bug | 0 |
| Invented requirement (provisional; verify specification) | 1 |
| **Total** | **8** |

**Overall finding:** Three tests genuinely detected defects fixed by the
group: cart total, bulk-import count, and empty checkout. Four tests
passed against both versions and detected nothing. The search-limit test
failed against both versions in our own runs. It is provisionally
classified as an invented requirement only if the project specification
does not require a ten-result limit. The other group's screenshot shows
their own result and is not substituted for our group's fixed-code
evidence.

------------------------------------------------------------------------

## Part 3 --- Coverage Against Our Own Bug Hunt

One row is included for each of the seven bugs in the group's
`FINDINGS.md`, plus a row for the search-limit behaviour asserted by the
supplied test but not recorded as a group finding. Every "Yes" in the
supplied-set column points to a test classified as a genuine detection
in Part 2.

| Bug (our description) | We found it | The supplied set catches it | Which test, and how we established that |
|---|---|---|---|
| Login fails with special characters in passwords. | Yes | No | `test_login_rejects_wrong_password` passes on both versions. It tests a wrong password, not preservation of special characters. The group's `test_login_preserves_symbols_in_password` tests the affected case. |
| Case-insensitive catalogue search fails. | Yes | No | `test_search_finds_exact_title` passes on both versions. Its exact-title assertion does not establish case-insensitive coverage. The group's `test_catalog_search_ignores_letter_case` tests this behaviour. |
| Empty-keyword search returns all products instead of an empty list. | Yes | No | None of the eight supplied tests specifically checks an empty search keyword. The group's `test_catalog_search_with_empty_keyword` tests this behaviour. |
| Cart total excludes the last item. | Yes | Yes | `test_cart_total_sums_items` fails on shipped code (10 instead of 30) and passes on fixed code. The group's `test_cart_total_includes_last_item` records the same defect. |
| Empty checkout returns `[]` instead of `None`. | Yes | Yes | `test_checkout_empty_returns_none` fails on shipped code and passes on fixed code. The group's `test_empty_checkout_returns_none_without_saving_order` checks the same empty-cart behaviour. |
| Login fails after registering 10,000 users. | Yes | No | None of the eight supplied tests checks registration and login with 10,000 users. The group's `test_register_and_login_many_users` tests this scenario. |
| Bulk import of 20,000 products returns an incorrect count. | Yes | Yes | `test_import_returns_count` fails on shipped code (3 instead of 2) and passes on fixed code. The group's `test_bulk_import_many_products` checks the same import-count behaviour at 20,000 products. |
| Search returns 20 results when the supplied test expects no more than 10. | No  | No | `test_search_is_limited_to_ten_results` fails on both shipped and fixed code. The pair does not establish a fixed defect. Verify the application specification before deciding whether a ten-result cap is required; the test's failure alone is not proof of a bug. |

**Part 3 finding:** The supplied set genuinely catches three bugs
already found by the group: cart total, empty checkout, and bulk-import
count. It does not establish coverage of the other four group findings.
It did not establish an additional confirmed bug that the group had
missed.

------------------------------------------------------------------------

## Part 4 --- Verdict (under 400 words)

**1. Which failure mode was most common?**

"Detects nothing" was the most common result, with **4 of 8 tests**.
Tests 2, 3, 5, and 7 passed against both shipped and fixed code. Three
tests were genuine detections, none locked in a bug, and one failed
against both versions.

**2. Why is a test that passes against buggy code more dangerous than
one that crashes?**

A failing test attracts attention and tells the team that something
needs investigation. A test that passes while a defect is present can
create false confidence. The team may believe the feature works
correctly and leave the defect undiscovered.

**3. Did the supplied set catch anything we had missed?**

No confirmed additional bug was found. The three genuine detections ---
cart total, import count, and empty checkout --- correspond to bugs
already recorded in our `FINDINGS.md`. The ten-result search test failed
in both versions, but that does not establish a real defect or an
application requirement.

**4. What will we check before trusting a generated test in future?**

We will inspect the test's setup and assertion, confirm that its
expected behaviour is required, and run it against both shipped and
fixed code. In this exercise, we compared the actual results: the
cart-total, import-count, and empty-checkout tests changed from FAIL to
PASS; four tests passed in both versions; and the ten-result search test
failed in both. We will also compare generated tests with our own
regression tests to ensure they check the same specific behaviour.

