Toyco utiliza tres operaciones para armar tres tipos de juguetes: trenes, camiones y carros. Los tiempos diarios disponibles para las tres operaciones son 430, 460 y 420 minutos, respectivamente, y los ingresos por unidad de tren, camión y carro de juguete son de $3, $2 y $5, respectivamente. Los tiempos de ensamble por tren en las tres operaciones son de 1, 3 y 1 minutos, respectivamente. Los tiempos correspondientes por camiones y por auto son (2,0,4) y (1,2,0) minutos, (un tiempo cero significa que no se utiliza).

### a)

*Obtenga por el método Simplex el resultado óptimo (Recuerde incluir, tabla inicial, intermedias y tabla final).*

#### Definición del problema
- Definicion de variables

    $\textrm{Producción Trenes} \to x_1$

    $\textrm{Producción Camiones} \to x_2$

    $\textrm{Producción Autos} \to x_3$

- Función objetivo $Z$

    $\textrm{Max} Z \to 3x_1 + 2x_2 + 5x_3$

- Restricciones

    $R_1 \to 1x_1 + 2x_2 + 1x_3 <= 430$

    $R_2 \to 3x_1 + 2x_3 <= 460$

    $R_3 \to 1x_1 + 4x_2 <= 420$

    $R_4 \to x_1, x_2, x_3 >=0$

#### Ecuaciones
   
$Z - 3x_1 - 2x_2 - 5x_3 + 0s_1 + 0s_2 + 0s_3 = 0$

$R_1 \to 1x_1 + 2x_2 + 1x_3 + s_1 = 430$

$R_2 \to 3x_1 + 2x_3 + s_2 = 460$

$R_3 \to 1x_1 + 4x_2 + s_3 = 420$

#### Tabla inicial
   
| $V_B$ | $Z$ | $x_1$ | $x_2$ | $x_3$    | $s_1$ | $s_2$ | $s_3$ | $Solucion$ |
| ----- | --- | ----- | ----- | -------- | ----- | ----- | ----- | ---------- |
| $Z$   | $1$ | $-3$  | $-2$  | ==$-5$== | $0$   | $0$   | $0$   | $0$        |
| $s_1$ | $0$ | $1$   | $2$   | $1$      | $1$   | $0$   | $0$   | $430$      |
| $s_2$ | $0$ | $3$   | $0$   | $2$      | $0$   | $1$   | $0$   | $460$      |
| $s_3$ | $0$ | $1$   | $4$   | $0$      | $0$   | $0$   | $1$   | $420$      |

$\textrm{Variable de entrada} \to V_E = x_3$

#### Primera iteración

##### Seleccionar variable pivote $V_P$

| Variables básicas | Columna $V_E$ | Columna $Solución$ | Relación mínima         | Válida |
| ----------------- | ------------- | ------------------ | ----------------------- | ------ |
| $s_1$             | $1$           | $430$              | $\frac{430}{1}=430$     | Sí     |
| $s_2$             | $2$           | $460$              | ==$\frac{460}{2}=230$== | Sí     |
| $s_3$             | $0$           | $420$              | $\frac{420}{0}=\infty$  | No     |

$\textrm{Variable pivote} \to V_P = s_2$

##### Actualizar la fila $V_P$ con $V_E$

$\textrm{Interesección entre la columna } V_E \textrm{ y la fila } V_P \to 2$

| $V_B$         | $Z$ | $x_1$         | $x_2$ | $x_3$         | $s_1$ | $s_2$         | $s_3$ | $Solucion$      |
| ------------- | --- | ------------- | ----- | ------------- | ----- | ------------- | ----- | --------------- |
| $s_2 \to x_3$ | $0$ | $\frac{3}{2}$ | $0$   | $\frac{2}{2}$ | $0$   | $\frac{1}{2}$ | $0$   | $\frac{460}{2}$ |
| $x_3$         | $0$ | $\frac{3}{2}$ | $0$   | $1$           | $0$   | $\frac{1}{2}$ | $0$   | $230$           |

