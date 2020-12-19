// Create an array of each country's numbers
let url = 'api/v1.0/hot'
d3.json(url).then(function(data){
  console.log(data);
  
  let distinctiveFeatures = [];
  data.forEach(item => distinctiveFeatures.push(item.distinctive_features));
  console.log(distinctiveFeatures);

  let sex = [];
  data.forEach(item => sex.push(item.sex));
  console.log(sex);

  // let eyeColor = [];
  // data.forEach(item => eyeColor.push(item.eye_color));
  // console.log(eyeColor);
  function onlyUnique(value, index, self) {
    return self.indexOf(value) === index;
  }
  let distinctive = data.distinctive_features;
  let disCount = distinctive.filter(onlyUnique)
  let disLength = distinctive.length
  // let distinctCounts = distinctive.c
  // console.log(distinctCounts)
  console.log(disCount)
  console.log(disLength)
});


// let distinct = Object.values(data.distinct);
// let sex = Object.values(data.sex);
// Create an array of music provider labels
// let labels = Object.keys(data.distinct);

// Display the default plot
function init() {
  let data = [{
    // values: distinct,
    // labels: labels,
    type: "pie"
  }];

  let layout = {
    height: 600,
    width: 800
  };

  Plotly.newPlot("pie", data, layout);
}

// On change to the DOM, call getData()
d3.selectAll("#selDataset").on("change", getData);

// Function called by DOM changes
function getData() {
  let dropdownMenu = d3.select("#selDataset");
  // Assign the value of the dropdown menu option to a variable
  let dataset = dropdownMenu.property("value");
  // Initialize an empty array for the country's data
  let data = [];

  // if (dataset == 'distinct') {
  //     data = distinct;
  // }
  // else if (dataset == 'sex') {
  //     data = sex;

}
  // Call function to update the chart
//   updatePlotly(data);
// }

// Update the restyled plot's values
function updatePlotly(newdata) {
  Plotly.restyle("pie", "values", [newdata]);
}

init();