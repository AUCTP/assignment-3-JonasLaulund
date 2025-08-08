import numpy as np

# TASK 1
def demand(days=30, d_demand=20):
    return [np.random.poisson(d_demand) for _ in range(days)]

def print_stat(demand_list):
    avg = np.mean(demand_list)
    std = np.std(demand_list)
    five_percentile = np.percentile(demand_list, 5)
    ninefive_percentile = np.percentile(demand_list, 95)
    print(f"""
Average: {avg}
Standard deviation: {std}
5% percentile (worst case): {five_percentile}
95% percentile (best case): {ninefive_percentile}
    """)

def run_task_1():
    days = int(input("Insert the number of days you will simulate over:\n"))
    dlist = demand(days=days)
    print_stat(dlist)
    return dlist

# TASK 2
def optimal_inventory_level(daily_demand=20, service_level=95):
    for i in range(10000):
        inventory = 1 + i
        enough = 0
        not_enough = 0
        for _ in range(1000):
            avg_monthly_demand = sum(demand(days=30, d_demand=daily_demand))
            if inventory >= avg_monthly_demand:
                enough += 1
            else:
                not_enough += 1
        if enough >= (service_level * 10):
            break
    return inventory

def run_task_2():
    inventory = optimal_inventory_level()
    print(f"The optimal inventory level securing a 95% service level is {inventory}.")

# TASK 3
def run_task_3():
    daily_demand = int(input('What is the average daily demand?\n'))
    service_level = int(input('What service level do you want to obtain? (0-100)\n'))
    inventory = optimal_inventory_level(daily_demand=daily_demand, service_level=service_level)
    print(f"The optimal inventory level securing a {service_level}% service level is {inventory}.")

# RUN CODES
while True:
    answer = int(input('What task-code do you want to try? (1-3)\n'))
    if answer == 1:
        run_task_1()
    elif answer == 2:
        run_task_2()
    elif answer == 3:
        run_task_3()
    else:
        print('Insert correct number!')
    if input('Do you want to try again? (yes/no)\n') == 'no':
        break
