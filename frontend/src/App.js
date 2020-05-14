import React from 'react';
import {BrowserRouter as Router, Route, Link, Switch} from 'react-router-dom'

import Home from './Components/Home'
import VerCapi from './Components/VerCapi'

function App() {
  return (

   <Router>
     <Switch>

      <Route exact path = "/" component ={Home}/>

       <Route  exact path="/ver-capi/:nombre" render ={
         props =>{
          const  codigoCap = String((props.match.params.nombre));
         return (<VerCapi
         codigo = {codigoCap}
         />)

          }
         
       }></Route>

     </Switch>


   </Router>
  );
}

export default App;
