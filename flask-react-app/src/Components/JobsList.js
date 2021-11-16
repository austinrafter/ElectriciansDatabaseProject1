import { Button } from 'react-bootstrap';
import React, { useState, useEffect } from 'react';
import WorkPackagesList from '../Components/Work_Packages_List';

const JobsList = (props) => {
const [siteName, setSiteName] = useState()
const [work_packages, setWorkPackages] = useState([]);

const handleClick = (event) => {
const site = event.target.value;
siteName = site
}

useEffect(()=>{
      fetch('http://localhost:5000/work_packages',{
        'methods':'GET',
        headers : {
          'Content-Type':'application/json'
        }
      })
      .then(response => response.json())
      .then(response => setWorkPackages(response))
      .catch(error => console.log(error))
    },[]);


    return (
        <div className="mt-2">
        {/* Display the job details if job is not None */}
        {props.jobs && props.jobs.map(job =>{
        return (

        <div key={job.job_id} >
        <h2 className="text-primary"> { job.site } </h2>
        <h3> "Location" </h3>
        <p> { job.location } </p>
        <h4> "Start Date" </h4>
        <p> { job.start } </p>
        <Button className="text-primary" onClick = {handleClick} value = {job.site}> { "work packages"  } </Button>
        <hr/>
        <WorkPackagesList work_packages = {work_packages}/>
        </div>
    )

        })}
    </div>
    )
}

export default JobsList;