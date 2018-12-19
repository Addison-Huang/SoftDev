//FannyPack
//Addison Huang, Michelle Tang
//SoftDev1 pd6
//K29 -- Sequential Progression
//2018-12-20

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
	     return a
    }

    // finds the smallest interval between the two numbers,
    // if that interval fully divides into b, that is the gcd
    else {
	     return gcd(b, a % b)
    }

};

var stulist = ["james", "tyler", "lauren", "becky", "oliver", "frank"];

var randstu = function(){

    // random num in range
    var num = Math.floor(Math.random() * stulist.length);

    // index that
    return stulist[num];
};

var fibBut = function() {
    console.log(fibb(8));
    var tag = document.createElement('h4');
    var element = document.createTextNode(fibb(8));
    tag.appendChild(element);
}

var fib = document.getElementById("fib");
fib.addEventListener('click', fibBut);

var gcdd = document.getElementById("gcd");
gcdd.addEventListener('click', gcdd);

