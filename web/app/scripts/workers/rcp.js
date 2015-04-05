// var myDataRef = new Firebase('https://aljohri-polls.firebaseio-demo.com/');
// myDataRef.set('User ' + name + ' says ' + text);

// var r = new XMLHttpRequest();
// r.open("GET", "http://cdn.realclearpolitics.com/epolls/json/latest_election_polls_clean.js", true);
// r.onreadystatechange = function () {
//     if (r.readyState != 4 || r.status != 200) return;
//     console.log(r.responseText);
// };
// r.send();


 // worker.js
this.onmessage = function (url) {
    getDataFromURL(url.data);
};

var HttpClient = function () {
    this.get = function (Url, Callback) {
        HttpRequest = new XMLHttpRequest();
        HttpRequest.onreadystatechange = function () {
        if (HttpRequest.readyState == 4 && HttpRequest.status == 200) {
                console.log(HttpRequest.responseText.length);
                Callback(HttpRequest.responseText);
            }
        }
        HttpRequest.open("GET", Url, true);
        HttpRequest.send(null);
    }
};

function getDataFromURL(url) {
    Client = new HttpClient();
    Client.get(url, function (answer) {
        postMessage(answer);
    });
}