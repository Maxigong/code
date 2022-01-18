<template>
  <div>
    <StadelNav />
    <h2>Discover</h2>
    <div class="section-center">
      <!-- paint -->
      <div class="paint"></div>
      <!-- end paint -->
      <!-- form -->
      <form class="form">
        <input
          class="enter-world-input"
          type="text"
          placeholder="Enter world"
          v-model="word"
        />
      </form>
      <!-- end of form -->
      <!-- btn options -->
      <div class="options">
        <button @click="enterWorld" class="enter-wold btn">Check world</button>
        <button class="hint btn">Request hint</button>
      </div>
      <!-- end btn options -->
      <!-- worlds result -->
      <div v-if="words">
        <div class="world-container">
          <p class="word" v-for="word in words" :key="word">{{ word }}</p>
        </div>
        <div v-if="error">
          {{ error }}
        </div>
      </div>
      <!-- end of world result -->
    </div>
  </div>
</template>

<script>
import StadelNav from '../../components/stadelComponents/StadelNav';
export default {
  components: { StadelNav },
  data() {
    return {
      word: '',
      words: ['hello', 'max'],
      error: '',
    };
  },
  methods: {
    enterWorld() {
      if (!this.words.find((word) => word === this.word)) {
        this.words.push(this.word);
        this.error = '';
      } else {
        this.error = 'please enter a new word';
      }
    },
  },
};
</script>

<style>
.section-center {
  width: 100%;
  max-width: 900px;
  display: flex;
  justify-content: center;
  align-content: center;
  flex-direction: column;
  margin: 0 auto;
  gap: 1rem;
}
.paint {
  width: 100%;
  max-width: 300px;
  height: 300px;
  background: red;
  margin: 0 auto;
}

/* options */
.options {
  display: flex;
  justify-content: center;
  align-content: center;
  gap: 2rem;
}
.btn {
  align-items: center;
  background-color: #fee6e3;
  border: 2px solid #111;
  border-radius: 8px;
  box-sizing: border-box;
  color: #111;
  cursor: pointer;
  display: flex;
  font-family: Inter, sans-serif;
  font-size: 14px;
  height: 48px;
  justify-content: center;
  line-height: 24px;
  max-width: 100%;
  padding: 0 25px;
  position: relative;
  text-align: center;
  text-decoration: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

.btn:after {
  background-color: #111;
  border-radius: 8px;
  content: '';
  display: block;
  height: 48px;
  left: 0;
  width: 100%;
  position: absolute;
  top: -2px;
  transform: translate(8px, 8px);
  transition: transform 0.2s ease-out;
  z-index: -1;
}

/* .btn:hover {
   transform: translate(0, 0); 
} */

.btn:active:after {
  background-color: #ffdeda;
  outline: 0;
  transform: translate(0, 0);
}

.btn:hover {
  outline: 0;
}

@media (min-width: 768px) {
  .btn {
    padding: 0 40px;
  }
}
/* form */
.enter-world-input {
  width: 100%;
  max-width: 300px;
  padding: 1rem;
}

/* word results */
.world-container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2rem;
}
.word {
  background: red;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  color: white;
}
</style>
