import { useState, useEffect } from "react";
import PositionAuthenticationFormTwo from '../Components/AuthenticateSalariedEmployeesTwo';


const Project_Manager = () => {

 const findProjectManager = (project_manager) =>{
    const new_projectManager = [...project_managers,project_manager]
    setProjectManagers(new_projectManager)
  }

  const [project_managers, setProjectManagers] = useState([]);


  const [showFormThree, setShowFormThree] = useState(false);

  const toggleShowFormThree = () => {
    setShowFormThree(!showFormThree);
  }

   return(
  <div>
   <button
          onClick={toggleShowFormThree}
          className="btn btn-primary"
           >
             Are you a project manager? See information about jobs here.
        <i className="bi bi-pencil-square m-2"></i>
        </button>
        {showFormThree && (
          <PositionAuthenticationFormTwo
          findProjectManager = {findProjectManager}
            />
            )}
            <hr/>
  </div>

  )
};

export default Project_Manager;