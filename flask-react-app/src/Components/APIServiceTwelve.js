export default class APIServiceTwelve{
    static InsertInventory(body){
    return fetch('http://localhost:5000/flaskapi/add_inventory',{
    'method': 'POST',
    headers : {
    'Content-Type' : 'application/json'},
    body:JSON.stringify(body)})
    .then(response => response.json())
    .catch(error => console.log(error))
    }
}