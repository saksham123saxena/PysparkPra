def isPrime(num):
    ans = False
    for ele in range(2, num):
        if num % ele == 0:
            ans = True
            break
    if ans is False:
        return f"given num : {num} is prime number"
    else:
        return f"given num : {num} is not a prime number"


if __name__ == '__main__':
    num = int(input("please enter your number !\n"))
    print(isPrime(num))
