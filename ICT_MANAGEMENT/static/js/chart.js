function gera_cor(qtd=1){
  var bg_color = []
  var border_color = []
  for(let i = 0; i < qtd; i++){
      let r = Math.random() * 255;
      let g = Math.random() * 255;
      let b = Math.random() * 255;
      bg_color.push('rgba(${r}, ${g}, ${b}, ${0.2})')
      border_color.push('rgba(${r}, ${g}, ${b}, ${1})')
  }
  return [bg_color, border_color]
}


var options = {
scales: {
xAxes: [{
    ticks:{
        stepSize : 40,

    },
    stacked: true,
  gridLines: {
          display: false,
          lineWidth: 1
      }
}],
yAxes: [{

    stacked: true,
    gridLines: {
      display: true,
      lineWidth: 5
  }
    

}]
},

responsive: true,
cutoutPercentage: 40,
tooltips: {
callbacks: {
label: function(tooltipItem, data) {
 return data['labels'][tooltipItem['index']] + ': ' + data['datasets'][0]['data'][tooltipItem['index']];
}
}
}
};

function n50schart(url){
  fetch(url,{
    method: 'get',
  }).then(function(result){
    return result.json()
  }).then(function(data){
  
  const ctx = document.getElementById('n50schart').getContext('2d');
  const myChart = new Chart (ctx, {
    type: 'bar', 
    data: {
      labels: data.labels,
      datasets: [{
        label:'Montados',
        data: data.data,
        backgroundColor:  ['#f5dc8c', '#8ed3ac', '#1EAEDB', '#1EAEDB', '#1EAEDB'],
        bordercolor: '#1bc07f',


      }]
    },
    options: options
  });
})
}

function m75chart(url){
  fetch(url,{
    method: 'get',
  }).then(function(result){
    return result.json()
  }).then(function(data){
  
  const ctx = document.getElementById('m75chart').getContext('2d');
  const myChart = new Chart (ctx, {
    type: 'bar', 
    data: {
      labels: data.labels,
      datasets: [{
        label:'Montados',
        data: data.data,
        backgroundColor:  ['#f5dc8c', '#8ed3ac', '#1EAEDB', '#1EAEDB', '#1EAEDB'],
        bordercolor: '#1bc07f',


      }]
    },
    options: options
  });
})
}

function ideapad3ichart(url){
  fetch(url,{
    method: 'get',
  }).then(function(result){
    return result.json()
  }).then(function(data){
  
  const ctx = document.getElementById('ideapad3ichart').getContext('2d');
  const myChart = new Chart (ctx, {
    type: 'bar', 
    data: {
      labels: data.labels,
      datasets: [{
        label:'Montados',
        data: data.data,
        backgroundColor:  ['#f5dc8c', '#8ed3ac', '#1EAEDB', '#1EAEDB', '#1EAEDB'],
        bordercolor: '#1bc07f',


      }]
    },
    options: options
  });
})
}

function ideapad3achart(url){
  fetch(url,{
    method: 'get',
  }).then(function(result){
    return result.json()
  }).then(function(data){
  
  const ctx = document.getElementById('ideapad3achart').getContext('2d');
  const myChart = new Chart (ctx, {
    type: 'bar', 
    data: {
      labels: data.labels,
      datasets: [{
        label:'Montados',
        data: data.data,
        backgroundColor:  ['#f5dc8c', '#8ed3ac', '#1EAEDB', '#1EAEDB', '#1EAEDB'],
        bordercolor: '#1bc07f',


      }]
    },
    options: options
  });
})
}

function e14chart(url){
  fetch(url,{
    method: 'get',
  }).then(function(result){
    return result.json()
  }).then(function(data){
  
  const ctx = document.getElementById('e14chart').getContext('2d');
  const myChart = new Chart (ctx, {
    type: 'bar', 
    data: {
      labels: data.labels,
      datasets: [{
        label:'Montados',
        data: data.data,
        backgroundColor:  ['#f5dc8c', '#8ed3ac', '#1EAEDB', '#1EAEDB', '#1EAEDB'],
        bordercolor: '#1bc07f',


      }]
    },
    options: options
  });
})
}

function ideapad1chart(url){
  fetch(url,{
    method: 'get',
  }).then(function(result){
    return result.json()
  }).then(function(data){
  
  const ctx = document.getElementById('ideapad1chart').getContext('2d');
  const myChart = new Chart (ctx, {
    type: 'bar', 
    data: {
      labels: data.labels,
      datasets: [{
        label:'Montados',
        data: data.data,
        backgroundColor:  ['#f5dc8c', '#8ed3ac', '#1EAEDB', '#1EAEDB', '#1EAEDB'],
        bordercolor: '#1bc07f',


      }]
    },
    options: options
  });
})
}

