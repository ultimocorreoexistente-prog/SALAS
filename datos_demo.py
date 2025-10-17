#!/usr/bin/env python3
"""
Datos de demostración para el Sistema de Reservas UFRO
Usado cuando el sistema principal no está disponible
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generar_datos_demo():
    """Genera datos de demostración para la aplicación"""
    
    # Datos de salas
    salas_demo = {
        'codigo': ['301-A', '302-A', '303-A', '205-B', '206-B', '401-C', '102-D', '103-D'],
        'capacidad': [35, 40, 30, 45, 50, 30, 60, 55],
        'facultad': ['Ingeniería', 'Ingeniería', 'Ingeniería', 'Ciencias', 'Ciencias', 'Medicina', 'Educación', 'Educación'],
        'equipamiento': ['Proyector, Sonido', 'Completo', 'Básico', 'Proyector', 'Completo', 'Básico', 'Proyector, Sonido', 'Completo']
    }
    
    # Datos de reservas
    fechas_base = datetime.now()
    reservas_demo = []
    
    for i in range(50):
        fecha = fechas_base + timedelta(days=np.random.randint(-15, 15))
        hora = np.random.choice(['08:00', '10:00', '12:00', '14:00', '16:00', '18:00'])
        
        reservas_demo.append({
            'fecha': fecha.strftime('%Y-%m-%d'),
            'hora': hora,
            'aula': np.random.choice(salas_demo['codigo']),
            'profesor': f"Prof. {np.random.choice(['García', 'López', 'Martínez', 'Rodríguez', 'González'])}",
            'asignatura': np.random.choice(['Matemáticas', 'Física', 'Química', 'Programación', 'Historia']),
            'estudiantes': np.random.randint(20, 60),
            'estado': np.random.choice(['Confirmada', 'Pendiente', 'Cancelada'], p=[0.8, 0.15, 0.05])
        })
    
    # Datos de ocupación por hora
    ocupacion_horaria = {
        'hora': ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00'],
        'ocupacion': [20, 35, 45, 52, 48, 25, 55, 45, 30, 25, 20, 15, 8]
    }
    
    # Datos de ocupación por facultad
    ocupacion_facultad = {
        'facultad': ['Ingeniería', 'Medicina', 'Educación', 'Ciencias', 'Derecho'],
        'ocupacion': [85, 72, 90, 68, 76]
    }
    
    return {
        'salas': pd.DataFrame(salas_demo),
        'reservas': pd.DataFrame(reservas_demo),
        'ocupacion_horaria': pd.DataFrame(ocupacion_horaria),
        'ocupacion_facultad': pd.DataFrame(ocupacion_facultad)
    }

def obtener_metricas_demo():
    """Obtiene métricas de demostración"""
    return {
        'salas_activas': 45,
        'reservas_hoy': 127,
        'conflictos': 3,
        'ocupacion': 78
    }

def obtener_conflictos_demo():
    """Obtiene conflictos de demostración"""
    return pd.DataFrame({
        'fecha': ['2024-10-15', '2024-10-16', '2024-10-15'],
        'hora': ['14:00', '10:00', '16:00'],
        'aula': ['301-A', '205-B', '301-A'],
        'conflicto': ['Doble reserva', 'Capacidad insuficiente', 'Equipamiento faltante'],
        'prioridad': ['🔴 Alta', '🟡 Media', '🟡 Media'],
        'estado': ['Pendiente', 'Resuelto', 'En proceso']
    })

if __name__ == "__main__":
    datos = generar_datos_demo()
    print("✅ Datos de demostración generados")
    print(f"📊 {len(datos['salas'])} salas, {len(datos['reservas'])} reservas")
