import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
df = pd.read_csv("ventas_productos.csv")

# Calcular el precio total por producto
df["Precio_Total"] = df["Cantidad"] * df["Precio"]

# Mostrar los primeros registros
print("📊 Datos cargados:")
print(df.head())

# Crear un gráfico de barras para visualizar el precio total por producto
plt.bar(df["Producto"], df["Precio_Total"], color="skyblue")
plt.xlabel("Producto")
plt.ylabel("Precio Total")
plt.title("📈 Análisis de Ventas por Producto")

# Guardar el gráfico como una imagen PNG
plt.savefig("grafico_precios.png")

# Mostrar el gráfico
plt.show()
