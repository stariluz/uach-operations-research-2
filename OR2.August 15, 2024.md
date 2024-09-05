5. Restricted optimization criteria
6. Linealizsation methods for problems with restrictions.
7. Generalization of direction methods based on linealization.
8. Integer programming

### Course Rules
1. In case that the student can't present an exam or present a work of the subject, in the established date, must advice to the Professor and present an official document expelled by the Academic Secretary, which justifies the ausence.
2. In case of plagiary, same works are pondered as zero. And the student must present the extraordinary exam of the course.

### Weightings
1. First Partial 30%
2. First Partial 30%
3. First Partial 40%

- Test 50%
- **Tasks** 50%

It is required the 80% of attendance.
For the extraordinary it is required the 60% of attendance

# Repaso
Redimix produce pintura para interiores y exteriores con 2 materias primas $M1$, $M2$.
Una encuesta de mercado indica que la demanda diaria de pintura para interiores
no puede exceder la de pintura para exteriores en mas de una tonelada. Asi mismo,
que la demanda diaria máxima de pinturas para interiores es de 2 toneladas.

Redimix se propone determinar la mejor combinación óptima de pinturas para interiores y exteriores que maximice la utilidad diaria total.

|                       | Pintura exterior | Pintura interior | Demanda diaria |
| --------------------- | ---------------- | ---------------- | -------------- |
| $MP_1$                | 6                | 4                | 24             |
| $MP_2$                | 1                | 2                | 6              |
| Utilidad por tonelada | 5                | 4                |                |


## Metodo gráfico
Definición del problema
1. Variables
   
   $x_1 \to P_e$ $x_2 \to P_i$ 

2. Función objetivo
   
   $\textrm{Max} Z = 5x_1 + 4x_2$

3. Restricciones
   
   $R_1 \to 6x_1 + 4x_2 \leq 24$

   $R_2 \to x_1 + 2x_2 \leq 6$

   $R_3 \to x_2 - x_1 \leq 1$

   $R_4 \to x_2 \leq 2$

   $R_5 \to x_1,x_2 \geq 0$

### $R_1$
Si $x_1=0$, entonces $x_2=6$

Si $x_2=0$, entonces $x_1=4$

### $R_2$
Si $x_1=0$, entonces $x_2=3$

Si $x_2=0$, entonces $x_1=6$

### $R_3$
Si $x_1=0$, entonces $x_2=1$

Si $x_2=0$, entonces $x_1=-1$

### $R_4$
$x_2=2$

![Grafico](./img/OR2.August%2015,%202024.img%201.png)

### Puntos esquina
| $PE$ | $x_1, x_2$ | $Z$  |
| ---- | ---------- | ---- |
| $A$  | $0, 0$     | $0$  |
| $B$  | $0, 1$     | $4$  |
| $C$  | $1, 2$     | $13$ |
| $D$  | $2, 2$     | $18$ |
| $E$  | $3, 15$    | $21$ |
| $F$  | $4, 0 $    | $20$ |

## Método algebraico
$C_n=\frac{n!}{m(n-m)!}$

$n$ es el número de ecuciones.

$m$ es el número de variables.

### Ecuaciones

$R_1 \to 6x_1 + 4x_2 + s_1 = 24$

$R_2 \to x_1 + 2x_2 + s_2 = 6$

> Por cuestiones de tiempo no usamos $R_3$ ni $R_4$
> 
> $R_3 \to x_2 - x_1 + s_3 = 1$
> 
> $R_4 \to x_2 + s_4 = 2$

$n=4$

$m=2$

$C_n=\frac{4!}{2(4-2)!}=6$

### Analisis
| $V_{NB}$  | $V_B$     | Valores  | $PE$ | $Z=Z = 5x_1 + 4x_2$ | ¿Factible? |
| --------- | --------- | -------- | ---- | ------------------- | ---------- |
| $x_1,x_2$ | $s_1,s_2$ | $24,6$   | $A$  | $0$                 | Si         |
| $x_1,s_1$ | $x_2,s_2$ | $6,-6$   | $B$  | ---                 | No         |
| $x_1,s_2$ | $x_2,s_1$ | $3,12$   | $C$  | $12$                | Si         |
| $x_2,s_1$ | $x_1,s_2$ | $4,2$    | $D$  | $20$                | Si         |
| $x_2,s_2$ | $x_1,s_1$ | $6,-12$  | $E$  | ---                 | No         |
| $s_1,s_2$ | $x_1,x_2$ | $3, 1.5$ | $F$  | ==$21$==            | Si         |

