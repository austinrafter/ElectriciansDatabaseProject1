import { useState, useEffect } from "react";
import PositionAuthenticationForm from '../Components/Authenticate_Salaried_Employees';

const Foreman = () => {

const findForeman = (foreman) =>{
    const new_salariedEmployee = [...foremen,foreman]
    setForemen(new_salariedEmployee)
  }
 const [foremen, setForemen] = useState([]);


  const [showForm, setShowForm] = useState(false);

  const toggleShowForm = () => {
    setShowForm(!showForm);
  }

  return(
  <div>
  <button
          onClick={toggleShowForm}
          className="btn btn-primary"
           >
             Are you a foreman? See information about jobs here.
        <i className="bi bi-pencil-square m-2"></i>
        </button>
        {showForm && (
          <PositionAuthenticationForm
          findForeman = {findForeman}
            />
            )}
            <hr/>
  </div>
  )

};

export default Foreman;