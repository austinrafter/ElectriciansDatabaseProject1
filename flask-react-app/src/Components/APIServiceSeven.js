export default class APIServiceSeven{
    static CheckPositionThree(body){
    return fetch('http://localhost:5000/flaskapi/general_manager',{
    'method': 'POST',
    headers : {
    'Content-Type' : 'application/json'},
    body:JSON.stringify(body)})
    .then(response => response.json())
    .catch(error => console.log(error))
    }
}