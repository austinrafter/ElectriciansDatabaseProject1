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