# 🐍 Clase 03 - Tipos de datos primitivos

## 🧠 1. Definición Conceptual

<aside>
💡

En Python, **cada valor tiene un tipo de dato** que indica qué tipo de información representa y qué operaciones se pueden realizar con él. Cuando asignamos un valor a una variable, **Python automáticamente determina su tipo** según el valor asignado.

</aside>

### 🔹 Principales tipos de datos básicos:

| Tipo | Descripción | Ejemplo |
| --- | --- | --- |
| `int` | Números enteros (positivos, negativos o cero) | `10`, `-3`, `0` |
| `float` | Números decimales (de punto flotante) | `3.14`, `-0.5`, `2.0` |
| `str` | Cadenas de texto (se escriben entre comillas) | `"Hola"`, `'Python'` |
| `bool` | Valores lógicos (booleanos) | `True`, `False` |

---

## 🧩 2. Ejemplos básicos de comprensión

### 🧱 Ejemplo 1 — Identificar tipos de datos con `type()`

```python
a = 10
b = 3.14
c = "Hola mundo"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
```

> La función `type()` devuelve el tipo de dato de cada variable.
> 

---

### 🧱 Ejemplo 2 — Comprobación con `isinstance()`

```python
x ="Python"
print(isinstance(x,str))# True
print(isinstance(x,int))# False
```

> `isinstance(variable, tipo)` devuelve `True` si la variable pertenece al tipo indicado.
> 

---

### 🧱 Ejemplo 3 — Inferencia automática de tipo

```python
edad = 25
precio = 19.99
nombre = "Ana"
activo = False

print(edad,type(edad))
print(precio,type(precio))
print(nombre,type(nombre))
print(activo,type(activo))
```

> Python **infiere automáticamente** el tipo de dato al asignar un valor a la variable.
> 

---

## ⚙️ 3. Ejercicios prácticos

### 🔸 Ejercicio 1 — Evaluar expresiones mixtas

```python
a = 10
b = 2.5
c = a + b
print(c,type(c))
```

> Al sumar un `int` y un `float`, Python convierte automáticamente el resultado en `float`.
> 

---

### 🔸 Ejercicio 2 — Conversión entre tipos

```python
x = 3.99
y = int(x)
print(y,type(y))
```

> La función `int()` convierte un número decimal en entero **truncando la parte decimal**.
> 

---

### 🔸 Ejercicio 3 — Evaluar cadenas y números

```python
texto = "123"
numero = int(texto)
print(numero + 7)
```

> Se puede convertir una cadena numérica a entero con `int()`, siempre que contenga solo dígitos.
> 

---

### 🔸 Ejercicio 4 — Evaluar booleanos en expresiones

```python
a = True
b = False
print(a + b)
print(a * 10)
```

> En operaciones numéricas, `True` se interpreta como `1` y `False` como `0`.
> 

---

---

## 🚀 4. Ejercicios propuestos

> ✏️ Escribe tu código en las celdas vacías y luego compara tu salida con la esperada.
> 

---

### 🧮 Ejercicio 4.1 — Evaluar tipos en una expresión compleja

**Enunciado:**

Evalúa la siguiente expresión y determina qué tipo de dato obtiene Python:

```python
resultado = (10 +2.5) *3 /2
```

```python
# Escribe tu código aquí
```

**Salida esperada:**

```
Resultado:18.75
Tipo: <class'float'>
```

---

### 🧮 Ejercicio 4.2 — Identificar tipo tras conversión de texto a número

**Enunciado:**

Convierte la cadena `"45.67"` a un número y verifica su tipo.

```python
# Escribe tu código aquí
```

**Salida esperada:**

```
Valor : 45.67
Tipo: <class'float'>
```

---

### 🧮 Ejercicio 3 — Determinar tipos en una expresión lógica

**Enunciado:**

Evalúa la expresión `5 > 3 and 2 < 8` y muestra su tipo.

```python
# Escribe tu código aquí
```

**Salida esperada:**

```
Resultado:True
Tipo: <class'bool'>
```

---

## Parte 2 Conversión de tipos

### 🔹 Tipos de datos comunes en Python

| Tipo | Ejemplo | Descripción |
| --- | --- | --- |
| `int` | `10` | Número entero |
| `float` | `3.14` | Número decimal |
| `str` | `"Hola"` | Cadena de texto |
| `bool` | `True`, `False` | Valor lógico |
| `list` | `[1, 2, 3]` | Colección ordenada y modificable |

Podemos cambiar un tipo de dato a otro mediante funciones integradas:

```python
int("45")     # Convierte cadena a entero → 45
float("3.14") # Convierte cadena a flotante → 3.14
str(100)      # Convierte número a texto → "100"
list("Hola")  # Convierte texto a lista de caracteres → ['H', 'o', 'l', 'a']
```

---

## 2️⃣ Ejemplos básicos de comprensión (genéricos)

