import { useState, useEffect } from "react";
import PositionAuthenticationFormTwo from '../Components/AuthenticateSalariedEmployeesTwo';
import Work_Package_Form from '../Components/Work_Package_Form';
import Work_Package_Form_Delete from '../Components/Delete_Work_Package';
import AddInventory from '../Components/AddInventory';

const Project_Manager = () => {

 const findProjectManager = (project_manager) =>{
    const new_projectManager = [...project_managers,project_manager]
    setProjectManagers(new_projectManager)
  }
  const addWorkPackage = (work_package) =>{
    const new_workPackages = [...work_packages,work_package]
    setWorkPackages(new_workPackages)
  }
  const addInventory = (inventory) =>{
    const new_inventory = [...inventorys,inventory]
    setWorkPackages(new_inventory)
  }

  const addElectricianToWorkPackage = (electrician_on_work_package) =>{
    const new_electricianOnWorkPackages = [...electricians_on_work_packages,electrician_on_work_package]
    setElectriciansOnWorkPackages(new_electricianOnWorkPackages)
  }

  const addMaterialToWorkPackage = (material_in_work_package) =>{
    const new_materialInWorkPackages = [...materials_in_work_package,material_in_work_package]
    setMaterialsInWorkPackages(new_materialInWorkPackages)
  }

  const [project_managers, setProjectManagers] = useState([]);
  const [work_packages, setWorkPackages] = useState([]);
  const [inventorys, setInventorys] = useState([]);
  const [electricians_on_work_packages, setElectriciansOnWorkPackages] = useState([]);
  const [materials_in_work_package, setMaterialsInWorkPackages] = useState([]);

  const [showFormNine, setShowFormNine] = useState(false);
  const [showFormEight, setShowFormEight] = useState(false);
  const [showFormSeven, setShowFormSeven] = useState(false);
  const [showFormSix, setShowFormSix] = useState(false);
  const [showFormFive, setShowFormFive] = useState(false);
  const [showFormFour, setShowFormFour] = useState(false);
  const [showFormThree, setShowFormThree] = useState(false);
  const [showFormTwo, setShowFormTwo] = useState(false);
  const [showForm, setShowForm] = useState(false);

  const toggleShowFormNine = () => {
    setShowFormNine(!showFormNine);
  }
  const toggleShowFormEight = () => {
    setShowFormEight(!showFormEight);
  }
  const toggleShowFormSeven = () => {
    setShowFormSeven(!showFormSeven);
  }
  const toggleShowFormSix = () => {
    setShowFormSix(!showFormSix);
  }
  const toggleShowFormFive = () => {
    setShowFormFive(!showFormFive);
  }
  const toggleShowFormFour = () => {
    setShowFormFour(!showFormFour);
  }

  const toggleShowFormThree = () => {
    setShowFormThree(!showFormThree);
  }
  const toggleShowFormTwo = () => {
    setShowFormTwo(!showFormTwo);
  }
  const toggleShowForm = () => {
    setShowForm(!showForm);
  }

   return(
  <div>
   <button
          onClick={toggleShowFormThree}
          className="btn btn-primary"
           >
             Are you a project manager? See information about jobs here.
        <i className="bi bi-pencil-square m-2"></i>
        </button>
        {showFormThree && (
          <PositionAuthenticationFormTwo
          findProjectManager = {findProjectManager}
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
          onClick={toggleShowForm}
          className="btn btn-primary"
           >
             Delete a work package from a job
        <i className="bi bi-pencil-square m-2"></i>
        </button>
        {showForm && (
          <Work_Package_Form_Delete
          addWorkPackage = {addWorkPackage}
            />
            )}
            <hr/>
      <button
          onClick={toggleShowFormFour}
          className="btn btn-primary"
           >
             Add inventory
        <i className="bi bi-pencil-square m-2"></i>
        </button>
        {showFormFour && (
          <AddInventory
          addInventory = {addInventory}
            />
            )}
            <hr/>

  </div>

  )
};

export default Project_Manager;