# Konversi Jarak

# Import

import streamlit as st

# Menjalankan program
# streamlit run 'Konversi Satuan.py'

st.write("# Konversi Satuan")

st.write("**Made by Devan Daniel**")

st.write('## **Satuan angka**')

ukuran_list = ["Ukuran", "Waktu", "Kecepatan", "Berat", "Kepadatan", "Energi", "Suhu", "Tekanan", "Frekuensi", "Data"]
ukuran = st.selectbox("Pilih jenis konversi satuan", ukuran_list, index=0)

def fungsi(angka):
    if round(angka, 3) == round(angka, 0):
        angka = int(angka)
    else:
        angka = round(angka, 3)
    
    return angka

if ukuran == ukuran_list[0]:
    jarak_list = ["Panjang", "Luas dengan kuadrat", "Luas dengan are", "Volume dengan kubik", "Volume dengan liter"]
    jarak = st.selectbox(f"Pilih jenis {ukuran}", jarak_list, index=0)

    if jarak == jarak_list[0]:
        angka = float(st.text_input(f"Angka satuan {jarak}", value=1))
        satuan_list = ["Meter", "Desimeter", "Centimeter", "Milimeter", "Dekameter", "Hektometer", "Kilometer", "Yard", "Kaki", "Inci", "Mil", "Mikrometer", "Nanometer"]
        satuan_panjang = [1, 0.1, 0.01, 0.001, 10, 100, 1000, 0.9144, 0.3048, 0.0254, 1609, 1e-6, 1e-9]
        satuan = st.selectbox(f"Dari satuan {jarak}", satuan_list, index=0)
        satuan_2 = st.selectbox(f"Ke satuan {jarak}", satuan_list, index=2)

        for n in range(len(satuan_list)):
            if satuan == satuan_list[n]:
                satuan_index = n
                break

        for n in range(len(satuan_list)):
            if satuan_2 == satuan_list[n]:
                satuan_2_index = n
                break

        angka_2 = angka * satuan_panjang[satuan_index] / satuan_panjang[satuan_2_index]

        st.write('## **Hasil Penyelesaian**')
        st.write(f"{fungsi(angka)} {satuan} = {fungsi(angka_2)} {satuan_2}")

    if jarak == jarak_list[1]:
        angka = float(st.text_input(f"Angka satuan {jarak}", value=1))
        satuan_list = ["Meter", "Desimeter", "Centimeter", "Milimeter", "Desimeter", "Hektometer", "Kilometer", "Yard", "Kaki", "Inci", "Mil"]
        satuan_panjang = [1, 0.1, 0.01, 0.001, 10, 100, 1000, 0.9144, 0.3048, 0.0254, 1609]
        satuan = st.selectbox(f"Dari satuan {jarak}", satuan_list, index=0)
        satuan_2 = st.selectbox(f"Ke satuan {jarak}", satuan_list, index=2)

        for n in range(len(satuan_list)):
            if satuan == satuan_list[n]:
                satuan_index = n
                break

        for n in range(len(satuan_list)):
            if satuan_2 == satuan_list[n]:
                satuan_2_index = n
                break

        angka_2 = angka * (satuan_panjang[satuan_index] / satuan_panjang[satuan_2_index]) ** 2

        st.write('## **Hasil Penyelesaian**')
        st.write(f"{fungsi(angka)} {satuan}^2 = {fungsi(angka_2)} {satuan_2}^2")

    if jarak == jarak_list[2]:
        angka = float(st.text_input(f"Angka satuan {jarak}", value=1))
        satuan_list = ["Are", "Desiare", "Centiare", "Miliare", "Desiare", "Hektoare", "Kiloare"]
        satuan_panjang = [1, 0.1, 0.01, 0.001, 10, 100, 1000]
        satuan = st.selectbox(f"Dari satuan {jarak}", satuan_list, index=0)
        satuan_2 = st.selectbox(f"Ke satuan {jarak}", satuan_list, index=2)

        for n in range(len(satuan_list)):
            if satuan == satuan_list[n]:
                satuan_index = n
                break

        for n in range(len(satuan_list)):
            if satuan_2 == satuan_list[n]:
                satuan_2_index = n
                break

        angka_2 = angka * (satuan_panjang[satuan_index] / satuan_panjang[satuan_2_index]) ** 2

        st.write('## **Hasil Penyelesaian**')
        st.write(f"{fungsi(angka)} {satuan}^2 = {fungsi(angka_2)} {satuan_2}^2")

    if jarak == jarak_list[3]:
        angka = float(st.text_input(f"Angka satuan {jarak}", value=1))
        satuan_list = ["Meter", "Desimeter", "Centimeter", "Milimeter", "Desimeter", "Hektometer", "Kilometer", "Yard", "Kaki", "Inci", "Mil"]
        satuan_panjang = [1, 0.1, 0.01, 0.001, 10, 100, 1000, 0.9144, 0.3048, 0.0254, 1609]
        satuan = st.selectbox(f"Dari satuan {jarak}", satuan_list, index=0)
        satuan_2 = st.selectbox(f"Ke satuan {jarak}", satuan_list, index=2)

        for n in range(len(satuan_list)):
            if satuan == satuan_list[n]:
                satuan_index = n
                break

        for n in range(len(satuan_list)):
            if satuan_2 == satuan_list[n]:
                satuan_2_index = n
                break

        angka_2 = angka * (satuan_panjang[satuan_index] / satuan_panjang[satuan_2_index]) ** 3

        st.write('## **Hasil Penyelesaian**')
        st.write(f"{fungsi(angka)} {satuan}^3 = {fungsi(angka_2)} {satuan_2}^3")

    if jarak == jarak_list[4]:
        angka = float(st.text_input(f"Angka satuan {jarak}", value=1))
        satuan_list = ["Liter", "Desiliter", "Centiliter", "Mililiter", "Desiliter", "Hektoliter", "Kiloliter"]
        satuan_panjang = [1, 0.1, 0.01, 0.001, 10, 100, 1000]
        satuan = st.selectbox(f"Dari satuan {jarak}", satuan_list, index=0)
        satuan_2 = st.selectbox(f"Ke satuan {jarak}", satuan_list, index=2)

        for n in range(len(satuan_list)):
            if satuan == satuan_list[n]:
                satuan_index = n
                break

        for n in range(len(satuan_list)):
            if satuan_2 == satuan_list[n]:
                satuan_2_index = n
                break

        angka_2 = angka * satuan_panjang[satuan_index] / satuan_panjang[satuan_2_index]

        st.write('## **Hasil Penyelesaian**')
        st.write(f"{fungsi(angka)} {satuan} = {fungsi(angka_2)} {satuan_2}")

