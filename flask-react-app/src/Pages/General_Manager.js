import { useState, useEffect } from "react";
import PositionAuthenticationFormThree from '../Components/AuthenticateSalariedEmployeesThree';

const General_Manager = () => {

  const findGeneralManager = (general_manager) =>{
    const new_generalManager = [...general_managers,general_manager]
    setGeneralManagers(new_generalManager)
  }

  const [general_managers, setGeneralManagers] = useState([]);

  const [showFormFour, setShowFormFour] = useState(false);

  const toggleShowFormFour = () => {
    setShowFormFour(!showFormFour);
  }


  return(
  <div>
    <button
          onClick={toggleShowFormFour}
          className="btn btn-primary"
           >
             Are you a general manager? See information about jobs here.
        <i className="bi bi-pencil-square m-2"></i>
        </button>
        {showFormFour && (
          <PositionAuthenticationFormThree
          findGeneralManager = {findGeneralManager}
            />
            )}
  </div>
  )

};

export default General_Manager;