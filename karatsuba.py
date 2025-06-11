import re

# Fungsi untuk menghapus nol di depan
def removeLeadingZeros(s):
    return re.sub("^0+(?!$)", "", s)

# Penjumlahan dua bilangan string berbasis base (kembalikan hasil sebagai string dalam format sesuai basis)
def findSum(str1, str2, base=10):
    try:
        sum_result = int(str1, base) + int(str2, base)
        # Jika basis adalah 2, hasil dikembalikan dalam format biner
        if base == 2:
            return bin(sum_result)[2:]  # Menghilangkan prefix '0b' untuk biner
        else:
            return str(sum_result)  # Untuk basis 10, hasilnya tetap dalam desimal
    except ValueError:
        return None

# Pengurangan dua bilangan string berbasis base (kembalikan hasil sebagai string dalam format sesuai basis)
def findDiff(str1, str2, base=10):
    try:
        diff_result = int(str1, base) - int(str2, base)
        # Jika basis adalah 2, hasil dikembalikan dalam format biner
        if base == 2:
            return bin(diff_result)[2:]  # Menghilangkan prefix '0b' untuk biner
        else:
            return str(diff_result)  # Untuk basis 10, hasilnya tetap dalam desimal
    except ValueError:
        return None


# Fungsi utama Karatsuba dengan logging langkah
def karatsuba(A, B, base=10, steps=None, level=0):
    if steps is None:
        steps = []

    # Menghapus nol di depan
    A = removeLeadingZeros(A)
    B = removeLeadingZeros(B)

    indent = '  ' * level
    steps.append(f"{indent}📌 Hitung Karatsuba (A = {A} dan B = {B})")

    # Base case: ketika panjang A dan B <= 2, lakukan perkalian langsung
    if len(A) <= 2 and len(B) <= 2:
        try:
            product = int(A, base) * int(B, base)
            result = format(product, 'b') if base == 2 else str(product)
            steps.append(f"{indent}🔷 Base case: {A} × {B} = {result}")
            return result
        except ValueError:
            steps.append(f"{indent}❌ Error konversi: Salah satu input tidak valid untuk basis {base}")
            return None

    # Tentukan panjang maksimal dan bagi A, B menjadi dua bagian
    n = max(len(A), len(B))
    n2 = n // 2
    A = A.zfill(n)
    B = B.zfill(n)

    Al, Ar = A[:n2], A[n2:]
    Bl, Br = B[:n2], B[n2:]

    steps.append(f"{indent}▶️ Panjang maksimum = {n}, dibagi menjadi dua bagian:")
    steps.append(f"{indent}  - A → {A} menjadi Al = {Al}, Ar = {Ar}")
    steps.append(f"{indent}  - B → {B} menjadi Bl = {Bl}, Br = {Br}")

    # Rekursif hitung z2, z1, dan z0
    z2 = karatsuba(Al, Bl, base, steps, level + 1)
    z0 = karatsuba(Ar, Br, base, steps, level + 1)
    sumA = findSum(Al, Ar, base)
    sumB = findSum(Bl, Br, base)
    z1 = karatsuba(sumA, sumB, base, steps, level + 1)

    # Jika salah satu rekursi gagal, hentikan proses
    if None in [z2, z0, z1]:
        steps.append(f"{indent}❌ Error: Salah satu rekursi menghasilkan None")
        return None

    z1 = findDiff(z1, findSum(z2, z0, base), base)

    steps.append(f"{indent}📍 Komponen utama Karatsuba:")
    steps.append(f"{indent}  - z2 = {Al} × {Bl} = {z2}")
    steps.append(f"{indent}    ↪ Rumus: z2 = Al × Bl")
    steps.append(f"{indent}  - z0 = {Ar} × {Br} = {z0}")
    steps.append(f"{indent}    ↪ Rumus: z0 = Ar × Br")
    steps.append(f"{indent}  - z1 = ({Al}+{Ar}) × ({Bl}+{Br}) - z2 - z0 = {z1}")
    steps.append(f"{indent}    ↪ Rumus: z1 = (Al + Ar)(Bl + Br) − z2 − z0")

    # Konversi ke integer untuk operasi shift
    try:
        z2_val = int(z2, base) if isinstance(z2, str) else z2
        z0_val = int(z0, base) if isinstance(z0, str) else z0
        z1_val = int(z1, base) if isinstance(z1, str) else z1
    except ValueError:
        steps.append(f"{indent}❌ Error konversi: Salah satu komponen tidak valid untuk basis {base}")
        return None

    # Penyesuaian posisi digit dan hasil akhir
    z2_shifted = z2_val * (base ** (2 * (n - n2)))
    z1_shifted = z1_val * (base ** (n - n2))
    total = z2_shifted + z1_shifted + z0_val

    # Format hasil akhir ke dalam bentuk yang sesuai
    result = format(total, 'b') if base == 2 else str(total)

    steps.append(f"{indent}🔄 Penyesuaian digit untuk posisi:")
    steps.append(f"{indent}  - z2 × 10^{2*(n-n2)} → {z2_shifted}")
    steps.append(f"{indent}  - z1 × 10^{n-n2} → {z1_shifted}")
    steps.append(f"{indent}#️⃣ Rumus akhir: xy = z2 × 10^(2m) + z1 × 10^m + z0")
    steps.append(f"{indent}   ✅ Hasil akhir = {z2_shifted} + {z1_shifted} + {z0_val} = {result}")

    return result

# Contoh penggunaan
A = "1101"
B = "1011"
steps = []
result = karatsuba(A, B, base=2, steps=steps)

# Menampilkan langkah-langkah
for step in steps:
    print(step)

# Menampilkan hasil akhir dengan pengecekan apakah result None
if result is not None:
    try:
        # Jika result adalah string, pastikan itu dalam format biner yang valid
        result_int = int(result, 2) if isinstance(result, str) else result
        print(f"\n💡 Dalam desimal: {int(A, 2)} × {int(B, 2)} = {result_int}")
    except ValueError:
        print("❌ Error: Hasil konversi biner tidak valid.")
else:
    print("❌ Perkalian tidak berhasil dihitung.")
