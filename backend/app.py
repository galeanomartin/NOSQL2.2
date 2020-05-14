from flask import Flask, request
from flask_cors import CORS
from flask import jsonify, json
import redis


app = Flask(__name__)
CORS(app)

def connect_db():
    """Crear conexion a la base de datos."""
    conexion = redis.StrictRedis(host="db-redis-flask",port=6379, db=0)
    if(conexion.ping()):
        print("conectado al servidor de redis")
    else:
        print("error")
    return conexion

db = connect_db()

#VACIAR Base de datos
'''
db.flushdb()


#FUNCIONES------------------------------------------------------------------
#CARGAR LOS EPISODIOS

def cargarepisodios(): 
    
    db.hset("Chapter1: The Mandalorian","estado","disponible")    
    db.hset("Chapter1: The Mandalorian","descripcion","Cinco años después de la derrota del Imperio Galáctico, un cazarrecompensas mandaloriano acepta un trabajo fuera de registro de un cliente enigmático con conexiones imperiales, que le exige que viaje al planeta desierto Arvala-7 y encuentre a un objetivo de 50 años.")
    db.hset("Chapter1: The Mandalorian", "precio", " 250,00")
    db.hset("Chapter1: The Mandalorian", "foto", "https://vignette.wikia.nocookie.net/es.starwars/images/4/45/TheMandalorianS1Poster.png/revision/latest?cb=20190824064722")

    db.hset("Chapter2: The Child","estado","disponible")    
    db.hset("Chapter2: The Child","descripcion","Mientras regresa a su nave a pie con el niño a cuestas, el Mandaloriano es emboscado por un trio de guerreros trandoshanos. Desintegra a uno de ellos que intenta apresarle y matar al niño, revelando un llavero de rastreo. Al regresar a su nave, se encuentra con un equipo de Jawas que roban partes de su nave. ")
    db.hset("Chapter2: The Child", "precio", " 270,00")    
    db.hset("Chapter2: The Child", "foto", "https://static-1.ivoox.com/audios/1/6/2/7/6391573207261_XXL.jpg")

    db.hset("Chapter3: The Sin","estado","disponible")    
    db.hset("Chapter3: The Sin","descripcion","El mandaloriano regresa a Nevarro y entrega al niño a su cliente, a quien le cuestiona sobre sus planes con el niño, pero éste se niega. El cliente le paga la recompensa en acero beskar, usándolo para mejorar su armadura, cortesía de la Armera que dirige su tribu.")
    db.hset("Chapter3: The Sin", "precio", " 260,00")
    db.hset("Chapter3: The Sin", "foto", "https://vignette.wikia.nocookie.net/es.starwars/images/f/fb/The_Mandalorian_Chapter_3_Original_Score.jpg/revision/latest?cb=20191123073809")

    db.hset("Chapter4: Sanctuary","estado","disponible")    
    db.hset("Chapter4: Sanctuary","descripcion","El mandaloriano llega junto con el niño al planeta Sorgon en búsqueda de refugio. Mientras inspecciona el planeta, se encuentra a una interesante Shock Trooper llamada Cara Dune quien demuestra una fortaleza y habilidades de combate impresionantes. ")
    db.hset("Chapter4: Sanctuary", "precio", " 300,00")
    db.hset("Chapter4: Sanctuary", "foto", "https://vignette.wikia.nocookie.net/es.starwars/images/6/67/The_Mandalorian_Chapter_4_Original_Score.jpg/revision/latest?cb=20191130210632")

    db.hset("Chapter5: The Gunslinger","estado","disponible")    
    db.hset("Chapter5: The Gunslinger","descripcion","El Mandaloriano derrota a un caza recompensas en una batalla espacial. Aterriza su nave dañada en un muelle de reparación cercano, dirigido por Peli Motto en Mos Eisley en Tatooine.")
    db.hset("Chapter5: The Gunslinger", "precio", " 290,00")
    db.hset("Chapter5: The Gunslinger","foto","https://vignette.wikia.nocookie.net/es.starwars/images/6/64/The_Mandalorian_Chapter_5_Original_Score.jpg/revision/latest?cb=20191208181313")

    db.hset("Chapter6: The Prisoner","estado","disponible")    
    db.hset("Chapter6: The Prisoner","descripcion","El Mandaloriano se acerca a su antiguo compañero Ran para trabajar. Ran le da la bienvenida a su estación espacial y le informa al Mandaloriano que lo necesita a él y a su nave para un trabajo de cinco hombres.")
    db.hset("Chapter6: The Prisoner", "precio", " 250,00")
    db.hset("Chapter6: The Prisoner", "foto", "https://vignette.wikia.nocookie.net/es.starwars/images/2/2c/The_Mandalorian_Chapter_6_Original_Score.jpg/revision/latest?cb=20191215195712")

    db.hset("Chapter7: The Reckoning","estado","disponible")    
    db.hset("Chapter7: The Reckoning","descripcion","El mandaloriano recibe un mensaje de Greef Karga. La ciudad de Karga ha sido invadida por tropas imperiales dirigidas por el Cliente, que esta desesperado por recuperar al Niño.")
    db.hset("Chapter7: The Reckoning", "precio", " 200,00")
    db.hset("Chapter7: The Reckoning", "foto", "https://vignette.wikia.nocookie.net/es.starwars/images/6/62/The_Mandalorian_Chapter_7_Original_Score.jpg/revision/latest?cb=20191218161324")

    db.hset("Chapter8: Redemption","estado","disponible")    
    db.hset("Chapter8: Redemption","descripcion","IG-11 rescata al Niño de los soldados exploradores. Gideon advierte a Karga, Dune, y el Mandaloriano (a quien se refiere por su verdadero nombre, Din Djarin) que a menos que acepten cooperar con él, seguramente moriran.")
    db.hset("Chapter8: Redemption", "precio", " 300,00")
    db.hset("Chapter8: Redemption", "foto", "https://vignette.wikia.nocookie.net/es.starwars/images/a/a8/The_Mandalorian_Chapter_8_Original_Score.jpg/revision/latest?cb=20191227060357")
    return 'Ok'

cargarepisodios()

#HASTA ACA
'''

