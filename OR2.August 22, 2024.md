> ### Metodo gráfico
> 1. Definición del problema
>    - Definicion de variables
>    - Función objetivo $Z_a$
>    - Restricciones
> 2. Graficar las restricciones
> 3. Calcular los puntos de esquina
> #### Analisis de sensibilidad
> ##### Precio duales
> 1. Cambiar disponibilidad de la restricción
> 2. Graficar nuevas restricciones
> 3. Calculo del precio dual
> 
>       $\textrm{Precio Dual}_{R_{i_a}}=\frac{Z_a-Z}{D_{R_{i_a}}-D_{R_i}}$
>

La tienda el chabrito produce 2 tipos de productos texanos. El producto
texano 1 requiere el doble de mano de obra que el tipo 2.
Si toda la mano de obra disponible se dedica solo a producir el
producto 2, la compañia puede producir un total de 400 productos de tipo 2
en 1 día. La utilidad es de $8 dolares por producto texano 1, y de $5 por
producto texano 2. Determine la cantidad óptima de productos texanos que
debe producir.
Los límites de mercado respectivos para los 2 tipos de producto es 150 y 200
productos por dia.

### a)
*Realice por el método gráfico.*

1. Definición del problema
   - Definicion de variables
  
     $\textrm{Disp. Prod. 1} \to x_1$

     $\textrm{Disp. Prod. 2} \to x_2$

   - Función objetivo $Z_a$
     $\textrm{Max} Z \to 8x_1 + 5x_2$

   - Restricciones
  
     $R_1 \to 2x_1 + x_2 <= 400$
 
     $R_2 \to x_1 <= 150$
 
     $R_3 \to x_2 <= 200$
 
     $R_4 \to x_1, x_2 =0$

2. Graficar las restricciones
![Grafica 1](./img/OR2.August%2022,%202024.img%201.png)

3. Calcular los puntos de esquina

#### Puntos esquina
| $PE$ | $x_1, x_2$ | $Z \to 8x_1 + 5x_2$ |
| ---- | ---------- | ------------------- |
| $A$  | $0, 0$     | $0$                 |
| $B$  | $0, 200$   | $1000$              |
| $C$  | $100, 200$ | ==$1800$==          |
| $D$  | $150, 100$ | $1700$              |
| $E$  | $150, 0$   | $1200$              |

### b)
*Determine el precio dual de la capacidad de producción en función
del producto de tipo 2 y el intervalo en el cual es aplicable.*

$R_1 \to 2x_1 + x_2 <= 400$

$R_{1_a} \to 2x_1 + x_2 <= 300$

![Grafica 2](./img/OR2.August%2022,%202024.img%202.png)

#### Puntos esquina
| $PE$ | $x_1, x_2$ | $Z \to 8x_1 + 5x_2$ |
| ---- | ---------- | ------------------- |
| $A$  | $0, 0$     | $0$                 |
| $B$  | $0, 200$   | $1000$              |
| $I$  | $50, 200$  | ==$1400$==          |
| $E$  | $150, 0$   | $1200$              |

#### $\textrm{Precio Dual } R_1$
$\textrm{Precio Dual}_{R_{1_a}}=\frac{{Z_a}-Z}{D_{R_{1_a}}-D_{R_1}}$

$\textrm{Precio Dual}_{R_{1_a}}=\frac{1400-1800}{300-400}=4$

#### Intervalo de factibilidad
|                                  |                                 |       |
| -------------------------------- | ------------------------------- | ----- |
| $\textrm{Punto B} \to (0,200)$   | $2x_1 + x_2 \to 2(0) + (200)$   | $200$ |
| $\textrm{Punto H} \to (150,200)$ | $2x_1 + x_2 \to 2(150) + (200)$ | $500$ |

Significa que $\textrm{Precio Dual}_{R_{1_a}}$ es válido en el intervalo
dado por $200 \leq  2x_1 + x_2  \leq 500$.

#### Ejemplo 1
Por ejemplo si
$2x_1 + x_2 \leq 500$

![Grafica 3](./img/OR2.August%2022,%202024.img%203.png)

| $PE$ | $x_1, x_2$ | $Z \to 8x_1 + 5x_2$ |
| ---- | ---------- | ------------------- |
| $A$  | $0, 0$     | $0$                 |
| $B$  | $0, 200$   | $1000$              |
| $H$  | $150, 200$ | ==$2200$==          |
| $E$  | $150, 0$   | $1200$              |

Nos da el máximo valor posible aumentando la capacidad de producción.
Si aumentasemos más la capacidad de producción las otras 2 restricciones
restringirían la máxima cantidad de productos producibles en un día
a 2200. 

#### Ejemplo 2
Por ejemplo si
$2x_1 + x_2 \leq 150$

![Grafica 5](./img/OR2.August%2022,%202024.img%205.png)

| $PE$ | $x_1, x_2$ | $Z \to 8x_1 + 5x_2$ |
| ---- | ---------- | ------------------- |
| $A$  | $0, 0$     | $0$                 |
| $M$  | $0, 150$   | $750$               |
| $N$  | $75, 0$    | ==$600$==           |

Si tratamos de obtener el punto óptimo original basados en la
diferencia y el precio dual:

$600 + 4(400 - 150) = 600 + 4(250) = 1600$

No nos devolvío el valor del punto óptimo, esto es debido a que a partir
del punto $B$ hacia abajo, el precio dual cambiaría de valor. (Borre por
accidente las pruebas, pero el precio dual pasa a ser 5).

### c)
*Si el límite de la demanda diaria del producto texano de tipo 1
se reduce a 120, utilice el precio dual para determinar el efecto
correspondiente en el ingreso óptimo.*

$R_2 \to x_1 <= 150$

$R_{2_b} \to x_1 <= 120$

![Grafica 4](./img/OR2.August%2022,%202024.img%204.png)

#### Puntos esquina
| $PE$ | $x_1, x_2$ | $Z \to 8x_1 + 5x_2$ |
| ---- | ---------- | ------------------- |
| $A$  | $0, 0$     | $0$                 |
| $B$  | $0, 200$   | $1000$              |
| $C$  | $100, 200$ | ==$1800$==          |
| $J$  | $120, 160$ | $1760$              |
| $K$  | $120, 0$   | $960$               |

#### $\textrm{Precio Dual } R_1$
$\textrm{Precio Dual}_{R_{2_b}}=\frac{{Z_b}-Z}{D_{R_{2_b}}-D_{R_2}}$

$\textrm{Precio Dual}_{R_{2_b}}=\frac{1800-1800}{150-120}=0$

El impacto será 0, no alterará el ingreso optimo debido a que $R_1$
está limitando el valor máximo actual a un valor de $x_1$ menor, esto
lo comprobamos con el intervalo de factibilidad.

#### Intervalo de factibilidad
|                                  |                 |       |
| -------------------------------- | --------------- | ----- |
| $\textrm{Punto C} \to (100,200)$ | $x_1 \to (100)$ | $100$ |
| $\textrm{Punto G} \to (200,0)$   | $x_1 \to (200)$ | $200$ |

Significa que $\textrm{Precio Dual}_{R_{2_b}}$ es válido solo en
el intervalo dado por $100 \leq x_1 \leq 200$.
