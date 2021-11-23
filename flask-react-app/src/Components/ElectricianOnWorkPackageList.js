import { Button } from 'react-bootstrap';
import React from 'react';

const ElectricianOnWorkPackageList = (props) => {
    return (
        <div className="mt-2">
        {/* Display the article details if article is not None */}
        <h1> Electrician On Work Package </h1>
        {props.electricians_on_packages && props.electricians_on_packages.map(electricians_on_package =>{
        return (

        <div key= { electricians_on_package.electricians_on_package_id }>
        <h2 variant="text-primary" size="lg">
        { electricians_on_package.first_name}
         </h2>
         <h2> { electricians_on_package.last_name } </h2>
         <h3> Work Package </h3>
        <p> { electricians_on_package.work_package_name } </p>
        <h3> Job site </h3>
        <p> { electricians_on_package.site_name } </p>
        <hr/>
        </div>
    )
        })}
    </div>
    )
}

export default ElectricianOnWorkPackageList;