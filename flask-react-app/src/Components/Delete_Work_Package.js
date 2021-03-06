import { useState } from 'react';
import APIServiceEleven from '../Components/APIServiceEleven.js'


const Work_Package_Form_Delete = (props) => {
    const [work_package_name, setWorkPackageName] = useState('')
    const [price_of_work, setPriceOfWork] = useState('')
    const [hours_alloted, setHoursAlloted] = useState('')
    const [hours_used, setHoursUsed] = useState('')
    const [first_name, setFirstName] = useState('')
    const [last_name, setLastName] = useState('')
    const [address, setAddress] = useState('')
    const [city, setCity] = useState('')
    const [state, setState] = useState('')
    const [zipcode, setZip] = useState('')
    const [position, setPosition] = useState('')
    const [pay_rate, setPayRate] = useState('')
    const [years_employed, setYearsEmployed] = useState('')
    const [job, setJob] = useState('')
    const [work_package, setWorkPackage] = useState('')

    const insertWorkPackage = () =>{
    APIServiceEleven.DeleteWorkPackage({work_package_name, price_of_work, hours_alloted, hours_used, first_name,last_name, address, city, state, zipcode,position, pay_rate, years_employed, job})
    .then((response) => setWorkPackage(response))
          .catch(error => console.log('error',error))
          }

    const handleSubmit=(event)=>{
          event.preventDefault()
          insertWorkPackage()
          setWorkPackageName('')
          setPriceOfWork('')
          setHoursAlloted('')
          setHoursUsed('')
          setFirstName('')
          setLastName('')
          setAddress('')
          setCity('')
          setState('')
          setZip('')
          setPosition('')
          setPayRate('')
          setYearsEmployed('')
          setJob('')

        }

      return (
           <div>
             <form onSubmit = {handleSubmit} >
                    <h2> "Enter information about the work package to delete" </h2>
                     <label htmlFor="work_package_name" className="form-label">Work Package Name</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter job name"
                     value={work_package_name}
                     onChange={(e)=>setWorkPackageName(e.target.value)}
                     required
                     />

                     <label htmlFor="job" className="form-label">Job</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter job_to_view"
                     value={job}
                     onChange={(e)=>setJob(e.target.value)}
                     required
                     />

                      <label htmlFor="price_of_work" className="form-label">Price of work </label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter location name"
                      value={price_of_work}
                      onChange={(e)=>setPriceOfWork(e.target.value)}
                      required
                      />

                      <label htmlFor="hours_used" className="form-label">Hours Used</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter job start date"
                      value={hours_used}
                      onChange={(e)=>setHoursUsed(e.target.value)}
                      required
                      />

                      <label htmlFor="hours_alloted" className="form-label">Hours Alloted</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter first name"
                     value={hours_alloted}
                     onChange={(e)=>setHoursAlloted(e.target.value)}
                     required
                     />

                     <h2> "This section to confirm you are a Foreman or Project Manager in our system" </h2>

                     <label htmlFor="first_name" className="form-label">PM or Foreman First Name</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter last name"
                      value={first_name}
                      onChange={(e)=>setFirstName(e.target.value)}
                      required
                      />

                      <label htmlFor="last_name" className="form-label">PM or Foreman Last Name</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter last name"
                      value={last_name}
                      onChange={(e)=>setLastName(e.target.value)}
                      required
                      />

                      <label htmlFor="address" className="form-label">PM or Foreman Address</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter address"
                      value={address}
                      onChange={(e)=>setAddress(e.target.value)}
                      required
                      />

                       <label htmlFor="city" className="form-label">PM or Foreman City</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter city"
                     value={city}
                     onChange={(e)=>setCity(e.target.value)}
                     required
                     />

                      <label htmlFor="state" className="form-label">PM or Foreman State</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter state"
                     value={state}
                     onChange={(e)=>setState(e.target.value)}
                     required
                     />

                      <label htmlFor="zipcode" className="form-label">PM or Foreman Zipcode</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter zip code"
                     value={zipcode}
                     onChange={(e)=>setZip(e.target.value)}
                     required
                     />

                      <label htmlFor="position" className="form-label">PM or Foreman Position</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter position"
                     value={position}
                     onChange={(e)=>setPosition(e.target.value)}
                     required
                     />

                      <label htmlFor="pay_rate" className="form-label">PM or Foreman Pay Rate</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter your pay rate"
                     value={pay_rate}
                     onChange={(e)=>setPayRate(e.target.value)}
                     required
                     />

                      <label htmlFor="years_employed" className="form-label">PM or Foreman Years Employed</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter years employed"
                     value={years_employed}
                     onChange={(e)=>setYearsEmployed(e.target.value)}
                     required
                     />

                     <button
                     className="btn btn-primary mt-2"
                     >
                     Delete Work Package</button>

                   </form>
           </div>
      )}


export default Work_Package_Form_Delete;