if ukuran == ukuran_list[1]:
    angka = float(st.text_input(f"Angka satuan {ukuran}", value=1))
    satuan_list = ["Detik", "Menit", "Jam", "Hari", "Minggu", "Bulan", "Tahun", "Caturwulan", "Lustrum", "Windu", "Dekade", "Abad"]
    satuan_panjang = [1, 60, 3600, 86400, 604800, 2592000, 31536000, 10368000, 5*31536000, 8*31536000, 10*31536000, 100*31536000]
    satuan = st.selectbox(f"Dari satuan {ukuran}", satuan_list, index=1)
    satuan_2 = st.selectbox(f"Ke satuan {ukuran}", satuan_list, index=0)

    for n in range(len(satuan_list)):
        if satuan == satuan_list[n]:
            satuan_index = n
            break

    for n in range(len(satuan_list)):
        if satuan_2 == satuan_list[n]:
            satuan_2_index = n
            break

    angka_2 = angka * satuan_panjang[satuan_index] / satuan_panjang[satuan_2_index]

    st.write('## **Hasil Penyelesaian**')
    st.write(f"{fungsi(angka)} {satuan} = {fungsi(angka_2)} {satuan_2}")

if ukuran == ukuran_list[2]:
    jarak_list = ["Simpel", "Kustom"]
    jarak = st.selectbox(f"Pilih bentuk {ukuran}", jarak_list, index=0)

    if jarak == jarak_list[0]:
        angka = float(st.text_input("Angka satuan", value=1))
        satuan_list = ["Meter per detik", "Kilometer per jam", "Kaki per detik", "Mil per jam"]
        satuan_panjang = [1, 1/3.6, 0.3048, 1.609/3.6]
        satuan = st.selectbox("Dari satuan", satuan_list, index=0)
        satuan_2 = st.selectbox("Ke satuan", satuan_list, index=1)

        for n in range(len(satuan_list)):
            if satuan == satuan_list[n]:
                satuan_index = n
                break

        for n in range(len(satuan_list)):
            if satuan_2 == satuan_list[n]:
                satuan_2_index = n
                break

        angka_2 = angka * satuan_panjang[satuan_index] / satuan_panjang[satuan_2_index]

        st.write('## **Hasil Penyelesaian**')
        st.write(f"{fungsi(angka)} {satuan} = {fungsi(angka_2)} {satuan_2}")

    if jarak == jarak_list[1]:
        angka = float(st.text_input(f"Angka satuan {jarak}", value=1))
        # satuan_list = ["Meter", "Desimeter", "Centimeter", "Milimeter", "Desimeter", "Hektometer", "Kilometer", "Yard", "Kaki", "Inci", "Mil"]
        satuan_list = ["Meter", "Desimeter", "Centimeter", "Milimeter", "Dekameter", "Hektometer", "Kilometer", "Yard", "Kaki", "Inci", "Mil"]
        satuan_2_list = ["Detik", "Menit", "Jam", "Hari", "Minggu", "Bulan", "Tahun"]
        satuan_panjang = [1, 0.1, 0.01, 0.001, 10, 100, 1000, 0.9144, 0.3048, 0.0254, 1609]
        satuan_2_panjang = [1, 60, 3600, 86400, 604800, 2592000, 31536000]
        satuan = st.selectbox(f"Dari satuan ukuran", satuan_list, index=0)
        satuan_2 = st.selectbox(f"Dari satuan per waktu", satuan_2_list, index=0)
        satuan_3 = st.selectbox(f"Ke satuan ukuran", satuan_list, index=6)
        satuan_4 = st.selectbox(f"Ke satuan per waktu", satuan_2_list, index=2)

        for n in range(len(satuan_list)):
            if satuan == satuan_list[n]:
                satuan_index = n
                break

        for n in range(len(satuan_2_list)):
            if satuan_2 == satuan_2_list[n]:
                satuan_2_index = n
                break

        for n in range(len(satuan_list)):
            if satuan_3 == satuan_list[n]:
                satuan_3_index = n
                break

        for n in range(len(satuan_2_list)):
            if satuan_4 == satuan_2_list[n]:
                satuan_4_index = n
                break

        angka_2 = angka * (satuan_panjang[satuan_index] / satuan_2_panjang[satuan_2_index]) / (satuan_panjang[satuan_3_index] / satuan_2_panjang[satuan_4_index])

        st.write('## **Hasil Penyelesaian**')
        st.write(f"{fungsi(angka)} {satuan} per {satuan_2} = {fungsi(angka_2)} {satuan_3} per {satuan_4}")

