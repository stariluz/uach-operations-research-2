from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Crear el problema
problem = LpProblem("Venta_de_Manzanas", LpMaximize)

# Variables de decisión
x1 = LpVariable("x1", lowBound=0, cat="Integer")
y1 = LpVariable("y1", lowBound=0, cat="Integer")
x2 = LpVariable("x2", lowBound=0, cat="Integer")
y2 = LpVariable("y2", lowBound=0, cat="Integer")
x3 = LpVariable("x3", lowBound=0, cat="Integer")
y3 = LpVariable("y3", lowBound=0, cat="Integer")

# Restricciones de venta total de manzanas
problem += 7 * x1 + y1 == 50, "Manzanas_Karen"
problem += 7 * x2 + y2 == 30, "Manzanas_Bill"
problem += 7 * x3 + y3 == 10, "Manzanas_John"

# Restricción de igual ingreso para todos
income = x1 + 3 * y1
problem += x2 + 3 * y2 == income, "Ingreso_igual_1"
problem += x3 + 3 * y3 == income, "Ingreso_igual_2"

# Maximizar ingresos
problem += income, "Maximizar_Ingresos"

# Resolver el problema
problem.solve()

# Mostrar resultados
print("Estado:", problem.status)
print("Ingreso de cada hijo: $", income.value())
print(f"Karen: paquetes={x1.value()}, individuales={y1.value()}")
print(f"Bill: paquetes={x2.value()}, individuales={y2.value()}")
print(f"John: paquetes={x3.value()}, individuales={y3.value()}")
