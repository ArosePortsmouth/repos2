// set the dimensions and margins of the graph
var width = 500
    height = 500
    margin = 250



var radius = Math.min(width, height) - margin

// append the svg object to the div called 'my_dataviz'
var svg = d3.select("#my_dataviz")
  .append("svg")
    .attr("width", width)
    .attr("height", height)
  .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

// Create data-set
var data= {"42":{"Country":"Africa","Hectares":624102.627},"65":{"Country":"Northern Africa","Hectares":28835.938},"90":{"Country":"Sub-Saharan Africa","Hectares":595266.689},"113":{"Country":"Eastern Africa","Hectares":197307.686},"134":{"Country":"Middle Africa","Hectares":303250.6},"155":{"Country":"Southern Africa","Hectares":27635.0},"176":{"Country":"Western Africa","Hectares":67073.403},"197":{"Country":"Americas","Hectares":1592663.3419999999},"220":{"Country":"Northern America","Hectares":657168.02},"245":{"Country":"Latin America & the Caribbean","Hectares":935495.322},"268":{"Country":"Caribbean","Hectares":7194.406},"289":{"Country":"Central America","Hectares":86290.3},"310":{"Country":"South America","Hectares":842010.6159999999},"331":{"Country":"Asia","Hectares":593361.5989999999},"354":{"Country":"Central Asia","Hectares":11704.9},"379":{"Country":"Eastern Asia","Hectares":257047.1},"404":{"Country":"South-eastern Asia","Hectares":210758.76},"429":{"Country":"Southern Asia","Hectares":94086.915},"454":{"Country":"Western Asia","Hectares":19763.924},"479":{"Country":"Europe","Hectares":1015482.4759999999},"502":{"Country":"Eastern Europe","Hectares":860425.0},"523":{"Country":"Northern Europe","Hectares":74734.759},"544":{"Country":"Southern Europe","Hectares":45638.717},"565":{"Country":"Western Europe","Hectares":34684.0},"588":{"Country":"Oceania","Hectares":173523.578},"613":{"Country":"Australia and New Zealand","Hectares":134903.46}}

const sorted = Object.values(data).sort((a, b) => a.Hectares - b.Hectares);
console.log(sorted)

var pieTitle = svg.append("text")
  .style("text-anchor", "middle")
  .attr("x", parseInt(width/40 - 10))
  .attr("y", height -710 )
  .style("font-family", "sans-serif")
  .text("REGIONS WITH THE HIGHEST FOREST COVER BY HECTARES")

function funct(){
  var data2 = {}
  var obj = Object.values(sorted)
  for (var i = 0; i<obj.length; i++){
    data2[obj[i].Country] = obj[i].Hectares
  }
  return data2
}



sortPie = funct()

console.log(data)

var dataList = Object.values(data)
dataList.sort((a, b) => b - a);
var labelLim = 250000
console.log(labelLim)







// set the color scale
var color = d3.scaleOrdinal()
  .domain(["a", "b", "c", "d", "e", "f", "g", "h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
  //.range(["#e8f6e3", "green"]);
  //.range(["#f0f8f0", "#00f800","#0A7514","#0A7F15","#0A8915","#0A9316","#099E17","#09A817","#08B217","#07BD18","#06C818","#05D318","#04DD18","#03E918","#02F417","#00FF17","#12FC27","#24F937","#36F647","#47F456","#57F265","#68F174","#77F082","#87F090","#96F09E","#A4F0AB","#B2F1B8","#C0F2C4","#CDF4D1"]);
  .range(["#00FF00", "#00FF00","#00FF00","#00FF00","#00FF17","#03F719","#06EF1B","#09E71D","#0CDF1F","#0FD721","#11CF22","#14C824","#16C025","#18B927","#1AB228","#1CAB29","#1EA42A","#1F9D2B","#21972B","#22902C","#238A2D","#25842D","#267E2D","#26782E","#27722E", "#29692A"]);
// Compute the position of each group on the pie:
var pie = d3.pie()
  .sort(null) // Do not sort group by size
  .value(function(d) {return d.value; })
var data_ready = pie(d3.entries(sortPie))

// The arc generator
var arc = d3.arc()
  .innerRadius(radius * 0.5)         // This is the size of the donut hole
  .outerRadius(radius * 0.8)

// Another arc that won't be drawn. Just for labels positioning
var outerArc = d3.arc()
  .innerRadius(radius * 0.9)
  .outerRadius(radius * 0.9)

// Build the pie chart: Basically, each part of the pie is a path that we build using the arc function.
svg
  .selectAll('allSlices')
  .data(data_ready)
  .enter()
  .append('path')
  .attr('d', arc)
  .attr('fill', function(d){ return(color(d.data.key)) })
  .attr("stroke", "white")
  .style("stroke-width", "2px")
  .style("opacity", 0.7)




svg
  .selectAll('allLabels')
  .data(data_ready)
  .enter()
  .append('text')
    //.text( function(d) { console.log(d.data.key) ; if(d.data.value<labelLim){return ''} else{return d.data.key }} )
    .attr('transform', function(d) {
        var _d = arc.centroid(d);
        _d[0] *= 1;	//multiply by a constant factor
        _d[1] *= 1;	//multiply by a constant factor
        return "translate(" + _d + ")";
      })
      .style("text-anchor", "middle")
      .style("font", "10px times")
      
      .text(function(d) { 
        if(d.data.value<labelLim){return ''} else{return d.data.key }
    })