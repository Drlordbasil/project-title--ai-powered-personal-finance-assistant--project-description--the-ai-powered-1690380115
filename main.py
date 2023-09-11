Optimized Python script:

    # AI-enhanced Personal Finance Assistant


class Expense:
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category


class Budget:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount


class Goal:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class PersonalFinanceAssistant:
    def __init__(self):
        self.expenses = []
        self.budgets = {}
        self.goals = []

    def add_expense(self, amount, category):
        expense = Expense(amount, category)
        self.expenses.append(expense)

    def add_budget(self, category, amount):
        budget = Budget(category, amount)
        self.budgets[category] = budget

    def add_goal(self, name, amount):
        goal = Goal(name, amount)
        self.goals.append(goal)

    def track_expenses(self):
        total_expenses = sum(expense.amount for expense in self.expenses)
        print("Total expenses:", total_expenses)

        categorized_expenses = {}
        for expense in self.expenses:
            categorized_expenses.setdefault(expense.category, 0)
            categorized_expenses[expense.category] += expense.amount

        print("Categorized expenses:")
        for category, amount in categorized_expenses.items():
            print(category, ":", amount)

    def monitor_budgets(self):
        for category, budget in self.budgets.items():
            expenses_in_category = sum(
                expense.amount for expense in self.expenses if expense.category == category)
            if expenses_in_category > budget.amount:
                print("Budget exceeded for", category)
            elif expenses_in_category >= budget.amount * 0.8:
                print("Approaching budget limit for", category)

    def track_goals(self):
        total_expenses = sum(expense.amount for expense in self.expenses)
        for goal in self.goals:
            progress = total_expenses / goal.amount * 100
            print(goal.name, "progress:", progress, "%")


if __name__ == "__main__":
    pfa = PersonalFinanceAssistant()

    pfa.add_expense(50, "Food")
    pfa.add_expense(30, "Transportation")
    pfa.add_expense(100, "Entertainment")

    pfa.track_expenses()

    pfa.add_budget("Food", 200)
    pfa.add_budget("Transportation", 100)

    pfa.monitor_budgets()

    pfa.add_goal("Vacation", 2000)

    pfa.track_goals()
