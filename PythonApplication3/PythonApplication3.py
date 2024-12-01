import re

def Open(file_name, mode):
    """
    Відкриття файлу з вказаним режимом.
    """
    try:
        file = open(file_name, mode)
    except Exception as e:
        print(f"Файл '{file_name}' не вдалося відкрити: {e}")
        return None
    else:
        print(f"Файл '{file_name}' успішно відкрито в режимі '{mode}'!")
        return file

# Основна програма
if __name__ == "__main__":
    # а) створення текстового файлу TF15_1 із символьних рядків
    file1_name = "TF15_1.txt"
    text_lines = [
        "Цей текст містить слова, такі як око, рівень, поп, несиметричні слова.",
        "А також слова на зразок радар, деякі з них не є симетричними.",
        "Ще один рядок з словами, як от топот, потоп, та інші."
    ]
    file_1_w = Open(file1_name, "w")

    if file_1_w is not None:
        for line in text_lines:
            file_1_w.write(line + '\n')
        print(f"Інформація успішно додана до файлу '{file1_name}'!")
        file_1_w.close()
        print(f"Файл '{file1_name}' закрито!")

    # б) знаходження симетричних слів і запис у файл TF15_2
    file2_name = "TF15_2.txt"
    file_2_r = Open(file1_name, "r")
    file_2_w = Open(file2_name, "w")

    if file_2_r is not None and file_2_w is not None:
        text = file_2_r.read()
        words = re.findall(r'\b\w+\b', text)
        symmetric_words = [word for word in words if word == word[::-1] and len(word) > 1]
        file_2_w.write(' '.join(symmetric_words))
        file_2_r.close()
        file_2_w.close()
        print(f"Файли '{file1_name}' та '{file2_name}' закрито!")

    # в) читання вмісту файла TF15_2 і друк кожного слова в окремому рядку
    print("\nСлова з файлу 'TF15_2.txt':")
    file_3_r = Open(file2_name, "r")

    if file_3_r is not None:
        for line in file_3_r.read().split():
            print(line)
        print(f"Файл '{file2_name}' закрито!")
        file_3_r.close()

