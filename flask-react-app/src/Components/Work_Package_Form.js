import { useState } from 'react';
import APIServiceTwo from '../Components/ApiServiceTwo.js'
import WorkPackagesList from '../Components/Work_Packages_List';


const Work_Package_Form = (props) => {
    const [work_package_name, setWorkPackageName] = useState('')
    const [price_of_work, setPriceOfWork] = useState('')
    const [hours_alloted, setHoursAlloted] = useState('')
    const [hours_used, setHoursUsed] = useState('')
    const [job, setJob] = useState('')
    const [work_packages, setWorkPackages] = useState('')

    const insertWorkPackage = () =>{
    APIServiceTwo.InsertWorkPackage({work_package_name, price_of_work, hours_alloted, hours_used, job})
    .then((response) => setWorkPackages(response))
          .catch(error => console.log('error',error))
          }

    const handleSubmit=(event)=>{
          event.preventDefault()
          insertWorkPackage()
          setWorkPackageName('')
          setPriceOfWork('')
          setHoursAlloted('')
          setHoursUsed('')
          setJob('')

        }

      return (
           <div>
             <form onSubmit = {handleSubmit} >
                    <h2> "Enter information about the work package to add" </h2>
                     <label htmlFor="work_package_name" className="form-label">Work Package Name</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter work package name"
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

                     <button
                     className="btn btn-primary mt-2"
                     >
                     Add Work Package</button>

                   </form>
                   <div>
        <WorkPackagesList work_packages={work_packages}/>
        </div>
           </div>
      )}


export default Work_Package_Form;
