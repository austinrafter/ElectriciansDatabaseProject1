import { useState, useEffect } from "react";
import PositionAuthenticationForm from '../Components/Authenticate_Salaried_Employees';
import Work_Package_Form from '../Components/Work_Package_Form';
import Work_Package_Form_Delete from '../Components/Delete_Work_Package';

const Foreman = () => {

const findForeman = (foreman) =>{
    const new_salariedEmployee = [...foremen,foreman]
    setForemen(new_salariedEmployee)
  }
const addWorkPackage = (work_package) =>{
    const new_workPackages = [...work_packages,work_package]
    setWorkPackages(new_workPackages)
  }

 const [foremen, setForemen] = useState([]);
 const [work_packages, setWorkPackages] = useState([]);


  const [showForm, setShowForm] = useState(false);
  const [showFormTwo, setShowFormTwo] = useState(false);
  const [showFormThree, setShowFormThree] = useState(false);

  const toggleShowForm = () => {
    setShowForm(!showForm);
  }

  const toggleShowFormTwo = () => {
    setShowFormTwo(!showFormTwo);
  }

  const toggleShowFormThree = () => {
    setShowFormThree(!showFormThree);
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
  </div>
  )

};

export default Foreman;