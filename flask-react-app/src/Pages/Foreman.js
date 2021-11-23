import { useState, useEffect } from "react";
import PositionAuthenticationForm from '../Components/Authenticate_Salaried_Employees';
import Work_Package_Form from '../Components/Work_Package_Form';
import Work_Package_Form_Delete from '../Components/Delete_Work_Package';
import AddInventory from '../Components/AddInventory';
import DeleteInventory from '../Components/DeleteInventory';
import AddElectricianOnWorkPackage from '../Components/AddElectricianOnWorkPackage';
import DeleteElectricianOffWorkPackage from '../Components/DeleteElectricianOffWorkPackage';
import AddMaterialToWorkPackage from '../Components/AddMaterialToWorkPackage';
import DeleteMaterialOffWorkPackage from '../Components/DeleteMaterialOffWorkPackage';

const Foreman = () => {

const findForeman = (foreman) =>{
    const new_salariedEmployee = [...foremen,foreman]
    setForemen(new_salariedEmployee)
  }
const addWorkPackage = (work_package) =>{
    const new_workPackages = [...work_packages,work_package]
    setWorkPackages(new_workPackages)
  }

const addInventory = (inventory) =>{
    const new_inventory = [...inventorys,inventory]
    setWorkPackages(new_inventory)
  }

const addElectricianOnWorkPackage = (electrician_on_work_package) =>{
    const new_electricianOnWorkPackage = [...electricians_on_work_packages,electrician_on_work_package]
    setElectricansOnWorkPackages(new_electricianOnWorkPackage)
  }

 const addMaterialToWorkPackage = (material_on_work_package) =>{
    const new_materialInWorkPackages = [...materials_on_work_packages,material_on_work_package]
    setMaterialsInWorkPackages(new_materialInWorkPackages)
  }

 const [foremen, setForemen] = useState([]);
 const [work_packages, setWorkPackages] = useState([]);
 const [inventorys, setInventorys] = useState([]);
 const [electricians_on_work_packages, setElectricansOnWorkPackages]= useState([]);
 const [materials_on_work_packages, setMaterialsInWorkPackages] = useState([]);


  const [showForm, setShowForm] = useState(false);
  const [showFormTwo, setShowFormTwo] = useState(false);
  const [showFormThree, setShowFormThree] = useState(false);
  const [showFormFour, setShowFormFour] = useState(false);
  const [showFormFive, setShowFormFive] = useState(false);
  const [showFormSix, setShowFormSix] = useState(false);
  const [showFormSeven, setShowFormSeven] = useState(false);
  const [showFormEight, setShowFormEight] = useState(false);
  const [showFormNine, setShowFormNine] = useState(false);


  const toggleShowForm = () => {
    setShowForm(!showForm);
  }

  const toggleShowFormTwo = () => {
    setShowFormTwo(!showFormTwo);
  }

  const toggleShowFormThree = () => {
    setShowFormThree(!showFormThree);
  }

  const toggleShowFormFour = () => {
    setShowFormFour(!showFormFour);
  }

  const toggleShowFormFive = () => {
    setShowFormFive(!showFormFive);
  }

  const toggleShowFormSix = () => {
    setShowFormSix(!showFormSix);
  }

  const toggleShowFormSeven = () => {
    setShowFormSeven(!showFormSeven);
  }

  const toggleShowFormEight = () => {
    setShowFormEight(!showFormEight);
  }

  const toggleShowFormNine = () => {
    setShowFormNine(!showFormNine);
  }

  return(
  <div>
  <button
          onClick={toggleShowForm}
          className="btn btn-primary"
           >
             Are you a foreman? See information about jobs here.
        <i className="bi bi-pencil-square m-2"></i>
        </button>
        {showForm && (
          <PositionAuthenticationForm
          findForeman = {findForeman}
            />
            )}
            <hr/>

   <button
          onClick={toggleShowFormTwo}
          className="btn btn-primary"
           >
             Add a work package to a job
        <i className="bi bi-pencil-square m-2"></i>
        </button>
        {showFormTwo && (
          <Work_Package_Form
          addWorkPackage = {addWorkPackage}
            />
            )}
            <hr/>
   <button
          onClick={toggleShowFormThree}
          className="btn btn-primary"
           >
             Delete a work package from a job
        <i className="bi bi-pencil-square m-2"></i>
        </button>
        {showFormThree && (
          <Work_Package_Form_Delete
          addWorkPackage = {addWorkPackage}
            />
            )}
            <hr/>
   <button
          onClick={toggleShowFormFour}
          className="btn btn-primary"
           >
             Add inventory to system

        <i className="bi bi-pencil-square m-2"></i>
        </button>
        {showFormFour && (
          <AddInventory
          addInventory = {addInventory}
            />
            )}
            <hr/>

      <button
          onClick={toggleShowFormFive}
          className="btn btn-primary"
           >
             Delete inventory from system
        <i className="bi bi-pencil-square m-2"></i>
        </button>
        {showFormFive && (
          <DeleteInventory
          addInventory = {addInventory}
            />
            )}
            <hr/>

      <button
          onClick={toggleShowFormSix}
          className="btn btn-primary"
           >
             Add electrician to work package
        <i className="bi bi-pencil-square m-2"></i>
        </button>
        {showFormSix && (
          <AddElectricianOnWorkPackage
          addElectricianOnWorkPackage = {addElectricianOnWorkPackage}
            />
            )}
            <hr/>

      <button
          onClick={toggleShowFormSeven}
          className="btn btn-primary"
           >
             Delete electrician from work package
        <i className="bi bi-pencil-square m-2"></i>
        </button>
        {showFormSeven && (
          <DeleteElectricianOffWorkPackage
          addElectricianOnWorkPackage = {addElectricianOnWorkPackage}
            />
            )}
            <hr/>

      <button
          onClick={toggleShowFormEight}
          className="btn btn-primary"
           >
             Add material to work package
        <i className="bi bi-pencil-square m-2"></i>
        </button>
        {showFormEight && (
          <AddMaterialToWorkPackage
          addMaterialToWorkPackage = {addMaterialToWorkPackage}
            />
            )}
            <hr/>

      <button
          onClick={toggleShowFormNine}
          className="btn btn-primary"
           >
             Delete material from work package
        <i className="bi bi-pencil-square m-2"></i>
        </button>
        {showFormNine && (
          <DeleteMaterialOffWorkPackage
          addMaterialToWorkPackage = {addMaterialToWorkPackage}
            />
            )}
            <hr/>
  </div>
  )

};

export default Foreman;