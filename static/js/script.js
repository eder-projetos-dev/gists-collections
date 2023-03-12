clickfunc = function(link) {
  var t = link.innerText || link.textContent;
  //alert(t);
  document.write("<h2>Tag "+t+"</h2>");
}