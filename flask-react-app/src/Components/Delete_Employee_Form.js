import { useState } from 'react';
import APIServiceTen from '../Components/APIServiceTen.js'
import EmployeesList from '../Components/EmployeesList'


const Employee_Form_Delete = (props) => {
    const [first_name, setFirstName] = useState('')
    const [last_name, setLastName] = useState('')
    const [address, setAddress] = useState('')
    const [city, setCity] = useState('')
    const [state, setState] = useState('')
    const [zipcode, setZipCode] = useState('')
    const [position, setPosition] = useState('')
    const [pay_rate, setPayRate] = useState('')
    const [years_employed, setYearsEmployed] = useState('')
    const [position_gm, setPositionGm] = useState('')
    const [employees, setEmployees] = useState([])


    const insertEmployee = () =>{
    APIServiceTen.DeleteEmployee({first_name,last_name,address,city,state,zipcode,position,pay_rate,years_employed})
    .then((response) => setEmployees(response))
          .catch(error => console.log('error',error))
          }

    const handleSubmit=(event)=>{
          event.preventDefault()
          insertEmployee()
          setFirstName('')
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
                    <h2> "Enter information about the employee to delete" </h2>

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

                      <label htmlFor="pay_rate" className="form-label">Employee Pay Rate</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter your pay rate"
                     value={pay_rate}
                     onChange={(e)=>setPayRate(e.target.value)}
                     required
                     />

                      <label htmlFor="years_employed" className="form-label">Employee Years Employed</label>
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
                     > Delete Employee</button>

                   </form>
                   <EmployeesList employees = {employees} />
           </div>
      )}


export default Employee_Form_Delete;