| $V_B$ | $Z$ | $x_1$         | $x_2$ | $x_3$    | $s_1$ | $s_2$         | $s_3$ | $Solucion$ |
| ----- | --- | ------------- | ----- | -------- | ----- | ------------- | ----- | ---------- |
| $Z$   | $1$ | $-3$          | $-2$  | ==$-5$== | $0$   | $0$           | $0$   | $0$        |
| $s_1$ | $0$ | $1$           | $2$   | $1$      | $1$   | $0$           | $0$   | $430$      |
| $x_3$ | $0$ | $\frac{3}{2}$ | $0$   | $1$      | $0$   | $\frac{1}{2}$ | $0$   | $230$      |
| $s_3$ | $0$ | $1$           | $4$   | $0$      | $0$   | $0$           | $1$   | $420$      |

##### Actualizar las demás filas respecto a la fila $V_E$

###### Actualizar $Z$

| $V_B$             | $Z$ | $x_1$           | $x_2$ | $x_3$    | $s_1$ | $s_2$          | $s_3$ | $Solucion$ |
| ----------------- | --- | --------------- | ----- | -------- | ----- | -------------- | ----- | ---------- |
| $Z$               | $1$ | $-3$            | $-2$  | ==$-5$== | $0$   | $0$            | $0$   | $0$        |
| $x_3$             | $0$ | $\frac{3}{2}$   | $0$   | $1$      | $0$   | $\frac{1}{2}$  | $0$   | $230$      |
| $-5x_3$           | $0$ | $\frac{-15}{2}$ | $0$   | $-5$     | $0$   | $\frac{-5}{2}$ | $0$   | $-1150$    |
| $Z = Z - (-5x_3)$ | $1$ | $\frac{9}{2}$   | $-2$  | $0$      | $0$   | $\frac{5}{2}$  | $0$   | $1150$     |

###### Actualizar $s_1$

| $V_B$              | $Z$ | $x_1$          | $x_2$ | $x_3$   | $s_1$ | $s_2$          | $s_3$ | $Solucion$ |
| ------------------ | --- | -------------- | ----- | ------- | ----- | -------------- | ----- | ---------- |
| $s_1$              | $0$ | $1$            | $2$   | ==$1$== | $1$   | $0$            | $0$   | $430$      |
| $x_3$              | $0$ | $\frac{3}{2}$  | $0$   | $1$     | $0$   | $\frac{1}{2}$  | $0$   | $230$      |
| $1x_3$             | $0$ | $\frac{3}{2}$  | $0$   | $1$     | $0$   | $\frac{1}{2}$  | $0$   | $230$      |
| $s_1 = s_1 - 1x_3$ | $0$ | $\frac{-1}{2}$ | $2$   | $0$     | $1$   | $\frac{-1}{2}$ | $0$   | $200$      |

###### Actualizar $s_3$

| $V_B$              | $Z$ | $x_1$         | $x_2$ | $x_3$   | $s_1$ | $s_2$         | $s_3$ | $Solucion$ |
| ------------------ | --- | ------------- | ----- | ------- | ----- | ------------- | ----- | ---------- |
| $s_3$              | $0$ | $1$           | $4$   | ==$0$== | $0$   | $0$           | $1$   | $420$      |
| $x_3$              | $0$ | $\frac{3}{2}$ | $0$   | $1$     | $0$   | $\frac{1}{2}$ | $0$   | $230$      |
| $0x_3$             | $0$ | $0$           | $0$   | $0$     | $0$   | $0$           | $0$   | $0$        |
| $s_3 = s_3 - 0x_3$ | $0$ | $1$           | $4$   | $0$     | $0$   | $0$           | $1$   | $420$      |

##### Actualizar tabla con las filas actualizadas

| $V_B$ | $Z$ | $x_1$          | $x_2$    | $x_3$ | $s_1$ | $s_2$          | $s_3$ | $Solucion$ |
| ----- | --- | -------------- | -------- | ----- | ----- | -------------- | ----- | ---------- |
| $Z$   | $1$ | $\frac{9}{2}$  | ==$-2$== | $0$   | $0$   | $\frac{5}{2}$  | $0$   | $1150$     |
| $s_1$ | $0$ | $\frac{-1}{2}$ | $2$      | $0$   | $1$   | $\frac{-1}{2}$ | $0$   | $200$      |
| $x_3$ | $0$ | $\frac{3}{2}$  | $0$      | $1$   | $0$   | $\frac{1}{2}$  | $0$   | $230$      |
| $s_3$ | $0$ | $1$            | $4$      | $0$   | $0$   | $0$            | $1$   | $420$      |

