function sendChatPrompt() {
    const inputTextArea = document.getElementById("inputTextArea")
    const chatText = document.getElementById("chatTextArea")
    let prompt_text = inputTextArea.value
    inputTextArea.value = ""
    const httpRequest = new XMLHttpRequest();
    httpRequest.open("POST", "/ReEdgeGPT/chat", true)
    httpRequest.setRequestHeader("content-type", "application/json")
    httpRequest.send(
        JSON.stringify({
            "prompt": prompt_text,
            "conversation_style": null,
            "simplify_response": true,
            "attachment": null
        })
    )
    httpRequest.onreadystatechange = function () {
        if (httpRequest.readyState === XMLHttpRequest.DONE && httpRequest.status === 200) {
            let responseJson = JSON.parse(httpRequest.response)
            console.log(responseJson)
            sourceText = responseJson["sources"]
            chatText.innerHTML +=  `
                       <div class="d-flex flex-row justify-content-start mb-4">
                           <div class="p-3 ms-3" style="border-radius: 15px; background-color: rgba(57, 192, 237,.2);">
                               <p class="small mb-0">
                                   ${sourceText}
                               </p>
                           </div>
                       </div>`
        }
    }
}


