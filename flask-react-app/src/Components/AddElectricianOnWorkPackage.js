import { useState } from 'react';
import APIServiceFourteen from '../Components/APIServiceFourteen.js'
import ElectricianOnWorkPackageList from '../Components/ElectricianOnWorkPackageList';


const AddElectricianOnWorkPackage = (props) => {
    const insertedElectricanOnPackage = (electrician_on_package) =>{
        const new_electricianOnPackage = [...electrician_on_package,electricians_on_packages]
        setElectriciansOnPackages(new_electricianOnPackage)
    }

    const [electricians_first_name, setElectriciansFirstName] = useState('')
    const [electricians_last_name, setElectriciansLastName] = useState('')
    const [electricians_position, setELectriciansPosition] = useState('')
    const [electricians_address, setELectriciansAddress] = useState('')
    const [work_package_name, setWorkPackageName] = useState('')
    const [site_name, setSiteName] = useState('')
    const [first_name, setFirstName] = useState('')
    const [last_name, setLastName] = useState('')
    const [address, setAddress] = useState('')
    const [city, setCity] = useState('')
    const [state, setState] = useState('')
    const [zipcode, setZip] = useState('')
    const [position, setPosition] = useState('')
    const [pay_rate, setPayRate] = useState('')
    const [years_employed, setYearsEmployed] = useState('')
    const [general_managers, setGeneralManagers] = useState([]);
    const [electricians_on_packages, setElectriciansOnPackages] = useState([]);

    const checkInventory = () =>{
    APIServiceFourteen.InsertElectricianToWorkPackage({electricians_first_name,electricians_last_name,electricians_position,electricians_address, work_package_name, site_name ,first_name,last_name,position,address,city,state,zipcode})
    .then((response) => setElectriciansOnPackages(response))
          .catch(error => console.log('error',error))
          }

    const handleSubmit=(event)=>{
          event.preventDefault()
          checkInventory()
          setElectriciansFirstName('')
          setElectriciansLastName('')
          setELectriciansPosition('')
          setELectriciansAddress('')
          setWorkPackageName('')
          setSiteName('')
          setFirstName('')
          setLastName('')
          setAddress('')
          setCity('')
          setState('')
          setZip('')
          setPosition('')
          setPayRate('')
          setYearsEmployed('')

        }

        const [showFormTwo, setShowFormTwo] = useState(false);

        const toggleShowFormTwo = () => {
        setShowFormTwo(!showFormTwo);
        }

      return (
           <div>
           <h2> Enter information about the electrician and work package </h2>
             <form onSubmit = {handleSubmit} >

                     <label htmlFor="electricians_first_name" className="form-label">Electricians First Name</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter electricians first name"
                     value={electricians_first_name}
                     onChange={(e)=>setElectriciansFirstName(e.target.value)}
                     required
                     />

                      <label htmlFor="electricians_last_name" className="form-label">Electricians Last Name</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter electricians last name"
                      value={electricians_last_name}
                      onChange={(e)=>setElectriciansLastName(e.target.value)}
                      required
                      />

                      <label htmlFor="electricians_position" className="form-label">Electricians Position</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter electricians position"
                      value={electricians_position}
                      onChange={(e)=>setELectriciansPosition(e.target.value)}
                      required
                      />

                      <label htmlFor="electricians_address" className="form-label">Electricians Address</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter electricians address"
                      value={electricians_address}
                      onChange={(e)=>setELectriciansAddress(e.target.value)}
                      required
                      />

                      <label htmlFor="work_package_name" className="form-label">Work Package Name</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter work package name to add electrician to"
                      value={work_package_name}
                      onChange={(e)=>setWorkPackageName(e.target.value)}
                      required
                      />

                      <label htmlFor="site_name" className="form-label">Site Name</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter job that work package is on"
                     value={site_name}
                     onChange={(e)=>setSiteName(e.target.value)}
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

                      <label htmlFor="zipcode" className="form-label">Zipcode</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter zip code"
                     value={zipcode}
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


                     <button
                     className="btn btn-primary mt-2"
                     >
                     Add electrician to work package</button>

                   </form>

                <div>
            <ElectricianOnWorkPackageList electricians_on_packages={electricians_on_packages}/>
            </div>
           </div>
      )}


export default AddElectricianOnWorkPackage;
