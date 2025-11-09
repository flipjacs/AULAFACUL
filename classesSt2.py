import datetime

class Produto:
    def __init__(self,nome:str,categoria:str,preco:float,quantEstoque:int,dataValidade:datetime):
        self.__nome:str=nome
        self.__categoria:str=categoria
        self.__preco:float=preco
        self.__quantEstoque:int=quantEstoque
        self.__dataValidade:datetime=dataValidade

        @property
        def nome(self)->str:
            return self.__nome
        @nome.setter
        def nome(self,nome:str):
            self.__nome=nome

        @property
        def categoria(self)->str:
            return self.__categoria
        @categoria.setter
        def categoria(self,categoria:str):
            self.__categoria=categoria
        
        @property
        def preco(self)->float:
            return self.__preco
        @preco.setter
        def preco(self,preco:float):
            self.__preco=preco
        
        @property
        def quantEstoque(self)->int:
            return self.__quantEstoque
        @quantEstoque.setter
        def quantEstoque(self,quantEstoque:int):
            self.__quantEstoque=quantEstoque

        @property
        def dataValidade(self)->datetime:
            return self.__dataValidade
        @dataValidade.setter
        def dataValidade(self,dataValidade:datetime):
            self.__dataValidade=dataValidade
        

class Fornecedor:
     def __init__(self, nome:str,cnpj: str,telefone:str,email:str, cidade:str):
        self.__nome:str=nome
        self.__cnpj:str=cnpj
        self.__telefone:str=telefone
        self.__email:str=email
        self.__cidade:str=cidade


        @property
        def nome(self)->str:
            return self.__nome
        @nome.setter
        def nome(self,nome:str):
            self.__nome=nome

        @property
        def cnpj(self)->str:
            return self.__cnpj
        @cnpj.setter
        def cnpj(self,cnpj:str):
            self.__cnpj=cnpj
        
        @property
        def telefone(self)->str:
            return self.telefone
        @telefone.setter
        def telefone(self,telefone:str):
            self.__telefone=telefone
        
        @property
        def email(self)->str:
            return self.__quantEstoque
        @email.setter
        def email(self,email:str):
            self.__email=email

        @property
        def cidade(self)->str:
            return self.cidade
        @cidade.setter
        def cidade(self,cidade:str):
            self.__cidade=cidade