#LISTAR LOS EPIOSIDIOS
def listarEpisodios():
    
    liste = ["Chapter1: The Mandalorian","Chapter2: The Child","Chapter3: The Sin","Chapter4: Sanctuary","Chapter5: The Gunslinger","Chapter6: The Prisoner","Chapter7: The Reckoning","Chapter8: Redemption"]
    for k in liste:
        #print(k)
        #if(db.type(k) == 'hash'):
        if (db.pttl('reservado'+ k) == -2) and (db.pttl('alquilado'+ k) == -2) : 
            
            #if(db.hget(k,"estado") != "disponible"):
            db.hset(k,"estado","disponible")
            print(db.type(k))
        
    
    chapters = [        
        
            {
            "nombre": "Chapter1: The Mandalorian",
            "estado": db.hget("Chapter1: The Mandalorian","estado").decode("utf-8"),
            "descripcion": db.hget("Chapter1: The Mandalorian","descripcion").decode("utf-8"),
            "precio": db.hget("Chapter1: The Mandalorian","precio").decode("utf-8"),
            "foto": db.hget("Chapter1: The Mandalorian","foto").decode("utf-8")
            },       
        
            {
            "nombre": "Chapter2: The Child",
            "estado": db.hget("Chapter2: The Child", "estado").decode("utf-8"),
            "descripcion": db.hget("Chapter2: The Child","descripcion").decode("utf-8"),
            "precio": db.hget("Chapter2: The Child","precio").decode("utf-8"),
            "foto": db.hget("Chapter2: The Child","foto").decode("utf-8")
            },       
        
            {
            "nombre": "Chapter3: The Sin",
            "estado": db.hget("Chapter3: The Sin", "estado").decode("utf-8"),
            "descripcion": db.hget("Chapter3: The Sin","descripcion").decode("utf-8"),
            "precio": db.hget("Chapter3: The Sin","precio").decode("utf-8"),
            "foto": db.hget("Chapter3: The Sin","foto").decode("utf-8")
            },        
        
            {
            "nombre": "Chapter4: Sanctuary",
            "estado": db.hget("Chapter4: Sanctuary", "estado").decode("utf-8"),
            "descripcion": db.hget("Chapter4: Sanctuary","descripcion").decode("utf-8"),
            "precio": db.hget("Chapter4: Sanctuary","precio").decode("utf-8"),
            "foto": db.hget("Chapter4: Sanctuary","foto").decode("utf-8")
            },       
        
            {
            "nombre": "Chapter5: The Gunslinger",
            "estado": db.hget("Chapter5: The Gunslinger", "estado").decode("utf-8"),
            "descripcion": db.hget("Chapter5: The Gunslinger","descripcion").decode("utf-8"),
            "precio": db.hget("Chapter5: The Gunslinger","precio").decode("utf-8"),
            "foto": db.hget("Chapter5: The Gunslinger","foto").decode("utf-8")
            },       
        
            {
            "nombre": "Chapter6: The Prisoner",
            "estado": db.hget("Chapter6: The Prisoner", "estado").decode("utf-8"),
            "descripcion": db.hget("Chapter6: The Prisoner","descripcion").decode("utf-8"),
            "precio": db.hget("Chapter6: The Prisoner","precio").decode("utf-8"),
            "foto": db.hget("Chapter6: The Prisoner","foto").decode("utf-8")
            },        
        
            {
            "nombre": "Chapter7: The Reckoning",
            "estado": db.hget("Chapter7: The Reckoning", "estado").decode("utf-8"),
            "descripcion": db.hget("Chapter7: The Reckoning","descripcion").decode("utf-8"),
            "precio": db.hget("Chapter7: The Reckoning","precio").decode("utf-8"),
            "foto": db.hget("Chapter7: The Reckoning","foto").decode("utf-8")
            },        
        
            {
            "nombre": "Chapter8: Redemption",
            "estado": db.hget("Chapter8: Redemption", "estado").decode("utf-8"),
            "descripcion": db.hget("Chapter8: Redemption","descripcion").decode("utf-8"),
            "precio": db.hget("Chapter8: Redemption","precio").decode("utf-8"),
            "foto": db.hget("Chapter8: Redemption","foto").decode("utf-8")
            }
                 
    ]
        
    a = jsonify(chapters)
    return (a)
  

