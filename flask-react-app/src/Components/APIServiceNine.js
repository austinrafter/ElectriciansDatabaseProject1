export default class APIServiceNine{
    static AddEmployee(body){
    return fetch('http://localhost:5000/delete_job',{
    'method': 'POST',
    headers : {
    'Content-Type' : 'application/json'},
    body:JSON.stringify(body)})
    .then(response => response.json())
    .catch(error => console.log(error))
    }
}