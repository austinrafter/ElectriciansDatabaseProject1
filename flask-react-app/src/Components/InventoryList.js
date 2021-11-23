import { Button } from 'react-bootstrap';
import React from 'react';

const InventoryList = (props) => {
    return (
        <div className="mt-2">
        {/* Display the article details if article is not None */}
        <h1> Inventory </h1>
        {props.inventorys && props.inventorys.map(inventory =>{
        return (

        <div key= { inventory.inventory_id }>
        <h2 variant="text-primary" size="lg">
        { inventory.material_name}
         </h2>
         <h3> Cost per unit </h3>
         <p> { inventory.cost_per_unit } </p>
         <h3> Weight per unit </h3>
        <p> { inventory.weight_per_unit } </p>
        <hr/>
        </div>
    )
        })}
    </div>
    )
}

export default InventoryList;