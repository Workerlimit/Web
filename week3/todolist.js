var list = document.querySelector('ul');
var nodes = document.getElementsByTagName("LI");
var i;
var close = document.getElementsByClassName("delete");

list.addEventListener('click', function(ev) {
  if (ev.target.tagName === 'LI') {
    ev.target.classList.toggle('checking');
  }
}, false);

function newItem() {
  var li = document.createElement("li");
  var input = document.getElementById("input-text").value;
  var t = document.createTextNode(input);
  li.appendChild(t);
  if (input === '') {
    alert("You must write something!");
  } else {
    document.getElementById("list-ul").appendChild(li);
  }
  document.getElementById("input-text").value = "";
    
  img = document.createElement("img");
  img.src = "trash.jfif";
  img.className = "delete";
  document.getElementsByTagName("LI").appendChild(img);

  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}

for (i = 0; i < nodes.length; i++) {
    var img1 = document.createElement("img");
    img1.src = "trash.jfif";
    img1.className = "delete";
    nodes[i].appendChild(img1);
}

for (i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    var div = this.parentElement;
    div.style.display = "none";
  }
}