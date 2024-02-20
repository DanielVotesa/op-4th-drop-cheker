import requests

# URL, содержащий список адресов для эирдропа
url = "https://raw.githubusercontent.com/ethereum-optimism/op-analytics/main/reference_data/address_lists/op_airdrop_4_simple_list.csv"

# Загрузка списка адресов для эирдропа
response = requests.get(url)
# Извлечение и преобразование адресов к нижнему регистру
airdrop_addresses = [line.split(',')[0].lower() for line in response.text.split('\n')]

# Путь к файлу с вашими адресами
file_path = 'wallets.txt'  # Замените на путь к вашему файлу

# Чтение адресов из файла и преобразование к нижнему регистру
with open(file_path, 'r') as file:
    my_addresses = [line.strip().lower() for line in file.readlines()]

# Поиск совпадений
matches = [address for address in my_addresses if address in airdrop_addresses]

# Вывод совпадений
print("Адреса, получающие эирдроп:")
for match in matches:
    print(match)

