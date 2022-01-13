import { useState } from 'react';
import APIServiceNineteen from '../Components/APIServiceNineteen.js'
import UsersList from '../Components/UserList';


const CreateUserForm = (props) => {
    const [first_name, setFirstName] = useState('')
    const [last_name, setLastName] = useState('')
    const [position_name, setPosition] = useState('')
    const [address, setAddress] = useState('')
    const [city, setCity] = useState('')
    const [state, setState] = useState('')
    const [zipcode, setZipcode] = useState('')

    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [users, setUsers] = useState('')

    const createUser = () =>{
    APIServiceNineteen.CreateUser({username,password})
    .then((response) => setUsers(response))
          .catch(error => console.log('error',error))
          }

    const handleSubmit=(event)=>{
          event.preventDefault()
          createUser()
          setUsername('')
          setPassword('')
          setFirstName('')
          setLastName('')
          setPosition('')
          setAddress('')
          setCity('')
          setState('')
          setZipcode('')
        }

      return (
           <div>
             <form onSubmit = {handleSubmit} >
                    <h2> "Enter employee information" </h2>
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

                      <label htmlFor="position_name" className="form-label">Position</label>
                     <input
                     type="text"
                     className="form-control"
                     placeholder ="Enter position"
                     value={position_name}
                     onChange={(e)=>setPosition(e.target.value)}
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
                     placeholder ="Enter zipcode"
                     value={zipcode}
                     onChange={(e)=>setZipcode(e.target.value)}
                     required
                     />


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
                     Add User</button>

                   </form>
                   <div>
                <UsersList users={users}/>
        </div>
           </div>
      )}


export default CreateUserForm;
