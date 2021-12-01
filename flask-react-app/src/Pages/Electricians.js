import { useState, useEffect } from "react";
import EmployeesList from '../Components/EmployeesList';

const Electricians = () => {
const [employees, setEmployees] = useState([]);

useEffect(()=>{
      fetch('http://localhost:5000/flaskapi/electricians',{
        'methods':'GET',
        headers : {
          'Content-Type':'application/json'
        }
      })
      .then(response => response.json())
      .then(response => setEmployees(response))
      .catch(error => console.log(error))
    },[]);

    return(
    <div>
    <h1>Electricians</h1>
        <EmployeesList
         employees={employees}
         />
         </div>
    )

};

export default Electricians;