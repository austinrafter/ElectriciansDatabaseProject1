import { useState } from 'react';
import APIServiceTwelve from '../Components/APIServiceTwelve.js'
import InventoryList from '../Components/InventoryList';


const AddInventory = (props) => {
    const insertedJob = (job) =>{
        const new_jobs = [...jobs,job]
        setJobs(new_jobs)
    }

    const [material_name, setMaterialName] = useState('')
    const [cost_per_unit, setCostPerUnit] = useState('')
    const [weight_per_unit, setWeightPerUnit] = useState('')
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
    const [general_managers, setGeneralManagers] = useState([]);
    const [inventorys, setInventorys] = useState([]);

    const checkInventory = () =>{
    APIServiceSeven.InsertEmployee({material_name,cost_per_unit,weight_per_unit ,first_name,last_name,address,city,state,zip,position,pay_rate,years_employed, job_to_view})
    .then((response) => setInventorys(response))
          .catch(error => console.log('error',error))
          }

    const handleSubmit=(event)=>{
          event.preventDefault()
          checkInventory()
          setMaterialName('')
          setCostPerUnit('')
          setWeightPerUnit('')
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

        const [showFormTwo, setShowFormTwo] = useState(false);

        const toggleShowFormTwo = () => {
        setShowFormTwo(!showFormTwo);
        }

      return (
           <div>
           <h2> Enter your information to see the right info about jobs </h2>
             <form onSubmit = {handleSubmit} >

                     <label htmlFor="material_name" className="form-label">First Name</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter material name"
                     value={material_name}
                     onChange={(e)=>setMaterialName(e.target.value)}
                     required
                     />

                      <label htmlFor="cost_per_unit" className="form-label">Last Name</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter cost per unit"
                      value={cost_per_unit}
                      onChange={(e)=>setCostPerUnit(e.target.value)}
                      required
                      />

                      <label htmlFor="weight_per_unit" className="form-label">Address</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter weight_per_unit"
                      value={weight_per_unit}
                      onChange={(e)=>setWeightPerUnit(e.target.value)}
                      required
                      />

                      <h3> "This section to confirm you are a foreman or project manager" </h3>

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
        <InventoryList inventorys={inventorys}/>
        </div>
           </div>
      )}


export default PositionAuthenticationFormThree;
