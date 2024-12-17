## (a) $\textrm{Maximizar} z = -5x_1 + 2x_2$ sujeto a

$-x_1 + x_2  \leq -2 \to x_1 - x_2  \geq 2$

$2x_1 + 3x_2 \leq 5$

$x_1,x_2 \geq 0$

### Ecuaciones del problema primal

$\textrm{Maximizar} z = -5x_1 + 2x_2 + 0x_3 + 0x_4$

$1x_1 - x_2 - x_3 + 0x_4 = 2$

$2x_1 + 3x_2 + 0x_3 + x_4 = 5$

$x_1, x_2, x_3, x_4 \geq 0$

### Problema dual y Restricciones duales

$\textrm{Minimizar} w = -2y_1 + 5y_2$

$1y_1 + 2y_2 \geq -5$

$-y_1 + 3y_2 \geq 2$

$\begin{rcases}
-y_1 + 0y_2 \geq 0 \to y_1 \leq 0 \\
\\
0y_1 + 1y_2 \geq 0 \to y_2 \geq 0 \\
\\
y_1, y_2 \textrm{ irrestricta} \\
\end{rcases}\to  y_1 \leq 0, y_2 \geq 0$

## (b) $\textrm{Minimizar} z = 6x_1 + 3x_2$ sujeto a

$6x_1 - 3x_2 + x_3  \geq 2$

$3x_1 + 4x_2 + x_3  \geq 5$

$x_1, x_2, x_3  \geq 0$

### Ecuaciones del problema primal

$\textrm{Minimizar} z = 6x_1 + 3x_2 + 0x_3 + 0x_4 + 0x_5$

$6x_1 - 3x_2 + x_3 - x_4 + 0x_5  = 2$

$3x_1 + 4x_2 + x_3 + 0x_4 - x_5  = 5$

$x_1, x_2, x_3, x_4, x_5  \geq 0$

### Problema dual y Restricciones duales

$\textrm{Maximizar} w = 2y_1 + 5y_2$

$6y_1 + 3y_2 \leq 6$

$-3y_1 + 4y_2 \leq 3$

$y_1 + y_2 \leq 0$

$\begin{rcases}
-y_1 \leq 0 \to y_1 \geq 0 \\
\\
-y_2 \leq 0 \to y_2 \geq 0 \\
\\
y_1, y_2 \textrm{ irrestricta} \\
\end{rcases}\to y_1, y_2 \geq 0$

## (c) $\textrm{Maximizar} z = x_1 + x_2$ sujeto a

$2x_1 + x_2 = 5$

$3x_1 - x_2 = 6$

$x_1, x_2 \textrm{ irrestricta}$


### Ecuaciones del problema primal

Las restricciones y funcion objetivo son iguales ya que no tenemos desigualdades, por ende no
hay holguras ni superhábits

### Problema dual y Restricciones duales

$\textrm{Minimizar} w = 5y_1 + 6y_2$

$2y_1 + 3y_2 \geq 1$

$y_1 - y_2 \geq 1$

$y_1, y_2 \textrm{ irrestricta}$

## Fuentes bibliograficas
Taha, H. A. (2012). Investigación de operaciones.