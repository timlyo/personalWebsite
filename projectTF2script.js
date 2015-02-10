var selectedClass

function init(){
	document.getElementById("scout").addEventListener("click", onClassSelect(1))
	document.getElementById("soldier").addEventListener("click", onClassSelect(2))
	document.getElementById("pyro").addEventListener("click", onClassSelect(3))
	document.getElementById("demoman").addEventListener("click", onClassSelect(4))
	document.getElementById("heavy").addEventListener("click", onClassSelect(5))
	document.getElementById("engineer").addEventListener("click", onClassSelect(6))
	document.getElementById("medic").addEventListener("click", onClassSelect(7))
	document.getElementById("sniper").addEventListener("click", onClassSelect(7))
	document.getElementById("spy").addEventListener("click", onClassSelect(8))
}

function onClassSelect(var class){
	console.log("click");
}