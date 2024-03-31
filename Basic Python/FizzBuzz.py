def fizzbuzz(n: int):
    output = []
    if n > 1:
        for i in range(1, n):
            if i % 3 == 0:
                output.append("Fizz")
            elif i % 5 == 0:
                output.append("Buzz")
            else:
                output.append(i)
    print(output)
    return output


fizzbuzz(33)
