// https://stackoverflow.com/questions/4810841/pretty-print-json-using-javascript
function syntaxHighlight(json) {
    json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function (match) {
        let cls = 'number';
        if (/^"/.test(match)) {
            if (/:$/.test(match)) {
                cls = 'key';
            } else {
                cls = 'string';
            }
        } else if (/true|false/.test(match)) {
            cls = 'boolean';
        } else if (/null/.test(match)) {
            cls = 'null';
        }
        return '<span class="' + cls + '">' + match + '</span>';
    });
}

let jsonObj = {
    "temperature": "2.3 C",
    "units": "metric",
    "city": "Gothenburg",
    "country": "SE",
    "weather": "Clouds",
    "lat": 57.7072,
    "lon": 11.9668
};

let jsonStr = JSON.stringify(jsonObj, undefined, 4);
document.getElementById("json-example").innerHTML = syntaxHighlight(jsonStr);
