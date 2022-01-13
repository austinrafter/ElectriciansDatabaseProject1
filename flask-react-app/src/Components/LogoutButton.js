import { useState } from 'react';
import APIServiceTwenty from '../Components/APIServiceTwenty.js'
import UsersList from '../Components/UserList';


const LogoutForm = (props) => {

    const [users, setUsers] = useState('')

    const logoutUser = () =>{
    APIServiceTwenty.LoginUser({})
    .then((response) => setUsers(response))
          .catch(error => console.log('error',error))
          }

    const handleSubmit=(event)=>{
          event.preventDefault()
          logoutUser()
        }

      return (
           <div>
             <form onSubmit = {handleSubmit} >

                     <button
                     className="btn btn-primary mt-2"
                     >
                     Logout</button>

                   </form>
                   <div>
                <UsersList users={users}/>
        </div>
           </div>
      )}


export default LogoutForm;
