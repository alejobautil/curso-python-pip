import utils
import read_csv
import charts
import pandas as pd

def run():
  '''
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  '''
  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage']

  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv('./data.csv')

  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'],labels, values)
  

if __name__ == '__main__':
  run()
  
"""
#Para poder ejecutar el modulo, ya que vuelto función, no tenemos control en la ejecución, hacemos lo siguiente:
if __name__ == '__main__':
  run()
#Este if lo que esta diciendo al archivo main.py es que si es ejecutado desde la terminal, ejecutar el método de run, pero si es ejecutado desde otro archivo no es ejecutado. A esto se le llama ENTRY POINT.
#Que quiere decir, que si ejecuto main desde la terminal, este sera ejecutado completamente, pero si lo ejecuto desde otro archivo que no sea la terminal, esto no sera ejecutado completamente
"""