#### $A$
$x_1,x_2=0$

$R_1 \to 6x_1 + 4x_2 + s_1 = 24$

$R_1 \to 6(0) + 4(0) + s_1 = 24$

$R_1 \to s_1 = 24$

$R_2 \to x_1 + 2x_2 + s_2 = 6$

$R_2 \to (0) + 2(0) + s_2 = 6$

$R_2 \to s_2 = 6$

#### $B$
$x_1,s_1=0$

$R_1 \to 6x_1 + 4x_2 + s_1 = 24$

$R_1 \to 6(0) + 4x_2 + (0) = 24$

$R_1 \to x_2 = \frac{24}{4} = 6$

$R_2 \to x_1 + 2x_2 + s_2 = 6$

$R_2 \to (0) + 2(6) + s_2 = 6$

$R_2 \to s_2 = 6 - 12 = -6$

#### $C$
$x_1,s_2=0$

$R_1 \to 6x_1 + 4x_2 + s_1 = 24$

$R_2 \to x_1 + 2x_2 + s_2 = 6$

$R_2 \to (0) + 2x_2 + (0) = 6$

$R_2 \to x_2 = \frac{6}{2} = 3$

$R_1 \to 6(0) + 4(3) + s_1 = 24$

$R_1 \to s_1 = 24 - 12 = 12$

#### $D$
$x_2,s_1=0$

$R_1 \to 6x_1 + 4x_2 + s_1 = 24$

$R_1 \to 6x_1 + 4(0) + (0) = 24$

$R_1 \to x_1 = \frac{24}{6} = 4$

$R_2 \to x_1 + 2x_2 + s_2 = 6$

$R_2 \to (4) + 2(0) + s_2 = 6$

$R_2 \to  s_2 = 6 - 4 = 2$

#### $E$
$x_2,s_2=0$

$R_1 \to 6x_1 + 4x_2 + s_1 = 24$

$R_2 \to x_1 + 2x_2 + s_2 = 6$

$R_2 \to x_1 + 2(0) + (0) = 6$

$R_2 \to x_1 = 6$

$R_1 \to 6(6) + 4(0) + s_1 = 24$

$R_1 \to s_1 = 24 - 36 = -12$

#### $F$
$s_1,s_2=0$

$R_1 \to 6x_1 + 4x_2 + s_1 = 24$

$R_2 \to x_1 + 2x_2 + s_2 = 6$

$R_1 \to 6x_1 + 4x_2 + (0) = 24$

$R_2 \to x_1 + 2x_2 + (0) = 6$

$R_2 \to x_1 = 6 - 2x_2$

$R_1 \to 6(6 - 2x_2) + 4x_2 = 24$

$R_1 \to 36 - 12x_2 + 4x_2 = 24$

$R_1 \to - 8x_2 = 24 - 36$

$R_1 \to x_2 = \frac{-12}{-8} = 1.5$

$R_2 \to x_1 = 6 - 2(1.5) = 3$

## Método SIMPLEX

### Ecuaciones

$Z - 5x_1 - 4x_2 =0$

$R_1 \to 6x_1 + 4x_2 + s_1 = 24$

$R_2 \to x_1 + 2x_2 + s_2 = 6$

| Variables básicas | $Z$ | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $Solucion$ |
| ----------------- | --- | ----- | ----- | ----- | ----- | ---------- |
| $Z$               | $1$ | $-5$  | $-4$  | $0$   | $0$   | $0$        |
| $s_1$             | $0$ | $6$   | $4$   | $1$   | $0$   | $24$       |
| $s_2$             | $0$ | $1$   | $2$   | $0$   | $1$   | $6$        |

## Primera iteración

### Seleccionar variable de entrada ($V_E$)

> ¿Qué variable de mi función $Z$ afecta más a mi modelo?

$V_E=x_1$

| Variables básicas | Columna $V_E$ | Columna $Solución$ | Relación mínima      | Válida |
| ----------------- | ------------- | ------------------ | -------------------- | ------ |
| $s_1$             | $6$           | $24$               | ==$\frac{24}{6}=4$== | Sí     |
| $s_2$             | $1$           | $6$                | s$\frac{6}{1}=6$     | Sí     |

$s_1$ es nuestra variable pivote ($V_P$)

### Actualizar la fila de la variable pivote ($V_P$)
Sustituímos $V_P$ por $V_E$ en la columna $V_B$. Es decir $s_1$ por $x_1$, esto indica que nuestra fila pivote $V_P$ ahora se llamá $x_1$


