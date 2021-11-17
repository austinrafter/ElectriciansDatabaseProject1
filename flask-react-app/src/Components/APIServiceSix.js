export default class APIServiceSix{
    static CheckPositionTwo(body){
    return fetch('http://localhost:5000/project_manager',{
    'method': 'POST',
    headers : {
    'Content-Type' : 'application/json'},
    body:JSON.stringify(body)})
    .then(response => response.json())
    .catch(error => console.log(error))
    }
}