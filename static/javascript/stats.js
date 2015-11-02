ram_chart = null;
cpu_chart = null;

function get_ram(){
	$.ajax({
		url: "/_ram",
		dataType: "json",
		success: function(msg){
			kernel = msg["kernel"],
			server = msg["server"],
			other = msg["other"],
			data = {series: [msg["server"], msg["other"]]};
			ram_chart.options.total = msg["total"];
			ram_chart.update(data, ram_chart.options);
		}
	})
}

function get_cpu(){
	$.ajax({
		url: "/_cpu",
		dataType: "json",
		success: function(msg){
			percentage = msg["percentage"],
			data = {series: [percentage]};
			cpu_chart.update(data, ram_chart.options);
		}
	})
}

function create_graphs(){
	ram_chart = new Chartist.Pie('#ram', {
        labels: ["server", "other"],
        series: []
    }, {
      donut: true,
      startAngle: 0,
      donutWidth: 60,
      showLabel: true
    });

	cpu_chart = new Chartist.Line('#cpu', {
        series: [[5, 1, 10, 4]],
        labels: ["5","4", "3", "2", "1"]
    }, {
		showLabel: true,
    });

    console.log(cpu_chart);
}
