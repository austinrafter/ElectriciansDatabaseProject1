export default class APIServiceNine{
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