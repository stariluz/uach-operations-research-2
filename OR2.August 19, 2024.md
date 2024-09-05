# Analisis de sensibilidad

## Método gráfico

$\textrm{Max} Z = 5x_1 + 4x_2$

$R_1 \to 6x_1 + 4x_2 \leq 24$

$R_2 \to x_1 + 2x_2 \leq 6$

$Z=21$

![Grafica](./img/OR2.August%2019,%202024.img%201.png)

El análisis de sensibilidad nos permite preveer como mejorar nuestra función objetivo.
Para obtener un precio dual, debemos obtener un nuevo valor de Z, manipulando una de las restricciones.

---
### Obtener $\textrm{Precio Dual}_{R_1}$

$R_{1.a} = 6x_1 + 4x_2 = 28$

Si $x_1=0$, entonces $x_2=7$

Si $x_2=0$, entonces $x_1=4.66$

En $x_1=4, x_2=1$ obtenemos el punto óptimo $Z_B=24$

$\textrm{Precio Dual}_{R_1}=\frac{Z_B-Z_A}{P_{1.a}-P_{1}}=\frac{24-21}{28-24}=\frac{3}{4}$

$\textrm{Precio Dual}_{R_1}$ nos indica que al manipular la $R_1$ en una unidad, varia en $\frac{3}{4}$ en el valor de $Z$.

#### Intervalo de factibilidad del $\textrm{Precio Dual}_{R_1}$

|                              |                               |      |
| ---------------------------- | ----------------------------- | ---- |
| $\textrm{Punto B} \to (0,3)$ | $6x_1 + 4x_2 \to 6(0) + 4(3)$ | $12$ |
| $\textrm{Punto F} \to (6,0)$ | $6x_1 + 4x_2 \to 6(6) + 4(0)$ | $36$ |

El precio dual calculado solo es valido mientras $R_1$ se mantenga entre estos valores.

$12 \leq \textrm{ R }_1 \leq 28$

---

### Obtener $\textrm{Precio Dual}_{R_2}$

$R_{2.a}=x_1 + 2x_2=8$

Si $x_1=0$, entonces $x_2=4$

Si $x_2=0$, entonces $x_1=8$

En $x_1=2, x_2=3$ obtenemos el punto óptimo $Z_C=22$

$\textrm{Precio Dual}_{R_2}=\frac{Z_C-Z_A}{R_{2.a}-R_{2}}=\frac{22-21}{8-6}=\frac{1}{2}$

$\textrm{Precio Dual}_{R_2}$ nos indica que al manipular la $R_2$ en una unidad, varia en $\frac{1}{2}$ en el valor de $Z$.

#### Intervalo de factibilidad del $\textrm{Precio Dual}_{R_2}$

|                              |                             |      |
| ---------------------------- | --------------------------- | ---- |
| $\textrm{Punto D} \to (4,0)$ | $x_1 + 2x_2 \to (4) + 2(0)$ | $4$  |
| $\textrm{Punto E} \to (0,6)$ | $x_1 + 2x_2 \to (0) + 2(6)$ | $12$ |


El precio dual calculado solo es valido mientras $R_2$ se mantenga entre estos valores.

$4 \leq \textrm{ R }_2 \leq 12$

---

La restricción que más afecta es $R_1$ por lo cual si queremos mejorar el punto óptimo, aumentar esta restricción maximizará el valor.

### Intervalo de optimalidad

El intervalo de optimalidad es el intervalo en el cual el punto óptimo se va a mantener al cambiar los valores de los coeficientes. Si la optimalidad se sale de este intervalo, entonces, el punto óptimo cambiará.

> Para $Z = C_1x_1+C_2x_2$ su optimalidad $O = \frac{C_1}{C_2}$
> 
> De $R_i \to c_{i_1}x_1 + c_{i_2}x_2 \leq C{i}$ obtenemos $L_i=\frac{c_{i_1}}{c_{i_2}}$
> 
> Entonces con  $L_i \leq L_j$, el intervalo de optimalidad es $L_i \leq O \leq L_j$


