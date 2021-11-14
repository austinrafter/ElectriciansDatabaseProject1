import { useState } from 'react';
import APIServiceTwo from '../Components/ApiServiceTwo.js'


const Work_Package_Form = (props) => {
    const [hours_used, setHoursUsed] = useState('')

    const insertHoursUsed = () =>{
    APIService.InsertWorkPackage({hours_used})
    .then((response) => props.insertedWorkPackage(response))
          .catch(error => console.log('error',error))
          }

    const handleSubmit=(event)=>{
          event.preventDefault()
          insertWorkPackage()
          setInsertedHours('')
        }

      return (
           <div>
             <form onSubmit = {handleSubmit} >

                     <label htmlFor="job_name" className="form-label">Job Name</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter job name"
                     value={site_name}
                     onChange={(e)=>setSiteName(e.target.value)}
                     required
                     />

                      <label htmlFor="location" className="form-label">Job Location</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter location name"
                      value={location}
                      onChange={(e)=>setLocation(e.target.value)}
                      required
                      />

                      <label htmlFor="start_date" className="form-label">Job Start Date</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter job start date"
                      value={start_date}
                      onChange={(e)=>setStartDate(e.target.value)}
                      required
                      />

                     <button
                     className="btn btn-primary mt-2"
                     >
                     Add job</button>

                   </form>
           </div>
      )}


export default Work_Package_Form;
