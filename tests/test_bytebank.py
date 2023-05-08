import pytest as pytest

from codigo.bytebank import Funcionario

class TestClass:

    @pytest.fixture
    def funcionario(self):
        return Funcionario('Camila Santos', '17/01/1997', 1111)


    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self, funcionario):
        camila = funcionario #Given
        esperado = 26
        resultado = camila.idade() #When
        assert resultado == esperado #Then

    def test_quando_sobrenome_recebe_Camila_Santos_deve_retornar_Santos(self, funcionario):
        camila = funcionario #Given
        esperado = 'Santos'
        resultado = camila.sobrenome() #When
        assert resultado == esperado #Then

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_nome = 'Paulo Bragança'
        entrada_salario = 100000 #Given
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)

        funcionario_teste.decrescimo_salario() #When
        resultado = funcionario_teste.salario

        assert resultado == esperado #Then

    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000  # Given
        esperado = 100

        funcionario_teste = Funcionario('Teste', '11/11/2000', entrada_salario)
        resultado = funcionario_teste.calcular_bonus() #When

        assert resultado == esperado  # Then

    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada_salario = 100000000 # Given

            funcionario_teste = Funcionario('Teste', '11/11/2000', entrada_salario)
            resultado = funcionario_teste.calcular_bonus()  # When

            assert resultado # Then

    def test_retorno_str(self):
        nome, data_nascimento, salario = 'Teste', '12/03/2000', 1000  # Given

        esperado = 'Funcionario(Teste, 12/03/2000, 1000)'

        funcionario_teste = Funcionario(nome, data_nascimento, salario)
        resultado = funcionario_teste.__str__()

        assert resultado == esperado  # Then
