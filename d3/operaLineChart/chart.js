async function drawLineChart() {
  // console.log('Hello, World!');
  // console.log('Access Data');

  // Accessor functions
  const dateParser = d3.timeParse('%Y%m%d');

  // 1. Access Data

  // read the operas as a text file
  const text = await d3.text('./../../opera.csv');

  // split data
  const operas = text.split('\r\n');

  // transform data into objects
  const data = operas.map((opera) => {
    const psv = d3.dsvFormat('|');
    const performance = psv.parse(opera);
    const components = performance.columns;
    return {
      season: components[0],
      country: components[1],
      city: components[3],
      composer: components[5],
      composerBirth: components[6],
      composerDeath: components[7],
      composerCountry: components[8],
      composerGender: components[9],
      opera: components[10],
      operaLanguage: components[11],
      performanceDate: components[13],
    };
  });

  console.log(data);

  // 2. Create chart dimensions
  let dimensions = {
    width: window.innerWidth * 0.9,
    height: 400,
    margin: {
      top: 15,
      right: 15,
      bottom: 40,
      left: 60,
    },
  };
}

drawLineChart();
