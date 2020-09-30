import pandas as pd

'''
Tugas Statistika Komputasi

- Mean
- Weighted mean
- Median
- Weighted Median
- Trimmed mean
- Robuts, dan
- Outlier
'''


def mean(data):
    sumVal = 0
    length = len(data)
    for num in data:
        sumVal += num

    return sumVal / length


def weightedMean(data, weights):
    sumVal, totalWeight = 0, 0
    length = len(data)
    # Sum item * weightnya
    for i in range(length):
        sumVal += data[i] * weights[i]
    # Sum weightnya
    for weight in weights:
        totalWeight += weight

    return sumVal / totalWeight


dataObatLaris = pd.read_excel("./obat_terlaris.xls")
dataWeight = dataObatLaris['Weight']
dataJumlahTransaksi = dataObatLaris['Jumlah Transaksi']
# Konversi angka dari string ke float
dataJumlahTransaksi = list(
    map(lambda jml: float(jml.replace(',', '.')), dataJumlahTransaksi))

rata2 = mean(dataJumlahTransaksi)
rata2weight = weightedMean([1,2,3,4,5], [20,20,20,20,20])

print(f"Nilai mean adalah: {rata2weight}")
