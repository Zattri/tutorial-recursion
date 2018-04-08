import binary

def countdown(x):
    print(x)
    if x > 0:
        countdown(x-1)


def factorial(x):
    if x > 1:
        return x * factorial(x-1)
    else:
        return 1

def tailFactorial(x, acc=1):
    if x == 0:
        return acc
    else:
        return tailFactorial(x-1, acc * x)


# Binary Tree
rootNode = binary.Node(0)
node1 = binary.Node(1)
node2 = binary.Node(2)
node3 = binary.Node(3)
node4 = binary.Node(4)
node5 = binary.Node(5)

rootNode.addLeft(node1)
rootNode.addRight(node2)
node1.addLeft(node3)
node2.addLeft(node4)
node2.addRight(node5)


# Binary Tree Recursive Print
def treeTraverse(root):
    print(root.v)
    if (root.l or root.r):
        if root.l:
            print("Left")
            treeTraverse(root.l)
        if root.r:
            print("Right")
            treeTraverse(root.r)
    else:
        print("Up")


def treeSearch(root, val):
    if (root.v == val):
        print("Found")
    else:
        if (root.l or root.r):
            if root.l:
                treeSearch(root.l, val)
            if root.r:
                treeSearch(root.r, val)


def msort3(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x) / 2)
    y = msort3(x[:mid])
    z = msort3(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result

# Merge sort example - This code was taken from someone else because it's late and I'm lazy
#numList = [34, 30, 75, 27, 8, 58, 10, 1, 59, 25]
#print(msort3(numList))

# Countdown Example - Counts down from the input number to 0
# countdown(10)


# Factorial Example - Calculates the factorial for the input number
# - large numbers exceed the recursive stack size and crash
# - fun fact, 980 is the maximum recursive depth, which will do for most things
#print(factorial(3))


# Tail recursion example - Python doesn't support tail recursion, so this still only goes up to 980
#print(tailFactorial(4))


# Tree Traversal Example - Goes from the root node and reaches every node on the tree at least once
#treeTraverse(rootNode)
# Question - Why does it stop at Up


# Tree search example - Checks whether a node of a given value is in a binary tree
#treeSearch(rootNode, 2)
#treeSearch(rootNode, 16)


