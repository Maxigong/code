<template>
  <div v-if="post">
    <h2>{{ post.title }}</h2>
    <div class="tags" v-for="tag in post.tag" :key="tag">
      <span>{{ tag }}</span>
    </div>
    <div v-html="post.body"></div>
    <p>{{ post.date }}</p>
    <!-- comments -->
    <div v-if="post.comments">
      <div v-for="comment in post.comments" :key="comment.id">
        <h2>{{ comment.name }}</h2>
        <p>{{ comment.messege }}</p>
      </div>
    </div>
    <!--  end of comments -->
    <!-- form -->
    <form>
      <label for="name">Title</label>
      <input type="text" id="title" v-model="title" />
      <label for="name">Name</label>
      <input type="text" id="name" v-model="name" />
      <label for="messege">Messege</label>
      <input type="text" id="messege" v-model="messege" />
      <button type="submit" @click.prevent="sendComment" class="btn">
        submit
      </button>
    </form>
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
      post: [],
      slug: this.$route.params.slug,
      name: '',
      messege: '',
      title: '',
    };
  },
  methods: {
    async getPost() {
      try {
        let response = await axios.get(
          `http://127.0.0.1:8000/api/v1/post/${this.slug}/`
        );
        this.post = await response.data;
      } catch (error) {
        console.log(error);
      }
    },
    async sendComment() {
      let data = {
        name: this.name,
        title: this.title,
        messege: this.messege,
        post: this.post.id,
      };
      try {
        let response = await axios.post(
          `http://127.0.0.1:8000/api/v1/comments/`,
          data
        );
        this.post = await response.data;
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style></style>
