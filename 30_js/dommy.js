/* Team SmallFish - Addison Huang and Dennis Chen
SoftDev1 pd6
K30 -- Sequential Progression III: Season of the Witch
2018-12-20*/

/*Changes the text of the heading when you mouse over or mouse out of an item in the list*/
var changeHeading = function(e) {
    var h = document.getElementById("h");
    //console.log(e);
    if (e.type == 'mouseover'){
	//console.log(this.innerHTML);
	h.innerHTML = this.innerHTML;
    }
    else{
	h.innerHTML = 'Hello World';
    }
};

/*removes an item from the list if you click on it*/
var removeItem = function(e) {
    //console.log(e);
    this.remove();
};

/*Adds event listeners for element in the list*/
var lis = document.getElementsByTagName("li");
for(var i=0; i < lis.length; i++) {
    lis[i].addEventListener('mouseover',changeHeading);
    lis[i].addEventListener('mouseout',changeHeading);
    lis[i].addEventListener('click',removeItem);
};

/*Adds WORD to the list when you click The button and gives it event listeners*/
var addItem = function(e) {
    var list = document.getElementById('thelist');
    var item = document.createElement("li");
    item.innerHTML = 'WORD';
    list.appendChild(item);
    lis[lis.length - 1].addEventListener('mouseover',changeHeading);
    lis[lis.length - 1].addEventListener('mouseout',changeHeading);
    lis[lis.length - 1].addEventListener('click',removeItem);
};
var button = document.getElementById("b");
button.addEventListener('click', addItem);

/*recursive fib function that doesn't use dynamic programming*/
var fib = function(n) {
    if(n < 2){
        return 1;
    } else {
        return fib(n-1) + fib(n-2);
    }
};
/*Adds the fibIndex of the fibonacci sequence when fib button is clicked and increments fibIndex with each click*/
var fibIndex = 1
var addFib = function(e){
    var lis = document.getElementById('fiblist');
    var item = document.createElement('li');
    item.innerHTML = fib(fibIndex);
    fibIndex += 1;
    lis.appendChild(item);
    //console.log(e);
};

/*recursive fib function that uses dynamic programming*/
var fibonacci = function(n) {
  var sum = [0,1];
  for (var i = 2; i <= n; i++) {
    sum.push(sum[i-2] + sum[i-1]);
  }
  return sum[sum.length - 1];
};

/*Adds the fibIndex of the fibonacci sequence when fib button is clicked and increments fibIndex with each click*/
var addFib2 = function(e){
    var lis = document.getElementById('fiblist');
    var item = document.createElement('li');
    item.innerHTML = fibonacci(fibIndex);
    fibIndex += 1;
    lis.appendChild(item);
    //console.log(e);
};

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