$Z = 5x_1 + 4x_2$ entonces $O = \frac{5}{4}$

$R_1 \to 6x_1 + 4x_2 \leq 24$ entonces $L_1=\frac{6}{4}=\frac{3}{2}$

$R_2 \to x_1 + 2x_2 \leq 6$ entonces $L_2=\frac{1}{2}$

El intervalo de optimalidad de la funcion objetivo es $L_2 \leq O \leq L_1 \to \frac{1}{2} \leq O \leq \frac{3}{2}$


## Método algebraico

$\textrm{Max} Z = 5x_1 + 4x_2$

$R_1 \to 6x_1 + 4x_2 + s_1 = 24$

$R_2 \to x_1 + 2x_2 + s_2 = 6$

| $V_{NB}$  | $V_B$     | Valores  | $PE$ | $Z=Z = 5x_1 + 4x_2$ | ¿Factible? |
| --------- | --------- | -------- | ---- | ------------------- | ---------- |
| $x_1,x_2$ | $s_1,s_2$ | $24,6$   | $A$  | $0$                 | Si         |
| $x_1,s_1$ | $x_2,s_2$ | $6,-6$   | $B$  | ---                 | No         |
| $x_1,s_2$ | $x_2,s_1$ | $3,12$   | $C$  | $12$                | Si         |
| $x_2,s_1$ | $x_1,s_2$ | $4,2$    | $D$  | $20$                | Si         |
| $x_2,s_2$ | $x_1,s_1$ | $6,-12$  | $E$  | ---                 | No         |
| $s_1,s_2$ | $x_1,x_2$ | $3, 1.5$ | $F$  | ==$21$==            | Si         |

---
### Obtener $\textrm{Precio Dual}_{R_1}$

$R_{1.a} = 6x_1 + 4x_2 = 28$

Recalculamos el punto óptimo obtenido con la nueva $R_1$

#### Punto $F$
$s_1,s_2=0$

$R_1 \to 6x_1 + 4x_2 + s_1 = 28$

$R_2 \to x_1 + 2x_2 + s_2 = 6$

$R_1 \to 6x_1 + 4x_2 + (0) = 28$

$R_2 \to x_1 + 2x_2 + (0) = 6$

$R_2 \to x_1 = 6 - 2x_2$

$R_1 \to 6(6 - 2x_2) + 4x_2 = 28$

$R_1 \to 36 - 12x_2 + 4x_2 = 28$

$R_1 \to - 8x_2 = 28 - 36$

$R_1 \to x_2 = \frac{-8}{-8} = 1$

$R_2 \to x_1 = 6 - 2(1) = 4$

En $x_1=4, x_2=1$ obtenemos el punto óptimo con $Z_B = 5(4) + 4(1)=24$

El resto del procedimiento, es igual al realizado con el método gráfico.

---
### Obtener $\textrm{Precio Dual}_{R_2}$

$R_{2.a}=x_1 + 2x_2=8$

Recalculamos el punto óptimo obtenido con la nueva $R_1$

#### Punto $F$
$s_1,s_2=0$

$R_1 \to 6x_1 + 4x_2 + s_1 = 24$

$R_2 \to x_1 + 2x_2 + s_2 = 8$

$R_1 \to 6x_1 + 4x_2 + (0) = 24$

$R_2 \to x_1 + 2x_2 + (0) = 8$

$R_2 \to x_1 = 8 - 2x_2$

$R_1 \to 6(8 - 2x_2) + 4x_2 = 24$

$R_1 \to 48 - 12x_2 + 4x_2 = 24$

$R_1 \to - 8x_2 = 24 - 48$

$R_1 \to x_2 = \frac{-24}{-8} = 3$

$R_2 \to x_1 = 8 - 2(3) = 2$

En $x_1=2, x_2=3$ obtenemos el punto óptimo con $Z_C = 5(2) + 4(3)=22$

El resto del procedimiento, es igual al realizado con el método gráfico.
