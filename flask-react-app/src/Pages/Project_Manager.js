import { useState, useEffect } from "react";
import PositionAuthenticationFormTwo from '../Components/AuthenticateSalariedEmployeesTwo';
import Work_Package_Form from '../Components/Work_Package_Form';
import Work_Package_Form_Delete from '../Components/Delete_Work_Package';

const Project_Manager = () => {

 const findProjectManager = (project_manager) =>{
    const new_projectManager = [...project_managers,project_manager]
    setProjectManagers(new_projectManager)
  }
  const addWorkPackage = (work_package) =>{
    const new_workPackages = [...work_packages,work_package]
    setWorkPackages(new_workPackages)
  }

  const [project_managers, setProjectManagers] = useState([]);
  const [work_packages, setWorkPackages] = useState([]);


  const [showFormThree, setShowFormThree] = useState(false);
  const [showFormTwo, setShowFormTwo] = useState(false);
  const [showForm, setShowForm] = useState(false);

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
  </div>

  )
};

export default Project_Manager;