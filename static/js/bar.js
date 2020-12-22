// base url
let url = "/api/v1.0/hot"

// /create d3 api querry and build bar charts...
d3.json(url).then((data) =>{
  let dataCopy = data;
  console.log(dataCopy);

  let sex = [];
    dataCopy.forEach(item => sex.push(item.sex));
    let sexTable = sex.reduce(function(obj, val) {
        obj[val] = ++obj[val] || 1;
        return obj;
      }, {});
    console.log(sexTable)
    let eyeColor = [];
    dataCopy.forEach(item => eyeColor.push(item.eye_color));
    let eyeTable = eyeColor.reduce(function(obj, val) {
        obj[val] = ++obj[val] || 1;
        return obj;
      }, {});
    console.log(eyeTable);
    let distinctiveFeatures= [];
    dataCopy.forEach(item => distinctiveFeatures.push(item.distinctive_features));
    let distinctiveTable = distinctiveFeatures.reduce(function(obj, val) {
        obj[val] = ++obj[val] || 1;
        return obj;
      }, {});
    console.log(distinctiveTable);
    let ratio = [];
    dataCopy.forEach(item => ratio.push(item['ratio(wt/ht)']));
    let ratioTable = ratio.reduce(function(obj, val) {
        obj[val] = ++obj[val] || 1;
        return obj;
      }, {});
    console.log(ratioTable);
    let age = [];
    dataCopy.forEach(item => age.push(item.age));
    let ageTable = age.reduce(function(obj, val) {
        obj[val] = ++obj[val] || 1;
        return obj;
      }, {});
    console.log(ageTable);
    let hotTest = [];
    dataCopy.forEach(item => hotTest.push(item.hot_test));
    let hotTable = hotTest.reduce(function(obj, val) {
    obj[val] = ++obj[val] || 1;
    return obj;
    }, {});
    console.log(hotTable)
    // build bar chart for Eye Color..
    let trace1 = {
        x: Object.keys(eyeTable),
        y: Object.values(eyeTable),
        type: 'bar',
        // text: [sex, hotTest]
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
        x: Object.keys(sexTable),
        y: Object.values(sexTable),
        type: 'bar',
        // name: "Not Hot",
        // text: hotTest
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
        x: Object.keys(distinctiveTable),
        y: Object.values(distinctiveTable),
        type: 'bar',
        // text: sex.reverse()
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
        x: Object.keys(ratioTable),
        y: Object.values(ratioTable),
        type: 'bar',
        // text: sex.reverse()
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
        x: Object.keys(ageTable),
        y: Object.values(ageTable),
        type: 'bar',
        // text: sex.reverse()
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