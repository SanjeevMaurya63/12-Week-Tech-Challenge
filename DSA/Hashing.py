#Hashing in Python (List based)
n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

hash_list = [0] * 11
for num in n:
    hash_list[num] += 1

for num in m:
    if num < 0 or num > 10:
        print(0)
    else:
        print(hash_list[num])

#Hashing using Dictionary & Character Hashing
n_list= [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

hash_map = {}
n = len(n)

for i in range(0, n):
    hash_map[n_list[i]] = hash_map.get(n_list[i], 0) + 1

print("Frequency Dictionary:")
for key, value in hash_map.items():
    print(f"{key} : {value}")


# Character Hashing:
s = "azyxyyzaaaa"
q = ["d", "a", "y", "h"]

hash_list = [0] * 26

for ch in s:
    ascii_val = ord(ch)
    index = ascii_val - 97
    hash_list[index] += 1

for ch in q:
    ascii_val = ord(ch)
    index = ascii_val - 97
    print(hash_list[index])
