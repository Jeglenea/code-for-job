def generate_ips(base_ips):
    result_ips = []
    for ip in base_ips:
        prefix, last_octet = ip.rsplit(".", 1)
        for i in range(30, 33):
            new_ip = f"{prefix}.{last_octet[:-1]}{i}"
            result_ips.append(f"call checken_sql.bat {new_ip}")
    return result_ips

# Kullanıcıdan IP listesini alıyoruz
input_ips = input("Lütfen IP listesini virgülle ayırarak girin: ")
base_ips = input_ips.split(",")

# IP listesi içindeki boşlukları temizliyoruz
base_ips = [ip.strip() for ip in base_ips]

ips_with_variations = generate_ips(base_ips)

for ip in ips_with_variations:
    print(ip)