from . import Expense
import matplotlib.pyplot as plt
import timeit

def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    divided_for_loop = expenses.categorize_for_loop()
    divided_set_comp = expenses.categorize_set_comprehension()

    if not divided_set_comp == divided_for_loop:
        print ("Sets are NOT equal by == test")
    
    for a, b in zip(divided_for_loop, divided_set_comp):
        if not (a.issubset(b) and b.issubset(a)):
            print("Sets are NOT equal by subset test")
    
    print(timeit.timeit(stmt='expenses.categorize_for_loop()', 
    setup = 
    '''
from . import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
    ''',
    number =100000,
    globals=globals()
    ))

    print(timeit.timeit(stmt='expenses.categorize_set_comprehension()', 
    setup = 
    '''
from . import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
    ''',
    number =100000,
    globals=globals()
    ))

    fig,ax=plt.subplots()
    labels = ['Expenses', 'Overages', 'Budget']
    values = [myBudgetList.sum_expenses, myBudgetList.sum_overages, myBudgetList.budget]
    ax.bar(labels, values, color=['green', 'red', 'blue'])
    ax.set_title('Your total expenses vs. total budget')
    plt.show()

if __name__ == "__main__":
    main()