if ukuran == ukuran_list[3]:
    angka = float(st.text_input(f"Angka satuan {ukuran}", value=1))
    satuan_list = ["Kilogram", "Gram", "Desigram", "Centigram", "Miligram", "Desigram", "Hektogram", "Pon", "Ons", "Kuintal", "Ton", "Mikrogram"]
    satuan_panjang = [1000, 1, 0.1, 0.01, 0.001, 10, 100, 454, 28, 100000, 1000000, 1e-6]
    satuan = st.selectbox(f"Dari satuan {ukuran}", satuan_list, index=0)
    satuan_2 = st.selectbox(f"Ke satuan {ukuran}", satuan_list, index=7)

    for n in range(len(satuan_list)):
        if satuan == satuan_list[n]:
            satuan_index = n
            break

    for n in range(len(satuan_list)):
        if satuan_2 == satuan_list[n]:
            satuan_2_index = n
            break

    angka_2 = angka * satuan_panjang[satuan_index] / satuan_panjang[satuan_2_index]

    st.write('## **Hasil Penyelesaian**')
    st.write(f"{fungsi(angka)} {satuan} = {fungsi(angka_2)} {satuan_2}")

if ukuran == ukuran_list[4]:
    jarak_list = ["Simpel", "Kustom"]
    jarak = st.selectbox(f"Pilih bentuk {ukuran}", jarak_list, index=0)

    if jarak == jarak_list[0]:
        angka = float(st.text_input("Angka satuan", value=1))
        satuan_list = ["g/cm3", "kg/m3"]
        satuan_panjang = [1, 0.001]
        satuan = st.selectbox("Dari satuan", satuan_list, index=0)
        satuan_2 = st.selectbox("Ke satuan", satuan_list, index=1)

        for n in range(len(satuan_list)):
            if satuan == satuan_list[n]:
                satuan_index = n
                break

        for n in range(len(satuan_list)):
            if satuan_2 == satuan_list[n]:
                satuan_2_index = n
                break

        angka_2 = angka * satuan_panjang[satuan_index] / satuan_panjang[satuan_2_index]

        st.write('## **Hasil Penyelesaian**')
        st.write(f"{fungsi(angka)} {satuan} = {fungsi(angka_2)} {satuan_2}")

    if jarak == jarak_list[1]:
        angka = float(st.text_input(f"Angka satuan {jarak}", value=1))
        # satuan_list = ["Meter", "Desimeter", "Centimeter", "Milimeter", "Desimeter", "Hektometer", "Kilometer", "Yard", "Kaki", "Inci", "Mil"]
        satuan_list = ["Meter", "Desimeter", "Centimeter", "Milimeter", "Dekameter", "Hektometer", "Kilometer", "Yard", "Kaki", "Inci", "Mil"]
        satuan_2_list = ["Detik", "Menit", "Jam", "Hari", "Minggu", "Bulan", "Tahun"]
        satuan_panjang = [1, 0.1, 0.01, 0.001, 10, 100, 1000, 0.9144, 0.3048, 0.0254, 1609]
        satuan_2_panjang = [1, 60, 3600, 86400, 604800, 2592000, 31536000]
        satuan = st.selectbox(f"Dari satuan ukuran", satuan_list, index=0)
        satuan_2 = st.selectbox(f"Dari satuan per waktu", satuan_2_list, index=0)
        satuan_3 = st.selectbox(f"Ke satuan ukuran", satuan_list, index=6)
        satuan_4 = st.selectbox(f"Ke satuan per waktu", satuan_2_list, index=2)

        for n in range(len(satuan_list)):
            if satuan == satuan_list[n]:
                satuan_index = n
                break

        for n in range(len(satuan_2_list)):
            if satuan_2 == satuan_2_list[n]:
                satuan_2_index = n
                break

        for n in range(len(satuan_list)):
            if satuan_3 == satuan_list[n]:
                satuan_3_index = n
                break

        for n in range(len(satuan_2_list)):
            if satuan_4 == satuan_2_list[n]:
                satuan_4_index = n
                break

        angka_2 = angka * (satuan_panjang[satuan_index] / satuan_2_panjang[satuan_2_index]) / (satuan_panjang[satuan_3_index] / satuan_2_panjang[satuan_4_index])

        st.write('## **Hasil Penyelesaian**')
        st.write(f"{fungsi(angka)} {satuan} per {satuan_2} = {fungsi(angka_2)} {satuan_3} per {satuan_4}")

