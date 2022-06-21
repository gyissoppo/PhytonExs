import this
import ExerciciosModel
this.opcao = -1

this.num3 = int
this.dia = int
this.ano = int
this.mes = int
this.base = float
this.altura = float
this.valido = int
this.branco = int
this.nulo = int

def menu():
    print('Menu\n\n' +
          '1. Exercício 01\n' +
          '2. Exercicio 02\n' +
          '3. Exercicio 03\n' +
          '4. Exercicio 04\n' +
          '5. Exercicio 05\n' +
          '6. Exercício 06\n' +
          '7. Exercicio 07\n' +
          '8. Exercicio 08\n' +
          '9. Exercicio 09\n' +
          '10. Exercicio 10\n' +
          '11. Exercicio 11\n' +
          '12. Exercicio 12\n' +
          '13. Exercicio 13\n' +
          '14. Exercicio 14\n' +
          '15. Exercicio 15\n' +
          '16. Exercicio 16\n' +
          '17. Exercicio 17\n' +
          '18. Exercicio 18\n' +
          '19. Exercicio 19\n' +
          '20. Exercicio 20\n' +
          '0. Sair\n' +
          'Escolha uma das opções acima: ')
    this.opcao = int(input())

def executar():
    while(this.opcao != 0):
        menu()
        if this.opcao == 0:
            print('Sair!')
        elif this.opcao == 1:
            print(ExerciciosModel.exercicio01())
        elif this.opcao == 2:
            print(ExerciciosModel.exercicio02())
            #print ('informe um número')
            #num1 = int(input())
        elif this.opcao == 3:
            print(ExerciciosModel.exercicio03())
        elif this.opcao == 4:
            print(ExerciciosModel.exercicio04())
        elif this.opcao == 5:
            print(ExerciciosModel.exercicio05())
        elif this.opcao == 6:
            print(ExerciciosModel.exercicio06())
        elif this.opcao == 7:
            print(ExerciciosModel.exercicio07())
        elif this.opcao == 8:
            print(ExerciciosModel.exercicio08())
        elif this.opcao == 9:
            print(ExerciciosModel.exercicio09())
        elif this.opcao == 10:
            print(ExerciciosModel.exercicio10())
        elif this.opcao == 11:
            print(ExerciciosModel.exercicio11())
        elif this.opcao == 12:
            print(ExerciciosModel.exercicio12())
        elif this.opcao == 13:
            print(ExerciciosModel.exercicio13())
        elif this.opcao == 14:
            print(ExerciciosModel.exercicio14())
        elif this.opcao == 15:
            print(ExerciciosModel.exercicio15())
        elif this.opcao == 16:
            print(ExerciciosModel.exercicio16())
        elif this.opcao == 17:
            print(ExerciciosModel.exercicio17())
        elif this.opcao == 18:
            print(ExerciciosModel.exercicio18())
        elif this.opcao == 19:
            print(ExerciciosModel.exercicio19())
        elif this.opcao == 20:
            print(ExerciciosModel.exercicio20())
        else:
            print('Código digitado não é válido!')


