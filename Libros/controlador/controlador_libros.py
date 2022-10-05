from Libros import app
from flask import render_template, request, redirect
from Libros.modelos.modelo_libros import Libro
from Libros.modelos.modelo_autor import Autor

@app.route('/libro')# El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def libros():
    resultado = Libro.todos_libros()
    print(resultado)
    return render_template('libros.html', libros = resultado)

@app.route('/libro/<id>')
def mostrar_libros(id):
    data = {
        'libro_id': id
    }
    resultado = Autor.autores_libros(data)
    data2 = {
        'id' : id
    }
    todos_autores = Autor.todos_autores()
    libro = Libro.mostrar_libro(data2)
    return render_template('mostrar_libros.html', autores = resultado, libro = libro, todos_autores = todos_autores)

@app.route('/crear_libro',methods=['POST'])# El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def crear_libro():
    result = Libro.crear_libro(request.form)
    return redirect('/libro')

@app.route('/agregar_favorito_libro', methods = ['POST'])
def agregar_favorito_libro():
    resultado = Autor.grabar_favoritos(request.form)
    return redirect('/libro/' + request.form['libro_id'])
    
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "ESTA RUTA NO FUE ENCONTRADA", 404
    #return render_template('404.html'), 404