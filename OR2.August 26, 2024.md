Una compañia que funciona 10h al día, fabrica 2 productos en 3
procesos secuenciales, los cuales se ejecutan las 10h sin periodos de
descanso.

<table>
<theader>
<tr>
<td></td>
<td colspan="3" align="center">Minutos</td>
<td></td>
</tr>
<tr>
<th></th>
<th>Proc. 1</th>
<th>Proc. 2</th>
<th>Proc. 3</th>
<th>Utilidad unitaria</th>
</tr>
</theader>
<tbody>
<tr>
<td> Prod_1 </td>
<td> 10 </td>
<td> 6   </td>
<td> 8 </td>
<td> $2 </td>
</tr>
<tr>
<td> Prod_2 </td>
<td> 5 </td>
<td> 20 </td>
<td> 10 </td>
<td> $3 </td>
</tr>
</tbody>
</table>

### a)
*Determine por el método gráfico la combinación óptima.*

1. Definición del problema
   - Definicion de variables
  
     $\textrm{Producción Prod. 1} \to x_1$

     $\textrm{Producción Prod. 2} \to x_2$

   - Función objetivo $Z_a$
     $\textrm{Max} Z \to 2x_1 + 3x_2$

   - Restricciones
  
     $R_1 \to 10x_1 + 5x_2 <= 600$
 
     $R_2 \to 6x_1 + 20x_2 <= 600$
 
     $R_3 \to 8x_1 + 10x_2 <= 600$
 
     $R_4 \to x_1, x_2 >=0$

2. Graficar las restricciones
   ![Grafica 1](./img/OR2.August%2026,%202024.img%201.png)

3. Obtener los puntos de esquina
   
   | $PE$ | $x_1, x_2$     | $Z \to 2x_1 + 3x_2$ |
   | ---- | -------------- | ------------------- |
   | $A$  | $0, 0$         | $0$                 |
   | $B$  | $0, 30$        | $90$                |
   | $C$  | $52.94, 14.12$ | ==$148.28$==        |
   | $D$  | $60, 0$        | $120$               |

Es decir que producir 51 productos del tipo uno y
14 del producto 2 es la combinación óptima para
obtener mayores ganancias.


### b)
*Determine el Precio Dual del proceso 2.*

1. Modificar la restricción
   
   $R_2 \to 6x_1 + 20x_2 <= 600$

   $R_2 \to 6x_1 + 20x_2 <= 450$

2. Graficar las restricciones
   
   ![Grafica 2](./img/OR2.August%2026,%202024.img%202.png)

3. Obtener los puntos de esquina.
   
   | $PE$ | $x_1, x_2$    | $Z \to 2x_1 + 3x_2$ |
   | ---- | ------------- | ------------------- |
   | $A$  | $0, 0$        | $0$                 |
   | $E$  | $0, 22.5$     | $67.5$              |
   | $F$  | $57.35, 5.29$ | ==$130.57$==        |
   | $D$  | $60, 0$       | $120$               |

4. $\textrm{Precio Dual}_{R_{2_a}}$

   $\textrm{Precio Dual}_{R_{2_a}}=\frac{{Z_{a}}-Z}{D_{R_{2_a}}-D_{R_2}}$

   $\textrm{Precio Dual}_{R_{2_a}}=\frac{130.57-148.28}{450-600}=0.1167$

5. Intervalo de factibilidad
   
   |                                |                                   |       |
   | ------------------------------ | --------------------------------- | ----- |
   | $\textrm{Punto D} \to (60,0)$  | $6x_1 + 20x_2 \to 6(60) + 20(0)$  | $360$ |
   | $\textrm{Punto G} \to (50,20)$ | $6x_1 + 20x_2 \to 6(50) + 20(20)$ | $700$ |

   Significa que $\textrm{Precio Dual}_{R_{2_a}}$ es válido en el intervalo
   dado por $360 \leq  6x_1 + 20x_2  \leq 700$.

### c)

*Si el límite de tiempo del proceso 2 se reduce 1hr, cuanto afecta a $Z$. Calcule
utilizando el precio dual.*

1. Modificar la restricción
   
   $R_2 \to 6x_1 + 20x_2 <= 600$

   $R_2 \to 6x_1 + 20x_2 <= 540$

2. Dado que cae en el intervalo de factibilidad, podemos utilizar el precio dual calculado.
   
   $Z_b=Z-(D_{R_2}-D_{R_{2_b}})(\textrm{Precio Dual}_{R_{2_a}})$
   
   $Z_b=148.28-(600-540)(0.1167)=141.278$

   El valor disminuye en $7.002$ unidades por cada hora reducida en el intervalo calculado previamente.