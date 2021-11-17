import { Button } from 'react-bootstrap';
import React from 'react';

const ProjectManagersList = (props) => {
    return (
        <div className="mt-2">
        {/* Display the article details if article is not None */}
        {props.project_managers && props.project_managers.map(project_manager =>{
        return (

        <div key = {project_manager.project_manager_id}>
        <h2>Project Managers View </h2>
        <h2 variant="text-primary" size="lg">
        { project_manager.work_package_name}
         </h2>
         <h3> Job name </h3>
         <p> { project_manager.site_name } </p>
         <h3> Material Cost</h3>
        <p> { project_manager.material_cost } </p>
        <h3> Hours used</h3>
        <p> { project_manager.hours_used } </p>
        <h3> Work Package cost </h3>
        <p> { project_manager.work_package_cost } </p>
        <h3> Amount made </h3>
        <p> { project_manager.amount_made } </p>
        <h3> Total profits </h3>
        <p> { project_manager.total_profits } </p>
        <hr/>
        </div>
    )
        })}
    </div>
    )
}

export default ProjectManagersList;