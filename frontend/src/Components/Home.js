import React, { useState, useEffect, Component } from 'react'
import { Link } from 'react-router-dom'
import $ from 'jquery'
import axios from 'axios'
import fondo from '../Images/background.jpg'
/*/home/mag/Nosql/flask-redis/frontend/src/Images/background.jpg

/*import Card from './Card'*/
import CardExample from './Card'



class Home extends Component {

    state = {
        listado: []
    }

    actualizarListado() {
        axios.get('http://localhost:5000/obtenerListado').then((res) => {
            this.setState({ listado: res.data })
            console.log(this.state.listado)
        })
            .catch((error) => {
                console.log(error);
            })

    }

    componentDidMount() {
        this.actualizarListado()
    }

    style = {
        backgroundImage: `url(${fondo})`,
        backgroundSize: '100% 100%',
        overflowY: 'hidden',
        overflowX: 'hidden'
    }

    render() {

        return (
            
            <div style={this.style}>
                <div align="center">
                    <div className="grillita" >
                        <div className="row row-cols-1 row-cols-md-3" >
                            {this.state.listado.map(list => (
                                /*<Card*/
                                <CardExample
                                    list={list}
                                />
                            ))}
                        </div>

                    </div>
                </div>
            </div>
        )
    }


}
export default Home;