#Recursion Basic Example (count == 4)
count = 1

def func():
    global count
    if count == 4:
        return
    print("c Maurya")
    count += 1
    func()

func()

#Head Recursion
def func():
    global count
    if count == 4:
        return
    print("Maurya")
    count += 1
    func()

count = 1
func()

#Tail Recursion
def func():
    global count
    if count == 4:
        return
    func()
    count += 1
    print("Maurya")

count = 1
func()

#Recursion Tree
# Head Recursion
def func(N):
    if N == 0:
        return
    print(N)
    func(N - 1)

func(3)
# Output: 3 2 1

# Tail Recursion
def func(i, N):
    if i > N:
        return
    func(i + 1, N)
    print(i)

func(1, 3)
# Output: 3 2 1


