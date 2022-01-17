<template>
  <div>
    <CaptureHtml />
    <div v-for="img in allImages" :key="img.id">
      <img :src="img.img" alt="" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import CaptureHtml from '../components/CaptureHtml';
export default {
  components: { CaptureHtml },
  mounted() {
    this.getData();
  },
  data() {
    return {
      allImages: [],
    };
  },
  methods: {
    async getData() {
      try {
        const response = await axios.get(
          'http://127.0.0.1:8000/api/v1/userDetails/'
        );
        this.allImages = await response.data;
        // this.detailList = this.room.details.split(' ');
        console.log(this.allImages);
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style scoped>
img {
  height: 200px;
  width: 200px;
  background: red;
}
</style>
