from Libros.configuracion.mysqlconnection import connectToMySQL

class Libro:
    def __init__(self, data):
        self.id = data['id']
        self.titulo = data['titulo']
        self.numero_de_pagina = data['numero_de_pagina']
        self.creado_en = data['creado_en']
        self.actualizado_en = data['actualizado_en']

    @classmethod
    def crear_libro(cls, data):
        query = "INSERT INTO libros (titulo, numero_de_pagina) VALUES (%(titulo)s, %(numero_de_pagina)s);"
        resultado = connectToMySQL('libros').query_db(query, data)
        return resultado

    #METODO SOLO DE LECTURA
    @classmethod
    def mostrar_libro(cls,data):
        query = "SELECT * FROM libros WHERE id = %(id)s;"
        resultado = connectToMySQL('libros'). query_db(query, data)
        return resultado[0]
    
    @classmethod
    def todos_libros(cls):
        query = "SELECT * FROM libros;"
        resultado = connectToMySQL('libros'). query_db(query)
        print(resultado)
        return resultado

    @classmethod
    def libros_autor(cls, data):
        query = " SELECT * FROM libros join favoritos on libros.id = favoritos.libro_id where autor_id = %(autor_id)s;"
        resultado = connectToMySQL('libros'). query_db(query, data)
        print(resultado)
        return resultado