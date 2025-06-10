import re

# Fungsi untuk menghapus nol di depan

def removeLeadingZeros(s):
    return re.sub("^0+(?!$)", "", s)

# Penjumlahan dua bilangan string berbasis base (kembalikan hasil sebagai string desimal)

def findSum(str1, str2, base=10):
    return str(int(str1, base) + int(str2, base))

# Pengurangan dua bilangan string (kembalikan hasil sebagai string desimal)

def findDiff(str1, str2, base=10):
    return str(int(str1, base) - int(str2, base))

# Fungsi utama Karatsuba dengan logging langkah

def karatsuba(A, B, base=10, steps=None, level=0):
    if steps is None:
        steps = []

    A = removeLeadingZeros(A)
    B = removeLeadingZeros(B)

    indent = '  ' * level
    steps.append(f"{indent}📌 Hitung Karatsuba (A = {A} dan B = {B})")

    if len(A) <= 2 and len(B) <= 2:
        product = int(A, base) * int(B, base)
        result = format(product, 'b') if base == 2 else str(product)
        steps.append(f"{indent}🔷 Base case: {A} × {B} = {result}")
        return result

    n = max(len(A), len(B))
    n2 = n // 2
    A = A.zfill(n)
    B = B.zfill(n)

    Al, Ar = A[:n2], A[n2:]
    Bl, Br = B[:n2], B[n2:]

    steps.append(f"{indent}▶️ Panjang maksimum = {n}, dibagi menjadi dua bagian:")
    steps.append(f"{indent}  - A → {A} menjadi Al = {Al}, Ar = {Ar}")
    steps.append(f"{indent}  - B → {B} menjadi Bl = {Bl}, Br = {Br}")

    z2 = karatsuba(Al, Bl, base, steps, level + 1)
    z0 = karatsuba(Ar, Br, base, steps, level + 1)
    sumA = findSum(Al, Ar, base)
    sumB = findSum(Bl, Br, base)
    z1 = karatsuba(sumA, sumB, base, steps, level + 1)
    z1 = findDiff(z1, findSum(z2, z0, base), base)

    steps.append(f"{indent}📍 Komponen utama Karatsuba:")
    steps.append(f"{indent}  - z2 = {Al} × {Bl} = {z2}")
    steps.append(f"{indent}    ↪ Rumus: z2 = Al × Bl")
    steps.append(f"{indent}  - z0 = {Ar} × {Br} = {z0}")
    steps.append(f"{indent}    ↪ Rumus: z0 = Ar × Br")
    steps.append(f"{indent}  - z1 = ({Al}+{Ar}) × ({Bl}+{Br}) - z2 - z0 = {z1}")
    steps.append(f"{indent}    ↪ Rumus: z1 = (Al + Ar)(Bl + Br) − z2 − z0")

    # Konversi ke integer untuk operasi shift
    z2_val = int(z2, base)
    z0_val = int(z0, base)
    z1_val = int(z1, base)

    z2_shifted = z2_val * (base ** (2 * (n - n2)))
    z1_shifted = z1_val * (base ** (n - n2))
    total = z2_shifted + z1_shifted + z0_val

    result = format(total, 'b') if base == 2 else str(total)

    steps.append(f"{indent}🔄 Penyesuaian digit untuk posisi:")
    steps.append(f"{indent}  - z2 × 10^{2*(n-n2)} → {z2_shifted}")
    steps.append(f"{indent}  - z1 × 10^{n-n2} → {z1_shifted}")
    steps.append(f"{indent}#️⃣ Rumus akhir: xy = z2 × 10^(2m) + z1 × 10^m + z0")
    steps.append(f"{indent}   ✅ Hasil akhir = {z2_shifted} + {z1_shifted} + {z0_val} = {result}")

    return result

