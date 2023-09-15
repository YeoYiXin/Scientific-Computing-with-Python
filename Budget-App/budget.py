class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []

  def __str__(self):
    budget = self.category.center(30, "*") + "\n"
    for item in self.ledger:
      spend = f"{item['description'][:23]:23}{item['amount']:7.2f}"
      budget += spend + "\n"
    budget += "Total: " + str(self.get_balance())
    return budget

  def deposit(self, amount, description=""):
    spend = {}
    spend['amount'] = amount
    spend['description'] = description
    self.ledger.append(spend)

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      spend = {}
      spend['amount'] = -amount
      spend['description'] = description
      self.ledger.append(spend)
      return True
    else:
      return False

  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item['amount']
    return balance

  def transfer(self, amount, budget_category):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + budget_category.category)
      budget_category.deposit(amount, "Transfer from " + self.category)
      return True
    else:
      return False

  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    return True


def create_spend_chart(categories):
  title = "Percentage spent by category"
  money_spent = []
  for category in categories:
    temp = 0
    for item in category.ledger:
      if item['amount'] < 0:
        temp += abs(item['amount'])
    money_spent.append(temp)

  total_spent = sum(money_spent)
  percentage = []
  for i in money_spent:
    percentage.append(i / total_spent * 100)

  for i in range(100, -1, -10):
    title += "\n" + str(i).rjust(3) + "|"
    for j in percentage:
      if j > i:
        title += " o "
      else:
        title += "   "
    title += " "
  title += "\n" + "    " + "----------"

  category_length = []
  for category in categories:
    category_length.append(len(category.category))
  max_length = max(category_length)

  for i in range(max_length):
    title += "\n" + "    "
    for j in range(len(categories)):
      if i < category_length[j]:
        title += " " + categories[j].category[i] + " "
      else:
        title += "   "
    title += " "

  return title
