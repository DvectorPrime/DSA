class TopTransactions:
    def __init__(self, size=5):
        self._transactions = [None] * size
        self._max_size = size
        self._n = 0  # Keeps the actual size of the list

    
    class Transaction:
        def __init__(self, amount, description):
            self._amount = amount
            self._description = description
    
        def __str__(self):
            return f"(${self._amount}: {self._description})"

    def __getitem__(self, k):
        return self._transactions[k] if  k < self._max_size else None
    
    def add(self, amount, description):

        is_good = self._n < self._max_size or amount > self._transactions[-1]._amount

        if is_good:
            if self._n < self._max_size:
                self._n += 1
            
            index = self._n - 1

            while (index > 0 and  amount > self._transactions[index - 1]._amount):
                self._transactions[index] = self._transactions[index - 1]
                index -= 1

            self._transactions[index] = self.Transaction(amount, description)
    
    def __str__(self):
        return "\n".join(str(self[k]) for k in range(self._n))
    

tracker = TopTransactions()
tracker.add(100, "Groceries")
tracker.add(500, "Rent")
tracker.add(20, "Coffee")
tracker.add(1000, "Freelance Gig")
tracker.add(50, "Gas")
tracker.add(600, "Sold Bike")

print(tracker)