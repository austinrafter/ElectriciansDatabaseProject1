import { Button } from 'react-bootstrap';
import React, { useState, useEffect } from 'react';
import WorkPackagesList from '../Components/Work_Packages_List';
import APIServiceFive from '../Components/APIServiceFive'



const JobsList = (props) => {
const [jobSite, setJobSite] = useState({
"job_site" : "job" })
const [work_packages, setWorkPackages] = useState([]);


const workPackages = (work_package) =>{
    const new_WorkPackage = [...work_packages,work_package]
    setWorkPackages(new_WorkPackage)
  }

const checkPosition = () =>{
    APIServiceFive.InsertJobName({jobSite})
    .then((response) => setWorkPackages(response))
         .catch(error => console.log('error',error))
          }

    const handleSubmit=(event)=>{
    //event.preventDefault()
    console.log(jobSite)
    const changedReason = event.target.getAttribute('job_site');
    setJobSite({job_site : event.target.value} )
    checkPosition()
    console.log(jobSite)

        }

    return (
        <div className="mt-2">
        <h3> "Double click the button under a job to see the work packages for that job" </h3>
        {/* Display the job details if job is not None */}
        {props.jobs && props.jobs.map(job =>{
        return (

        <div key={job.job_id} >
        <h2 className="text-primary"> { job.site } </h2>
        <h3> "Location" </h3>
        <p> { job.location } </p>
        <h4> "Start Date" </h4>
        <p> { job.start } </p>
        <Button className="text-primary" onClick = {handleSubmit} value = {job.site}> { "work packages"  } </Button>
        <hr/>
        <hr/>
        <div>
        <WorkPackagesList work_packages={work_packages}/>
        </div>

        </div>
    )

        })}
    </div>
    )
}

export default JobsList;