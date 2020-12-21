// base url
let url = "/api/v1.0/hot"

// /create d3 api querry and build bar charts...
d3.json(url).then((data) =>{
  let dataCopy = data;
  console.log(dataCopy);

  let sex = [];
  dataCopy.forEach(item => sex.push(item.sex));
  console.log(sex);

  let eyeColor = [];
  dataCopy.forEach(item => eyeColor.push(item.eye_color));
  console.log(eyeColor);

  let distinctiveFeatures= [];
  dataCopy.forEach(item => distinctiveFeatures.push(item.distinctive_features));
  console.log(distinctiveFeatures);

  let ratio = [];
  dataCopy.forEach(item => ratio.push(item['ratio(wt/ht)']));
  console.log(ratio);

  let age = [];
  dataCopy.forEach(item => age.push(item.age));
  console.log(age);

  let hotTest = [];
  dataCopy.forEach(item => hotTest.push(item.hot_test));
  console.log(hotTest);
  
  // build bar chart for Eye Color..
  let trace1 = {
    x: eyeColor.reverse(),
    y: hotTest.reverse(),
    type: 'bar',
    text: sex.reverse()
  };

  let dataTrace1 = [trace1];

  let barLayout1 = {
    title: "Eye Color",
    margin: {
      l: 100,
      r: 100,
      t: 100,
      b: 100
    }
  };

  Plotly.newPlot('eyebar', dataTrace1, barLayout1); 

  // build bar chart for Sex..
  let trace2 = {
    x:sex.reverse(),
    y: hotTest.reverse(),
    type: 'bar',
    text: sex
  };

  let dataTrace2 = [trace2];

  let barLayout2 = {
    title: "Sex",
    margin: {
      l: 100,
      r: 100,
      t: 100,
      b: 100
    },
  };

  Plotly.newPlot('sexbar', dataTrace2, barLayout2); 

  // build bar chart for Distinctive Feature..
  let trace3 = {
    x: distinctiveFeatures.reverse(),
    y: hotTest.reverse(),
    type: 'bar',
    text: sex.reverse()
  };

  let dataTrace3 = [trace3];

  let barLayout3 = {
    title: "Distinctive Features",
    margin: {
      l: 100,
      r: 100,
      t: 100,
      b: 100
    }
  };

  Plotly.newPlot('distbar', dataTrace3, barLayout3); 

  // build bar chart for Weight/Height Ratio.. 
  let trace4 = {
    x: ratio.reverse(),
    y: hotTest.reverse(),
    type: 'bar',
    text: sex.reverse()
  };

  let dataTrace4 = [trace4];

  let barLayout4 = {
    title: "Ratio (wt/ht)",
    margin: {
      l: 100,
      r: 100,
      t: 100,
      b: 100
    }
  };

  Plotly.newPlot('ratiobar', dataTrace4, barLayout4); 

  // build bar for Age..
  let trace5 = {
    x: age.reverse(),
    y: hotTest.reverse(),
    type: 'bar',
    text: sex.reverse()
  };

  let dataTrace5 = [trace5];

  let barLayout5 = {
    title: "Age",
    margin: {
      l: 100,
      r: 100,
      t: 100,
      b: 100
    }
  };

  Plotly.newPlot('agebar', dataTrace5, barLayout5);  

});