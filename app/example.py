import main
#A veces por importar un modulo, podría estar cayendo en el error de ejecutar todo el modulo completo, y yo solo quiero importar un dato o una variable. Para empezar a tener buenos habitos y controlar los módulos, lo que hacemos es volver el modulo una función, que podamos controlar o ejecutar. Para ver el ejemplo vaya al archivo main.py
#print(main.data)

#Ya una vez cambiado el modulo y vuelto una función, lo podemos controlar, y ya podemos llamar variables que hay dentro del modulo, sin necesidad de ejectuar todo el modulo
print(main.data)
#si queremos ejecutar el modulo hacemos esto:
main.run()