import { Button } from 'react-bootstrap';
import React from 'react';

const WorkPackagesList = (props) => {
    return (
        <div className="mt-2">
        {/* Display the article details if article is not None */}
        <h1> Work Packages </h1>
        {props.work_packages && props.work_packages.map(work_package =>{
        return (

        <div key= { work_package.work_package_id }>
        <h2 variant="text-primary" size="lg">
        { work_package.work_package_name}
         </h2>
         <h3> Job name </h3>
         <p> { work_package.job_site } </p>
         <h3> Price of work </h3>
        <p> { work_package.price_of_work } </p>
        <h3> Hours alloted </h3>
        <p> { work_package.hours_alloted } </p>
        <h3> Price hours used </h3>
        <p> { work_package.hours_used } </p>
        <hr/>
        </div>
    )
        })}
    </div>
    )
}

export default WorkPackagesList;