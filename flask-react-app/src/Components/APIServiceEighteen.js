export default class APIServiceEighteen{
    static LoginUser(body){
    return fetch('http://localhost:5000/flaskapi/login_user',{
    'method': 'POST',
    headers : {
    'Content-Type' : 'application/json'},
    body:JSON.stringify(body)})
    .then(response => response.json())
    .catch(error => console.log(error))
    }
}