| Variables básicas | $Z$ | $x_1$         | $x_2$                     | $s_1$         | $s_2$         | $Solucion$       |
| ----------------- | --- | ------------- | ------------------------- | ------------- | ------------- | ---------------- |
| $s_1 \to x_1$     | $0$ | $\frac{6}{6}$ | $\frac{4}{6}=\frac{2}{3}$ | $\frac{1}{6}$ | $\frac{0}{6}$ | $\frac{24}{6}=4$ |

| Variables básicas | $Z$ | $x_1$ | $x_2$         | $s_1$         | $s_2$ | $Solucion$ |
| ----------------- | --- | ----- | ------------- | ------------- | ----- | ---------- |
| $Z$               | $1$ | $-5$  | $-4$          | $0$           | $0$   | $0$        |
| $x_1$             | $0$ | $1$   | $\frac{2}{3}$ | $\frac{1}{6}$ | $0$   | $4$        |
| $s_2$             | $0$ | $1$   | $2$           | $0$           | $1$   | $6$        |

### Actualizar las demás filas respecto a la fila pivote
> Para todas las filas $M_i$: <br>
> $M_i = M_i -  M_{i,V_E} \cdot M_{V_P}$

#### Actualizar $Z$

| Variables básicas | $Z$ | $x_1$    | $x_2$           | $s_1$          | $s_2$ | $Solucion$ |
| ----------------- | --- | -------- | --------------- | -------------- | ----- | ---------- |
| $Z$               | $1$ | ==$-5$== | $-4$            | $0$            | $0$   | $0$        |
| $x_1$             | $0$ | $1$      | $\frac{2}{3}$   | $\frac{1}{6}$  | $0$   | $4$        |
| $-5(x_1)$         | $0$ | $-5$     | $\frac{-10}{3}$ | $\frac{-5}{6}$ | $0$   | $-20$      |
| $Z=Z-(-5x_1)$     | $1$ | $0$      | $\frac{-2}{3}$  | $\frac{5}{6}$  | $0$   | $20$       |

#### Actualizar $s_2$

| Variables básicas | $Z$ | $x_1$   | $x_2$         | $s_1$          | $s_2$ | $Solucion$ |
| ----------------- | --- | ------- | ------------- | -------------- | ----- | ---------- |
| $s_2$             | $0$ | ==$1$== | $2$           | $0$            | $1$   | $6$        |
| $x_1$             | $0$ | $1$     | $\frac{2}{3}$ | $\frac{1}{6}$  | $0$   | $4$        |
| $1(x_1)$          | $0$ | $1$     | $\frac{2}{3}$ | $\frac{1}{6}$  | $0$   | $4$        |
| $s_2=s_2-x_1$     | $0$ | $0$     | $\frac{4}{3}$ | $\frac{-1}{6}$ | $1$   | $2$        |

### Actualizar tabla con las filas actualizadas

| Variables básicas | $Z$ | $x_1$ | $x_2$          | $s_1$          | $s_2$ | $Solucion$ |
| ----------------- | --- | ----- | -------------- | -------------- | ----- | ---------- |
| $Z$               | $1$ | $0$   | $\frac{-2}{3}$ | $\frac{5}{6}$  | $0$   | $20$       |
| $x_1$             | $0$ | $1$   | $\frac{2}{3}$  | $\frac{1}{6}$  | $0$   | $4$        |
| $s_2$             | $0$ | $0$   | $\frac{4}{3}$  | $\frac{-1}{6}$ | $1$   | $2$        |

## Segunda iteración

### Seleccionar variable de entrada ($V_E$)

$V_E=x_2$

| Variables básicas | Columna $V_E$ | Columna $Solución$ | Relación mínima                                      | Válida |
| ----------------- | ------------- | ------------------ | ---------------------------------------------------- | ------ |
| $x_1$             | $\frac{2}{3}$ | $4$                | $\frac{4}{\frac{2}{3}}=\frac{12}{2}$=6               | Sí     |
| $s_2$             | $\frac{4}{3}$ | $2$                | ==s$\frac{2}{\frac{4}{3}}=\frac{6}{4}=\frac{3}{2}==$ | Sí     |

$s_2$ es nuestra variable pivote ($V_P$)

### Actualizar la fila de la variable pivote ($V_P$)
Sustituímos $V_P$ por $V_E$ en la columna $V_B$. Es decir $s_2$ por $x_2$, esto indica que nuestra fila pivote $V_P$ ahora se llama $x_2$


