import re

def Open(file_name, mode):
    """
    ³������� ����� � �������� �������.
    """
    try:
        file = open(file_name, mode)
    except Exception as e:
        print(f"���� '{file_name}' �� ������� �������: {e}")
        return None
    else:
        print(f"���� '{file_name}' ������ ������� � ����� '{mode}'!")
        return file

# ������� ��������
if __name__ == "__main__":
    # �) ��������� ���������� ����� TF15_1 �� ���������� �����
    file1_name = "TF15_1.txt"
    text_lines = [
        "��� ����� ������ �����, ��� �� ���, �����, ���, ����������� �����.",
        "� ����� ����� �� ������ �����, ���� � ��� �� � ������������.",
        "�� ���� ����� � �������, �� �� �����, �����, �� ����."
    ]
    file_1_w = Open(file1_name, "w")

    if file_1_w is not None:
        for line in text_lines:
            file_1_w.write(line + '\n')
        print(f"���������� ������ ������ �� ����� '{file1_name}'!")
        file_1_w.close()
        print(f"���� '{file1_name}' �������!")

    # �) ����������� ����������� ��� � ����� � ���� TF15_2
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
        print(f"����� '{file1_name}' �� '{file2_name}' �������!")

    # �) ������� ����� ����� TF15_2 � ���� ������� ����� � �������� �����
    print("\n����� � ����� 'TF15_2.txt':")
    file_3_r = Open(file2_name, "r")

    if file_3_r is not None:
        for line in file_3_r.read().split():
            print(line)
        print(f"���� '{file2_name}' �������!")
        file_3_r.close()

