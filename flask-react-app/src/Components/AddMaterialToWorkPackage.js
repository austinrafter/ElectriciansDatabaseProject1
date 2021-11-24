import { useState } from 'react';
import APIServiceSixteen from '../Components/APIServiceSixteen.js'
import MaterialInWorkPackageList from '../Components/MaterialInWorkPackageList';


const AddMaterialToWorkPackage = (props) => {
    const insertedMaterialOnPackage = (material_on_package) =>{
        const new_materialOnPackage = [...material_on_package,materials_on_packages]
        setMaterialsOnPackages(new_materialOnPackage)
    }

    const [material_name, setMaterialName] = useState('')
    const [work_package_name, setWorkPackageName] = useState('')
    const [site_name, setSiteName] = useState('')
    const [amount_alloted, setAmountAlloted] = useState('')
    const [amount_used, setAmountUsed] = useState('')
    const [first_name, setFirstName] = useState('')
    const [last_name, setLastName] = useState('')
    const [address, setAddress] = useState('')
    const [city, setCity] = useState('')
    const [state, setState] = useState('')
    const [zip, setZip] = useState('')
    const [position, setPosition] = useState('')
    const [pay_rate, setPayRate] = useState('')
    const [years_employed, setYearsEmployed] = useState('')
    const [general_managers, setGeneralManagers] = useState([]);
    const [materials_on_packages, setMaterialsOnPackages] = useState([]);

    const checkInventory = () =>{
    APIServiceSixteen.InsertMaterialToWorkPackage({material_name,work_package_name,site_name,amount_alloted, amount_used,first_name,last_name,position,address,city,state,zip})
    .then((response) => setMaterialsOnPackages(response))
          .catch(error => console.log('error',error))
          }

    const handleSubmit=(event)=>{
          event.preventDefault()
          checkInventory()
          setMaterialName('')
          setWorkPackageName('')
          setSiteName('')
          setAmountAlloted('')
          setAmountUsed('')
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
           <h2> Enter the information about the material on the job </h2>
             <form onSubmit = {handleSubmit} >

                     <label htmlFor="material_name" className="form-label">Material Name</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter the material name"
                     value={material_name}
                     onChange={(e)=>setMaterialName(e.target.value)}
                     required
                     />

                      <label htmlFor="work_package_name" className="form-label">Work Package Name</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter the work package the material is used for"
                      value={work_package_name}
                      onChange={(e)=>setWorkPackageName(e.target.value)}
                      required
                      />

                      <label htmlFor="site_name" className="form-label">Site Name</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter the job the work package is on"
                      value={site_name}
                      onChange={(e)=>setSiteName(e.target.value)}
                      required
                      />

                      <label htmlFor="amount_alloted" className="form-label">Amount Alloted</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter the amount alloted"
                      value={amount_alloted}
                      onChange={(e)=>setAmountAlloted(e.target.value)}
                      required
                      />

                      <label htmlFor="amount_used" className="form-label">Amount Used</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter the amount used"
                      value={amount_used}
                      onChange={(e)=>setAmountUsed(e.target.value)}
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


                     <button
                     className="btn btn-primary mt-2"
                     >
                     Add material to work package</button>

                   </form>

                <div>
            <MaterialInWorkPackageList materials_on_packages={materials_on_packages}/>
            </div>
           </div>
      )}


export default AddMaterialToWorkPackage;
