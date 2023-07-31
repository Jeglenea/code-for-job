def compare_text_files(file1_path, file2_path):
    try:
        with open(file1_path, 'r') as file1:
            data1 = file1.read()
        
        with open(file2_path, 'r') as file2:
            data2 = file2.read()

        if data1 == data2:
            print("İki dosya içeriği aynı.")
        else:
            print("İki dosya içeriği farklı.")
    except FileNotFoundError:
        print("Dosya bulunamadı.")
    except Exception as e:
        print(f"Hata oluştu: {e}")


# İki dosyayı karşılaştırmak için dosya yollarını belirtin
file1_path = r"C:\Users\erayo\Desktop\Karsilastirma1.txt"
file2_path = r"C:\Users\erayo\Desktop\Karsilastirma2.txt"

compare_text_files(file1_path, file2_path)