let loadingInterval;

let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    startLoading(); // 🔥 start animation

    let xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState == 4) {
            stopLoading(); // 🔥 stop animation

            if (this.status == 200) {
                document.getElementById("system_response").innerHTML = xhttp.responseText;
            } else {
                document.getElementById("system_response").innerHTML = "Error: Unable to fetch sentiment.";
            }
        }
    };

    xhttp.open("GET", "sentimentAnalyzer?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);

    xhttp.send();
};

function startLoading() {
    let dots = 0;
    loadingInterval = setInterval(() => {
        dots = (dots + 1) % 4;
        document.getElementById("system_response").innerHTML = "Analyzing" + ".".repeat(dots);
    }, 500);
}

function stopLoading() {
    clearInterval(loadingInterval);
}
