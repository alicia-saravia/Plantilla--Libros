from Libros.configuracion.mysqlconnection import connectToMySQL

class Favoritos:
    def __init__(self, data):
        self.autor_id = data['autor_id']
        self.libro_id = data['libro_id']

    @classmethod
    def crear_autor(cls, data):
        query = "INSERT INTO favoritos (autor_id, libro_id) VALUES (%(autor_id)s, %(libro_id)s);"
        resultado = connectToMySQL('Libros').query_db(query, data)
        return resultado

    #METODO SOLO DE LECTURA
    @classmethod
    def mostrar_autor(cls,data):
        query = "SELECT * FROM favoritos WHERE autor_id = %(autor_id)s;"
        resultado = connectToMySQL('Libros'). query_db(query, data)
        return resultado[0]

    @classmethod
    def mostrar_libros(cls,data):
        query = "SELECT * FROM favoritos WHERE libro_id = %(libro_id)s;"
        resultado = connectToMySQL('Libros'). query_db(query, data)
        return resultado[0]
    
    @classmethod
    def todos_autores(cls):
        query = "SELECT * FROM favoritos;"
        resultado = connectToMySQL('Libros'). query_db(query)
        return resultado
