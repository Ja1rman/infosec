import string

# Полный алфавит
RUSSIAN_ALPHABET_UPPER = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
RUSSIAN_ALPHABET_LOWER = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ENGLISH_ALPHABET_UPPER = string.ascii_uppercase  # A-Z
ENGLISH_ALPHABET_LOWER = string.ascii_lowercase  # a-z
DIGITS = string.digits  # 0-9
SPECIAL_CHARACTERS = string.punctuation  # Спецсимволы

# Сбор в общий алфавит
FULL_ALPHABET = (
    RUSSIAN_ALPHABET_UPPER
    + RUSSIAN_ALPHABET_LOWER
    + ENGLISH_ALPHABET_UPPER
    + ENGLISH_ALPHABET_LOWER
    + DIGITS
    + SPECIAL_CHARACTERS
)
N = len(FULL_ALPHABET)


def vigenere_encrypt(text: str, key: str) -> str:
    """Функция шифрования по методу Виженера.

    Args:
        text (str): текст шифрования
        key (str): ключ шифрования

    Returns:
        str: зашифрованный текст
    """
    result = []
    key = key * (len(text) // len(key)) + key[: len(text) % len(key)]

    for m, k in zip(text, key):
        if m in FULL_ALPHABET:
            c = (FULL_ALPHABET.index(m) + FULL_ALPHABET.index(k)) % N
            result.append(FULL_ALPHABET[c])
        else:
            result.append(m)

    return "".join(result)


def vigenere_decrypt(text: str, key: str) -> str:
    """Функция дешифрования метода Виженера.

    Args:
        text (str): зашифрованный текст
        key (str): ключ расшифровки

    Returns:
        str: расшифрованный текст
    """
    result = []
    key = key * (len(text) // len(key)) + key[: len(text) % len(key)]

    for c, k in zip(text, key):
        if c in FULL_ALPHABET:
            m = (FULL_ALPHABET.index(c) - FULL_ALPHABET.index(k)) % N
            result.append(FULL_ALPHABET[m])
        else:
            result.append(c)

    return "".join(result)


def frequency_analysis(encrypted_text):
    unique_letters = set(encrypted_text)
    lenth = len(encrypted_text)
    print("Частотный криптоанализ зашифрованного текста:")
    for letter in unique_letters:
        print(f"'{letter}': {encrypted_text.count(letter)/lenth*100:.2f}%")


def encrypt_file(input_file, output_file, key):
    with open(input_file) as file:
        text = file.read()

    encrypted_text = vigenere_encrypt(text, key)
    frequency_analysis(encrypted_text)
    with open(output_file, "w") as file:
        file.write(encrypted_text)


def decrypt_file(input_file, output_file, key):
    with open(input_file) as file:
        text = file.read()

    decrypted_text = vigenere_decrypt(text, key)

    with open(output_file, "w") as file:
        file.write(decrypted_text)

# Пример варианта
key_phrase = "кларнет"
encrypt_file("input.txt", "encrypted.txt", key_phrase)
decrypt_file("encrypted.txt", "decrypted.txt", key_phrase)
