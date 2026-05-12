'''
Count how many elements are common between two arrays.
'''
def common(s1,s2):
    count =0
    visited = []
    for i in s1:
        if i in s2 and i not in visited:
            count += 1
            visited.append(i)
    return count

n1 = input("Enter the first string: ")
n2 = input("Enter the second string: ")
print(f"Number of common elements: {common(n1, n2)}")
