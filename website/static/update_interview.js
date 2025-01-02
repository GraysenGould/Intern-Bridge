
function update_interview () {
    fetch("/interview-questions")
        .then(response => response.json()
        .then(data => console.log(data))
        .catch(error => console.errror(er))
        )
}