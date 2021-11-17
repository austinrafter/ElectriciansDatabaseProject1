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
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Foreman from "./Pages/Foreman";
import Project_Manager from "./Pages/Project_Manager";
import General_Manager from "./Pages/General_Manager";
import Jobs from "./Pages/Jobs";
import Home from "./Pages/Home";

function App() {
 const insertedJob = (job) =>{
    const new_jobs = [...jobs,job]
    setJobs(new_jobs)
  }

  const findForeman = (foreman) =>{
    const new_salariedEmployee = [...foremen,foreman]
    setForemen(new_salariedEmployee)
  }

   const findProjectManager = (project_manager) =>{
    const new_projectManager = [...project_managers,project_manager]
    setProjectManagers(new_projectManager)
  }

   const findGeneralManager = (general_manager) =>{
    const new_generalManager = [...general_managers,general_manager]
    setGeneralManagers(new_generalManager)
  }

  const [jobs, setJobs] = useState([]);
  const [foremen, setForemen] = useState([]);
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
      <Router>
      <div>
        <Link to="/">Home</Link>
      </div>
      <div>
        <Link to="/jobs">Jobs</Link>
      </div>
      <div>
        <Link to="/general_manager">General Managers</Link>
      </div>
      <div>
        <Link to="/project_manager">Project Managers</Link>
      </div>
      <div>
        <Link to="/foreman">Foremen</Link>
      </div>

      <hr />

      <Routes>
      <Route path="/" element={<Home />}>
        </Route>
        <Route path="/jobs" element={<Jobs />}>
        </Route>
        <Route path="/general_manager" element={<General_Manager />}>
        </Route>
        <Route path="/project_manager" element={<Project_Manager />}>
        </Route>
        <Route path="/foreman" element={<Foreman />}>
        </Route>
      </Routes>
    </Router>
        </div>
        </div>

         </div>

  );
}


export default App;
