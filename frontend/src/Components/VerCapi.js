import React, { useState, useEffect, Fragment } from 'react'
import { Redirect, Link } from 'react-router-dom'
import axios from 'axios'
import Swal from 'sweetalert2'
import fondo from '../Images/background.jpg'
//import CardExample from './Card'


function VerCapi(codigo) {

  const [estado, setEstado] = useState('')
  const [precio, setPrecio] = useState('')
  const [nombre, setNombre] = useState('')
  const [descripcion, setDescripcion] = useState('')
  const [foto, setFoto] = useState('')
  const [pagar, setPagar] = useState('false')
  const [reservar, setReservar] = useState('false')
  const [redirigir, setRedirigir] = useState('false')


  //Peticion para traer el listado actualizado
  const actualizarListado = () => {
    axios.get('http://localhost:5000/obtenerListado').then((res) => {
      console.log(res.data)
      console.log(codigo.codigo)
      let capbuscado = res.data.filter(cap => cap.nombre === codigo.codigo)

      setNombre(capbuscado[0].nombre)
      setPrecio(capbuscado[0].precio)
      setDescripcion(capbuscado[0].descripcion)
      setFoto(capbuscado[0].foto)
      setEstado(capbuscado[0].estado)

    })
      .catch((error) => {
        console.log(error);
      })

  }


  const pagarChapter = (nombre) => {

    if (estado === 'reservado') {
      axios({
        "method": "POST",
        "url": "http://localhost:5000/pagarCapitulo",
        "params": {
          "capitulo": nombre.nombre,
        }
      }
      ).then((res) => {
        if (res.data === 'Pagado') {
          Swal.fire({
            title: 'Episodio Alquilado!',
            text: 'Usted alquilo' + nombre.nombre + '. El alquiler es por 24hs. a partir de este momento tiene un día para disfrutar.',

          }).then((result) => {
            if (result.value) {
              let link = '/'
              window.location.href = link
            }
          })


        }
      }).catch((error) => {
        console.log(error);
      })
    }

  }

  //PETICION PARA RESERVAR UN CAPITULO
  const reservarCapitulo = (nombre) => {

    if (estado === 'disponible') {

      console.log(nombre.nombre)
      axios({
        "method": "POST",
        "url": "http://localhost:5000/reservarCapitulo",
        "params": {
          "capitulo": nombre.nombre,
        }
      }
      ).then((res) => {
        if (res.data === 'Reservado con exito') {
          Swal.fire({
            title: 'Episodio Reservado!',
            text: 'Recuerde que la reserva es por 4 minutos si en ese lapso no abona el episodio la reserva será cancelada.',

          }).then((result) => {
            if (result.value) {
              let link = '/'
              window.location.href = link
            }
          })
        }

      }).catch((error) => {
        console.log(error);
      })
    }
  }


  const Style = {
    float: 'left',
    // paddingLeft: '10px',
    paddingTop: '10px',
    // marginLeft: '57px',
    position: 'relative',
    widht: '45%',
    height: 'auto',
    // marginRight: 'auto',
    // marginLeft: 'auto'
  }

  const vaderStyle = {
    marginTop: '10px',
    float: 'right',
    paddingTop: '10px',
    width: '45%',
    height: 'auto',
    paddingleft: '10px',
    position: 'relative',
    marginRight: 'auto',
    marginLeft: 'auto'


  }

  const content = {
    widht: '100%'
  }

  const container = {


  }

  const body = {
    backgroundImage: `url(${fondo})`,
    backgroundPosition: 'center',
    height: '100vh',
    overflowY: 'hidden',
    overflowX: 'hidden'
  }


  const t = {
    widht: '100%',

  }

  useEffect(() => {

    actualizarListado();

    ;


  }, [])

  const btnreservar = () => {
    if (estado === 'disponible') {
      return false
      //this.button.disabled = false;
    }
    else {
      //this.button.disabled = true;
      return true
    }
  }

  const btnpagar = () => {
    if (estado === 'disponible') {
      return true
      //this.button.disabled = false;
    } else {
      //this.button.disabled = true;
      return false
    }
  }



  return (

    <body style={body}>
      <div className="container col-xl-12 ml-0 mr-0" >
        <div class=" content col-xl-6" style={vaderStyle} >
          <div class="right" >

            <div align="center">
              <ul>

                <h4 class="animated fadeInRight text-info"> Precio : ${precio} </h4>

                <button type="button" class="btn btn-info btn-sm mr-2 animated fadeInRight delay-1s" disabled={btnreservar()} onClick={() => reservarCapitulo({ nombre })} >Reservar</button>

                <button type="button" class="btn btn-info btn-sm mr-3 animated fadeInRight delay-1s " disabled={btnpagar()} onClick={() => pagarChapter({ nombre })}>Alquilar</button>

                <Link to="/" type="button" class="btn btn-info btn-sm mr-2 animated fadeInRight delay-1s">Home</Link>
              </ul>
            </div>
          </div>

        </div>

        <div className="content col-xl-6 mr-5 pr-5 mb-3" style={Style}>
          <div class="left" >

            <div >
              <img class="img-fluid animated fadeInLeft" align="left" src={foto} alt="" width="400" height="500" />
            </div>

          </div>

        </div>

        <div class="col-sm-6 text-center ml-0 animated fadeInLeft" style={t} >
          <h3 className="mb-3 text-info" align="left" >{nombre}</h3>
          {/*<figcaption className="text-justify text-xs-left text-danger">{descripcion}</figcaption>*/}
        </div>
      </div>
    </body>
  )
}

export default VerCapi;
