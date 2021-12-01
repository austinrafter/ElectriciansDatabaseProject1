export default class APIService{
    static InsertJob(body){
    return fetch('http://localhost:5000/flaskapi/add_job',{
    'method': 'POST',
    headers : {
    'Content-Type' : 'application/json'},
    body:JSON.stringify(body)})
    .then(response => response.json())
    .catch(error => console.log(error))
    }
}



