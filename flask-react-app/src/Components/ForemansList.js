import { Button } from 'react-bootstrap';
import React from 'react';

const ForemansList = (props) => {
    return (
        <div className="mt-2">
        {/* Display the article details if article is not None */}
        {props.foremans && props.foremans.map(foreman =>{
        return (

        <div key = {foreman.foreman_id}>
        <h2> Foremans View </h2>
        <h2 variant="text-primary" size="lg">
        { foreman.work_package_name}
         </h2>
         <h3> Job name </h3>
         <p> { foreman.site_name } </p>
         <h3> Worker</h3>
        <p> { foreman.worker_first_name } </p>
        <p> { foreman.worker_last_name } </p>
        <h3> Hours alloted to worker </h3>
        <p> { foreman.individual_hours_alloted } </p>
        <hr/>
        </div>
    )
        })}
    </div>
    )
}

export default ForemansList;