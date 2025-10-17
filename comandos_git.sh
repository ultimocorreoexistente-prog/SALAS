#!/bin/bash
# Script de comandos Git para subir a GitHub
# Ejecutar línea por línea en tu terminal

echo "🚀 Subiendo Sistema de Reservas UFRO a GitHub"
echo "=============================================="

# Inicializar repositorio Git
git init

# Agregar todos los archivos
git add .

# Primer commit
git commit -m "🏛️ Sistema Inteligente de Reservas UFRO v1.0

✨ Características principales:
- Dashboard interactivo con métricas en tiempo real
- Gestión inteligente de reservas con IA
- Análisis predictivo y detección de conflictos
- Centro de reportes con exportación PDF/Excel
- Optimizado para deploy en Railway

🤖 Desarrollado por: MiniMax Agent
📅 Fecha: 2025-10-14
"

echo "✅ Repositorio inicializado y commit creado"
echo ""
echo "🌐 PRÓXIMOS PASOS:"
echo "1. Crea un nuevo repositorio en GitHub llamado: sistema-reservas-ufro"
echo "2. Copia la URL del repositorio (ejemplo: https://github.com/tu-usuario/sistema-reservas-ufro.git)"
echo "3. Ejecuta estos comandos:"
echo ""
echo "   git remote add origin https://github.com/TU-USUARIO/sistema-reservas-ufro.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "4. Ve a railway.app y conecta tu repositorio"
echo "5. ¡Tu sistema estará online en 2 minutos!"
