import re

# Fungsi untuk menghapus nol di depan

def removeLeadingZeros(s):
    return re.sub("^0+(?!$)", "", s)

# Penjumlahan dua bilangan string berbasis base

def findSum(str1, str2, base=10):
    if len(str1) > len(str2):
        str1, str2 = str2, str1
    str1, str2 = str1.zfill(len(str2)), str2.zfill(len(str1))
    carry = 0
    result = ""

    for i in range(len(str2) - 1, -1, -1):
        total = int(str1[i], base) + int(str2[i], base) + carry
        result = format(total % base, 'b' if base == 2 else '') + result
        carry = total // base

    if carry:
        result = format(carry, 'b' if base == 2 else '') + result

    return result

# Pengurangan dua bilangan string (diasumsikan str1 >= str2)

def findDiff(str1, str2, base=10):
    str1, str2 = str1.zfill(len(str2)), str2.zfill(len(str1))
    carry = 0
    result = ""

    for i in range(len(str1) - 1, -1, -1):
        diff = int(str1[i], base) - int(str2[i], base) - carry
        if diff < 0:
            diff += base
            carry = 1
        else:
            carry = 0
        result = format(diff, 'b' if base == 2 else '') + result

    return result.lstrip('0') or "0"

# Fungsi utama Karatsuba dengan logging langkah

def karatsuba(A, B, base=10, steps=None, level=0):
    if steps is None:
        steps = []

    A = removeLeadingZeros(A)
    B = removeLeadingZeros(B)

    indent = '  ' * level
    steps.append(f"{indent}📌 Hitung Karatsuba (A = {A} dan B = {B})")

    if len(A) <= 2 and len(B) <= 2:
        result = format(int(A, base) * int(B, base), 'b' if base == 2 else '')
        steps.append(f"{indent}🔹 Base case: {A} × {B} = {result}")
        return result

    n = max(len(A), len(B))
    n2 = n // 2
    A = A.zfill(n)
    B = B.zfill(n)

    Al, Ar = A[:n2], A[n2:]
    Bl, Br = B[:n2], B[n2:]

    steps.append(f"{indent}➤ Panjang maksimum = {n}, dibagi menjadi dua bagian:")
    steps.append(f"{indent}    - A → {A} menjadi Al = {Al}, Ar = {Ar}")
    steps.append(f"{indent}    - B → {B} menjadi Bl = {Bl}, Br = {Br}")

    p = karatsuba(Al, Bl, base, steps, level + 1)
    q = karatsuba(Ar, Br, base, steps, level + 1)
    sumA = findSum(Al, Ar, base)
    sumB = findSum(Bl, Br, base)
    r = karatsuba(sumA, sumB, base, steps, level + 1)
    r = findDiff(r, findSum(p, q, base), base)

    steps.append(f"{indent}➤ Komponen utama Karatsuba:")
    steps.append(f"{indent}    - p = {Al} × {Bl} = {p}")
    steps.append(f"{indent}    - q = {Ar} × {Br} = {q}")
    steps.append(f"{indent}    - r = ({Al}+{Ar}) × ({Bl}+{Br}) - p - q = {r}")

    p_shifted = p + '0' * (2 * (n - n2))
    r_shifted = r + '0' * (n - n2)

    steps.append(f"{indent}➤ Penyesuaian digit untuk posisi:")
    steps.append(f"{indent}    - p × 10^{2*(n-n2)} → {p_shifted}")
    steps.append(f"{indent}    - r × 10^{n-n2} → {r_shifted}")

    result = removeLeadingZeros(findSum(findSum(p_shifted, r_shifted, base), q, base))
    steps.append(f"{indent}✅ Hasil akhir = {p_shifted} + {r_shifted} + {q} = {result}")

    return result
