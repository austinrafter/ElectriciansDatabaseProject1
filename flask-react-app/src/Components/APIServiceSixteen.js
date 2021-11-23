export default class APIServiceSixteen{
    static InsertMaterialToWorkPackage(body){
    return fetch('http://localhost:5000/insert_material_in_work_package',{
    'method': 'POST',
    headers : {
    'Content-Type' : 'application/json'},
    body:JSON.stringify(body)})
    .then(response => response.json())
    .catch(error => console.log(error))
    }
}