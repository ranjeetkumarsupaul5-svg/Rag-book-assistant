const questionInput = document.getElementById("questionInput");
const sendButton = document.getElementById("sendButton");
const chatBox = document.getElementById("chatBox");
const fileInput = document.getElementById("fileInput");
const uploadButton = document.getElementById("uploadButton");
const uploadStatus = document.getElementById("uploadStatus");


function addMessage(message, type) {

    const messageDiv = document.createElement("div");

    messageDiv.className = `message ${type}`;

    const avatar = document.createElement("div");
    avatar.className = "avatar";
    avatar.textContent = type === "user" ? "You" : "AI";

    const content = document.createElement("div");
    content.className = "message-content";

    const paragraph = document.createElement("p");
    paragraph.textContent = message;

    content.appendChild(paragraph);

    messageDiv.appendChild(avatar);
    messageDiv.appendChild(content);

    chatBox.appendChild(messageDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}


/* Upload Book */

async function uploadBook() {

    const file = fileInput.files[0];

    if (!file) {
        uploadStatus.textContent = "Please select a PDF first.";
        return;
    }

    if (!file.name.toLowerCase().endsWith(".pdf")) {
        uploadStatus.textContent = "Only PDF files are allowed.";
        return;
    }

    uploadButton.disabled = true;
    uploadButton.textContent = "Processing...";
    uploadStatus.textContent = "Uploading and processing your book...";

    const formData = new FormData();

    formData.append("file", file);

    try {

        const response = await fetch("/upload", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (!response.ok) {
            uploadStatus.textContent = data.message;
            return;
        }

        uploadStatus.textContent =
            `✅ ${data.filename} uploaded successfully! ` +
            `${data.pages} pages processed.`;

        addMessage(
            `Your book "${data.filename}" is ready! You can now ask questions about it.`,
            "assistant"
        );

    } catch (error) {

        uploadStatus.textContent =
            "Something went wrong while uploading the book.";

        console.error(error);

    } finally {

        uploadButton.disabled = false;
        uploadButton.textContent = "Upload PDF";

    }
}


/* Ask Question */

async function sendQuestion() {

    const question = questionInput.value.trim();

    if (!question) {
        return;
    }

    addMessage(question, "user");

    questionInput.value = "";

    sendButton.disabled = true;
    sendButton.textContent = "Thinking...";


    const typingDiv = document.createElement("div");

    typingDiv.className = "message assistant";
    typingDiv.id = "typingMessage";

    typingDiv.innerHTML = `
        <div class="avatar">AI</div>
        <div class="message-content">
            <p class="typing">Thinking...</p>
        </div>
    `;

    chatBox.appendChild(typingDiv);

    chatBox.scrollTop = chatBox.scrollHeight;


    try {

        const response = await fetch("/ask", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });


        const data = await response.json();


        const typingMessage =
            document.getElementById("typingMessage");

        if (typingMessage) {
            typingMessage.remove();
        }


        addMessage(data.answer, "assistant");


    } catch (error) {

        const typingMessage =
            document.getElementById("typingMessage");

        if (typingMessage) {
            typingMessage.remove();
        }

        addMessage(
            "Something went wrong. Please try again.",
            "assistant"
        );

        console.error(error);

    }


    sendButton.disabled = false;
    sendButton.textContent = "Send";

    questionInput.focus();
}


/* Suggestion Questions */

function askQuestion(question) {

    questionInput.value = question;

    sendQuestion();

}


/* Enter Key */

questionInput.addEventListener("keydown", function(event) {

    if (event.key === "Enter" && !event.shiftKey) {

        event.preventDefault();

        sendQuestion();

    }

});