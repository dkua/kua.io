anchorHeaders = function() {
  var headers = document.querySelectorAll("h1, h2, h3, h4, h5, h6");
  for (var i = 0; i < headers.length; i++) {
    var anchor = document.createElement("sup");
    var aTag = document.createElement("a");
    aTag.setAttribute("href", "#"+headers[i].id);
    aTag.innerHTML = "&para;";
    anchor.appendChild(aTag);
    headers[i].appendChild(anchor);
  }
}

anchorCitations = function() {
  var citations = document.getElementsByClassName("cite");

  // Find all the citations and store their id.
  var d = {};
  for (var i = 0; i < citations.length; i++) {
    if (!(citations[i].id in d)) {
      var href = citations[i].href;
      d[citations[i].id] = href.substring(href.lastIndexOf("#")+1);
    }
  }

  for (var id in d) {
    var citation = document.getElementById(d[id]).querySelector(".citation")
    var cites = document.querySelectorAll("#".concat(id));
    if (cites.length == 1) { // Add the single single link
      var i = 0;
      cites[i].id = cites[i].id.concat("-", i);
      var backTag = document.createElement("a");
      backTag.setAttribute("href", "#".concat(cites[i].id));
      backTag.innerHTML = "&#8629;";
      citation.appendChild(backTag);
    } else { // Add back text + the multiple anchor links
      citation.insertAdjacentHTML("beforeend", "&#8629;");
      var anchors = document.createElement("sup");
      for (var i = 0; i < cites.length; i++) {
        cites[i].id = cites[i].id.concat("-", i);
        var aTag = document.createElement("a");
        aTag.innerText = i;
        aTag.setAttribute("href", "#".concat(cites[i].id));
        anchors.appendChild(aTag);
      }
      citation.appendChild(anchors);
    }
  }
}
