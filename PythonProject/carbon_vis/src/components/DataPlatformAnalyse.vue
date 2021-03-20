<template>
  <div>
    <div class="md-layout md-alignment-center-center">
        <div class="md-layout-item md-size-100">
		<h1>magic portal</h1>
                <button v-on:click="getStructuralData">fun switch</button>
             	<div>{{StructuralDataList}}</div>
        </div> 
    </div>        
  </div>
</template>
<script>

export default {
  name: "DataPlatformAnalyse",
  components: {

  },
  props: {},
  watch: {
    
  },
  computed: {
    
  },
 data() {
    return {
      StructuralDataList: []
    };
  },
   methods: {
    getStructuralData() {
      fetch("out_data.json")
        .then(response => response.json())
        .then(data => (this.StructuralDataList = data))
		.then;
    }
  },
  mounted() {
    
  }
};
</script>
<style scoped lang="scss" />
