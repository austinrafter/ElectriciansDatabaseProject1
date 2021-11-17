import { useState, useEffect } from "react";
import JobsList from '../Components/JobsList';

const Jobs = () => {
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

    return(
    <div>
    <h2>Jobs</h2>
        <JobsList
         jobs={jobs}
         />
         </div>
    )

};

export default Jobs;