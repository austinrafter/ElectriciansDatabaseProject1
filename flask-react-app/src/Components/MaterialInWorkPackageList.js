import { Button } from 'react-bootstrap';
import React from 'react';

const MaterialInWorkPackageList = (props) => {
    return (
        <div className="mt-2">
        {/* Display the article details if article is not None */}
        <h1> Inventory </h1>
        {props.materials_on_work_packages && props.materials_on_work_packages.map(material_on_work_package =>{
        return (

        <div key= { material_on_work_package.material_in_work_package_id }>
        <h2 variant="text-primary" size="lg">
        { material_on_work_package.material_name}
         </h2>
         <h3> Amount Alloted </h3>
         <p> { material_on_work_package.amount_alloted } </p>
         <h3> Amount used </h3>
        <p> { material_on_work_package.amount_used } </p>
        <h3> Work package </h3>
        <p> { material_on_work_package.work_package_name } </p>
        <h3> Site of work package </h3>
        <p> { material_on_work_package.site_name } </p>
        <hr/>
        </div>
    )
        })}
    </div>
    )
}

export default MaterialInWorkPackageList;