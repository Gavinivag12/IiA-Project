import {Bar} from 'vue-chartjs'
	
export default ({
	extends: Bar,
	data() {
		
	},
	
	mounted() {
			this.renderChart({'datasets': [{'label': 'RHX1FSNpM.json', 'backgroundColor': '#ff6666', 'data': [58.90700000000001, 74.20800000000001, 1.5311852192367725], 'type': 'bar'}, {'label': 'QSGAnXVdI.json', 'backgroundColor': '#ffff66', 'data': [69.40700000000001, 60.024999999999984, 1.5311852192367719], 'type': 'bar'}, {'label': 'taNRrjz3u.json', 'backgroundColor': '#66ff66', 'data': [69.40700000000002, 63.707999999999984, 1.5311852192367719], 'type': 'bar'}], 'labels': [3.5, 7, 10.5]},
			{responsive: true, maintainAspectRatio: true, 
			scales: {
        xAxes: [ {
          display: true,
          scaleLabel: {
            display: true,
            labelString: 'Elevation (m)'
          },
          ticks: {
            major: {
              fontStyle: 'bold',
              fontColor: '#FF0000'
            }
          }
        } ],
        yAxes: [ {
          display: true,
          scaleLabel: {
            display: true,
            labelString: 'Volume (m3)'
          },
		  ticks: {
            major: {
              fontStyle: 'bold',
              fontColor: '#FF0000'
            }
          }
        } ]
      }
			}
			) 
	}
})
