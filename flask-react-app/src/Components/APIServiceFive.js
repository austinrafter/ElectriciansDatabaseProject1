export default class APIServiceFive{
    static InsertJobName(body){
    return fetch('http://localhost:5000/work_packages',{
    'method': 'POST',
    headers : {
    'Content-Type' : 'application/json'},
    body:JSON.stringify(body)})
    .then(response => response.json())
    .catch(error => console.log(error))
    }
}