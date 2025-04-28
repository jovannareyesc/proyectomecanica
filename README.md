# PROYECTO MECÁNICA
## Finalidad del proyecto
 
1. **Analizar la conversión de energía** en reactores nucleares aplicando principios de mecánica clásica (trabajo, energía cinética y conservación de energía) para modelar su eficiencia térmica y producción eléctrica.  
2. **Evaluar pérdidas energéticas** (fricción, calor residual) mediante regresión y simulaciones, cuantificando cómo limitan el rendimiento según las leyes de la termodinámica.  
3. **Optimizar variables operativas** (temperatura, flujo de refrigerante) usando herramientas computacionales (Python, OpenMC) para maximizar la eficiencia bajo restricciones físicas reales.  
4. **Proponer mejoras** basadas en datos, integrando IA o diseños innovadores (como SMRs), para reducir brechas entre modelos teóricos y desempeño práctico en sistemas nucleares.  

## Salida esperada

**Resultados de modelos:**
-> R² para RBMK y BWR (ej: RBMK (R²): 0.87).
-> Archivos de OpenMC (tallies.out, summary.h5) para Chicago Pile-1.
**Gráfico:**
->Un scatter plot mostrando la correlación entre temperatura y eficiencia.
![scatterplot](scatterplot.png)

## Pasos para ejecutar el código
Abajo, se adjuntan los pasos a seguir para ejecutar el código exitosamente desde una terminal de preferencia:

1.
   ```sh
   git clone https://github.com/jovannareyesc/proyectomecanica
   ```
2. 
   ```sh
   pip install pandas scikit-learn matplotlib openmc
   ```
3. 
   ```sh
   python main.py
   ```

## Conclusiones

El estudio evidenció que, a pesar de que los reactores atómicos enfrentan restricciones por ineficiencias en la termodinámica y pérdidas en la mecánica, tecnologías como la simulación por computadora y la inteligencia artificial pueden mejorar su concepción.  Un caso particular sería ajustar el paso del refrigerante en los RBMKs, lo cual podría prevenir inestabilidad, mientras que vigilar el nivel de agua en los BWRs ayudaría a evitar siniestros. 
