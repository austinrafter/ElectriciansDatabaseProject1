import { useState } from 'react';
import APIServiceFour from '../Components/ApiServiceFour.js'
import ForemansList from '../Components/ForemansList'


const PositionAuthenticationForm = (props) => {

    const [job_to_view, setJobToView] = useState('')
    const [foremen, setForemen] = useState([]);

    const checkPosition = () =>{
    APIServiceFour.CheckPosition({job_to_view})
    .then((response) => setForemen(response))
          .catch(error => console.log('error',error))
          }

    const handleSubmit=(event)=>{
          event.preventDefault()
          checkPosition()
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
                <ForemansList foremen = {foremen} />
                </div>
           </div>
      )}


export default PositionAuthenticationForm;
