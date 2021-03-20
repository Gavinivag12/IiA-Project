<template>
<div class="VolumeChartWrapper">
	<div class="box box-primary">
		<div class="box-header with-border">
			<h3 class="box-title">Difference in Volume Data</h3>
		</div>
		<div class="box-body">
			<div class="row">
				<div class="col-md-8".
					<bar-chart-2></bar-chart-2>
				</div>
				
			</div>
		</div>
	</div>
</div>
</template>
<script>
	import BarChart_2 from "./BarChart_2.js"
	export default {
	
		components : {
		'bar-chart-2' : BarChart_2
		}
	}
</script>