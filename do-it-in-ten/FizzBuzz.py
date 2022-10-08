# My attempt
tmp = []
FIZZ = lambda n : [[(tmp.append("FizzBuzz")) if i%15==0 else ((tmp.append("Fizz")) if i%3==0 else ((tmp.append("Buzz")) if i%5==0 else (tmp.append(str(i))))) for i in range(1, n)], tmp][1]

print(FIZZ(20))
