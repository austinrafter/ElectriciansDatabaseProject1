export default class APIServiceThirteen{
    static DeleteInventory(body){
    return fetch('http://localhost:5000/delete_inventory',{
    'method': 'POST',
    headers : {
    'Content-Type' : 'application/json'},
    body:JSON.stringify(body)})
    .then(response => response.json())
    .catch(error => console.log(error))
    }
}