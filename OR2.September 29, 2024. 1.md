# a) Metodo M
Es utilizado cuando una ecuación $i$ no tiene holgura (o una variable que pueda dese,éñar el papel de una). Se agrega una variable artificial $R_i$, para formar una solución inicial parecida a la solución básica de total de holgura.

Las variables artificiales no forman parte del problema original, y se requiere un artificio de modelado para igualarlas a $0$ en el momento en que alcancen la iteración óptima (en caso que tenga una solución factible). La meta se logra penalizando estas variables en la función objetivo utilizando la siguiente regla: 
- Regla de penalización para variables artificiales. Dado $M$, un valor positivo suficientemente grande, donde $M \to \infty$, el coeficiente objetivo de una variable artificial representa una penalización adecuada sí:
  
$\textrm{Coeficiente objetivo de variable artificial } = \begin{cases}
    -M, \textrm{ para problemas de maximización}, \\
    M, \textrm{ para problemas de minimización}
\end{cases}$

### Funcion objetivo

$\textrm{Minimizar} = 4x_1 + x_2$

### Restricciones

$\textrm{Restriccion}_1 \to 3x_1 + x_2 = 3$

$\textrm{Restriccion}_2 \to 4x_1 + 3x_2 \geq 6$

$\textrm{Restriccion}_3 \to x_1 + 2x_2 \leq 4$

$\textrm{Restriccion}_4 \to x_1, x_2 >= 0$

### Ecuaciones

> Las ecuaciones sin holgura se le suma una variable artificial $R_i$

$Z - 4x_1 - x_2 - MR_1 - MR_2 = 0$

$\textrm{Restriccion}_1 \to 3x_1 + x_2 + R_1 = 3$

$\textrm{Restriccion}_2 \to 4x_1 + 3x_2 - S_2 + R_2 = 6$

$\textrm{Restriccion}_3 \to x_1 + 2x_2 + s_3 = 4$

Utilizaremos el valor de $M$ en $M=100$

$Z - 4x_1 - x_2 - 100R_1 - 100R_2 = 0$


### Comprobación de la función Z.
Considerando que las holguras son R_1, R_2 y s_3, estás son nuestras variables de entrada.

| $V_B$ | $Z$ | $x_1$ | $x_2$ | $S_2$ | $s_3$ | $R_1$  | $R_2$  | $Solución$ |
| ----- | --- | ----- | ----- | ----- | ----- | ------ | ------ | ---------- |
| $Z$   | $1$ | $-4$  | $-1$  | $0$   | $0$   | $-100$ | $-100$ | $0$        |
| $R_1$ | $0$ | $3$   | $1$   | $0$   | $0$   | $1$    | $0$    | $3$        |
| $R_2$ | $0$ | $4$   | $3$   | $-1$  | $0$   | $0$    | $1$    | $6$        |
| $s_3$ | $0$ | $1$   | $2$   | $0$   | $1$   | $0$    | $0$    | $4$        |

$Z = 0 \neq  4(0) + 1(0) + 100(3) + 100(4) = 900$

### Corregir Z

De $\textrm{Restriccion}_1 \to 3x_1 + x_2 + R_1 = 3$ :

$R_1 = - 3x_1 - x_2 + 3$

De $\textrm{Restriccion}_2 \to 4x_1 + 3x_2 - S_2 + R_2 = 6$

$R_2 = - 4x_1 - 3x_2 + S_2 + 6$

Sustituyendo en $Z - 4x_1 - 1x_2 - 100R_1 - 100R_2 = 0$

$Z - 4x_1 - x_2 - 100(-3x_1 - x_2 + 3) - 100(- 4x_1 - 3x_2 + S_2 + 6) = 0$

$Z - 4x_1 - x_2 + 300x_1 + 100x_2 - 300 + 400x_1 + 300x_2 - 100S_2 - 600 = 0$

$Z + 696x_1 + 399x_2  - 100S_2 = 900$

## Tabla inicial
| $V_B$ | $Z$ | $x_1$ | $x_2$ | $S_2$  | $s_3$ | $R_1$ | $R_2$ | $Solución$ |
| ----- | --- | ----- | ----- | ------ | ----- | ----- | ----- | ---------- |
| $Z$   | $1$ | $696$ | $399$ | $-100$ | $0$   | $0$   | $0$   | $900$      |
| $R_1$ | $0$ | $3$   | $1$   | $0$    | $0$   | $1$   | $0$   | $3$        |
| $R_2$ | $0$ | $4$   | $3$   | $-1$   | $0$   | $0$   | $1$   | $6$        |
| $s_3$ | $0$ | $1$   | $2$   | $0$    | $1$   | $0$   | $0$   | $4$        |


## Primera iteración

### $V_E$ y $V_P$

$V_E=x_1$

| $V_B$ | Columna $V_E$ | Columna $Solución$ | Relación mínima           | Válida |
| ----- | ------------- | ------------------ | ------------------------- | ------ |
| $R_1$ | $3$           | $3$                | $\frac{3}{3}=1$           | Sí     |
| $R_2$ | $4$           | $6$                | $\frac{6}{4}=\frac{3}{2}$ | Sí     |
| $s_3$ | $1$           | $4$                | $\frac{4}{1}=4$           | Sí     |

$V_P = R_1$

### Actualizar fila $V_P$

| $V_B$         | $Z$ | $x_1$           | $x_2$         | $S_2$ | $s_3$ | $R_1$         | $R_2$ | $Solución$      |
| ------------- | --- | --------------- | ------------- | ----- | ----- | ------------- | ----- | --------------- |
| $R_1 \to x_1$ | $0$ | $\frac{3}{3}=1$ | $\frac{1}{3}$ | $0$   | $0$   | $\frac{1}{3}$ | $0$   | $\frac{3}{3}=1$ |

| $V_B$ | $Z$ | $x_1$ | $x_2$         | $S_2$  | $s_3$ | $R_1$         | $R_2$ | $Solución$ |
| ----- | --- | ----- | ------------- | ------ | ----- | ------------- | ----- | ---------- |
| $Z$   | $1$ | $696$ | $399$         | $-100$ | $0$   | $0$           | $0$   | $900$      |
| $x_1$ | $0$ | $1$   | $\frac{1}{3}$ | $0$    | $0$   | $\frac{1}{3}$ | $0$   | $1$        |
| $R_2$ | $0$ | $4$   | $3$           | $-11$  | $0$   | $0$           | $1$   | $6$        |
| $s_3$ | $0$ | $1$   | $2$           | $0$    | $1$   | $0$           | $0$   | $4$        |

