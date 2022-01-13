import { useState, useEffect } from "react";
import PositionAuthenticationFormThree from '../Components/AuthenticateSalariedEmployeesThree';
import LoginForm from '../Components/LoginForm';
import CreateUserForm from '../Components/CreateUserForm';

const UserAuthentication= () => {

const insertedUser = (user) =>{
    const new_users = [...users,user]
    setUsers(new_users)
  }

  const [users, setUsers] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [showFormTwo, setShowFormTwo] = useState(false);

   const toggleShowForm = () => {
    setShowForm(!showForm);
  }

  const toggleShowFormTwo = () => {
    setShowFormTwo(!showFormTwo);
  }


  return(
  <div>
    <div>
    <button
          onClick={toggleShowFormTwo}
          className="btn btn-primary"
           >
            Login
        <i className="bi bi-pencil-square m-2"></i>
        </button>
         {showFormTwo && (
          <LoginForm
          insertedUser = {insertedUser}
            />
            )}
            </div>
     <div>
    <button
          onClick={toggleShowForm}
          className="btn btn-primary"
           >
             "Create a username and password if you are a salaried employee"
        <i className="bi bi-pencil-square m-2"></i>
        </button>
         {showForm && (
          <CreateUserForm
          insertedUser = {insertedUser}
            />
            )}
            </div>

  </div>
  )

};

export default UserAuthentication;