#!/usr/bin/env python3
"""
🚀 Script para rodar a aplicação

Execute este arquivo para iniciar o servidor de desenvolvimento.
Comando: python run.py
"""

import uvicorn
import os

if __name__ == "__main__":
    # Mudar para a pasta app se não estivermos nela
    if not os.path.exists("main.py"):
        os.chdir("app")
    
    print("🚀 Iniciando Task API...")
    print("📚 Documentação: http://localhost:8000/docs")
    print("🔄 Pressione Ctrl+C para parar")
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Reinicia automaticamente quando o código muda
        log_level="info"
    )