### Actualizar filas respecto a la fila $V_P$

#### Actualizar $Z$

| $V_B$              | $Z$ | $x_1$     | $x_2$         | $S_2$  | $s_3$ | $R_1$         | $R_2$ | $Solución$ |
| ------------------ | --- | --------- | ------------- | ------ | ----- | ------------- | ----- | ---------- |
| $Z$                | $1$ | ==$696$== | $399$         | $-100$ | $0$   | $0$           | $0$   | $900$      |
| $x_1$              | $0$ | $1$       | $\frac{1}{3}$ | $0$    | $0$   | $\frac{1}{3}$ | $0$   | $1$        |
| $-696x_1$          | $0$ | $-696$    | $-232$        | $0$    | $0$   | $-232$        | $0$   | $-696$     |
| $Z \to Z - 696x_1$ | $1$ | $0$       | $167$         | $-100$ | $0$   | $-232$        | $0$   | $204$      |

#### Actualizar $R_2$

| $V_B$                | $Z$ | $x_1$   | $x_2$          | $S_2$ | $s_3$ | $R_1$          | $R_2$ | $Solución$ |
| -------------------- | --- | ------- | -------------- | ----- | ----- | -------------- | ----- | ---------- |
| $R_2$                | $0$ | ==$4$== | $3$            | $-1$  | $0$   | $0$            | $1$   | $6$        |
| $x_1$                | $0$ | $1$     | $\frac{1}{3}$  | $0$   | $0$   | $\frac{1}{3}$  | $0$   | $1$        |
| $-4x_1$              | $0$ | $-4$    | $\frac{-4}{3}$ | $0$   | $0$   | $\frac{-4}{3}$ | $0$   | $-4$       |
| $R_2 \to R_2 - 4x_1$ | $0$ | $0$     | $\frac{5}{3}$  | $-1$  | $0$   | $\frac{-4}{3}$ | $1$   | $2$        |

#### Actualizar $s_3$

| $V_B$                | $Z$ | $x_1$   | $x_2$          | $S_2$ | $s_3$ | $R_1$          | $R_2$ | $Solución$ |
| -------------------- | --- | ------- | -------------- | ----- | ----- | -------------- | ----- | ---------- |
| $s_3$                | $0$ | ==$1$== | $2$            | $0$   | $1$   | $0$            | $0$   | $4$        |
| $x_1$                | $0$ | $1$     | $\frac{1}{3}$  | $0$   | $0$   | $\frac{1}{3}$  | $0$   | $1$        |
| $-1x_1$              | $0$ | $-1$    | $\frac{-1}{3}$ | $0$   | $0$   | $\frac{-1}{3}$ | $0$   | $-1$       |
| $s_3 \to s_3 - 1x_1$ | $0$ | $0$     | $\frac{5}{3}$  | $0$   | $1$   | $\frac{-1}{3}$ | $0$   | $3$        |

### Actualizar tabla con filas actualizadas

| $V_B$ | $Z$ | $x_1$ | $x_2$         | $S_2$  | $s_3$ | $R_1$          | $R_2$ | $Solución$ |
| ----- | --- | ----- | ------------- | ------ | ----- | -------------- | ----- | ---------- |
| $Z$   | $1$ | $0$   | $167$         | $-100$ | $0$   | $-232$         | $0$   | $204$      |
| $x_1$ | $0$ | $1$   | $\frac{1}{3}$ | $0$    | $0$   | $\frac{1}{3}$  | $0$   | $1$        |
| $R_2$ | $0$ | $0$   | $\frac{5}{3}$ | $-1$   | $0$   | $\frac{-4}{3}$ | $1$   | $2$        |
| $s_3$ | $0$ | $0$   | $\frac{5}{3}$ | $0$    | $1$   | $\frac{-1}{3}$ | $0$   | $3$        |

## Segunda iteración

### $V_E$ y $V_P$

$V_E=x_2$

| $V_B$ | Columna $V_E$ | Columna $Solución$ | Relación mínima                         | Válida |
| ----- | ------------- | ------------------ | --------------------------------------- | ------ |
| $x_1$ | $\frac{1}{3}$ | $1$                | $\frac{1}{\frac{1}{3}}=3$               | Sí     |
| $R_2$ | $\frac{5}{3}$ | $2$                | ==$\frac{2}{\frac{5}{3}}=\frac{6}{5}$== | Sí     |
| $s_3$ | $\frac{5}{3}$ | $3$                | $\frac{3}{\frac{5}{3}}=\frac{9}{5}$     | Sí     |

$V_P = R_2$

### Actualizar fila $V_P$

| $V_B$         | $Z$ | $x_1$ | $x_2$                               | $S_2$                                 | $s_3$ | $R_1$                                           | $R_2$                               | $Solución$                          |
| ------------- | --- | ----- | ----------------------------------- | ------------------------------------- | ----- | ----------------------------------------------- | ----------------------------------- | ----------------------------------- |
| $R_2 \to x_2$ | $0$ | $0$   | $\frac{\frac{5}{3}}{\frac{5}{3}}=1$ | $\frac{-1}{\frac{5}{3}}=\frac{-3}{5}$ | $0$   | $\frac{\frac{-4}{3}}{\frac{5}{3}}=\frac{-4}{5}$ | $\frac{1}{\frac{5}{3}}=\frac{3}{5}$ | $\frac{2}{\frac{5}{3}}=\frac{6}{5}$ |

| $V_B$ | $Z$ | $x_1$ | $x_2$         | $S_2$          | $s_3$ | $R_1$          | $R_2$         | $Solución$    |
| ----- | --- | ----- | ------------- | -------------- | ----- | -------------- | ------------- | ------------- |
| $Z$   | $1$ | $0$   | $167$         | $-100$         | $0$   | $-232$         | $0$           | $204$         |
| $x_1$ | $0$ | $1$   | $\frac{1}{3}$ | $0$            | $0$   | $\frac{1}{3}$  | $0$           | $1$           |
| $x_2$ | $0$ | $0$   | $1$           | $\frac{-3}{5}$ | $0$   | $\frac{-4}{5}$ | $\frac{3}{5}$ | $\frac{6}{5}$ |
| $s_3$ | $0$ | $0$   | $\frac{5}{3}$ | $0$            | $1$   | $\frac{-1}{3}$ | $0$           | $3$           |

