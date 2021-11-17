import { useState, useEffect } from "react";
import PositionAuthenticationFormThree from '../Components/AuthenticateSalariedEmployeesThree';
import JobForm from '../Components/Job_form';

const General_Manager = () => {

const insertedJob = (job) =>{
    const new_jobs = [...jobs,job]
    setJobs(new_jobs)
  }

  const findGeneralManager = (general_manager) =>{
    const new_generalManager = [...general_managers,general_manager]
    setGeneralManagers(new_generalManager)
  }

  const [general_managers, setGeneralManagers] = useState([]);
  const [jobs, setJobs] = useState([]);
  const [showFormTwo, setShowFormTwo] = useState(false);
  const [showFormFour, setShowFormFour] = useState(false);

  const toggleShowFormTwo = () => {
    setShowFormTwo(!showFormTwo);
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
  </div>
  )

};

export default General_Manager;