# REPORT.md
**Group:** Duty Free

**Members:**
- Aung Myo Naing — 6705140039
- So Pyay Htoo — 6705140034
- Zarr Ni Htut — 6705140005
- Min Khant Kyaw — 6705140008
- Zay Htet — 6705140013

## Part A -- Test typess
### 1. Smoke Testing

**Definition:** Smoke testing is a basic test performed to check whether the main functions of an application work. It helps identify major problems before spending time on more detailed testing.

**When it runs:** Smoke tests are usually run first after a new build or deployment. They can also be run before other test types to check that the application is stable enough for further testing.

**Bookstore examples:**
- Register a new user and check that the account is created successfully.
- Add a product to the cart and check that the cart contains the product.

### 2. Regression Testing

**Definition:** Regression testing checks whether existing features still work correctly after code changes or bug fixes. It helps ensure that a change in one part of the application has not broken another part.

**When it runs:** Regression tests are commonly run after code changes, bug fixes, and before a release. They may also run automatically in a CI/CD pipeline.

**Bookstore examples:**
- Check that a user can log in with a password containing special characters.
- Check that the cart total includes the price of the last item added.

### 3. Slow Testing

**Definition:** Slow testing checks application behavior that takes more time or uses larger amounts of data or resources. These tests can reveal performance or scalability problems that may not appear in small, quick tests.

**When it runs:** Slow tests are usually run less frequently than smoke tests, such as in scheduled CI jobs, before major releases, or when performance and large-data behavior need to be checked.

**Bookstore examples:**
- Register and log in a large number of users, such as 10,000 users.
- Add and search a large catalog containing 20,000 products.

## Part B -- Scenario classification
For each of the six scenarios: smoke / regression / slow (may be more than one)
with a 2-3 sentence justification.

## Part F -- Team reflection
1. Why is running only regression tests before every commit inefficient?
2. Why do smoke tests usually run first in a CI/CD pipeline?
3. What risks arise if slow tests are never run?
4. Can one test belong to two categories? Give an example.
5. Bug-finders and bug-fixers are often different people in a real QA team.
   What does that separation change about how a bug report must be written?
