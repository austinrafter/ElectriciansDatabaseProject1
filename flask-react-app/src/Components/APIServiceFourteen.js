export default class APIServiceFourteen{
    static InsertElectricianToWorkPackage(body){
    return fetch('http://localhost:5000/add_electrician_to_work_package',{
    'method': 'POST',
    headers : {
    'Content-Type' : 'application/json'},
    body:JSON.stringify(body)})
    .then(response => response.json())
    .catch(error => console.log(error))
    }
}