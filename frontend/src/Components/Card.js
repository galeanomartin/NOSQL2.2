import React, { useState } from 'react'
import { Redirect } from 'react-router-dom'

import { MDBBtn, MDBCard, MDBCardBody, MDBCardImage, MDBCardTitle, MDBCardText, MDBCol } from 'mdbreact';

function CardExample(list) {
  const [verCapitulo, estado] = useState('false')

  const Style = {
    width: '18rem',
    marginTop: '20px'
  }

  if (verCapitulo === 'true') {
    return (<Redirect to={`/ver-capi/${list.list.nombre}`} />)
    // return (<Redirect to={`/ver-capi/${list.list.nombre}`}/>)       

  }

  const verificaEstado = () => {
    if ((list.list.estado === 'reservado') || (list.list.estado === 'alquilado')) {
      return 'btn btn-danger mr-3'
    } else if (list.list.estado === 'disponible') {
      return 'btn btn-info mr-3'
    } else {
      return 'btn btn-info mr-3'
    }
  }

  const btnapagado = () => {
    if ((list.list.estado === 'alquilado')) {
      return true
      //this.button.disabled = false;
    } else {
      //this.button.disabled = true;
      return false
    }
  }


  return (

    <MDBCol style={{ maxWidth: "22rem" }}>

      <MDBCard>
        <MDBCardImage className="img-fluid" src={list.list.foto} style={Style}
          waves />
        <MDBCardBody>
          <MDBCardTitle>{list.list.nombre}</MDBCardTitle>
          <MDBCardText>{list.list.descripcion}</MDBCardText>
          {/*<MDBBtn href="#">Click</MDBBtn>*/}

          <button class={verificaEstado()} disabled >{list.list.estado}</button>

          <button class="btn btn-success mr-3" disabled={btnapagado()} onClick={() => estado('true')} >Reservar/Alquilar</button>


        </MDBCardBody>
      </MDBCard>
    </MDBCol>
  )
}


export default CardExample;