$\textrm{Variable de entrada} \to V_E = x_2$

#### Segunda iteración

##### Seleccionar variable pivote $V_P$

| Variables básicas | Columna $V_E$ | Columna $Solución$ | Relación mínima         | Válida |
| ----------------- | ------------- | ------------------ | ----------------------- | ------ |
| $s_1$             | $2$           | $200$              | ==$\frac{200}{2}=100$== | Sí     |
| $x_3$             | $0$           | $230$              | $\frac{230}{0}=\infty$  | No     |
| $s_3$             | $4$           | $420$              | $\frac{420}{4}=105$     | Sí     |

$\textrm{Variable pivote} \to V_P = s_1$

##### Actualizar la fila $V_P$ con $V_E$

$\textrm{Interesección entre la columna } V_E \textrm{ y la fila } V_P \to 2$

| $V_B$         | $Z$ | $x_1$                    | $x_2$         | $x_3$ | $s_1$         | $s_2$                    | $s_3$ | $Solucion$      |
| ------------- | --- | ------------------------ | ------------- | ----- | ------------- | ------------------------ | ----- | --------------- |
| $s_1 \to x_2$ | $0$ | $\frac{\frac{-1}{2}}{2}$ | $\frac{2}{2}$ | $0$   | $\frac{1}{2}$ | $\frac{\frac{-1}{2}}{2}$ | $0$   | $\frac{200}{2}$ |
| $x_2$         | $0$ | $\frac{-1}{4}$           | $1$           | $0$   | $\frac{1}{2}$ | $\frac{-1}{4}$           | $0$   | $100$           |

| $V_B$ | $Z$ | $x_1$          | $x_2$    | $x_3$ | $s_1$         | $s_2$          | $s_3$ | $Solucion$ |
| ----- | --- | -------------- | -------- | ----- | ------------- | -------------- | ----- | ---------- |
| $Z$   | $1$ | $\frac{9}{2}$  | ==$-2$== | $0$   | $0$           | $\frac{5}{2}$  | $0$   | $1150$     |
| $x_2$ | $0$ | $\frac{-1}{4}$ | $1$      | $0$   | $\frac{1}{2}$ | $\frac{-1}{4}$ | $0$   | $100$      |
| $x_3$ | $0$ | $\frac{3}{2}$  | $0$      | $1$   | $0$           | $\frac{1}{2}$  | $0$   | $230$      |
| $s_3$ | $0$ | $1$            | $4$      | $0$   | $0$           | $0$            | $1$   | $420$      |

##### Actualizar las demás filas respecto a la fila $V_E$

###### Actualizar $Z$

| $V_B$             | $Z$ | $x_1$          | $x_2$    | $x_3$ | $s_1$         | $s_2$          | $s_3$ | $Solucion$ |
| ----------------- | --- | -------------- | -------- | ----- | ------------- | -------------- | ----- | ---------- |
| $Z$               | $1$ | $\frac{9}{2}$  | ==$-2$== | $0$   | $0$           | $\frac{5}{2}$  | $0$   | $1150$     |
| $x_2$             | $0$ | $\frac{-1}{4}$ | $1$      | $0$   | $\frac{1}{2}$ | $\frac{-1}{4}$ | $0$   | $100$      |
| $-2x_2$           | $0$ | $\frac{1}{2}$  | $-2$     | $0$   | $-1$          | $\frac{1}{2}$  | $0$   | $-200$     |
| $Z = Z - (-2x_2)$ | $1$ | $4$            | $0$      | $0$   | $1$           | $2$            | $0$   | $1350$     |

###### Actualizar $x_3$

