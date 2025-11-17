def vec_add(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must be the same length")
    return [a[i] + b[i] for i in range(len(a))]
print("change in friends code")
# Example
v1 = [1, 2, 3]
v2 = [4, 5, 6]
result = vec_add(v1, v2)
print(result)  # [5, 7, 9]