### Actualizar filas respecto a la fila $V_P$

#### Actualizar $Z$

| $V_B$              | $Z$ | $x_1$ | $x_2$     | $S_2$           | $s_3$ | $R_1$            | $R_2$            | $Solución$        |
| ------------------ | --- | ----- | --------- | --------------- | ----- | ---------------- | ---------------- | ----------------- |
| $Z$                | $1$ | $0$   | ==$167$== | $-100$          | $0$   | $-232$           | $0$              | $204$             |
| $x_2$              | $0$ | $0$   | $1$       | $\frac{-3}{5}$  | $0$   | $\frac{-4}{5}$   | $\frac{3}{5}$    | $\frac{6}{5}$     |
| $-167x_2$          | $0$ | $0$   | $-167$    | $\frac{501}{5}$ | $0$   | $\frac{668}{5}$  | $\frac{-501}{5}$ | $\frac{-1002}{5}$ |
| $Z \to Z - 167x_2$ | $1$ | $0$   | $0$       | $\frac{1}{5}$   | $0$   | $\frac{-492}{5}$ | $\frac{-501}{5}$ | $\frac{18}{5}$    |

#### Actualizar $x_1$

| $V_B$                          | $Z$ | $x_1$ | $x_2$             | $S_2$          | $s_3$ | $R_1$          | $R_2$          | $Solución$     |
| ------------------------------ | --- | ----- | ----------------- | -------------- | ----- | -------------- | -------------- | -------------- |
| $x_1$                          | $0$ | $1$   | ==$\frac{1}{3}$== | $0$            | $0$   | $\frac{1}{3}$  | $0$            | $1$            |
| $x_2$                          | $0$ | $0$   | $1$               | $\frac{-3}{5}$ | $0$   | $\frac{-4}{5}$ | $\frac{3}{5}$  | $\frac{6}{5}$  |
| $-\frac{1}{3}x_2$              | $0$ | $0$   | $\frac{-1}{3}$    | $\frac{1}{5}$  | $0$   | $\frac{4}{15}$ | $\frac{-1}{5}$ | $\frac{-2}{5}$ |
| $x_1 \to x_1 - \frac{1}{3}x_2$ | $0$ | $1$   | $0$               | $\frac{1}{5}$  | $0$   | $\frac{3}{5}$  | $\frac{-1}{5}$ | $\frac{3}{5}$  |

#### Actualizar $s_3$

| $V_B$               | $Z$ | $x_1$ | $x_2$             | $S_2$          | $s_3$ | $R_1$          | $R_2$         | $Solución$    |
| ------------------- | --- | ----- | ----------------- | -------------- | ----- | -------------- | ------------- | ------------- |
| $s_3$               | $0$ | $0$   | ==$\frac{5}{3}$== | $0$            | $1$   | $\frac{-1}{3}$ | $0$           | $3$           |
| $x_2$               | $0$ | $0$   | $1$               | $\frac{-3}{5}$ | $0$   | $\frac{-4}{5}$ | $\frac{3}{5}$ | $\frac{6}{5}$ |
| $-\frac{5}{3}x_2$   | $0$ | $0$   | $\frac{-5}{3}$    | $1$            | $0$   | $\frac{4}{3}$  | $-1$          | $-2$          |
| $s_3 \to s_3 - x_2$ | $0$ | $0$   | $0$               | $1$            | $1$   | $1$            | $-1$          | $1$           |


### Actualizar tabla con filas actualizadas

| $V_B$ | $Z$ | $x_1$ | $x_2$ | $S_2$          | $s_3$ | $R_1$            | $R_2$            | $Solución$     |
| ----- | --- | ----- | ----- | -------------- | ----- | ---------------- | ---------------- | -------------- |
| $Z$   | $1$ | $0$   | $0$   | $\frac{1}{5}$  | $0$   | $\frac{-492}{5}$ | $\frac{-501}{5}$ | $\frac{18}{5}$ |
| $x_1$ | $0$ | $1$   | $0$   | $\frac{1}{5}$  | $0$   | $\frac{3}{5}$    | $\frac{-1}{5}$   | $\frac{3}{5}$  |
| $x_2$ | $0$ | $0$   | $1$   | $\frac{-3}{5}$ | $0$   | $\frac{-4}{5}$   | $\frac{3}{5}$    | $\frac{6}{5}$  |
| $s_3$ | $0$ | $0$   | $0$   | $1$            | $1$   | $1$              | $-1$             | $1$            |

## Tercera iteración

### $V_E$ y $V_P$

$V_E = S_2$

| $V_B$ | Columna $V_E$  | Columna $Solución$ | Relación mínima                       | Válida |
| ----- | -------------- | ------------------ | ------------------------------------- | ------ |
| $x_1$ | $\frac{1}{5}$  | $\frac{3}{5}$      | $\frac{\frac{3}{5}}{\frac{1}{5}} = 3$ | Sí     |
| $x_2$ | $\frac{-3}{5}$ | $\frac{6}{5}$      | $\frac{\frac{6}{5}}{\frac{-3}{5}}$    | No     |
| $s_3$ | $1$            | $1$                | ==$\frac{1}{1} = 1$==                 | Sí     |

$V_P = s_3$

### Actualizar fila $V_P$

| $V_B$         | $Z$ | $x_1$ | $x_2$ | $S_2$ | $s_3$ | $R_1$ | $R_2$ | $Solución$ |
| ------------- | --- | ----- | ----- | ----- | ----- | ----- | ----- | ---------- |
| $s_3 \to S_2$ | $0$ | $0$   | $0$   | $1$   | $1$   | $1$   | $-1$  | $1$        |

