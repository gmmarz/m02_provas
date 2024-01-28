class Material:
    def __init__(self, titulo: str, autor_ou_editora:str) -> None:
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora
        
    def exibir_informacoes(self) -> None:
        print(f"Titulo: {self.titulo}, autor_ou_editora: {self.autor_ou_editora}")
        
class Livro(Material):
    def __init__(self, titulo: str, autor_ou_editora: str, genero: str) -> None:
        super().__init__(titulo, autor_ou_editora)
        self.genero = genero
        
    def exibir_informacoes(self) -> None:
        print(f"Livro\nTitulo: {self.titulo}\n Autor ou Editora: {self.autor_ou_editora}\n Genero: {self.genero}")
        
class Revista(Material):
    def __init__(self, titulo: str, autor_ou_editora: str, edicao: str) -> None:
        super().__init__(titulo, autor_ou_editora)
        self.edicao = edicao
        
    def exibir_informacoes(self) -> None:
        print(f"Revista\nTitulo: {self.titulo}\n Autor ou Editora: {self.autor_ou_editora}\n Edicao: {self.edicao}")
        

if __name__ == "__main__":
    print("Este é um módulo e não deve ser executado diretamente")