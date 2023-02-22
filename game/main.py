import random 



#Crearemos una función primero para escoger las opciones del usuario y de la computadora

def choose_option():
  options = ("piedra", "papel", "tijera")
  user_option = input('Piedra, Papel o Tijera = ')
  user_option = user_option.lower()
  
  if not user_option in options:
    print('Esa opción no es valida')
    #continue
    return None, None 
    
  computer_option = random.choice(options)
  
  print('User option = ', user_option)
  print('Computer option = ', computer_option)

  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  
  if user_option == computer_option:
    print('Empate !')
    
  elif user_option =='piedra':
    if computer_option == 'tijera':
      print('Piedra gana a tijera')
      print('User gano')
      user_wins +=1
    else:
      print('Papel gana a piedra')
      print('Computer gano')
      computer_wins +=1
      
  elif user_option =='papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('User gano')
      user_wins +=1
    else:
      print('tijera gana a papel')
      print('Computer gano')
      computer_wins +=1
      
  elif user_option =='tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('User gano')
      user_wins +=1
    else:
      print('piedra gana a tijera')
      print('Computer gano')
      computer_wins +=1
  return user_wins , computer_wins

def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1
  
  while True:
  
    print('*'*10)
    print('ROUNDS', rounds)
    print('*'*10)
    
    print('computer_wins', computer_wins)
    print('user_wins', user_wins)
  
    user_option, computer_option =choose_option()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
  
    rounds+=1
    if computer_wins == 2:
      print('El ganador es la computadora')
      break
      
    if user_wins == 2:
      print('El ganador es la computadora')
      break

run_game()
      
