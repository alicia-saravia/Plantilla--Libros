from Libros.configuracion.mysqlconnection import connectToMySQL

class Autor:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.crado_en = data['creado_en']
        self.actualizado_en = data['actualizado_en']

    @classmethod
    def crear_autor(cls, data):
        query = "INSERT INTO autores (nombre) VALUES (%(nombre)s);"
        resultado = connectToMySQL('Libros').query_db(query, data)
        return resultado

    #METODO SOLO DE LECTURA
    @classmethod
    def mostrar_autor(cls,data):
        query = "SELECT * FROM autores WHERE id = %(id)s;"
        resultado = connectToMySQL('Libros'). query_db(query, data)
        print(resultado)
        return resultado[0]
    
    @classmethod
    def todos_autores(cls):
        query = "SELECT * FROM autores;"
        resultado = connectToMySQL('Libros'). query_db(query)
        return resultado

    @classmethod
    def grabar_favoritos(cls, data):
        query = "INSERT  INTO favoritos (autor_id, libro_id) VALUES (%(autor_id)s, %(libro_id)s)"
        resultado = connectToMySQL('Libros').query_db(query, data)
        return resultado
    
    @classmethod
    def autores_libros(cls, data):
        query = " SELECT * FROM autores join favoritos on autores.id = favoritos.autor_id where libro_id = %(libro_id)s;"
        resultado = connectToMySQL('libros'). query_db(query, data)
        print(resultado)
        return resultado

