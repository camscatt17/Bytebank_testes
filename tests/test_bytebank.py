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