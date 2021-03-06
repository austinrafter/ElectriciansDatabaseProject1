import { Button } from 'react-bootstrap';
import React from 'react';

const EmployeesList = (props) => {
    return (
        <div className="mt-2">
        {/* Display the article details if article is not None */}
        {props.employees && props.employees.map(employee =>{
        return (

        <div key= { employee.employee_id }>
        <h2 variant="text-primary" size="lg">
        { employee.position}
         </h2>
         <h3>  Name </h3>
         <p> { employee.first_name }  {employee.last_name} </p>
         <h3> Position </h3>
         <p> {employee.position} </p>
        <h3> Years Employed </h3>
        <p> { employee.years_employed } </p>
        <hr/>
        </div>
    )
        })}
    </div>
    )
}

export default EmployeesList;