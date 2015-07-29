"use strict";

//see javascript/levenshetinenate.js for full source + credits
var levenshteinenator=function(){function r(r,t){var a,e=r.length,v=t.length;if(v>e){var f=r;r=t,t=f;var o=e;e=v,v=o}var u=[];u[0]=[];for(var f=0;v+1>f;++f)u[0][f]=f;for(var c=1;e+1>c;++c){u[c]=[],u[c][0]=c;for(var h=1;v+1>h;++h)a=r.charAt(c-1)===t.charAt(h-1)?0:1,u[c][h]=n(u[c-1][h]+1,u[c][h-1]+1,u[c-1][h-1]+a)}return u}function n(r,n,t){return n>r&&t>r?r:r>n&&t>n?n:t}return r}();

function onInputChange(){
	var string = $("#searchBox").val();

	$("#searchResults").empty();
	var results = new Set();

	//pages loaded in header
	for(var key in pages){
		var distArray = levenshteinenator(string, key);
		var dist = distArray[ distArray.length - 1 ][ distArray[ distArray.length - 1 ].length - 1 ];

		if(dist < 7){
			var pagename = pages[key].replace(".html", "");
			var html = "<li> <a href=" + pages[key] + ">" + pagename + "</a></li>";
			results.add("<li>	 <a href=" + pages[key] + ">" + pagename + "</a></li>")
		}
	}

	// results.sort();
	console.log(results);
	for(let result of results.values()) $(result).appendTo("#searchResults").hide().slideDown();
}

$("#searchBox").on("input", onInputChange);
