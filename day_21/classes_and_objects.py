# Exercise: Level 1
# 1
class Statistics:
    def __init__(self, num_list: list[int]) -> None:
        if not num_list:
            raise ValueError("The number list cannot be empty")
        self.num_list = num_list

    def count(self) -> int:
        if not self.num_list:
            raise ValueError("Cannot calculate the count")
        return len(self.num_list)

    def sum(self):
        if not self.num_list:
            raise ValueError("Cannot calculate the sum")
        sum_of_nums = 0
        for num in self.num_list:
            sum_of_nums += num
        return sum_of_nums

    def min(self):
        if not self.num_list:
            raise ValueError("Cannot find the minimum number")
        return min(self.num_list)

    def max(self):
        if not self.num_list:
            raise ValueError("Cannot find the maximum number")
        return max(self.num_list)

    def range(self):
        if not self.num_list:
            raise ValueError("Cannot calculate the range")
        return self.max() - self.min()

    def mean(self):
        if not self.num_list:
            raise ValueError("Cannot calculate the mean")
        mean = self.sum() / self.count()
        return mean

    def median(self):
        if not self.num_list:
            raise ValueError("Cannot calculate the median")
        n = self.count()
        sorted_list = sorted(self.num_list)
        if n % 2 == 0:
            median_position = ((n / 2) + (n / 2 + 1)) // 2
        median_position = (n + 1) // 2
        return sorted_list[median_position - 1]

    def mode(self):
        if not self.num_list:
            raise ValueError("Cannot calculate the mode")
        frequency_counter = {}
        for age in self.num_list:
            frequency_counter[age] = frequency_counter.get(age, 0) + 1

        mode = sorted(frequency_counter.items(), key=lambda x: x[1], reverse=True)[0]
        return (mode[0], mode[1])

    def var(self):
        if not self.num_list:
            raise ValueError("Cannot calculate the variance")

        variance = sum((value - self.mean()) ** 2 for value in self.num_list)
        sample_variance = variance / self.count()
        return float(f"{sample_variance:.1f}")

    def std(self):
        if not self.num_list:
            raise ValueError("Cannot calculate the standard deviation")
        standard_deviation = self.var() ** 0.5
        return float(f"{standard_deviation:.1f}")

    def freq_dist(self):
        if not self.num_list:
            raise ValueError("Cannot calculate the frequency distribution")
        frequency_counter = {}
        for age in self.num_list:
            frequency_counter[age] = frequency_counter.get(age, 0) + 1

        frequency_list = sorted(
            (
                (count / self.count() * 100, age)
                for age, count in frequency_counter.items()
            ),
            reverse=True,
        )
        return frequency_list

    def describe(self):
        return (
            f"Count: {self.count()}\n"
            f"Sum:  {self.sum()}\n"
            f"Min:  {self.min()}\n"
            f"Max:  {self.max()}\n"
            f"Range:  {self.range()}\n"
            f"Mean:  {round(self.mean())}\n"
            f"Median:  {self.median()}\n"
            f"Mode:  {self.mode()}\n"
            f"Variance:  {self.var()}\n"
            f"Standard Deviation:  {self.std()}\n"
            f"Frequency Distribution: {self.freq_dist()}"
        )


ages = [
    31,
    26,
    34,
    37,
    27,
    26,
    32,
    32,
    26,
    27,
    27,
    24,
    32,
    33,
    27,
    25,
    26,
    38,
    37,
    31,
    34,
    24,
    33,
    29,
    26,
]
data = Statistics(ages)
print(data.describe())


# Exercise: Level 2
# 2
class PersonAccount:
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = set()
        self.expenses = set()

    def total_income(self) -> float:
        return sum(income[0] for income in self.incomes)

    def total_expenses(self) -> float:
        return sum(expense[0] for expense in self.expenses)

    def account_info(self) -> None:
        print(
            f"\n\nAccount Summary .....\n"
            f"Account Name: {self.firstname} {self.lastname}\n"
            f"Total Income: {self.total_income():.2f}\n"
            f"Total Expenses: {self.total_expenses():.2f}\n"
            f"Account Balance: {self.account_balance():.2f}\n"
        )

    def add_income(self, amount: float, description: str) -> None:
        if amount <= 0:
            raise ValueError("Income must be positive")
        self.incomes.add((amount, description))

    def add_expense(self, amount: float, description: str) -> None:
        if amount <= 0:
            raise ValueError("Expense must be positive")
        self.expenses.add((amount, description))

    def account_balance(self) -> float:
        return self.total_income() - self.total_expenses()


bode = PersonAccount("Anita", "Bade")

bode.add_expense(1000, "TP")
bode.add_income(40000, "Salary")
bode.account_info()