| $V_B$ | $Z$ | $x_1$ | $x_2$ | $S_2$          | $s_3$ | $R_1$            | $R_2$            | $Solución$     |
| ----- | --- | ----- | ----- | -------------- | ----- | ---------------- | ---------------- | -------------- |
| $Z$   | $1$ | $0$   | $0$   | $\frac{1}{5}$  | $0$   | $\frac{-492}{5}$ | $\frac{-501}{5}$ | $\frac{18}{5}$ |
| $x_1$ | $0$ | $1$   | $0$   | $\frac{1}{5}$  | $0$   | $\frac{3}{5}$    | $\frac{-1}{5}$   | $\frac{3}{5}$  |
| $x_2$ | $0$ | $0$   | $1$   | $\frac{-3}{5}$ | $0$   | $\frac{-4}{5}$   | $\frac{3}{5}$    | $\frac{6}{5}$  |
| $S_2$ | $0$ | $0$   | $0$   | $1$            | $1$   | $1$              | $-1$             | $1$            |

### Actualizar filas respecto a la fila $V_P$

#### Actualizar $Z$

| $V_B$                      | $Z$ | $x_1$ | $x_2$ | $S_2$             | $s_3$          | $R_1$            | $R_2$            | $Solución$     |
| -------------------------- | --- | ----- | ----- | ----------------- | -------------- | ---------------- | ---------------- | -------------- |
| $Z$                        | $1$ | $0$   | $0$   | ==$\frac{1}{5}$== | $0$            | $\frac{-492}{5}$ | $\frac{-501}{5}$ | $\frac{18}{5}$ |
| $S_2$                      | $0$ | $0$   | $0$   | $1$               | $1$            | $1$              | $-1$             | $1$            |
| $\frac{-1}{5}S_2$          | $0$ | $0$   | $0$   | $\frac{-1}{5}$    | $\frac{-1}{5}$ | $\frac{-1}{5}$   | $\frac{1}{5}$    | $\frac{-1}{5}$ |
| $Z \to Z - \frac{1}{5}S_2$ | $1$ | $0$   | $0$   | $0$               | $0$            | $\frac{-493}{5}$ | $-100$           | $\frac{17}{5}$ |

#### Actualizar $x_1$

| $V_B$                          | $Z$ | $x_1$ | $x_2$ | $S_2$             | $s_3$          | $R_1$          | $R_2$          | $Solución$     |
| ------------------------------ | --- | ----- | ----- | ----------------- | -------------- | -------------- | -------------- | -------------- |
| $x_1$                          | $0$ | $1$   | $0$   | ==$\frac{1}{5}$== | $0$            | $\frac{3}{5}$  | $\frac{-1}{5}$ | $\frac{3}{5}$  |
| $S_2$                          | $0$ | $0$   | $0$   | $1$               | $1$            | $1$            | $-1$           | $1$            |
| $\frac{-1}{5}S_2$              | $0$ | $0$   | $0$   | $\frac{-1}{5}$    | $\frac{-1}{5}$ | $\frac{-1}{5}$ | $\frac{1}{5}$  | $\frac{-1}{5}$ |
| $x_1 \to x_1 - \frac{1}{5}S_2$ | $0$ | $1$   | $0$   | $0$               | $\frac{-1}{5}$ | $\frac{2}{5}$  | $0$            | $\frac{2}{5}$  |

#### Actualizar $x_2$

| $V_B$                          | $Z$ | $x_1$ | $x_2$ | $S_2$              | $s_3$         | $R_1$          | $R_2$          | $Solución$    |
| ------------------------------ | --- | ----- | ----- | ------------------ | ------------- | -------------- | -------------- | ------------- |
| $x_2$                          | $0$ | $0$   | $1$   | ==$\frac{-3}{5}$== | $0$           | $\frac{-4}{5}$ | $\frac{3}{5}$  | $\frac{6}{5}$ |
| $S_2$                          | $0$ | $0$   | $0$   | $1$                | $1$           | $1$            | $-1$           | $1$           |
| $\frac{3}{5}S_2$               | $0$ | $0$   | $0$   | $\frac{3}{5}$      | $\frac{3}{5}$ | $\frac{3}{5}$  | $\frac{-3}{5}$ | $\frac{3}{5}$ |
| $x_2 \to x_2 + \frac{3}{5}S_2$ | $0$ | $0$   | $1$   | $0$                | $\frac{3}{5}$ | $\frac{-1}{5}$ | $0$            | $\frac{3}{5}$ |

### Actualizar tabla con filas actualizadas

| $V_B$ | $Z$ | $x_1$ | $x_2$ | $S_2$ | $s_3$          | $R_1$            | $R_2$  | $Solución$     |
| ----- | --- | ----- | ----- | ----- | -------------- | ---------------- | ------ | -------------- |
| $Z$   | $1$ | $0$   | $0$   | $0$   | $0$            | $\frac{-493}{5}$ | $-100$ | $\frac{17}{5}$ |
| $x_1$ | $0$ | $1$   | $0$   | $0$   | $\frac{-1}{5}$ | $\frac{2}{5}$    | $0$    | $\frac{2}{5}$  |
| $x_2$ | $0$ | $0$   | $1$   | $0$   | $\frac{3}{5}$  | $\frac{-1}{5}$   | $0$    | $\frac{3}{5}$  |
| $S_2$ | $0$ | $0$   | $0$   | $1$   | $1$            | $1$              | $-1$   | $1$            |

> Esta es la tabla final


# b) Método de 2 fases

En el método M, el uso de la penalización puede conducir a errores de redondeo.

El método de 2 fases, elimina el uso de la constante M. En la fase 1 se trata de encontrar la solución factible básica inicial, y si se encuentra una se invoca la fase 2.

### Funcion objetivo

$\textrm{Minimizar} = 4x_1 + x_2$

### Restricciones

$\textrm{Restriccion}_1 \to 3x_1 + x_2 = 3$

$\textrm{Restriccion}_2 \to 4x_1 + 3x_2 \geq 6$

$\textrm{Restriccion}_3 \to x_1 + 2x_2 \leq 4$

$\textrm{Restriccion}_4 \to x_1, x_2 >= 0$

### Ecuaciones

> La holgura se suma, el superhabit se resta

$\textrm{Restriccion}_1 \to 3x_1 + x_2 + R_1 = 3$

$\textrm{Restriccion}_2 \to 4x_1 + 3x_2 - S_2 + R_2 = 6$

$\textrm{Restriccion}_3 \to x_1 + 2x_2 + s_3 = 4$

$\textrm{Restriccion}_4 \to x_1, x_2, R_1, R_2, S_2, s_3 >= 0$

