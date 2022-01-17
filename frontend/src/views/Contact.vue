<template>
  <div class="contact">
    <form class="form">
      <label for="name">Name</label>
      <input type="text" id="name" v-model="name" />
      <label for="title"> Title</label>
      <input type="text" id="title" v-model="title" />

      <label for="text"> Text</label>
      <textarea type="text" id="text" v-model="text"></textarea>
      <button @click.prevent="sendComment" type="submit">submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      name: '',
      title: '',
      text: '',
    };
  },
  methods: {
    async sendComment() {
      const data = {
        name: this.name,
        title: this.title,
        text: this.text,
      };
      try {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/api/v1/FormView/',
          data: data,
        });
        this.name = '';
        this.title = '';
        this.text = '';
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style scoped>
.form {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  border: 2px solid red;
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  padding: 2rem;
}
label,
input {
  margin: 10px 0;
}
input {
  width: 100%;
  height: 20px;
}
textarea {
  width: 100%;
  height: 200px;
}
</style>
