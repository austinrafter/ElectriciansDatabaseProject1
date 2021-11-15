import logo from './logo.svg';
import './App.css';
import Job_Form from './Components/Job_form';
import JobsList from './Components/JobsList';
import { useState, useEffect } from "react";


function App() {
  const [jobs, setJobs] = useState([]);

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
      <h1>Connecting a React Frontend to a Flask Backend.</h1>
        </div>
        </div>
        <JobsList
         jobs={jobs}
         />

         </div>
  );
}


export default App;
