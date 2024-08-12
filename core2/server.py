from flask import Flask, render_template
app = Flask(__name__)  

@app.route('/')

def bienvenido():
   
   return render_template('index.html')

@app.route('/paises')

def lista_de_paises():

   lista_paises= [

       {'pais': 'Argentina' , 'capital': 'Buenos Aires'},

       {'pais': 'Brasil' , 'capital': 'Brasilia'},

       {'pais': 'Chile' , 'capital': 'Santiago de Chile'},

       {'pais': 'Colombia' , 'capital': 'Bogotá'},

       {'pais': 'Costa Rica' , 'capital': 'San José'},

       {'pais': 'Paraguay' , 'capital': 'Asunción'},

       {'pais': 'Perú' , 'capital': 'Lima'}
   ]

   return render_template('paises.html', paises=lista_paises)


if __name__=="__main__":    

   app.run(debug=True)   
