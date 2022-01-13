import { useState } from 'react';
import APIServiceSeven from '../Components/APIServiceSeven.js'
import GeneralManagersList from '../Components/GeneralManagersList';


const PositionAuthenticationFormThree = (props) => {
    const insertedJob = (job) =>{
        const new_jobs = [...jobs,job]
        setJobs(new_jobs)
    }
    const [job_to_view, setJobToView] = useState('')
    const [general_managers, setGeneralManagers] = useState([]);
    const [jobs, setJobs] = useState([]);

    const checkPositionThree = () =>{
    APIServiceSeven.CheckPositionThree({job_to_view})
    .then((response) => setGeneralManagers(response))
          .catch(error => console.log('error',error))
          }

    const handleSubmit=(event)=>{
          event.preventDefault()
          checkPositionThree()
          setJobToView('')
        }

        const [showFormTwo, setShowFormTwo] = useState(false);

        const toggleShowFormTwo = () => {
        setShowFormTwo(!showFormTwo);
        }

      return (
           <div>
           <h2> Enter your information to see the right info about jobs </h2>
             <form onSubmit = {handleSubmit} >

                     <label htmlFor="job_to_view" className="form-label">Job to view</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter job_to_view"
                     value={job_to_view}
                     onChange={(e)=>setJobToView(e.target.value)}
                     required
                     />

                     <button
                     className="btn btn-primary mt-2"
                     >
                     Check Position</button>

                   </form>
                <div>
                <GeneralManagersList general_managers = {general_managers} />
                </div>
                <div>
                </div>
           </div>
      )}


export default PositionAuthenticationFormThree;
