def get_complete_rows(coins: int) -> int:
    rows = 0
    count = 0
    for val in range(1, coins + 1):
        count += val
        rows += 1
        if count > coins:
            return rows - 1


try:
    number_of_coins = int(input("Enter the number of coins : "))
    print("The number of complete rows are : ", get_complete_rows(number_of_coins))
except ValueError:
    print("Invalid Input, Please enter only integers")
