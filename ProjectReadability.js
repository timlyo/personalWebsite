var subredditList = ["announcements", "art", "askreddit", "askscience", "aww", "blog", "books", "creepy", "dataisbeautiful", "diy",
	"documentaries", "earthporn", "explainlikeimfive", "fitness", "food", "funny", "futurology", "gadgets", "gaming",
	"getmotivated", "gifs", "history", "iama", "internetisbeautiful", "jokes", "lifeprotips", "listentothis",
	"mildlyinteresting", "movies", "music", "news", "nosleep", "nottheonion", "oldschoolcool", "personalfinance",
	"philosophy", "photoshopbattles", "pics", "science", "showerthoughts", "space", "sports", "television", "tifu",
	"todayilearned", "twoxchromosomes", "upliftingnews", "videos", "worldnews", "writingprompts", "writing"];

var options = {
    hAxis: {title: 'Score'},
    vAxis: {title: 'Readability'},
    legend: 'none'
};

var chart;

function createChart(){
    console.log("Creating chart");

    chart = new google.visualization.ScatterChart(document.getElementById("chart"));

    draw();
}

function draw(){
    rawData = [['readability', 'score'],];
    for(var i = 0; i < subredditList.length; i++){
        if(document.getElementById(subredditList[i]).checked){
            console.log("showing " + subredditList[i])
            console.log(subredditList[i]);
            rawData = rawData.concat(allData[i])
        }
    }
    
    console.log(rawData);
    
    var data = google.visualization.arrayToDataTable(rawData);
    
    chart.draw(data, options);
    console.log("Done with chart");
}

function selectDefaults(){
    document.getElementById("announcements").checked = true;
    document.getElementById("funny").checked = true;
}