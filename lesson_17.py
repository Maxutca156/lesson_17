import hashlib

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 100]
result = []
for number in numbers:
    if 5 < number < 50:
        result.append(number)
print(result)

result = filter(lambda number:5 < number < 50, numbers)
print(list(result))

result1 = [number for number in numbers if 5 < number < 50]
print(result1)

spisok = [50,67,34,200,543]

result2 = [number for number in spisok if 49 < number < 376]
print(result2)

result012 = {i:i**2 for i in range(1, 10)}
print(result012)

hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())