if ukuran == ukuran_list[5]:
    angka = float(st.text_input(f"Angka satuan {ukuran}", value=1))
    satuan_list = ['Joule', 'Kilojoule', 'Kalori', 'Kilokalori', 'Watt per jam', 'Kilowatt per jam']
    satuan_panjang = [1, 1000, 0.239, 239, 1/3600, 1/3600000]
    satuan = st.selectbox(f"Dari satuan {ukuran}", satuan_list, index=0)
    satuan_2 = st.selectbox(f"Ke satuan {ukuran}", satuan_list, index=2)

    for n in range(len(satuan_list)):
        if satuan == satuan_list[n]:
            satuan_index = n
            break

    for n in range(len(satuan_list)):
        if satuan_2 == satuan_list[n]:
            satuan_2_index = n
            break

    angka_2 = angka * satuan_panjang[satuan_index] / satuan_panjang[satuan_2_index]

    st.write('## **Hasil Penyelesaian**')
    st.write(f"{fungsi(angka)} {satuan} = {fungsi(angka_2)} {satuan_2}")

if ukuran == ukuran_list[6]:
    angka = float(st.text_input("Angka satuan jarak", value=1))
    satuan_list = ["Celcius", "Fahrenheit", "Kelvin", "Reamur"]
    satuan = st.selectbox(f"Dari satuan {ukuran}", satuan_list, index=0)
    satuan_2 = st.selectbox(f"Ke satuan {ukuran}", satuan_list, index=1)

    if satuan == satuan_list[0]:
        if satuan_2 == satuan_list[0]: angka_2 = angka
        if satuan_2 == satuan_list[1]: angka_2 = angka * 1.8 + 32
        if satuan_2 == satuan_list[2]: angka_2 = angka + 273
        if satuan_2 == satuan_list[3]: angka_2 = angka * 0.8
    if satuan == satuan_list[1]:
        if satuan_2 == satuan_list[0]: angka_2 = (angka - 32) * 5/9
        if satuan_2 == satuan_list[1]: angka_2 = angka
        if satuan_2 == satuan_list[2]: angka_2 = (angka - 32) * 5/9 + 273
        if satuan_2 == satuan_list[3]: angka_2 = (angka - 32) * 4/9
    if satuan == satuan_list[2]:
        if satuan_2 == satuan_list[0]: angka_2 = angka - 273
        if satuan_2 == satuan_list[1]: angka_2 = (angka - 273) * 1.8 + 32
        if satuan_2 == satuan_list[2]: angka_2 = angka
        if satuan_2 == satuan_list[3]: angka_2 = (angka - 273) * 0.8
    if satuan == satuan_list[3]:
        if satuan_2 == satuan_list[0]: angka_2 = angka * 1.25
        if satuan_2 == satuan_list[1]: angka_2 = angka * 2.25 + 32
        if satuan_2 == satuan_list[2]: angka_2 = angka * 1.25 + 273
        if satuan_2 == satuan_list[3]: angka_2 = angka

    st.write('## **Hasil Penyelesaian**')
    st.write(f"{fungsi(angka)} {satuan} = {fungsi(angka_2)} {satuan_2}")

