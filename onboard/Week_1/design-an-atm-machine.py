from typing import List

class ATM:
    def __init__(self):
        self.notes = {20: 0, 50: 0, 100: 0, 200: 0, 500: 0}
        self.pair = {0: 20, 1: 50, 2: 100, 3: 200, 4: 500}
        self.count = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.notes[self.pair[i]] += banknotesCount[i]
            self.count[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        res = [0] * 5
        remaining = amount

        for i in range(4, -1, -1):
            num_notes = min(remaining // self.pair[i], self.notes[self.pair[i]])
            res[i] = num_notes
            remaining -= num_notes * self.pair[i]

        if remaining != 0:
            return [-1]  
        for i in range(len(self.count)):
            self.count[i] -= res[i]
            self.notes[self.pair[i]] -= res[i]

        return res

