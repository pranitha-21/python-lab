def generate_magic_square(n):
    if n < 3:
        raise ValueError("Magic square not possible for n < 3")
    if n % 2 == 1:
        return generate_odd_magic_square(n)
    elif n % 4 == 0:
        return generate_doubly_even_magic_square(n)
    else:
        return generate_singly_even_magic_square(n)

def generate_odd_magic_square(n):
    magic_square = [[0]*n for _ in range(n)]
    i, j = 0, n//2

    for num in range(1, n*n + 1):
        magic_square[i][j] = num
        i_new, j_new = (i-1)%n, (j+1)%n
        if magic_square[i_new][j_new]:
            i += 1
        else:
            i, j = i_new, j_new
    return magic_square

def generate_doubly_even_magic_square(n):
    magic_square = [[(n*y)+x+1 for x in range(n)] for y in range(n)]

    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or ((i+j) % 4 == 3):
                magic_square[i][j] = n*n - (n*i + j)
    return magic_square

def generate_singly_even_magic_square(n):
    half_n = n // 2
    sub_square_size = half_n
    sub_square = generate_odd_magic_square(half_n)
    magic_square = [[0]*n for _ in range(n)]

    # Offsets for 4 sub-squares
    offsets = [0, 2, 3, 1]
    for r in range(n):
        for c in range(n):
            quadrant = (r//half_n)*2 + (c//half_n)
            value = sub_square[r % half_n][c % half_n]
            magic_square[r][c] = value + offsets[quadrant]*sub_square_size**2

    # Swap columns
    k = (n - 2) // 4
    for i in range(n):
        for j in range(n):
            if i < half_n:
                if j < k or j >= n-k:
                    if j % n != n//2:
                        # Swap values between quadrant A and D
                        magic_square[i][j], magic_square[i+half_n][j] = magic_square[i+half_n][j], magic_square[i][j]
            elif j == n//2:
                # Always swap middle column
                magic_square[i][j], magic_square[i - half_n][j] = magic_square[i - half_n][j], magic_square[i][j]
    return magic_square

def print_magic_square(square):
    n = len(square)
    print(f"Magic Square (N={n})")
    for row in square:
        print(" ".join(f"{num:4}" for num in row))
    print(f"Magic constant: {n * (n**2 + 1) // 2}")
    print("-" * (n * 5))

# Example: Generate magic squares for N=4 to N=8
for N in range(4, 9):
    square = generate_magic_square(N)
    print_magic_square(square)