def reservar(capitulo):
    r = db.hget(capitulo,"estado").decode("utf-8")
    print(r)
    if(r == 'disponible'):  
        db.hset(capitulo,"estado","reservado")
        db.setex('reservado' + capitulo, 240, capitulo)
        return 'Si'
    if(r == 'reservado'):   
        print('ENTRO EN NO')            
        return 'No'
    if(r == 'alquilado'):
        print(r)
        return 'No'

def pagar(capitulo):
    
    if(db.pttl('reservado'+ capitulo) != -2):
        db.delete('reservado' + capitulo)
        db.hset(capitulo,"estado","alquilado")
        db.setex('alquilado'+capitulo, 86400, capitulo)
        return 'Alquilado por 24hrs'
    else:   
        return 'No se encuentra reservado'


@app.route('/obtenerListado', methods=['GET'])
def obtenerListado():    
    if request.method == 'GET':
        e = listarEpisodios()
        return e
    
    
@app.route('/pagarCapitulo', methods=['POST'])
def pagarCapitulo():
    if request.method == 'POST':                
        e = request.args['capitulo']
        aux = pagar(e)
        
        if(aux == 'No se encuentra reservado'):
            return 'falta reservarlo o se encuentra alquilado'
        else:
            return 'Pagado'


@app.route('/reservarCapitulo', methods=['POST'])
def reservarCapitulo():
    if request.method == 'POST':
        e = request.args['capitulo']
        aux = reservar(e)
        if (aux == 'Si'):
            return 'Reservado con exito'
        if (aux == 'No'):
            return 'Ya se encuentra reservado o alquilado'


       


if __name__ == '__main__':
    app.run(host='backend', port='5000', debug=False)

