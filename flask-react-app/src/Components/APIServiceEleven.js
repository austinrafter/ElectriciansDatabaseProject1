export default class APIServiceEleven{
    static DeleteWorkPackage(body){
    return fetch('http://localhost:5000/flaskapi/delete_work_package',{
    'method': 'POST',
    headers : {
    'Content-Type' : 'application/json'},
    body:JSON.stringify(body)})
    .then(response => response.json())
    .catch(error => console.log(error))
    }
}