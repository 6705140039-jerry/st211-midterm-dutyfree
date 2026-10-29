"""Product catalog: adding products and searching."""


class Catalog:
    def __init__(self):
        self.products = {}   # product_id -> {"title":..., "price":...}

    def add_product(self, product_id, title, price):
        self.products[product_id] = {"title": title, "price": price}

    def search(self, keyword):
        """Return product IDs whose titles contain the keyword."""
        if not keyword:
            return []

        results = []
        keyword = keyword.casefold()

        for pid, info in self.products.items():
            if keyword in info["title"].casefold():
                results.append(pid)

        return results
