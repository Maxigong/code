<template>
  <div>
    <div v-for="post in posts" :key="post.id">
      <router-link :to="{ name: 'post', params: { slug: post.slug } }">
        <h2>{{ post.title }}</h2>
      </router-link>
      <div class="tags" v-for="tag in post.tag" :key="tag">
        <span>{{ tag }}</span>
      </div>
      <p>{{ post.date }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  created() {
    this.getPost();
  },
  data() {
    return {
      posts: [],
    };
  },
  methods: {
    async getPost() {
      try {
        let response = await axios.get(`http://127.0.0.1:8000/api/v1/post/`);
        this.posts = await response.data;
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style></style>
