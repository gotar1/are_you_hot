

d3.select("tbody")
.selectAll("tr")
.data(austinWeather)
.enter()
.append("tr")
.html(function(d) {
  return `<td>${d.date}</td><td>${d.low}</td><td>${d.high}</td>`
});