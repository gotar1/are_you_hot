// base url
let url = "/api/v1.0/hot"

// /create d3 api querry and build pie charts...
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

  // build age pie chart
  let ageData = [{
    values: hotTest,
    labels: hotTest,
    text: age,
    type: 'pie'
  }];

  Plotly.newPlot('agepie', ageData);

  // build ratio pie chart
  let ratioData = [{
    values: hotTest,
    labels: hotTest,
    text: ratio,
    type: 'ratiopie'
  }];

  Plotly.newPlot('ratiopie', ratioData);

  // build sex pie chart
  let sexData = [{
    values: hotTest,
    labels: hotTest,
    text: sex,
    type: 'pie'
  }];
  
  Plotly.newPlot('sexpie', sexData);

  // build hair color pie chart
  let hairData = [{
    values: hotTest,
    labels: hotTest,
    text: distinctiveFeatures,
    type: 'pie'
  }];

  Plotly.newPlot('distpie', hairData);

  // build eye color pie chart
  let eyeData = [{
    values: hotTest,
    labels: hotTest,
    text: eyeColor,
    type: 'pie'
  }];

  Plotly.newPlot('distpie', eyeData);
  
});
  
  
  
  

  