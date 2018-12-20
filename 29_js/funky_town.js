//FannyPack
//Addison Huang, Michelle Tang
//SoftDev1 pd6
//K29 -- Sequential Progression
//2018-12-19

var fibb = function(n){
    // base case 0
    if(n == 0){
	     return 0;
    }
    // base case 1
    else if (n == 1){
	     return 1;
    }
    // add prev two
    else{
	     return fibb(n -1) + fibb(n -2);
    }
};

var gcd = function (a,b) {
    // this means the previous modulo was 0, so a divided into b
    if (b == 0) {
	return a;
    }
    // finds the smallest interval between the two numbers,
    // if that interval fully divides into b, that is the gcd
    else {
	return gcd(b, a % b);
    }
};

var stulist = ["james", "tyler", "lauren", "becky", "taylor", "swift"];

var randstu = function(){
    // random num in range
    var num = Math.floor(Math.random() * stulist.length);
    // index that
    return stulist[num];
};

// If the event is 'clicked,' follow this fib function
var jFib = document.getElementById("fib");
jFib.addEventListener("click", function() {
    console.log("Finds the nth number in the fib sequence, fibb(5):");
    var ans = fibb(5);
    console.log(ans);
    var para = document.createElement("h4");
    var node = document.createTextNode("fibb(5)= " + ans);
    para.appendChild(node);
    var element = document.getElementById("ans");
    element.appendChild(para);
});

// If the event is 'clicked,' follow this GCD function
var jGcd = document.getElementById("gcd");
jGcd.addEventListener("click", function() {
    console.log("Finds the GCD, gcd(120, 75):");
    var ans = gcd(120,75);
    console.log(ans);
    var para = document.createElement("h4");
    var node = document.createTextNode("gcd(120,75)= " + ans);
    para.appendChild(node);
    var element = document.getElementById("ans");
    element.appendChild(para);
});

// If the event is 'clicked,' follow this random student function
var jRandS = document.getElementById("rand");
jRandS.addEventListener("click", function() {
    console.log("Gets a random student, randstu():");
    var ans = randstu();
    console.log(ans);
    var para = document.createElement("h4");
    var node = document.createTextNode("randstu()= " + ans);
    para.appendChild(node);
    var element = document.getElementById("ans");
    element.appendChild(para);
});
