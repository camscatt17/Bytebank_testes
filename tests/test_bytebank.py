from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000' #Given- Contexto
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() #When-ação

        assert resultado == esperado #Then-desfecho

    def test_quando_sobrenome_recebe_Camila_Santos_deve_retornar_Santos(self):
        entrada = ' Camila Santos ' #Given
        esperado = 'Santos'

        camila = Funcionario(entrada, '11/11/2000', 1111)
        resultado = camila.sobrenome() #When

        assert resultado == esperado