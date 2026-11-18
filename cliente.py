#CadastroCliente integrado em AdicionarCliente => ok, adicionar_cliente é um método em agencia
#AdicionarCliente, ListarClientes, ValidarCPF, Listagem dos clientes/conta e buscas por cpf/conta é função da agencia.
# => ListarClientes está no html de agencia; 
#Seção: Edição de Perfil - dados, mudança de titular e excluir
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = [] #1 cliente pode ter N contas

    #transforma o objeto em dicionário só para salvar no json
    def to_dict(self):
        return {"nome": self.nome, "cpf": self.cpf}