## Fase 1
Ponga el problema en forma de ecuación y agregue las variables artificiales necesarias en las restricciones. A continuación, determine una solución básica de la ecuación resultante que siempre minimice la suma de las variables artificiales independientemente si el problema es para maximizar o minimizar. Si el valor mínimo de la suma es positivo, el problema no tiene solución factible; si el valor mínimo es 0, prosiga con la fase 2.

> 1. Definir las ecuaciones
> 2. Minimizar la sumatoria de las variables artificiales

### Definición del problema

$Min r = R_1 + R_2$

$r - R_1 - R_2 = 0$

$\textrm{Restriccion}_1 \to 3x_1 + x_2 + R_1 = 3$

$\textrm{Restriccion}_2 \to 4x_1 + 3x_2 - S_2 + R_2 = 6$

$\textrm{Restriccion}_3 \to x_1 + 2x_2 + s_3 = 4$

### Tabla inicial

| $V_B$ | $r$ | $x_1$ | $x_2$ | $S_2$ | $s_3$ | $R_1$ | $R_2$ | $Solución$ |
| ----- | --- | ----- | ----- | ----- | ----- | ----- | ----- | ---------- |
| $r$   | $1$ | $0$   | $0$   | $0$   | $0$   | $-1$  | $-1$  | $0$        |
| $R_1$ | $0$ | $3$   | $1$   | $0$   | $0$   | $1$   | $0$   | $3$        |
| $R_2$ | $0$ | $4$   | $3$   | $-1$  | $0$   | $0$   | $1$   | $6$        |
| $s_3$ | $0$ | $1$   | $2$   | $0$   | $1$   | $0$   | $0$   | $4$        |

### Corregir r
Se suman $r+R_1+R_2$ para convertir r a 0.

$\textrm{Nueva fila }r \to \text{Fila actual }r+C_1R_1+C_2R_2$

Donde $C_1$ es el coeficiente que anula el valor de la fila $r$ en la columna $R_1$ 
y $C_2$ es el coeficiente que anula el valor de la fila $r$ en la columna $R_2$.

| $V_B$               | $r$ | $x_1$ | $x_2$ | $S_2$ | $s_3$ | $R_1$ | $R_2$ | $Solución$ |
| ------------------- | --- | ----- | ----- | ----- | ----- | ----- | ----- | ---------- |
| $r$                 | $1$ | $0$   | $0$   | $0$   | $0$   | $-1$  | $-1$  | $0$        |
| $R_1$               | $0$ | $3$   | $1$   | $0$   | $0$   | $1$   | $0$   | $3$        |
| $R_2$               | $0$ | $4$   | $3$   | $-1$  | $0$   | $0$   | $1$   | $6$        |
| $r \to r+1R_1+1R_2$ | $1$ | $7$   | $4$   | $-1$  | $0$   | $0$   | $0$   | $9$        |

### Tabla inicial

| $V_B$ | $r$ | $x_1$ | $x_2$ | $S_2$ | $s_3$ | $R_1$ | $R_2$ | $Solución$ |
| ----- | --- | ----- | ----- | ----- | ----- | ----- | ----- | ---------- |
| $r$   | $1$ | $7$   | $4$   | $-1$  | $0$   | $0$   | $0$   | $9$        |
| $R_1$ | $0$ | $3$   | $1$   | $0$   | $0$   | $1$   | $0$   | $3$        |
| $R_2$ | $0$ | $4$   | $3$   | $-1$  | $0$   | $0$   | $1$   | $6$        |
| $s_3$ | $0$ | $1$   | $2$   | $0$   | $1$   | $0$   | $0$   | $4$        |

### Primera iteración

#### $V_E$ y $V_P$

$V_E=x_1$

| $V_B$ | Columna $V_E$ | Columna $Solución$ | Relación mínima           | Válida |
| ----- | ------------- | ------------------ | ------------------------- | ------ |
| $R_1$ | $3$           | $3$                | ==$\frac{3}{3}=1$==       | Sí     |
| $R_2$ | $4$           | $6$                | $\frac{6}{4}=\frac{3}{2}$ | Sí     |
| $s_3$ | $1$           | $4$                | $\frac{4}{1}=4$           | Sí     |

$V_P = R_1$

#### Actualizar fila $V_P$

| $V_B$         | $r$ | $x_1$           | $x_2$         | $S_2$ | $s_3$ | $R_1$         | $R_2$ | $Solución$      |
| ------------- | --- | --------------- | ------------- | ----- | ----- | ------------- | ----- | --------------- |
| $R_1 \to x_1$ | $0$ | $\frac{3}{3}=1$ | $\frac{1}{3}$ | $0$   | $0$   | $\frac{1}{3}$ | $0$   | $\frac{3}{3}=1$ |

| $V_B$ | $r$ | $x_1$ | $x_2$         | $S_2$ | $s_3$ | $R_1$         | $R_2$ | $Solución$ |
| ----- | --- | ----- | ------------- | ----- | ----- | ------------- | ----- | ---------- |
| $r$   | $1$ | $7$   | $4$           | $-1$  | $0$   | $0$           | $0$   | $9$        |
| $x_1$ | $0$ | $1$   | $\frac{1}{3}$ | $0$   | $0$   | $\frac{1}{3}$ | $0$   | $1$        |
| $R_2$ | $0$ | $4$   | $3$           | $-11$ | $0$   | $0$           | $1$   | $6$        |
| $s_3$ | $0$ | $1$   | $2$           | $0$   | $1$   | $0$           | $0$   | $4$        |

#### Actualizar filas respecto a la fila $V_P$

##### Actualizar $r$

| $V_B$            | $r$ | $x_1$   | $x_2$          | $S_2$ | $s_3$ | $R_1$          | $R_2$ | $Solución$ |
| ---------------- | --- | ------- | -------------- | ----- | ----- | -------------- | ----- | ---------- |
| $r$              | $1$ | ==$7$== | $4$            | $-1$  | $0$   | $0$            | $0$   | $9$        |
| $x_1$            | $0$ | $1$     | $\frac{1}{3}$  | $0$   | $0$   | $\frac{1}{3}$  | $0$   | $1$        |
| $-7x_1$          | $0$ | $-7$    | $\frac{-7}{3}$ | $0$   | $0$   | $\frac{-7}{3}$ | $0$   | $-7$       |
| $r \to r - 7x_1$ | $1$ | $0$     | $\frac{5}{3}$  | $-1$  | $0$   | $\frac{-7}{3}$ | $0$   | $2$        |

