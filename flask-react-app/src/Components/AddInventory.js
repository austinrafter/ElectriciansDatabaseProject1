import { useState } from 'react';
import APIServiceTwelve from '../Components/APIServiceTwelve.js'
import InventoryList from '../Components/InventoryList';


const AddInventory = (props) => {
    const insertedInventory = (inventory) =>{
        const new_inventory = [...inventorys,inventory]
        setInventorys(new_inventory)
    }

    const [material_name, setMaterialName] = useState('')
    const [cost_per_unit, setCostPerUnit] = useState('')
    const [weight_per_unit, setWeightPerUnit] = useState('')
    const [general_managers, setGeneralManagers] = useState([]);
    const [inventorys, setInventorys] = useState([]);

    const checkInventory = () =>{
    APIServiceTwelve.InsertInventory({material_name,cost_per_unit,weight_per_unit})
    .then((response) => setInventorys(response))
          .catch(error => console.log('error',error))
          }

    const handleSubmit=(event)=>{
          event.preventDefault()
          checkInventory()
          setMaterialName('')
          setCostPerUnit('')
          setWeightPerUnit('')
        }

        const [showFormTwo, setShowFormTwo] = useState(false);

        const toggleShowFormTwo = () => {
        setShowFormTwo(!showFormTwo);
        }

      return (
           <div>
           <h2> Enter your information to see the right info about jobs </h2>
             <form onSubmit = {handleSubmit} >

                     <label htmlFor="material_name" className="form-label">Material Name</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter material name"
                     value={material_name}
                     onChange={(e)=>setMaterialName(e.target.value)}
                     required
                     />

                      <label htmlFor="cost_per_unit" className="form-label">Cost per unit</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter cost per unit"
                      value={cost_per_unit}
                      onChange={(e)=>setCostPerUnit(e.target.value)}
                      required
                      />

                      <label htmlFor="weight_per_unit" className="form-label">Weight per unit</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter weight_per_unit"
                      value={weight_per_unit}
                      onChange={(e)=>setWeightPerUnit(e.target.value)}
                      required
                      />

                     <button
                     className="btn btn-primary mt-2"
                     >
                     Add inventory</button>

                   </form>

                <div>
            <InventoryList inventorys={inventorys}/>
            </div>
           </div>
      )}


export default AddInventory;
