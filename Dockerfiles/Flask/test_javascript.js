function callChatbot() {
    let httpRequest = new XMLHttpRequest();
    httpRequest.open("POST", "/ReEdgeGPT/chat", true)
    httpRequest.setRequestHeader("content-type", "application/json")
    httpRequest.send(JSON.stringify({
        "prompt": "Deer stew",
        "conversation_style": "balanced",
        "simplify_response": true,
        "attachment": null
    }))
    httpRequest.onreadystatechange = function () {
        if (httpRequest.readyState === XMLHttpRequest.DONE && httpRequest.status === 200) {
            console.log(httpRequest.response)
        } else if (httpRequest.readyState === XMLHttpRequest.DONE && httpRequest.status !== 200) {
            console.log(httpRequest.response)
        }
    }
}

function callImagebot() {
    let httpRequest = new XMLHttpRequest();
    httpRequest.open("POST", "/ReEdgeGPT/image", true)
    httpRequest.setRequestHeader("content-type", "application/json")
    httpRequest.send(JSON.stringify({
        "prompt": "La Tour Eiffel",
    }))
    httpRequest.onreadystatechange = function () {
        if (httpRequest.readyState === XMLHttpRequest.DONE && httpRequest.status === 200) {
            console.log(httpRequest.response)
        } else if (httpRequest.readyState === XMLHttpRequest.DONE && httpRequest.status !== 200) {
            console.log(httpRequest.response)
        }
    }
}