##### Actualizar $R_2$

| $V_B$                | $r$ | $x_1$   | $x_2$          | $S_2$ | $s_3$ | $R_1$          | $R_2$ | $Solución$ |
| -------------------- | --- | ------- | -------------- | ----- | ----- | -------------- | ----- | ---------- |
| $R_2$                | $0$ | ==$4$== | $3$            | $-1$  | $0$   | $0$            | $1$   | $6$        |
| $x_1$                | $0$ | $1$     | $\frac{1}{3}$  | $0$   | $0$   | $\frac{1}{3}$  | $0$   | $1$        |
| $-4x_1$              | $0$ | $-4$    | $\frac{-4}{3}$ | $0$   | $0$   | $\frac{-4}{3}$ | $0$   | $-4$       |
| $R_2 \to R_2 - 4x_1$ | $0$ | $0$     | $\frac{5}{3}$  | $-1$  | $0$   | $\frac{-4}{3}$ | $1$   | $2$        |

##### Actualizar $s_3$

| $V_B$                | $r$ | $x_1$   | $x_2$          | $S_2$ | $s_3$ | $R_1$          | $R_2$ | $Solución$ |
| -------------------- | --- | ------- | -------------- | ----- | ----- | -------------- | ----- | ---------- |
| $s_3$                | $0$ | ==$1$== | $2$            | $0$   | $1$   | $0$            | $0$   | $4$        |
| $x_1$                | $0$ | $1$     | $\frac{1}{3}$  | $0$   | $0$   | $\frac{1}{3}$  | $0$   | $1$        |
| $-1x_1$              | $0$ | $-1$    | $\frac{-1}{3}$ | $0$   | $0$   | $\frac{-1}{3}$ | $0$   | $-1$       |
| $s_3 \to s_3 - 1x_1$ | $0$ | $0$     | $\frac{5}{3}$  | $0$   | $1$   | $\frac{-1}{3}$ | $0$   | $3$        |

#### Actualizar tabla con filas actualizadas

| $V_B$ | $R$ | $x_1$ | $x_2$         | $S_2$ | $s_3$ | $R_1$          | $R_2$ | $Solución$ |
| ----- | --- | ----- | ------------- | ----- | ----- | -------------- | ----- | ---------- |
| $r$   | $1$ | $0$   | $\frac{5}{3}$ | $-1$  | $0$   | $\frac{-7}{3}$ | $0$   | $2$        |
| $x_1$ | $0$ | $1$   | $\frac{1}{3}$ | $0$   | $0$   | $\frac{1}{3}$  | $0$   | $1$        |
| $R_2$ | $0$ | $0$   | $\frac{5}{3}$ | $-1$  | $0$   | $\frac{-4}{3}$ | $1$   | $2$        |
| $s_3$ | $0$ | $0$   | $\frac{5}{3}$ | $0$   | $1$   | $\frac{-1}{3}$ | $0$   | $3$        |

### Segunda iteración

#### $V_E$ y $V_P$

$V_E=x_2$

| $V_B$ | Columna $V_E$ | Columna $Solución$ | Relación mínima                         | Válida |
| ----- | ------------- | ------------------ | --------------------------------------- | ------ |
| $x_1$ | $\frac{1}{3}$ | $1$                | $\frac{1}{\frac{1}{3}}=3$               | Sí     |
| $R_2$ | $\frac{5}{3}$ | $2$                | ==$\frac{2}{\frac{5}{3}}=\frac{6}{5}$== | Sí     |
| $s_3$ | $\frac{5}{3}$ | $3$                | $\frac{3}{\frac{5}{3}}=\frac{9}{5}$     | Sí     |

$V_P = R_2$

#### Actualizar fila $V_P$

| $V_B$         | $r$ | $x_1$ | $x_2$                               | $S_2$                                 | $s_3$ | $R_1$                                           | $R_2$                               | $Solución$                          |
| ------------- | --- | ----- | ----------------------------------- | ------------------------------------- | ----- | ----------------------------------------------- | ----------------------------------- | ----------------------------------- |
| $R_2 \to x_2$ | $0$ | $0$   | $\frac{\frac{5}{3}}{\frac{5}{3}}=1$ | $\frac{-1}{\frac{5}{3}}=\frac{-3}{5}$ | $0$   | $\frac{\frac{-4}{3}}{\frac{5}{3}}=\frac{-4}{5}$ | $\frac{1}{\frac{5}{3}}=\frac{3}{5}$ | $\frac{2}{\frac{5}{3}}=\frac{6}{5}$ |

| $V_B$ | $r$ | $x_1$ | $x_2$         | $S_2$          | $s_3$ | $R_1$          | $R_2$         | $Solución$    |
| ----- | --- | ----- | ------------- | -------------- | ----- | -------------- | ------------- | ------------- |
| $r$   | $1$ | $0$   | $\frac{5}{3}$ | $-1$           | $0$   | $\frac{-7}{3}$ | $0$           | $2$           |
| $x_1$ | $0$ | $1$   | $\frac{1}{3}$ | $0$            | $0$   | $\frac{1}{3}$  | $0$           | $1$           |
| $x_2$ | $0$ | $0$   | $1$           | $\frac{-3}{5}$ | $0$   | $\frac{-4}{5}$ | $\frac{3}{5}$ | $\frac{6}{5}$ |
| $s_3$ | $0$ | $0$   | $\frac{5}{3}$ | $0$            | $1$   | $\frac{-1}{3}$ | $0$           | $3$           |

#### Actualizar filas respecto a la fila $V_P$

##### Actualizar $r$

| $V_B$                      | $r$ | $x_1$ | $x_2$             | $S_2$          | $s_3$ | $R_1$          | $R_2$         | $Solución$    |
| -------------------------- | --- | ----- | ----------------- | -------------- | ----- | -------------- | ------------- | ------------- |
| $r$                        | $1$ | $0$   | ==$\frac{5}{3}$== | $-1$           | $0$   | $\frac{-7}{3}$ | $0$           | $2$           |
| $x_2$                      | $0$ | $0$   | $1$               | $\frac{-3}{5}$ | $0$   | $\frac{-4}{5}$ | $\frac{3}{5}$ | $\frac{6}{5}$ |
| $-\frac{5}{3}x_2$          | $0$ | $0$   | $-\frac{5}{3}$    | $1$            | $0$   | $\frac{4}{3}$  | $-1$          | $-2$          |
| $r \to r - \frac{5}{3}x_2$ | $1$ | $0$   | $0$               | $0$            | $0$   | $-1$           | $-1$          | $0$           |

