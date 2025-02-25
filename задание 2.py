import pandas as pd
import matplotlib.pyplot as plt
file_path = 'таблтца.xlsx'
df = pd.read_excel(file_path)
print(df.head())
plt.figure(figsize=(8, 6))
plt.plot(df['x'], df['y'], marker='o', label='ооо')
plt.title('График')
plt.xlabel('X')
plt.ylabel('ОY')
plt.legend()
plt.grid(True)
plt.show()