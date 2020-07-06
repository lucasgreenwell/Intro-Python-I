num = input("Enter a number: ")
num = int(round(num, 0))

def is_prime(num):
    #must return true or false
    # vast majority of cases are false
    # 3 or less returns true
    # any even number other than 2 returns false
    # divide by 2 subtract one and work way down from here
    if num < 1 or num % 1 != 0:
        print("error: input must be a postive integer")
        return "error: input must be a postive integer"
    elif num < 4:
        print("it's prime!")
        return True
    elif num % 2 == 0:
        print("it's not prime this time")
        return False
    else:
        half_of_num = int(num / 2)
        print(half_of_num)
        for possible_factor in range(half_of_num):
            if possible_factor > 1:
                if num % possible_factor == 0:
                    print("it's not prime this time")
                    return False
    print("it's prime!")
    return True

is_prime(num)