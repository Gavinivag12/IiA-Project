<template>
  <div class="md-layout md-alignment-center-center" style="margin-top:60px;">
    <md-card
      class="md-elevation-0 md-layout-item md-size-90 md-medium-size-75 md-small-size-100"
    >
      <md-card-content>
        <h1 class="md-display-2">Hello {{ $store.state.user.name }}!</h1>
        <p>
          To get started, click the button below
        </p>
        <md-button
          class="md-raised md-primary-xxx xxx-md-dense text-center btn-no-margin"
          style="width: 100%; backgroundColor: grey; color: white"
          to="/dataplatform/calc"
          >Data Platform</md-button
        >
      </md-card-content>
    </md-card>
  </div>
</template>
<script>
// @ is an alias to /src
import ReportCard from "@/components/ReportCard.vue";

export default {
  name: "HomeView",
  components: {
    ReportCard,
  },
  computed: {
    tags() {
      let set = new Set();
      this.allReports.forEach(({ tags }) => {
        set = new Set([...set, ...tags]);
      });
      return [...set];
    },
    allReports() {
      let reports = this.$store.state.streams
        .filter(
          stream =>
            stream.hasOwnProperty("isCarbonReport") &&
            stream.parent === null &&
            stream.deleted === false,
        )
        .sort((a, b) => {
          return new Date(b.updatedAt) - new Date(a.updatedAt);
        });
      return reports;
    },
    streams() {
      if (this.selectedTags.length === 0) return this.allReports;
      return this.allReports.filter(({ tags }) => {
        return tags.some(val => this.selectedTags.includes(val));
      });
    },
    displayStreams() {
      return this.streams.slice(
        this.currentIndex + this.pageNumber * this.sliceSize,
        this.sliceSize * (this.pageNumber + 1),
      );
    },
  },
  methods: {
    toggleTag(tag) {
      let index = this.selectedTags.indexOf(tag);
      if (index !== -1) this.selectedTags.splice(index, 1);
      else this.selectedTags.push(tag);
    },
  },
  data() {
    return {
      currentIndex: 0,
      sliceSize: 6,
      pageNumber: 0,
      selectedTags: [],
      showTags: true,
      hadNoStreams: false,
      sampleRetrieved: false,
    };
  },
  mounted() {
    this.showTags = window.innerWidth > 960;
  },
};
</script>
<style scoped lang="scss">
.tag-chip {
  height: 25px;
  line-height: 25px;
  margin-bottom: 5px;
}
</style>
