import time

t = time.time()

x = [{"apple", "banana", "cherry"}, {"apple", "banana", "cherry"}, {"apple", "banana", "cherry"}]
y = [{"google", "microsoft", "apple"}, {"google", "microsoft", "apple"}, {"google", "microsoft", "apple"}, {"google", "microsoft", "apple"}]

z = x[0].intersection(y[0])

print(time.time() - t)