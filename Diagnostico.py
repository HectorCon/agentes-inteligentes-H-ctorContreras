def diagnostico(sintomas):
    """Sistema experto básico para diagnóstico médico."""
    if "fiebre" in sintomas and "tos" in sintomas and "dificultad para respirar" in sintomas:
        return "Posible infección respiratoria. Consulte a un médico."
    elif "fiebre" in sintomas and "dolor de cabeza" in sintomas:
        return "Podría ser gripe. Se recomienda reposo e hidratación."
    elif "dolor de garganta" in sintomas and "tos" in sintomas:
        return "Podría ser faringitis. Consulte a un médico si persisten los síntomas."
    elif "dolor abdominal" in sintomas and "nauseas" in sintomas:
        return "Posible infección estomacal. Evite comidas pesadas y manténgase hidratado."
    else:
        return "Síntomas no reconocidos. Consulte a un especialista."

if __name__ == "__main__":
    print("Sistema Experto de Diagnóstico Médico")
    sintomas_usuario = input("Ingrese sus síntomas separados por comas: ").lower().split(", ")
    resultado = diagnostico(sintomas_usuario)
    print("Diagnóstico:", resultado)