##### Actualizar $x_1$

| $V_B$                          | $r$ | $x_1$ | $x_2$             | $S_2$          | $s_3$ | $R_1$          | $R_2$          | $Solución$     |
| ------------------------------ | --- | ----- | ----------------- | -------------- | ----- | -------------- | -------------- | -------------- |
| $x_1$                          | $0$ | $1$   | ==$\frac{1}{3}$== | $0$            | $0$   | $\frac{1}{3}$  | $0$            | $1$            |
| $x_2$                          | $0$ | $0$   | $1$               | $\frac{-3}{5}$ | $0$   | $\frac{-4}{5}$ | $\frac{3}{5}$  | $\frac{6}{5}$  |
| $-\frac{1}{3}x_2$              | $0$ | $0$   | $\frac{-1}{3}$    | $\frac{1}{5}$  | $0$   | $\frac{4}{15}$ | $\frac{-1}{5}$ | $\frac{-2}{5}$ |
| $x_1 \to x_1 - \frac{1}{3}x_2$ | $0$ | $1$   | $0$               | $\frac{1}{5}$  | $0$   | $\frac{3}{5}$  | $\frac{-1}{5}$ | $\frac{3}{5}$  |

##### Actualizar $s_3$

| $V_B$               | $r$ | $x_1$ | $x_2$             | $S_2$          | $s_3$ | $R_1$          | $R_2$         | $Solución$    |
| ------------------- | --- | ----- | ----------------- | -------------- | ----- | -------------- | ------------- | ------------- |
| $s_3$               | $0$ | $0$   | ==$\frac{5}{3}$== | $0$            | $1$   | $\frac{-1}{3}$ | $0$           | $3$           |
| $x_2$               | $0$ | $0$   | $1$               | $\frac{-3}{5}$ | $0$   | $\frac{-4}{5}$ | $\frac{3}{5}$ | $\frac{6}{5}$ |
| $-\frac{5}{3}x_2$   | $0$ | $0$   | $\frac{-5}{3}$    | $1$            | $0$   | $\frac{4}{3}$  | $-1$          | $-2$          |
| $s_3 \to s_3 - x_2$ | $0$ | $0$   | $0$               | $1$            | $1$   | $1$            | $-1$          | $1$           |


#### Actualizar tabla con filas actualizadas

| $V_B$ | $r$ | $x_1$ | $x_2$ | $S_2$          | $s_3$ | $R_1$          | $R_2$          | $Solución$    |
| ----- | --- | ----- | ----- | -------------- | ----- | -------------- | -------------- | ------------- |
| $r$   | $1$ | $0$   | $0$   | $0$            | $0$   | $-1$           | $-1$           | $0$           |
| $x_1$ | $0$ | $1$   | $0$   | $\frac{1}{5}$  | $0$   | $\frac{3}{5}$  | $\frac{-1}{5}$ | $\frac{3}{5}$ |
| $x_2$ | $0$ | $0$   | $1$   | $\frac{-3}{5}$ | $0$   | $\frac{-4}{5}$ | $\frac{3}{5}$  | $\frac{6}{5}$ |
| $s_3$ | $0$ | $0$   | $0$   | $1$            | $1$   | $1$            | $-1$           | $1$           |

> Como la solución de $r$ nos da $0$. Significa que el problema si tiene solución factible
> y podemos proseguir a la fase 2

## Fase 2

Use la solución factible de la fase 1 como una solución factible básica inicial
del problema original. Como las variables artificiales ya cumplieron su misión,
se rpocede a eliminar las columnas y se escribe el problema original.

> Eliminar columnas $R_1$ y $R_2$. Ya no será parte de la solución.


### Definición del problema

$\textrm{Minimizar} Z = 4x_1 + x_2$

$\textrm{Restriccion}_1 \to 1x_1 + \frac{1}{5}S_2 = \frac{3}{5}$

$\textrm{Restriccion}_2 \to 1x_2 - \frac{3}{5}S_2 = \frac{6}{5}$

$\textrm{Restriccion}_3 \to 1S_2 + 1s_3 = 1$

| $V_B$ | $Z$ | $x_1$ | $x_2$ | $S_2$          | $s_3$ | $Solución$    |
| ----- | --- | ----- | ----- | -------------- | ----- | ------------- |
| $Z$   | $1$ | $-4$  | $-1$  | $0$            | $0$   | $0$           |
| $x_1$ | $0$ | $1$   | $0$   | $\frac{1}{5}$  | $0$   | $\frac{3}{5}$ |
| $x_2$ | $0$ | $0$   | $1$   | $\frac{-3}{5}$ | $0$   | $\frac{6}{5}$ |
| $s_3$ | $0$ | $0$   | $0$   | $1$            | $1$   | $1$           |

> La fila Z no es congruente a la solución, así que corregiremos Z.

### Corregir Z
Se suman $Z+x_1+x_2$ para convertir Z a 0.

$\textrm{Nueva fila }Z \to \text{Fila actual }Z+C_1x_1+C_2x_2$

Donde $C_1$ es el coeficiente que anula el valor de la fila $Z$ en la columna $x_1$ 
y $C_2$ es el coeficiente que anula el valor de la fila $Z$ en la columna $x_2$.

| $V_B$             | $Z$ | $x_1$ | $x_2$ | $S_2$          | $s_3$ | $Solución$     |
| ----------------- | --- | ----- | ----- | -------------- | ----- | -------------- |
| $Z$               | $1$ | $-4$  | $-1$  | $0$            | $0$   | $0$            |
| $4x_1$            | $0$ | $4$   | $0$   | $\frac{4}{5}$  | $0$   | $\frac{12}{5}$ |
| $1x_2$            | $0$ | $0$   | $1$   | $\frac{-3}{5}$ | $0$   | $\frac{6}{5}$  |
| $Z \to Z+x_1+x_2$ | $1$ | $0$   | $0$   | $\frac{1}{5}$  | $0$   | $\frac{18}{5}$ |

### Tabla inicial