| Variables básicas | $Z$ | $x_1$ | $x_2$                                 | $s_1$                                           | $s_2$                               | $Solucion$                                      |
| ----------------- | --- | ----- | ------------------------------------- | ----------------------------------------------- | ----------------------------------- | ----------------------------------------------- |
| $s_2$             | $0$ | $0$   | $==\frac{4}{3}==$                     | $\frac{-1}{6}$                                  | $1$                                 | $2$                                             |
| $s_2 \to x_2$     | $0$ | $0$   | ${\frac{\frac{4}{3}}{\frac{4}{3}}}=1$ | $\frac{\frac{-1}{6}}{\frac{4}{3}}=\frac{-1}{8}$ | $\frac{1}{\frac{4}{3}}=\frac{3}{4}$ | $\frac{2}{\frac{4}{3}}=\frac{6}{4}=\frac{3}{2}$ |

| Variables básicas | $Z$ | $x_1$ | $x_2$          | $s_1$          | $s_2$         | $Solucion$    |
| ----------------- | --- | ----- | -------------- | -------------- | ------------- | ------------- |
| $Z$               | $1$ | $0$   | $\frac{-2}{3}$ | $\frac{5}{6}$  | $0$           | $20$          |
| $x_1$             | $0$ | $1$   | $\frac{2}{3}$  | $\frac{1}{6}$  | $0$           | $4$           |
| $x_2$             | $0$ | $0$   | $1$            | $\frac{-1}{8}$ | $\frac{3}{4}$ | $\frac{3}{2}$ |

### Actualizar las demás filas respecto a la fila pivote
> Para todas las filas $M_i$: <br>
> $M_i = M_i -  M_{i,V_E} \cdot M_{V_P}$

#### Actualizar $Z$

| Variables básicas           | $Z$ | $x_1$ | $x_2$              | $s_1$          | $s_2$          | $Solucion$    |
| --------------------------- | --- | ----- | ------------------ | -------------- | -------------- | ------------- |
| $Z$                         | $1$ | $0$   | $==\frac{-2}{3}==$ | $\frac{5}{6}$  | $0$            | $20$          |
| $x_2$                       | $0$ | $0$   | $1$                | $\frac{-1}{8}$ | $\frac{3}{4}$  | $\frac{3}{2}$ |
| $\frac{-2}{3}x_2$           | $0$ | $0$   | $\frac{-2}{3}$     | $\frac{1}{12}$ | $\frac{-1}{2}$ | $-1$          |
| $Z = Z - (\frac{-2}{3}x_2)$ | $1$ | $0$   | $0$                | $\frac{3}{4}$  | $\frac{1}{2}$  | $21$          |

#### Actualizar $x_1$

| Variables básicas            | $Z$ | $x_1$ | $x_2$             | $s_1$           | $s_2$          | $Solucion$    |
| ---------------------------- | --- | ----- | ----------------- | --------------- | -------------- | ------------- |
| $x_1$                        | $0$ | $1$   | ==$\frac{2}{3}$== | $\frac{1}{6}$   | $0$            | $4$           |
| $x_2$                        | $0$ | $0$   | $1$               | $\frac{-1}{8}$  | $\frac{3}{4}$  | $\frac{3}{2}$ |
| $\frac{2}{3}x_2$             | $0$ | $0$   | $\frac{2}{3}$     | $\frac{-1}{12}$ | $\frac{1}{2}$  | $1$           |
| $x_1 = x_1 - \frac{2}{3}x_2$ | $0$ | $1$   | $0$               | $\frac{1}{4}$   | $\frac{-1}{2}$ | $3$           |

### Actualizar tabla con las filas actualizadas

| Variables básicas | $Z$ | $x_1$ | $x_2$ | $s_1$          | $s_2$          | $Solucion$    |
| ----------------- | --- | ----- | ----- | -------------- | -------------- | ------------- |
| $Z$               | $1$ | $0$   | $0$   | $\frac{3}{4}$  | $\frac{1}{2}$  | ==$21$==      |
| $x_1$             | $0$ | $1$   | $0$   | $\frac{1}{4}$  | $\frac{-1}{2}$ | $3$           |
| $x_2$             | $0$ | $0$   | $1$   | $\frac{-1}{8}$ | $\frac{3}{4}$  | $\frac{3}{2}$ |

Volvemos a preguntar **¿Qué variable de mi función $Z$ afecta más a mi modelo?** Dado que actualmente, todas las variables para *Z* son nulas, o positivas, las variables ya no tienen impacto en el modelo. Esto quiere decir que encontramos nuestro punto óptimo.

$\textrm{Punto}_c(3\frac{3}{2}, \frac{3}{2}) \to Z=21$