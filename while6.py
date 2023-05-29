while True:
  print("\nOpções do menu: ")
  print("1 - contratar serviço de internet")
  print("2 - cancelar serviço de internet")
  print("3 - alterar dados do usuário")
  print("4 - emitir 2ª via do boleto")
  print("5 - falar com um dos nossos atendentes")
  print("6 - sair")
  
 
  opcao = int(input("digite a opção desejada: "))
      
 
  if (opcao == 1):
    print("\n Você escolheu a opção 1 - Contratar serviço de internet")
    print("Atualmente temos dois planos de dados. Mega 75Mb por R$ 79,90 e Super fibra 100Mb por R$99,99.")
    print("Informe seu CPF, nome completo, CEP, telefone de contato e plano escolhido, e aguarde alguns instantes.")

  elif (opcao == 2):
    print("\nVocê escolheu a opção 2 - Cancelar serviço de internet")
    print("Informe seu CPF e o motivo do cancelamento.")

  elif (opcao == 3):
    print("\nVocê escolheu a opção 3 - Alterar dados do usuário.")
    print("Informe seu CPF e o novo dado a ser atualizado.")

  elif (opcao == 4):
    print("\nVocê escolheu a opção 4 - Emitir 2ª via do boleto.")
    print("Informe seu CPF e o mês desejado para emissão da 2ª via.")

  elif (opcao == 5):
    print ("\nVocê escolheu a opção 5 - Falar com um dos nossos atendentes.")
    print ("Todos os nossos atendentes estão ocupados no momento. Aguarde até 5 minutos que você será atendido.")
    
  elif (opcao == 6):
    print ("Você saiu.")
    print ("Obrigado pelo contato.")
    break
    
  else:
    print("Opção inválida, digite novamente")

  