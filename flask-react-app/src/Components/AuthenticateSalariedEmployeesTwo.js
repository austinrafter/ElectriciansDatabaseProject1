import { useState } from 'react';
import APIServiceSix from '../Components/APIServiceSix.js'
import ProjectManagersList from '../Components/ProjectManagersList';


const PositionAuthenticationFormTwo = (props) => {
    const [job_to_view, setJobToView] = useState('')
    const [project_managers, setProjectManagers] = useState([]);

    const checkPositionTwo = () =>{
    APIServiceSix.CheckPositionTwo({job_to_view})
    .then((response) => setProjectManagers(response))
          .catch(error => console.log('error',error))
          }

    const handleSubmit=(event)=>{
          event.preventDefault()
          checkPositionTwo()
          setJobToView('')
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
                <ProjectManagersList project_managers = {project_managers} />
                </div>
           </div>
      )}


export default PositionAuthenticationFormTwo;