| $V_B$              | $Z$ | $x_1$          | $x_2$   | $x_3$ | $s_1$         | $s_2$          | $s_3$ | $Solucion$ |
| ------------------ | --- | -------------- | ------- | ----- | ------------- | -------------- | ----- | ---------- |
| $x_3$              | $0$ | $\frac{3}{2}$  | ==$0$== | $1$   | $0$           | $\frac{1}{2}$  | $0$   | $230$      |
| $x_2$              | $0$ | $\frac{-1}{4}$ | $1$     | $0$   | $\frac{1}{2}$ | $\frac{-1}{4}$ | $0$   | $100$      |
| $0x_2$             | $0$ | $0$            | $0$$    | $0$   | $0$           | $0$            | $0$   | $0$        |
| $x_3 = x_3 - 0x_2$ | $0$ | $\frac{3}{2}$  | $0$     | $1$   | $0$           | $\frac{1}{2}$  | $0$   | $230$      |

###### Actualizar $s_3$

| $V_B$              | $Z$ | $x_1$          | $x_2$   | $x_3$ | $s_1$         | $s_2$          | $s_3$ | $Solucion$ |
| ------------------ | --- | -------------- | ------- | ----- | ------------- | -------------- | ----- | ---------- |
| $s_3$              | $0$ | $1$            | ==$4$== | $0$   | $0$           | $0$            | $1$   | $420$      |
| $x_2$              | $0$ | $\frac{-1}{4}$ | $1$     | $0$   | $\frac{1}{2}$ | $\frac{-1}{4}$ | $0$   | $100$      |
| $4x_2$             | $0$ | $-1$           | $4$     | $0$   | $2$           | $-1$           | $0$   | $400$      |
| $s_3 = s_3 - 4x_2$ | $0$ | $2$            | $0$     | $0$   | $-2$          | $1$            | $1$   | $20$       |

##### Actualizar tabla con las filas actualizadas

| $V_B$ | $Z$ | $x_1$          | $x_2$ | $x_3$ | $s_1$         | $s_2$          | $s_3$ | $Solucion$ |
| ----- | --- | -------------- | ----- | ----- | ------------- | -------------- | ----- | ---------- |
| $Z$   | $1$ | $4$            | $0$   | $0$   | $1$           | $2$            | $0$   | $1350$     |
| $x_2$ | $0$ | $\frac{-1}{4}$ | $1$   | $0$   | $\frac{1}{2}$ | $\frac{-1}{4}$ | $0$   | $100$      |
| $x_3$ | $0$ | $\frac{3}{2}$  | $0$   | $1$   | $0$           | $\frac{1}{2}$  | $0$   | $230$      |
| $s_3$ | $0$ | $2$            | $0$   | $0$   | $-2$          | $1$            | $1$   | $20$       |

Dado que la ecuacion $Z$ ya no tiene coeficientes negativos, esta es nuestra tabla final, la cual nos indica que el resultado óptimo es $1350$, y se encuentra en el punto $C(0,100,230)$

Una manera de interpretar esto es que a la jugueteria le es más optimo no fabricar trenes.

### b)

*Obtenga el precio dual de los recursos y cuanto impacta a la función Z.*

De la tabla de arriba, pasamos las holguras como precios duales.

| $V_B$ | $Z$ | $Solucion$ | $\textrm{P. Dual }_{R_1}$ | $\textrm{P. Dual }_{R_2}$ | $\textrm{P. Dual }_{R_3}$ |
| ----- | --- | ---------- | ------------------------- | ------------------------- | ------------------------- |
| $Z$   | $1$ | $1350$     | $1$                       | $2$                       | $0$                       |
| $x_2$ | $0$ | $100$      | $\frac{1}{2}$             | $\frac{-1}{4}$            | $0$                       |
| $x_3$ | $0$ | $230$      | $0$                       | $\frac{1}{2}$             | $0$                       |
| $s_3$ | $0$ | $20$       | $-2$                      | $1$                       | $1$                       |

$Z=1350 + D_1 + 2D_2$

$x_2 = 100 + \frac{1}{2}D_1 - \frac{1}{4}D_2 + 0D_3 \geq 0$

