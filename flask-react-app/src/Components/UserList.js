import { Button } from 'react-bootstrap';
import React from 'react';

const UsersList = (props) => {
    return (
        <div className="mt-2">
        {/* Display the article details if article is not None */}
        {props.users && props.users.map(user =>{
        return (

        <div key = {user.user_id}>
        <h2>Project Managers View </h2>
        <h2 variant="text-primary" size="lg">
        { user.user_name}
         </h2>
        <hr/>
        </div>
    )
        })}
    </div>
    )
}

export default UsersList;