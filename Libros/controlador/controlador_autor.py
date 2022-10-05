from Libros import app
from flask import render_template, request, redirect
from Libros.modelos.modelo_autor import Autor
from Libros.modelos.modelo_libros import Libro

@app.route('/autores')# El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def autores():
    resultado = Autor.todos_autores()
    return render_template('autores.html', autores = resultado)

@app.route('/crear_autor',methods=['POST'])# El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def crear_autor():
    result = Autor.crear_autor(request.form)
    return redirect('/autores')

@app.route('/autores/<id>')
def mostrar_autores(id):
    data = {
        'autor_id': id
    }
    resultado = Libro.libros_autor(data)
    data2 = {
        'id' : id
    }
    todos_libros = Libro.todos_libros()
    autor = Autor.mostrar_autor(data2)
    return render_template('mostrar_autores.html', libros = resultado, autor = autor, todos_libros = todos_libros)

@app.route('/agregar_favorito', methods = ['POST'])
def agregar_favorito():
    resultado = Autor.grabar_favoritos(request.form)
    return redirect('/autores/' + request.form['autor_id'])

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "ESTA RUTA NO FUE ENCONTRADA", 404
    #return render_template('404.html'), 404