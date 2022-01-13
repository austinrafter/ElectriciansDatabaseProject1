import { useState } from 'react';
import APIServiceEighteen from '../Components/APIServiceEighteen.js'
import UsersList from '../Components/UserList';


const LoginForm = (props) => {
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
                     <label htmlFor="username" className="form-label">Username</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter username"
                     value={username}
                     onChange={(e)=>setUsername(e.target.value)}
                     required
                     />

                      <label htmlFor="password" className="form-label">Password</label>
                      <input
                      type="text"
                      className="form-control"
                      placeholder ="Enter password"
                      value={password}
                      onChange={(e)=>setPassword(e.target.value)}
                      required
                      />

                     <button
                     className="btn btn-primary mt-2"
                     >
                     Login</button>

                   </form>
                   <div>
                <UsersList users={users}/>
        </div>
           </div>
      )}


export default LoginForm;
