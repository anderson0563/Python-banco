#!/usr/bin/env python3
from mysql.connector import connect, Error

class ConectarDB:
    """Classe."""

    def __init__(self):
        """Construtor.

        O construtor é executado sempre que a classe é instanciada.
        """
        self.con = connect(host="127.0.0.1",port="8889",user="user",password="123456",database="pessoa")
        self.cur = self.con.cursor()

    def consultar_registros(self):
        resultado = []
        self.cur.execute("SELECT * FROM pessoa")
        for pessoa in self.cur.fetchall():
                resultado.append(pessoa)

        return resultado

    def inserir_registro(self, pessoa):
        try:
            self.cur.execute(
                f"INSERT INTO pessoa (`nome`) VALUES (%s)", [pessoa])
        except Exception as e:
            print('\n[x] Falha ao inserir registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            # rollback reverte/desfaz a operação.
            self.con.rollback()
        else:
            # commit registra a operação/transação no banco.
            self.con.commit()
            print('\n[!] Registro inserido com sucesso [!]\n')

    def remover_registro(self, pessoa):
        try:
            self.cur.execute(
                "DELETE FROM pessoa WHERE nome LIKE %s", [pessoa])
        except Exception as e:
            print('\n[x] Falha ao remover registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro removido com sucesso [!]\n')
    
    def alterar_registro(self, nome, id):
        try:
            self.cur.execute(
                "UPDATE pessoa SET nome=%s WHERE indice=%s", (nome, id))
        except Exception as e:
            print('\n[x] Falha na alteração do registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro alterado com sucesso [!]\n')
    
    def imprimir_registros(self, resultado):
        for pessoa in resultado:
            print(pessoa)

if __name__ == '__main__':
    banco = ConectarDB()

    resultado = banco.consultar_registros()
    banco.imprimir_registros(resultado)
    banco.inserir_registro('pereira')
    resultado = banco.consultar_registros()
    banco.imprimir_registros(resultado)
    banco.remover_registro('pereira')
    resultado = banco.consultar_registros()
    banco.imprimir_registros(resultado)
    banco.alterar_registro('anderson', 2)
    resultado = banco.consultar_registros()
    banco.imprimir_registros(resultado)