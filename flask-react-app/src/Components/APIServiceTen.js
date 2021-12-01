export default class APIServiceTen{
    static DeleteEmployee(body){
    return fetch('http://localhost:5000/flaskapi/delete_employee',{
    'method': 'POST',
    headers : {
    'Content-Type' : 'application/json'},
    body:JSON.stringify(body)})
    .then(response => response.json())
    .catch(error => console.log(error))
    }
}