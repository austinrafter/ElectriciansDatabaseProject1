import { useState, useEffect } from "react";
import JobsList from '../Components/JobsList';

const Jobs = () => {
const [jobs, setJobs] = useState([]);

useEffect(()=>{
      fetch('http://localhost:5000/flaskapi/jobs',{
        'methods':'GET',
        headers : {
          'Content-Type':'application/json'
        }
      })
      .then(response => response.json())
      .then(response => setJobs(response))
      .catch(error => console.log(error))
    },[]);

    return(
    <div>
    <h1>Jobs</h1>
        <JobsList
         jobs={jobs}
         />
         </div>
    )

};

export default Jobs;