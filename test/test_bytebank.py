from codigo.bytebank import Funcionario
import pytest


class TestClass:
    def test_de_idade_quando_receber_29_11_2001_deve_retornar_21(self):
        entrada = '29/11/2001'
        esperado = 21

        data_nascimento_test = Funcionario("teste", entrada, 1111)
        resultado = data_nascimento_test.idade()

        assert resultado == esperado

    def test_quando_sobrenome_recebe_Vinicius_Alexandre_deve_retornar_Alexandre(self):
        entrada ='Vinicius Alexandre'
        esperado ='Alexandre'

        funcionario_teste = Funcionario(entrada, '29/11/2001', 1000)
        resultado = funcionario_teste.sobrenome()

        assert resultado == esperado

    def test_quando_salario_eh_maior_que_100000_deve_aver_decrescimo_e_vai_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Vinicius Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '29//11/2001', entrada_salario)
        funcionario_teste.descrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    def test_quando_calcular_bonus_eh_igual_a_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        salario_teste = Funcionario('Vinicius Alexandre', '29/11/2001', entrada)
        resultado = salario_teste.calcular_bonus()

        assert resultado == esperado

    def test_quando_calcular_bonus_eh_maior_que_1000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000

            bonus = Funcionario('Vinicius Alexandre', '29/11/2001', entrada)
            resultado = bonus.calcular_bonus()

            assert resultado

    def test_quando_salario_eh_menor_que_100000_deve_aver_decrescimo_e_vai_retornar_false(self):
        entrada = 10000
        esperado = False

        salario_teste = Funcionario('vinicius alexandre', '29/11/2001', entrada)
        resultado = salario_teste.eh_diretor()

        assert resultado == esperado


