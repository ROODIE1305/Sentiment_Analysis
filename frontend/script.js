document.getElementById("sentiment-feedback-form").addEventListener("submit", async function (event) {
event.preventDefault(); // this finction will allows to prevent the page from getting refreshed  
const feedback = document.getElementById("sentiment-feedback-input").value;

try{
    const response = await fetch("http://localhost:8000/analyze", {
        method: "POST",
        headers: {"content-type": "application/json"},
        body: JSON.stringify({text: feedback})
    });

    const data= await response.json();
    document.getElementById("result").textContent =
    `Feedback: ${data.feedback} -> Sentiment: ${data.sentiment}`;
}catch (error){
    console.error("Error: ",error);
    document.getElementById("result").textContent = "Error in the backend side.";

}

});