function changeColor(number) {
  colorlst = ["red", "orange", "yellow", "green", "blue", "purple", "pink"];
  num = document.getElementById(number);
	new_color = colorlst[Math.floor(Math.random() * 7)];
  num.style.color = new_color;
}

function generateColors() {
  changeColor("num1");
  changeColor("num2");
  changeColor("num3");
}

function generateNewTopColor(){
	changeColor("num1");
}
function generateNewMiddleColor(){
	changeColor("num2");
}
function generateNewBottomColor(){
	changeColor("num3");
}

function randNum(number){
	num = document.getElementById(number);
  new_num = Math.floor(Math.random() * 10);
 	num.innerText=new_num.toString();
}

function generateSet(){
  randNum("num1");
  randNum("num2");
  randNum("num3"); 
}

function generateNewTopNum(){
	randNum("num1");
}
function generateNewMiddleNum(){
	randNum("num2");
}
function generateNewBottomNum(){
	randNum("num3");
}

function start(){
	location.href="/match";
}
