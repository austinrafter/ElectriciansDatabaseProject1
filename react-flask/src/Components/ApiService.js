export default class APIService{
    static InsertJob(body){
    return fetch('http://localhost:5000/add',{
    'method': 'POST',
    headers : {
    'Content-Type' : 'application/json'},
    body:JSON.stringify(body)})
    .then(response => response.json())
    .catch(error => console.log(error))
    }
}

export default class APIServiceTwo{
    static InsertWorkPackageb(body){
    return fetch('http://localhost:5000/add_work_package',{
    'method': 'POST',
    headers : {
    'Content-Type' : 'application/json'},
    body:JSON.stringify(body)})
    .then(response => response.json())
    .catch(error => console.log(error))
    }
}

export default class APIServiceThree{
    static InsertEmployee(body){
    return fetch('http://localhost:5000/add_employee',{
    'method': 'POST',
    headers : {
    'Content-Type' : 'application/json'},
    body:JSON.stringify(body)})
    .then(response => response.json())
    .catch(error => console.log(error))
    }
}

export default class APIServiceFour{
    static CheckPosition(body){
    return fetch('http://localhost:5000/check_salaried_employee',{
    'method': 'POST',
    headers : {
    'Content-Type' : 'application/json'},
    body:JSON.stringify(body)})
    .then(response => response.json())
    .catch(error => console.log(error))
    }
}