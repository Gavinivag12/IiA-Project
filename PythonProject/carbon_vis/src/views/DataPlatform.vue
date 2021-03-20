<template>
  <div>
    <md-steppers
      md-vertical
      style="-webkit-user-select: none; --moz-user-select: none; margin-bottom:100px"
      @md-changed="stepChanged"
      md-dynamic-height
    >
      <md-step
        id="data-input"
        md-label="Data"
        md-description="Add or remove streams that you want to perform structural analysis on"
      >
        <stream-search
          @selected-stream="addStream"
          :streams-to-omit="streamIds"
        ></stream-search>
        <br />
        <stream-card-renderer
          v-for="stream in streams"
          :stream="stream"
          :key="stream.streamId"
          @remove-stream="removeStream"
        ></stream-card-renderer>
        <md-divider></md-divider>
        <br />
		<DataPlatformAnalyse></DataPlatformAnalyse>
		<VolumeChart></VolumeChart>
		<DiffChart></DiffChart>
        <br />
      </md-step>
    </md-steppers>
  </div>
</template>
<script>
import StreamSearch from "@/components/StreamSearch.vue";
import StreamCardRenderer from "@/components/StreamCardRenderer.vue";
import DataPlatformAnalyse from "@/components/DataPlatformAnalyse.vue";
import VolumeChart from "@/components/VolumeChart/VolumeChart.vue";
import DiffChart from "@/components/DiffChart/DiffChart.vue";
export default {
  name: "DataPlatformCalculator",
  components: {
    StreamSearch,
    StreamCardRenderer,
    DataPlatformAnalyse,
	VolumeChart,
	DiffChart
  },
 
  props: [],
  watch: {
    
  },
  computed: {
    selectedObjects() {
      return this.$store.state.selectedObjects;
    },
    streams() {
      return this.streamIds.map(id =>
        this.$store.state.streams.find(s => s.streamId === id),
      );
    },
    streamIds() {
      return this.$store.state.loadedStreamIds;
    },
  },
  data() {
    return {
      toRequest: [],
      requestBuckets: [],
      isRequesting: false,
      pauseRequesting: false,
      bucketInProgress: false,
      removeInterval: null,
      streamsToRemove: [],
      analysisLegend: null,
      showLoading: false,
    };
  },
  methods: {
    addStream(streamId) {
      this.$emit("add-stream", streamId);
    },
    removeStream(streamId) {
      this.$emit("remove-stream", streamId);
    },
    stepChanged(step) {
    },
  },
  mounted() {
    this.objectAccumulator = [];
    if (window.renderer)
      window.renderer.unloadObjects({
        objIds: this.$store.state.objects.map(o => o._id),
      });
    this.$store.commit(
      "REMOVE_OBJECTS",
      this.$store.state.objects.map(o => o._id),
    );
  },
};
</script>
<style scoped lang="scss" />
