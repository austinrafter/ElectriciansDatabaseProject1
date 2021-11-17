import { useState } from 'react';
import APIServiceFour from '../Components/ApiServiceFour.js'
import ForemansList from '../Components/ForemansList'


const PositionAuthenticationForm = (props) => {
    const [first_name, setFirstName] = useState('')
    const [last_name, setLastName] = useState('')
    const [address, setAddress] = useState('')
    const [city, setCity] = useState('')
    const [state, setState] = useState('')
    const [zip, setZip] = useState('')
    const [position, setPosition] = useState('')
    const [pay_rate, setPayRate] = useState('')
    const [years_employed, setYearsEmployed] = useState('')
    const [job_to_view, setJobToView] = useState('')
    const [foremen, setForemen] = useState([]);

    const checkPosition = () =>{
    APIServiceFour.CheckPosition({first_name,last_name,address,city,state,zip,position,pay_rate,years_employed, job_to_view})
    .then((response) => setForemen(response))
          .catch(error => console.log('error',error))
          }

    const handleSubmit=(event)=>{
          event.preventDefault()
          checkPosition()
          setFirstName('')
          setLastName('')
          setAddress('')
          setCity('')
          setState('')
          setZip('')
          setPosition('')
          setPayRate('')
          setYearsEmployed('')
          setJobToView('')
        }

      return (
           <div>
           <h2> Enter your information to see the right info about jobs </h2>
             <form onSubmit = {handleSubmit} >

                     <label htmlFor="first_name" className="form-label">First Name</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter first name"
                     value={first_name}
                     onChange={(e)=>setFirstName(e.target.value)}
                     required
                     />

                      <label htmlFor="last_name" className="form-label">Last Name</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter last name"
                      value={last_name}
                      onChange={(e)=>setLastName(e.target.value)}
                      required
                      />

                      <label htmlFor="address" className="form-label">Address</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter address"
                      value={address}
                      onChange={(e)=>setAddress(e.target.value)}
                      required
                      />

                       <label htmlFor="city" className="form-label">City</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter city"
                     value={city}
                     onChange={(e)=>setCity(e.target.value)}
                     required
                     />

                      <label htmlFor="state" className="form-label">State</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter state"
                     value={state}
                     onChange={(e)=>setState(e.target.value)}
                     required
                     />

                      <label htmlFor="zip" className="form-label">Zipcode</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter zip code"
                     value={zip}
                     onChange={(e)=>setZip(e.target.value)}
                     required
                     />

                      <label htmlFor="position" className="form-label">Position</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter position"
                     value={position}
                     onChange={(e)=>setPosition(e.target.value)}
                     required
                     />

                      <label htmlFor="pay_rate" className="form-label">Pay Rate</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter your pay rate"
                     value={pay_rate}
                     onChange={(e)=>setPayRate(e.target.value)}
                     required
                     />

                      <label htmlFor="years_employed" className="form-label">Years Employed</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter years employed"
                     value={years_employed}
                     onChange={(e)=>setYearsEmployed(e.target.value)}
                     required
                     />

                     <label htmlFor="job_to_view" className="form-label">Years Employed</label>
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
