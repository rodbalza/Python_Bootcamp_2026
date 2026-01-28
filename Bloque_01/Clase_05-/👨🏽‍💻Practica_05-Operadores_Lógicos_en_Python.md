# 👨🏽‍💻Practica 05 - Operadores Lógicos en Python

<aside>
💡

# Instrucciones

**Entregar los ejercicios en uno o varios archivos.py**

</aside>

# 🧠 Conversión con bool()

<aside>
💡

## 💼 Ejercicios 2.1 y 2.2 de la clase 5.

</aside>

# 🧠 Operadores Lógicos

<aside>
💡

## 🚀 5.1 ¿ Es un buen día para salir ?

Crea un programa que reciba:

- una temperatura (en °C),
- un valor booleano que indique si hay lluvia (`True` o `False`), y muestre si **“Es un buen día para salir”** (solo si la temperatura está entre 20 y 30 y no está lloviendo).

💡 ***Pista:***  Usa `and`, `not` y comparaciones numéricas. **No usar if.**

</aside>

---

<aside>
💡

## 💼 5.2  🏦 Validación de transacciones bancarias.

Una fintech necesita validar si una transacción es **segura**:

- El monto debe ser **menor o igual a 10,000**.
- El país debe ser “México”, “Colombia” o “Chile”.
- El usuario debe haber confirmado la operación (`True`).

**Instrucciones:**

1. Pide los tres datos al usuario.
2. Usa operadores lógicos para evaluar la condición.
3. Muestra el resultado como `True` o `False`.
</aside>

---

<aside>
💡

## 💼 5.3 🛒 Sistema de verificación de descuentos.

Una tienda online quiere aplicar un descuento solo si:

- El cliente tiene más de 2 artículos en su carrito.
- El total de la compra supera los $500.
- Y el cliente **NO** es nuevo (ya ha comprado antes).

Crea un programa que evalúe si el descuento aplica. Usa operadores lógicos y compara los valores.

</aside>

---

# 🧠Precedencia y selección de operadores en Python

<aside>
💡

## 💼 5.4 Crea un programa que:

1. Pida al usuario una lista de 3 colores.
2. Pida un color para buscar.
3. Verifique dos cosas:
    - Si el color **está dentro de la lista**.
    - Si la lista **es idéntica** a otra lista con los mismos valores.

💡 ***Pista:*** Usa `in`, `is` y `and` para combinar las condiciones.

</aside>

---

<aside>
💡

## 💼 5.5 Validación de cliente activo

Una base de datos tiene una lista con los clientes activos:

```python
clientes_activos = ["Laura","Marta","Andrés"]
```

Crea una expresión que evalúe si:

- El nombre ingresado **está** en la lista (`in`).
- Y la lista **es la misma** referencia que `clientes_activos` (`is`).

El resultado debe ser un valor booleano.

</aside>

---

<aside>
💡

## 💼 5.6 Sistema de validación de producto

Crea un programa que evalúe si:

- Un producto ingresado está en la lista `productos_disponibles`,
- Y esa lista es **idéntica** a una copia temporal llamada `referencia_inventario`.

Muestra un solo valor booleano como resultado.

</aside>

---