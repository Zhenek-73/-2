import pandas as pd

def extract_data_from_excel(file_path, search_string):
       try:
           data = pd.read_excel(file_path)
       except FileNotFoundError:
           print("Файл не найден. Проверьте путь к файлу.")
           return
       except Exception as e:
           print(f"Произошла ошибка при загрузке файла: {e}")
           return

       filtered_data = data[data.apply(lambda row: row.astype(str).str.contains(search_string, case=False).any(), axis=1)]


       if not filtered_data.empty:
           print(filtered_data)

file_path = 'таблтца.xlsx'  #путь к Excel файлу
search_string = input("Введите строку для поиска от 1 до 6: ")
extract_data_from_excel(file_path, search_string)