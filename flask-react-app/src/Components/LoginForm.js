import { useState } from 'react';
import APIServiceEighteen from '../Components/ApiServiceEighteen.js'
import UsersList from '../Components/UserList';


const LoginForm = (props) => {
    const [work_package_name, setWorkPackageName] = useState('')
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [users, setUsers] = useState('')

    const loginUser = () =>{
    APIServiceEighteen.LoginUser({username,password})
    .then((response) => setUsers(response))
          .catch(error => console.log('error',error))
          }

    const handleSubmit=(event)=>{
          event.preventDefault()
          loginUser()
          setUsername('')
          setPassword('')
        }

      return (
           <div>
             <form onSubmit = {handleSubmit} >
                    <h2> "Enter username and password" </h2>
                     <label htmlFor="work_package_name" className="form-label">Username</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter username"
                     value={work_package_name}
                     onChange={(e)=>setUsername(e.target.value)}
                     required
                     />

                      <label htmlFor="price_of_work" className="form-label">Password</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter password"
                      value={price_of_work}
                      onChange={(e)=>setPassword(e.target.value)}
                      required
                      />

                     <button
                     className="btn btn-primary mt-2"
                     >
                     Add Work Package</button>

                   </form>
                   <div>
                <UserList users={users}/>
        </div>
           </div>
      )}


export default LoginForm;
