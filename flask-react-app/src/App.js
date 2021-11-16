import './App.css';
import JobForm from './Components/Job_form';
import JobsList from './Components/JobsList';
import WorkPackagesList from './Components/Work_Packages_List'
import PositionAuthenticationForm from './Components/Authenticate_Salaried_Employees'
import { useState, useEffect } from "react";



function App() {
 const insertedJob = (job) =>{
    const new_jobs = [...jobs,job]
    setJobs(new_jobs)
  }

  const salariedEmployee = (employee) =>{
    const new_salariedEmployee = [...employees,employee]
    salariedEmployee(new_salariedEmployee)
  }

  const [jobs, setJobs] = useState([]);
  const [employees, setEmployees] = useState([]);

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
        <h2>Are you supposed to be here? find out</h2>
        <PositionAuthenticationForm salariedEmployee = {salariedEmployee} />
        <h2>Jobs</h2>
        <JobsList
         jobs={jobs}
         />
         <JobForm insertedJob={insertedJob} />

         </div>

  );
}


export default App;
