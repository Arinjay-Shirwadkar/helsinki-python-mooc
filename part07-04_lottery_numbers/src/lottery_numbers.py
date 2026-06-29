from random import sample

def lottery_numbers(amount: int, lower: int, upper: int):
    rang = list(range(lower,upper+1))
    return sorted(sample(rang, amount))