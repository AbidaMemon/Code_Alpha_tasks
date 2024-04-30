def fibonacci(n):
  series=[0,1]
  for i in range(2,n):
    num=series[-1]+series[-2]
    series.append(num)
  return series
n=10
series=fibonacci(n)
print(series)
