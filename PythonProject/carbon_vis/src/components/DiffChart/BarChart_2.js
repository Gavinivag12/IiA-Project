import {Bar} from 'vue-chartjs'
	
export default ({
	extends: Bar,
	data() {
		
	},
	
	mounted() {
			this.renderChart({'datasets': [{'label': 'comparison', 'data': [10.5, -14.183000000000028, -6.661338147750939e-16], 'backgroundColor': '#ffff66', 'type': 'bar'}, {'label': 'comparison', 'data': [10.500000000000014, -10.500000000000028, -6.661338147750939e-16], 'backgroundColor': '#66ff66', 'type': 'bar'}], 'labels': [3.5, 7, 10.5]},
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
