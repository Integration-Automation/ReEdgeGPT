let httpRequest = new XMLHttpRequest();
httpRequest.open("POST", "/ReEdgeGPT/chat", true)
httpRequest.setRequestHeader("content-type", "application/json")
httpRequest.send(JSON.stringify({
    "prompt": "Deer stew",
}))
httpRequest.onreadystatechange = function () {
    if (httpRequest.readyState === XMLHttpRequest.DONE && httpRequest.status === 200) {
        console.log(httpRequest.response)
    } else if (httpRequest.readyState === XMLHttpRequest.DONE && httpRequest.status !== 200) {
        console.log(httpRequest.response)
    }
}