if ukuran == ukuran_list[7]:
    angka = float(st.text_input(f"Angka satuan {ukuran}", value=1))
    satuan_list = ['Pascal', 'Kilopascal', 'Megapascal', 'Atmosfer', 'Bar']
    satuan_panjang = [1, 1000, 1000000, 101300, 100000]
    satuan = st.selectbox(f"Dari satuan {ukuran}", satuan_list, index=3)
    satuan_2 = st.selectbox(f"Ke satuan {ukuran}", satuan_list, index=1)

    for n in range(len(satuan_list)):
        if satuan == satuan_list[n]:
            satuan_index = n
            break

    for n in range(len(satuan_list)):
        if satuan_2 == satuan_list[n]:
            satuan_2_index = n
            break

    angka_2 = angka * satuan_panjang[satuan_index] / satuan_panjang[satuan_2_index]

    st.write('## **Hasil Penyelesaian**')
    st.write(f"{fungsi(angka)} {satuan} = {fungsi(angka_2)} {satuan_2}")

if ukuran == ukuran_list[8]:
    angka = float(st.text_input(f"Angka satuan {ukuran}", value=1))
    satuan_list = ['Hertz', 'Millihertz', 'Kilohertz', 'Megahertz', 'Gigahertz']
    satuan_panjang = [1, 0.001, 1000, 1000000, 10**9]
    satuan = st.selectbox(f"Dari satuan {ukuran}", satuan_list, index=3)
    satuan_2 = st.selectbox(f"Ke satuan {ukuran}", satuan_list, index=2)

    for n in range(len(satuan_list)):
        if satuan == satuan_list[n]:
            satuan_index = n
            break

    for n in range(len(satuan_list)):
        if satuan_2 == satuan_list[n]:
            satuan_2_index = n
            break

    angka_2 = angka * satuan_panjang[satuan_index] / satuan_panjang[satuan_2_index]

    st.write('## **Hasil Penyelesaian**')
    st.write(f"{fungsi(angka)} {satuan} = {fungsi(angka_2)} {satuan_2}")

if ukuran == ukuran_list[9]:
    angka = float(st.text_input("Angka satuan jarak", value=1))
    satuan_list = ['Byte', 'Bit', 'Kilobyte', 'Megabyte', 'Gigabyte', 'Terabyte']
    satuan_panjang = [1, 1/8, 1000, 10**6, 10**9, 10**12]
    satuan = st.selectbox(f"Dari satuan {ukuran}", satuan_list, index=3)
    satuan_2 = st.selectbox(f"Ke satuan {ukuran}", satuan_list, index=2)

    for n in range(len(satuan_list)):
        if satuan == satuan_list[n]:
            satuan_index = n
            break

    for n in range(len(satuan_list)):
        if satuan_2 == satuan_list[n]:
            satuan_2_index = n
            break

    angka_2 = angka * satuan_panjang[satuan_index] / satuan_panjang[satuan_2_index]

    st.write('## **Hasil Penyelesaian**')
    st.write(f"{fungsi(angka)} {satuan} = {fungsi(angka_2)} {satuan_2}")
