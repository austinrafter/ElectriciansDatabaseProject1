import './App.css';
import JobForm from './Components/Job_form';
import JobsList from './Components/JobsList';
import WorkPackagesList from './Components/Work_Packages_List';
import PositionAuthenticationForm from './Components/Authenticate_Salaried_Employees';
import { useState, useEffect } from "react";
import ForemansList from './Components/ForemansList';
import ProjectManagersList from './Components/ProjectManagersList';
import GeneralManagersList from './Components/GeneralManagersList';
import PositionAuthenticationFormTwo from './Components/AuthenticateSalariedEmployeesTwo';
import PositionAuthenticationFormThree from './Components/AuthenticateSalariedEmployeesThree';


function App() {
 const insertedJob = (job) =>{
    const new_jobs = [...jobs,job]
    setJobs(new_jobs)
  }

  const findForeman = (foreman) =>{
    const new_salariedEmployee = [...foremans,foreman]
    setForemans(new_salariedEmployee)
  }

   const findProjectManager = (project_manager) =>{
    const new_salariedEmployee = [...project_managers,project_manager]
    setProjectManagers(new_salariedEmployee)
  }

   const findGeneralManager = (general_manager) =>{
    const new_salariedEmployee = [...general_managers,general_manager]
    setGeneralManagers(new_salariedEmployee)
  }

  const [jobs, setJobs] = useState([]);
  const [foremans, setForemans] = useState([]);
  const [project_managers, setProjectManagers] = useState([]);
  const [general_managers, setGeneralManagers] = useState([]);


 // define variables for the present state of the form and another to change its state
  const [showForm, setShowForm] = useState(false);
  const [showFormTwo, setShowFormTwo] = useState(false);
  const [showFormThree, setShowFormThree] = useState(false);
  const [showFormFour, setShowFormFour] = useState(false);

 // toggle between the two states,visible and hidden
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

    useEffect(()=>{
      fetch('http://localhost:5000/jobs',{
        'methods':'GET',
        headers : {
          'Content-Type':'application/json'
        }
      })
      .then(response => response.json())
      .then(response => setJobs(response))
      .catch(error => console.log(error))
    },[]);


  return (
      <div className="App container m-4">
      <div className="row">
      <div className="text-center">
      <h1>Welcome to SJ Electric Company.</h1>
        </div>
        </div>
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
              <button
          onClick={toggleShowForm}
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
              <button
          onClick={toggleShowForm}
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
        <ForemansList foremans = {foremans} />
        <ProjectManagersList project_managers = {project_managers} />
        <GeneralManagersList general_managers = {general_managers} />
        <h2>Jobs</h2>
        <JobsList
         jobs={jobs}
         />
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

  );
}


export default App;
