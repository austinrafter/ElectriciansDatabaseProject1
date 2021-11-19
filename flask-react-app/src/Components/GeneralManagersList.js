import { Button } from 'react-bootstrap';
import React from 'react';

const GeneralManagersList = (props) => {
    return (
        <div className="mt-2">
        <h3> "If you only see 1 job with all zeroes then you are not a general manager and are not meant to be here"</h3>
        {/* Display the article details if article is not None */}
        {props.general_managers && props.general_managers.map(general_manager =>{
        return (
        <div key = {general_manager.general_manager_id}>
        <h2>General Managers View </h2>
        <h2 variant="text-primary" size="lg">
        { general_manager.cost_of_project}
         </h2>
         <h3> Project cost </h3>
         <p> { general_manager.cost_of_project } </p>
         <h3> Amount made on project</h3>
        <p> { general_manager.amount_made } </p>
        <h3> Project profits</h3>
        <p> { general_manager.total_profits } </p>
        <h3> Days on project </h3>
        <p> { general_manager.number_of_days_on_project } </p>
        <hr/>
        </div>
    )
        })}
    </div>
    )
}

export default GeneralManagersList;