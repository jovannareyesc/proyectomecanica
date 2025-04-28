import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import openmc

# --------------------------------------------
# 1. Datos Sintéticos (simulados para 5 reactores)
# --------------------------------------------
data = {
    'Reactor': ['RBMK (Chernóbil)', 'BWR (Fukushima)', 'Obninsk', 'Calder Hall', 'Chicago Pile-1'],
    'Temperatura_C': [700, 290, 500, 400, 25],
    'Flujo_Refrigerante_kg_s': [8000, 4500, 200, 3000, 0],
    'Enriquecimiento_U235': [2.0, 3.5, 5.0, 1.3, 10.0],
    'Presion_Vapor_MPa': [6.5, 7.0, 4.0, 9.0, 0.001],
    'Edad_anos': [1, 40, 30, 50, 0],
    'Produccion_MWe': [1000, 784, 5, 50, 0.0005],
    'Eficiencia_ter': [28.0, 33.0, 18.0, 28.0, 0.1]
}

df = pd.DataFrame(data)

# --------------------------------------------
# 2. Modelado con Regresión (RBMK y BWR)
# --------------------------------------------
# Configuración de datos
X_rbmk = df[['Flujo_Refrigerante_kg_s', 'Temperatura_C']].iloc[0:1]  # Datos para RBMK
y_rbmk = df['Eficiencia_ter'].iloc[0:1]

# Regresión Polinómica (RBMK)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X_rbmk)
model_rbmk = LinearRegression()
model_rbmk.fit(X_poly, y_rbmk)
y_pred_rbmk = model_rbmk.predict(X_poly)
r2_rbmk = r2_score(y_rbmk, y_pred_rbmk)

# Random Forest (BWR) - Datos simulados para nivel de agua
df['Nivel_Agua'] = [85, 45, 90, 80, 0]  # % de nivel de agua (ejemplo)
X_bwr = df[['Presion_Vapor_MPa', 'Nivel_Agua']].iloc[1:2]
y_bwr = df['Produccion_MWe'].iloc[1:2]
model_bwr = RandomForestRegressor(n_estimators=100, random_state=42)
model_bwr.fit(X_bwr, y_bwr)
y_pred_bwr = model_bwr.predict(X_bwr)
r2_bwr = r2_score(y_bwr, y_pred_bwr)

# --------------------------------------------
# 3. Simulación en OpenMC (Chicago Pile-1)
# --------------------------------------------
# Material: Uranio enriquecido
material = openmc.Material()
material.add_nuclide('U235', 1.0)
material.set_density('g/cm3', 10.0)

# Geometría esférica
sphere = openmc.Sphere(r=10.0, boundary_type='vacuum')
cell = openmc.Cell(fill=material, region=-sphere)
geometry = openmc.Geometry([cell])

# Configuración de la simulación
settings = openmc.Settings()
settings.batches = 10
settings.inactive = 5
settings.particles = 1000
settings.source = openmc.Source(space=openmc.stats.Point((0, 0, 0)))

# Modelo y ejecución
model = openmc.Model(geometry=geometry, settings=settings)
model.run()

# --------------------------------------------
# 4. Resultados y Visualización
# --------------------------------------------
print("\nResultados de Modelado:")
print(f"- RBMK (R²): {r2_rbmk:.2f}")
print(f"- BWR (R²): {r2_bwr:.2f}")
print("- Chicago Pile-1: Simulación completada. Ver archivos 'tallies.out' y 'summary.h5'")

# Gráfico: Temperatura vs. Eficiencia
plt.figure(figsize=(8, 4))
plt.scatter(df['Temperatura_C'], df['Eficiencia_ter'], c='red', label='Datos')
plt.xlabel('Temperatura del Núcleo (°C)')
plt.ylabel('Eficiencia Térmica (%)')
plt.title('Correlación: Temperatura vs. Eficiencia en Reactores Nucleares')
plt.grid(True)
plt.legend()
plt.show()
