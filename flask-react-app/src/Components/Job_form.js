import { useState } from 'react';
import APIService from '../Components/ApiService.js'
import JobsList from '../Components/JobsList'

const JobForm = (props) => {
    const [location, setLocation] = useState('')
    const [site_name, setSiteName] = useState('')
    const [start_date, setStartDate] = useState('')
    const [first_name, setFirstName] = useState('')
    const [last_name, setLastName] = useState('')
    const [address, setAddress] = useState('')
    const [city, setCity] = useState('')
    const [state, setState] = useState('')
    const [zipcode, setZipCode] = useState('')
    const [position, setPosition] = useState('')
    const [jobs, setJobs] = useState([])

    const insertJob = () =>{
    APIService.InsertJob({site_name, location, start_date,first_name,last_name,address,city,state,zipcode,position})
    .then((response) => setJobs(response))
          .catch(error => console.log('error',error))
          }

    const handleSubmit=(event)=>{
          event.preventDefault()
          insertJob()
          setLocation('')
          setSiteName('')
          setStartDate('')
          setFirstName('')
          setLastName('')
          setAddress('')
          setCity('')
          setState('')
          setZipCode('')
          setPosition('')
        }

      return (
           <div>
             <form onSubmit = {handleSubmit} >
                    <h2>"Enter information about the job to add" </h2>
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
                      placeholder ="yyyy-mm-dd"
                      value={start_date}
                      onChange={(e)=>setStartDate(e.target.value)}
                      required
                      />

                      <h2> "This section to confirm you are a General Manager in our system" </h2>
                      <label htmlFor="first_name" className="form-label">Employee First Name</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter last name"
                      value={first_name}
                      onChange={(e)=>setFirstName(e.target.value)}
                      required
                      />

                      <label htmlFor="last_name" className="form-label">Employee Last Name</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter last name"
                      value={last_name}
                      onChange={(e)=>setLastName(e.target.value)}
                      required
                      />

                      <label htmlFor="address" className="form-label">Employee Address</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter address"
                      value={address}
                      onChange={(e)=>setAddress(e.target.value)}
                      required
                      />

                       <label htmlFor="city" className="form-label">Employee City</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter city"
                     value={city}
                     onChange={(e)=>setCity(e.target.value)}
                     required
                     />

                      <label htmlFor="state" className="form-label">Employee State</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter state"
                     value={state}
                     onChange={(e)=>setState(e.target.value)}
                     required
                     />

                      <label htmlFor="zipcode" className="form-label">Employee Zipcode</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter zip code"
                     value={zipcode}
                     onChange={(e)=>setZipCode(e.target.value)}
                     required
                     />

                      <label htmlFor="position" className="form-label">Employee Position</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter position"
                     value={position}
                     onChange={(e)=>setPosition(e.target.value)}
                     required
                     />

                     <button
                     className="btn btn-primary mt-2"
                     >
                     Add job</button>
                   </form>
                   <JobsList jobs = {jobs} />
           </div>
      )}


export default JobForm;
