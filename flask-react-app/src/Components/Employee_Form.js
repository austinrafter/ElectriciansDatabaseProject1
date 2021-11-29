import { useState } from 'react';
import APIServiceNine from '../Components/APIServiceNine.js'
import EmployeesList from '../Components/EmployeesList'


const Employee_Form = (props) => {
    const [first_name, setFirstName] = useState('')
    const [last_name, setLastName] = useState('')
    const [address, setAddress] = useState('')
    const [city, setCity] = useState('')
    const [state, setState] = useState('')
    const [zipcode, setZipCode] = useState('')
    const [position, setPosition] = useState('')
    const [pay_rate, setPayRate] = useState('')
    const [years_employed, setYearsEmployed] = useState('')
    const [first_name_gm, setFirstNameGm] = useState('')
    const [last_name_gm, setLastNameGm] = useState('')
    const [address_gm, setAddressGm] = useState('')
    const [city_gm, setCityGm] = useState('')
    const [state_gm, setStateGm] = useState('')
    const [zipcode_gm, setZipCodeGm] = useState('')
    const [position_gm, setPositionGm] = useState('')
    const [employees, setEmployees] = useState([])


    const insertEmployee = () =>{
    APIServiceNine.InsertEmployee({first_name,last_name,address,city,state,zipcode,position,pay_rate,years_employed,first_name_gm,last_name_gm,address_gm,city_gm,state_gm,zipcode_gm,position_gm})
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
          setFirstNameGm('')
          setLastNameGm('')
          setAddressGm('')
          setCityGm('')
          setStateGm('')
          setZipCodeGm('')
          setPositionGm('')

        }

      return (
           <div>
             <form onSubmit = {handleSubmit} >
                    <h2>"Enter information about the employee to add" </h2>
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

                     <h2> "This section to confirm you are a General Manager in our system" </h2>

                     <label htmlFor="first_name_gm" className="form-label">GM First Name</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter last name"
                      value={first_name_gm}
                      onChange={(e)=>setFirstNameGm(e.target.value)}
                      required
                      />

                      <label htmlFor="last_name_gm" className="form-label">GM Last Name</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter last name"
                      value={last_name_gm}
                      onChange={(e)=>setLastNameGm(e.target.value)}
                      required
                      />

                      <label htmlFor="address_gm" className="form-label">GM Address</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter address"
                      value={address_gm}
                      onChange={(e)=>setAddressGm(e.target.value)}
                      required
                      />

                       <label htmlFor="city_gm" className="form-label">GM City</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter city"
                     value={city_gm}
                     onChange={(e)=>setCityGm(e.target.value)}
                     required
                     />

                      <label htmlFor="state_gm" className="form-label">GM State</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter state"
                     value={state_gm}
                     onChange={(e)=>setStateGm(e.target.value)}
                     required
                     />

                      <label htmlFor="zipcode_gm" className="form-label">GM Zipcode</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter zip code"
                     value={zipcode_gm}
                     onChange={(e)=>setZipCodeGm(e.target.value)}
                     required
                     />

                      <label htmlFor="position_gm" className="form-label">GM Position</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter position"
                     value={position_gm}
                     onChange={(e)=>setPositionGm(e.target.value)}
                     required
                     />

                     <button
                     className="btn btn-primary mt-2"
                     > Add Employee</button>

                   </form>
                   <EmployeesList employees = {employees} />
           </div>
      )}


export default Employee_Form;
