import { useState } from 'react';
import APIServiceFour from '../Components/ApiServiceFour.js'


const Position_Authentication_Form = (props) => {
    const [first_name, setFirstName] = useState('')
    const [last_name, setLastName] = useState('')
    const [address, setAddress] = useState('')
    const [city, setCity] = useState('')
    const [state, setState] = useState('')
    const [zipcode, setZipCode] = useState('')
    const [position, setPosition] = useState('')
    const [pay_rate, setPayRate] = useState('')
    const [years_employed, setYearsEmployed] = useState('')

    const checkPosition = () =>{
    APIService.CheckPosition({first_name,last_name,address,city,state,zipcode,position,pay_rate,years_employed})
    .then((response) => props.insertedJob(response))
          .catch(error => console.log('error',error))
          }

    const handleSubmit=(event)=>{
          event.preventDefault()
          checkPosition()
          setFirst('')
          setLastName('')
          setAddress('')
          setCity('')
          setState('')
          setZipCode('')
          setPosition('')
          setPayRate('')
          setYearsEmployed('')
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


export default Position_Authentication_Form;