| $V_B$ | $Z$ | $x_1$ | $x_2$ | $S_2$          | $s_3$ | $Solución$     |
| ----- | --- | ----- | ----- | -------------- | ----- | -------------- |
| $Z$   | $1$ | $0$   | $0$   | $\frac{1}{5}$  | $0$   | $\frac{18}{5}$ |
| $x_1$ | $0$ | $1$   | $0$   | $\frac{1}{5}$  | $0$   | $\frac{3}{5}$  |
| $x_2$ | $0$ | $0$   | $1$   | $\frac{-3}{5}$ | $0$   | $\frac{6}{5}$  |
| $s_3$ | $0$ | $0$   | $0$   | $1$            | $1$   | $1$            |

### Primera iteración

#### $V_E$ y $V_P$

$V_E=S_2$

| $V_B$ | Columna $V_E$  | Columna $Solución$ | Relación mínima                     | Válida |
| ----- | -------------- | ------------------ | ----------------------------------- | ------ |
| $x_1$ | $\frac{1}{5}$  | $\frac{3}{5}$      | $\frac{\frac{3}{5}}{\frac{1}{5}}=3$ | Sí     |
| $x_2$ | $\frac{-3}{5}$ | $\frac{6}{5}$      | $\frac{\frac{6}{5}}{\frac{-3}{5}}$  | No     |
| $s_3$ | $1$            | $1$                | ==$\frac{1}{1}=1$==                 | Sí     |

$V_P = s_3$

#### Actualizar fila $V_P$

| $V_B$         | $Z$ | $x_1$ | $x_2$ | $S_2$ | $s_3$ | $Solución$ |
| ------------- | --- | ----- | ----- | ----- | ----- | ---------- |
| $s_3 \to S_2$ | $0$ | $0$   | $0$   | $1$   | $1$   | $1$        |

| $V_B$ | $Z$ | $x_1$ | $x_2$ | $S_2$          | $s_3$ | $Solución$     |
| ----- | --- | ----- | ----- | -------------- | ----- | -------------- |
| $Z$   | $1$ | $0$   | $0$   | $\frac{1}{5}$  | $0$   | $\frac{18}{5}$ |
| $x_1$ | $0$ | $1$   | $0$   | $\frac{1}{5}$  | $0$   | $\frac{3}{5}$  |
| $x_2$ | $0$ | $0$   | $1$   | $\frac{-3}{5}$ | $0$   | $\frac{6}{5}$  |
| $S_2$ | $0$ | $0$   | $0$   | $1$            | $1$   | $1$            |

#### Actualizar filas respecto a la fila $V_P$

##### Actualizar $Z$

| $V_B$                      | $Z$ | $x_1$ | $x_2$ | $S_2$          | $s_3$          | $Solución$     |
| -------------------------- | --- | ----- | ----- | -------------- | -------------- | -------------- |
| $Z$                        | $1$ | $0$   | $0$   | $\frac{1}{5}$  | $0$            | $\frac{18}{5}$ |
| $S_2$                      | $0$ | $0$   | $0$   | $1$            | $1$            | $1$            |
| $-\frac{1}{5}S_2$          | $0$ | $0$   | $0$   | $\frac{-1}{5}$ | $\frac{-1}{5}$ | $\frac{-1}{5}$ |
| $Z \to Z - \frac{1}{5}S_2$ | $1$ | $0$   | $0$   | $0$            | $\frac{-1}{5}$ | $\frac{17}{5}$ |

##### Actualizar $x_1$

| $V_B$               | $Z$ | $x_1$ | $x_2$ | $S_2$             | $s_3$          | $Solución$     |
| ------------------- | --- | ----- | ----- | ----------------- | -------------- | -------------- |
| $x_1$               | $0$ | $1$   | $0$   | ==$\frac{1}{5}$== | $0$            | $\frac{3}{5}$  |
| $S_2$               | $0$ | $0$   | $0$   | $1$               | $1$            | $1$            |
| $-\frac{1}{5}S_2$   | $0$ | $0$   | $0$   | $\frac{-1}{5}$    | $\frac{-1}{5}$ | $\frac{-1}{5}$ |
| $x_1 \to x_1 - S_2$ | $0$ | $1$   | $0$   | $0$               | $\frac{-1}{5}$ | $\frac{2}{5}$  |

##### Actualizar $x_2$

| $V_B$                          | $Z$ | $x_1$ | $x_2$ | $S_2$              | $s_3$         | $Solución$    |
| ------------------------------ | --- | ----- | ----- | ------------------ | ------------- | ------------- |
| $x_2$                          | $0$ | $0$   | $1$   | ==$\frac{-3}{5}$== | $0$           | $\frac{6}{5}$ |
| $S_2$                          | $0$ | $0$   | $0$   | $1$                | $1$           | $1$           |
| $\frac{3}{5}S_2$               | $0$ | $0$   | $0$   | $\frac{3}{5}$      | $\frac{3}{5}$ | $\frac{3}{5}$ |
| $x_2 \to x_2 + \frac{3}{5}S_2$ | $0$ | $0$   | $1$   | $0$                | $\frac{3}{5}$ | $\frac{9}{5}$ |

#### Actualizar tabla con filas actualizadas

| $V_B$ | $Z$ | $x_1$ | $x_2$ | $S_2$ | $s_3$          | $Solución$     |
| ----- | --- | ----- | ----- | ----- | -------------- | -------------- |
| $Z$   | $1$ | $0$   | $0$   | $0$   | $\frac{-1}{5}$ | $\frac{17}{5}$ |
| $x_1$ | $0$ | $1$   | $0$   | $0$   | $-1$           | $\frac{2}{5}$  |
| $x_2$ | $0$ | $0$   | $1$   | $0$   | $\frac{3}{5}$  | $\frac{9}{5}$  |
| $S_2$ | $0$ | $0$   | $0$   | $1$   | $1$            | $1$            |


# c) ¿Cuál método utilizar?

Ambos métodos son extensos, sin embargo el método realizado por el método M implica realizar solamente 1 ocasión el método Simplex, mientras que el método de 2 fases implica realizarlo en 2 ocasiones. Por esto mismo creo que es preferible el método M, no obstante, puede ser preocupante cometer un error en la elección arbitraria de M, ocasionando que el problema no sea resolvible, o llegar a una resolución incorrecta.