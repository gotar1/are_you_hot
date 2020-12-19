let url = 'api/v1.0/hot'

// Initializes the page with a default plot
function init() {
  // let trace1 = {
  //   x: [1, 2, 3, 4, 5],
  //   y: [1, 2, 4, 8, 16],
  //   // orientation: 'h',
  //   type: 'bar',
  //   // text: y
  // };

  // let dataTrace = [trace1];

  // let barLayout = {
  //   // title: "Bacteria Concentration Bar Chart",
  //   margin: {
  //     l: 100,
  //     r: 100,
  //     t: 100,
  //     b: 100
  //   }
  // };

  // Plotly.newPlot('plot', dataTrace, barLayout); 
  data1 = [{
    x: [1, 2, 3, 4, 5],
    y: [1, 2, 4, 8, 16], 
    type: 'bar'}];
  Plotly.newPlot("plot", data1);
};

// Call updatePlotly() when a change takes place to the DOM
d3.selectAll("#selDataset").on("change", updatePlotly);
// This function is called when a dropdown menu item is selected
function updatePlotly() {
  // Use D3 to select the dropdown menu
  let dropdownMenu = d3.select("#selDataset");

  // Assign the value of the dropdown menu option to a variable
  let dataset = dropdownMenu.property("value");

  // Initialize x and y arrays
  let x = [];
  let y = [];

  // / let hotData = data.filter(item => item;
  // console.log(filteredRecovery);
  // let covidData = data;
  // console.log(hotData);

  d3.json(url).then(function(data){
    console.log(data);
    
    let hotTest = [];
    data.forEach(item => hotTest.push(item.hot_test));
    console.log(hotTest);
  
    let hairColor = [];
    data.forEach(item => hairColor.push(item.hair_color));
    console.log(hairColor);
  
    let eyeColor = [];
    data.forEach(item => eyeColor.push(item.eye_color));
    console.log(eyeColor);
  
  });
  
  if (dataset === 'EyeColor') {
  x = hotTest;
  y = eyeColor;
  };

  if (dataset === 'HairColor') {
    x = [10, 20, 30, 40, 50];
    y = [1, 10, 100, 1000, 10000];
  };

  // Note the extra brackets around 'x' and 'y'
  Plotly.restyle("plot", "x", [x]);
  Plotly.restyle("plot", "y", [y]);  
};
init();