$x_3 = 230 + 0D_1 + \frac{1}{2}D_2 + 0D_3 \geq 0$

$s_3 = 20 - 2D_1 + 1D_2 + 1D_3 \geq 0$

Estos valores quieren decir que nuestra función $Z$ se vera afectada solamente por la diferencia en la disponibilidad de tiempo de las operaciones 1 y 2.

Dado que fue mas óptimo no fabricar trenes, el cambio en las disponibilidades de operaciones no genera cambios en su producción, esta seguira siendo 0.

Asi mismo, aunque la holgura de la disponibilidad de la operación 3 no intervene para obtener el valor óptimo, esta actua como restriccion, ya que de ser menor a 0, cambiaría los precios duales y por ende impactaría en la función objetivo.

### c)

*Si la disponibilidad de las operaciones 1,2 y 3 se cambia a 438, 500 y 410 minutos, demuestre si la solución básica permanece factible y explique porque. Determine el cambio del ingreso en z mediante los precios duales.*

$D_1 = 438 - 430 = 8$

$D_2 = 500 - 460 = 40$

Dado que aumentamos los valores de $D_1$ y $D_2$ no es requerido checar e mínimo de estos. No obstante, los límites de $D_3$ estan dados en terminos de $D_1$ y $D_2$, por esto lo debemos calcular con los precios duales antes obtenidos.

Para $s_3 \geq 0$:

$20 - 2D_1 + D_2 + D_3 \geq 0$

$D_3 \geq -20 + 2D_1 - D_2$

$D_3 \geq -20 + 2(8) - (40)$

$D_3 \geq -44$

$D_3 = 410 - 420  = -10$

El cambio en $D_3$ fue mayor al mínimo requerido, por ende, la solución sigue siendo factible.

$Z_B = 1350 + D_1 + 2D_2 = 1350 + (8) + 2(40) = 1438$

El cambio en $Z$ fue de $(8) + 2(40) = 88$

### d)

*Si la disponibilidad de las tres operaciones se cambia a 460, 440 y 380 minutos respectivamente,
aproveche las condiciones simultaneas para demostrar que la solución básica es no factible.*

- $D_2 = 440 - 460 = -20$

    Para $x_3 \geq 0$:

    $230 + \frac{1}{2}D_2 \geq 0$

    $\frac{1}{2}D_2 \geq -230$

    $D_2 \geq -460$

    Lo minimo que puede valer $D_2$ es $-460$, por ende, si cumple esta condición.

- $D_1 = 460 - 430 = 30$

    Para $x_2 \geq 0$:

    $100 + \frac{1}{2}D_1 - \frac{1}{4}D_2 \geq 0$

    $\frac{1}{2}D_1  \geq -100 + \frac{1}{4}D_2$

    $D_1  \geq -200 + \frac{1}{2}D_2$

    $D_1  \geq -200 + \frac{1}{2}(-20)$

    $D_1  \geq -210$

    Lo minimo que puede valer $D_1$ es $-210$, por ende, si cumple esta condición.

- $D_3 = 380 - 420 = -40$
  
    Para $s_3 \geq 0$:

    $20 - 2D_1 + D_2 + D_3 \geq 0$

    $D_3 \geq -20 + 2D_1 - D_2$

    $D_3 \geq -20 + 2(30) - (-20)$

    $D_3 \geq 60$

    Lo minimo que puede valer $D_1$ es $60$, sin embargo, vale -40. Lo cual es errorneo.

> ###### Nota de estudio
> No es necesario despejar los cambios en la disponibilidad de las restricciones $D_i$. Podríamos haber checado directamente en las ecuaciones. En este ejercicio, la tercer ecuacion se evaluaría en $-100$, incumpliendo el limite del precio dual.
> 
> $x_2 = 100 + \frac{1}{2}D_1 - \frac{1}{4}D_2 + 0D_3 \geq 0$
> 
> $x_3 = 230 + 0D_1 + \frac{1}{2}D_2 + 0D_3 \geq 0$
> 
> $s_3 = 20 - 2D_1 + 1D_2 + 1D_3 \geq 0$