### 🔸 Ejemplo 1: Conversión de tipos

```python
a = "25"
b = 5
resultado = int(a) + b
print(resultado)
```

> 📘 Convertimos `a` (cadena) a entero antes de sumarla con `b`.
> 

---

### 🔸 Ejemplo 2: Indexación y slicing

```python
texto = "Python"
print(texto[0]) # Primer carácter
print(texto[-1]) # Último carácter
print(texto[0:3]) # Desde índice 0 hasta antes del 3 → 'Pyt'
```

> 📘 Python indexa desde `0`. Los negativos cuentan desde el final.
> 

---

### 🔸 Ejemplo 3: Crear y acceder a listas

```python
numeros = [10,20,30,40]
print(numeros[1]) # Acceso al segundo elemento
print(numeros[-2]) # Penúltimo elemento
```

---

### 🔸 Ejemplo 4: Modificar listas

```python
colores = ["rojo","azul","verde"]
colores[1] = "amarillo"
print(colores)
```

> 📘 **Salida esperada:** `['rojo', 'amarillo', 'verde']`
> 

---

### 🔸 Ejemplo 5: Operaciones básicas con listas

```python
lista = [5,1,9,3,7]
print(max(lista)) # Máximo → 9
print(min(lista)) # Mínimo → 1
lista.sort()
print(lista)      # Orden ascendente
lista.reverse()
print(lista)      # Lista invertida
```

---

## 3️⃣ Ejercicios prácticos

### 🧮 Ejemplo 1: Fusión de listas

```python
nombres = ["Ana","Luis","Sofía"]
edades = [20,22,19]
fusion = nombres + edades
print(fusion)
```

> 📘 El operador `+` concatena listas.
> 

---

### 🧮 Ejemplo 2: Agregar e insertar elementos

```python
frutas = ["manzana","pera"]
frutas.append("naranja")       # Agrega al final
frutas.insert(1,"plátano")     # Inserta en posición 1
print(frutas)
```

---

### 🧮 Ejemplo 3: Eliminar elementos

```python
animales = ["gato","perro","loro","pez"]
animales.remove("loro")                        # Elimina por valor
del animales[0]                                # Elimina por índice
print(animales)
```

---

### 🧮 Ejemplo 4: División (slicing)

```python
numeros = [10,20,30,40,50,60]
print(numeros[:3])              # Primeros 3
print(numeros[3:])              # Desde el 4to al final
```

---

### 🧮 Ejemplo 5: Comparación de listas

```python
a = [1,2,3]
b = [1,2,3]
print(a == b)     # True (elementos iguales)
print(a is b)      # False (objetos distintos)
```

---

## 4️⃣ Ejercicios aplicados a contextos reales

### 📊 Contexto: Notas de estudiantes

### Ejercicio 1

**Enunciado:** Dada la lista de notas de un grupo, encuentra la nota máxima, mínima y el promedio.

```python
notas = [8.5,7.2,9.0,6.8,10,7.9]
# Escribe aquí tu solución
```

**Salida esperada:**

```
Máxima: 10
Mínima: 6.8
Promedio: 8.23
```

---

### Ejercicio 2

**Enunciado:** Ordena las notas de menor a mayor y luego invierte el orden.

```python
notas = [8.5,7.2,9.0,6.8,10,7.9]
# Escribe aquí tu solución
```

**Salida esperada:**

```
Ordenascendente:[6.8, 7.2, 7.9, 8.5, 9.0, 10]
Ordendescendente:[10, 9.0, 8.5, 7.9, 7.2, 6.8]
```

---

### 🛒 Contexto: Inventario de tienda

### Ejercicio 3

**Enunciado:** Crea una lista de productos y precios. Agrega un nuevo producto y elimina otro.

```python
productos = ["leche","pan","queso","café"]
precios = [1.5,1.0,3.2,2.8]
# Escribe aquí tu solución
```

**Salida esperada:**

```
Inventario actualizado:
['leche','pan','café','miel']
[1.5, 1.0, 2.8, 4.0]
```

---

### 💵 Contexto: Análisis de precios

### Ejercicio 4

**Enunciado:** Dada una lista de precios, encuentra el precio más alto y el más bajo, y calcula la diferencia.

```python
precios = [23.5,19.9,45.0,32.2,27.5]
# Escribe aquí tu solución
```

**Salida esperada:**

```
Máximo: 45.0
Mínimo: 19.9
Diferencia: 25.1
```

---

### 🧍 Contexto: Datos de usuarios

### Ejercicio 5

**Enunciado:** Combina las listas de nombres y edades para formar una lista única de pares.

```python
nombres = ["Ana","Luis","Sofía"]
edades = [20,22,19]
# Escribe aquí tu solución
```

**Salida esperada:**

```
[["Ana", 20],["Luis", 22],["Sofía", 19]]
```

---