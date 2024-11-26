import math

# Definimos la función p(t) y su derivada
def p(t):
    return 3 * math.exp(0.68 * t / 24) - 10 * t

def dp(t):
    return (0.68 / 24) * 3 * math.exp(0.68 * t / 24) - 10

# Parámetros iniciales
initial_t = 408  # en horas
target_population = 110
tolerance = 0.002  # Error relativo deseado
max_iterations = 100  # Límite de iteraciones

# Newton-Raphson
iterations = []
t_current = initial_t
for i in range(max_iterations):
    f_t = p(t_current) - target_population
    df_t = dp(t_current)
    t_next = t_current - f_t / df_t
    relative_error = abs((t_next - t_current) / t_current)
    
    # Guardar resultados para la tabla
    iterations.append({
        "Iteración": i + 1,
        "x0": t_current,
        "f(x0)": f_t,
        "f_prime(x0)": df_t,  # Cambiamos el nombre de la clave aquí
        "xi": t_next,
        "Error Relativo": relative_error,
    })
    
    if relative_error < tolerance:
        break
    t_current = t_next

# Imprimir tabla de resultados
print("\nTabla de resultados:")
print(f"{'Iteración':<10} {'x0 (horas)':<15} {'f(x0)':<20} {'f\'(x0)':<20} {'xi (horas)':<15} {'Error Relativo':<15}")
for row in iterations:
    print(f"{row['Iteración']:<10} {row['x0']:<15.6f} {row['f(x0)']:<20.6f} {row['f_prime(x0)']:<20.6f} {row['xi']:<15.6f} {row['Error Relativo']:<15.6f}")

# Resultados en días y horas
final_t = iterations[-1]["xi"]
days = int(final_t // 24)
hours = int(final_t % 24)
print(f"\nLa solución encontrada es aproximadamente {days} días y {hours} horas.")

# Describir las expresiones asociadas
print("\nExpresiones para las tres primeras iteraciones:")
for i, row in enumerate(iterations[:3]):
    print(f"\nIteración {i + 1}:")
    print(f"x0 = {row['x0']:.6f}")
    print(f"f(x0) = p(x0) - {target_population} = {row['f(x0)']:.6f}")
    print(f"f'(x0) = dp(x0) = {row['f_prime(x0)']:.6f}")  # Usamos el nuevo nombre aquí
    print(f"x1 = x0 - f(x0) / f'(x0) = {row['xi']:.6f}")
    print(f"Error Relativo = |x1 - x0| / |x0| = {row['Error Relativo']:.6f}")


    
