import { useState, useEffect } from "react";
import InventoryList from '../Components/InventoryList';

const Inventory = () => {
const [inventorys, setInventorys] = useState([]);

useEffect(()=>{
      fetch('http://localhost:5000/inventory',{
        'methods':'GET',
        headers : {
          'Content-Type':'application/json'
        }
      })
      .then(response => response.json())
      .then(response => setInventorys(response))
      .catch(error => console.log(error))
    },[]);

    return(
    <div>
    <h1>Inventory</h1>
        <InventoryList
         inventorys={inventorys}
         />
         </div>
    )

};

export default Inventory;