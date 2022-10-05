from Libros import app
from flask import render_template, request, redirect
from Libros.controlador import controlador_autor
from Libros.controlador import controlador_libros


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración