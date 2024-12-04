import xml.etree.ElementTree as ET

def parse_currency_xml(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        currency_data = {}

        for valute in root.findall(".//Valute"): 
            name = valute.findtext("Name")
            char_code = valute.findtext("CharCode")

            if name is not None and char_code is not None:
                currency_data[name] = char_code

        return currency_data

    except FileNotFoundError:
        print(f"Ошибка: файл {xml_file} не найден.")
        return None
    except ET.ParseError:
        print(f"Ошибка: не удалось распарсить XML-файл {xml_file}. Проверьте корректность файла.")
        return None
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return None


xml_filename = "currency.xml" 
result_dict = parse_currency_xml(xml_filename)

if result_dict:
    print("Словарь 'Name - CharCode':")
    for name, char_code in result_dict.items():
        print(f"{name}: {char_code}")