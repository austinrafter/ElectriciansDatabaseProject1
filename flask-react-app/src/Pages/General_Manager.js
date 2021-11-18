import { useState, useEffect } from "react";
import PositionAuthenticationFormThree from '../Components/AuthenticateSalariedEmployeesThree';
import JobForm from '../Components/Job_form';
import Employee_Form from '../Components/Employee_Form';
import JobFormDelete from '../Components/JobFormDelete';

const General_Manager = () => {

const insertedJob = (job) =>{
    const new_jobs = [...jobs,job]
    setJobs(new_jobs)
  }

const findEmployee = (employee) =>{
    const new_Employee = [...employees,employee]
    setEmployees(new_Employee)
  }

  const findGeneralManager = (general_manager) =>{
    const new_generalManager = [...general_managers,general_manager]
    setGeneralManagers(new_generalManager)
  }

  const [general_managers, setGeneralManagers] = useState([]);
  const [jobs, setJobs] = useState([]);
  const [employees, setEmployees] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [showFormTwo, setShowFormTwo] = useState(false);
  const [showFormThree, setShowFormThree] = useState(false);
  const [showFormFour, setShowFormFour] = useState(false);

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


  return(
  <div>
    <button
          onClick={toggleShowFormFour}
          className="btn btn-primary"
           >
             Are you a general manager? See information about jobs here.
        <i className="bi bi-pencil-square m-2"></i>
        </button>
        {showFormFour && (
          <PositionAuthenticationFormThree
          findGeneralManager = {findGeneralManager}
            />
            )}
    <div>
    <button
          onClick={toggleShowFormTwo}
          className="btn btn-primary"
           >
             Add a job
        <i className="bi bi-pencil-square m-2"></i>
        </button>
         {showFormTwo && (
          <JobForm
          insertedJob = {insertedJob}
            />
            )}
            </div>
    <div>
    <button
          onClick={toggleShowFormThree}
          className="btn btn-primary"
           >
             Delete a job
        <i className="bi bi-pencil-square m-2"></i>
        </button>
         {showFormThree && (
          <JobFormDelete
          insertedJob = {insertedJob}
            />
            )}
            </div>
     <div>
    <button
          onClick={toggleShowForm}
          className="btn btn-primary"
           >
             Add an employee
        <i className="bi bi-pencil-square m-2"></i>
        </button>
         {showForm && (
          <Employee_Form
          findEmployee = {findEmployee}
            />
            )}
            </div>

  </div>
  )

};

export default General_Manager;