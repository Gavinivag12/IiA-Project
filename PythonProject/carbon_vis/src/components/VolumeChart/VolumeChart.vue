<template>
<div class="VolumeChartWrapper">
	<div class="box box-primary">
		<div class="box-header with-border">
			<h3 class="box-title">Volume Data</h3>
		</div>
		<div class="box-body">
			<div class="row">
				<div class="col-md-8".
					<bar-chart></bar-chart>
				</div>
				
			</div>
		</div>
	</div>
</div>
</template>
<script>
	import BarChart from "./BarChart.js"
	export default {
	
		components : {
		'bar-chart' : BarChart
		}
	}
</script>