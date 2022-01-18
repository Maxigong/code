<template>
  <div class="main-container">
    <!-- svg path -->
    <div class="svg-container">
      <h2 class="zodiac-name">{{ svgClass }}</h2>
      <slot> </slot>
    </div>

    <div
      v-show="isModalActive"
      class="modal-container"
      @click.self="closeModal"
    >
      <div class="modal">
        <div class="card">
          <h2>{{ title }}</h2>
          <h2>{{ artist }}</h2>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { MotionPathPlugin } from 'gsap/MotionPathPlugin.js';

gsap.registerPlugin(ScrollTrigger, MotionPathPlugin);
export default {
  props: {
    svgClass: String,
  },
  mounted() {
    this.animations();
  },
  data() {
    return {
      isModalActive: false,
      title: '',
      artist: '',
    };
  },
  methods: {
    closeModal() {
      this.isModalActive = !this.isModalActive;
    },
    animations() {
      const svgContainer = document.querySelector(`.${this.svgClass}`);
      const svg = svgContainer.firstElementChild;

      let pointOne = svg.querySelector(`#pointOne${this.svgClass}`);
      let pointTwo = svg.querySelector(`#pointTwo${this.svgClass}`);
      let pointThree = svg.querySelector(`#pointThree${this.svgClass}`);
      let pointFour = svg.querySelector(`#pointFour${this.svgClass}`);
      let pointFive = svg.querySelector(`#pointFive${this.svgClass}`);
      let pointSix = svg.querySelector(`#pointSix${this.svgClass}`);

      let animation = gsap
        .to(`#star${this.svgClass}`, {
          duration: 16,
          ease: 'none',

          motionPath: {
            path: `#path${this.svgClass}`,
            align: `#star${this.svgClass}`,
          },
        })
        .pause();

      const showModal = () => {
        setTimeout(() => {
          this.isModalActive = !this.isModalActive;
        }, 500);
      };
      let duration = 2;
      // points
      pointOne.addEventListener('click', () => {
        this.title = 'Image One';
        this.artist = 'Artist one';
        animation.pause();
        gsap.to(animation, {
          progress: 0.08,
          duration: duration,
          onComplete: showModal,
        });
      });
      pointTwo.addEventListener('click', () => {
        this.title = 'Image Two';
        this.artist = 'Artist Two';
        animation.pause();
        gsap.to(animation, {
          progress: 0.15,
          duration: duration,
          onComplete: showModal,
        });
      });

      pointThree.addEventListener('click', () => {
        this.title = 'Image Three';
        this.artist = 'Artist Three';
        animation.pause();
        gsap.to(animation, {
          progress: 0.57,
          duration: duration,
          onComplete: showModal,
        });
      });

      pointFour.addEventListener('click', () => {
        this.title = 'Image Four';
        this.artist = 'Artist Four';
        animation.pause();
        gsap.to(animation, {
          progress: 0.7,
          duration: duration,
          onComplete: showModal,
        });
      });

      pointFive.addEventListener('click', () => {
        this.title = 'Image Quinto';
        this.artist = 'Artist Quinto';

        animation.pause();
        gsap.to(animation, {
          progress: 0.85,
          duration: duration,
          onComplete: showModal,
        });
      });
      pointSix.addEventListener('click', () => {
        this.title = 'Image sixth';
        this.artist = 'Artist sixth';
        animation.pause();
        gsap.to(animation, {
          progress: 0.94,
          duration: duration,
          onComplete: showModal,
        });
      });
    },
  },
};
</script>

<style scoped>
.zodiac-name {
  color: white;
  z-index: 100;
}
.svg-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 10;
  perspective: 600px;
}

#nav {
  width: 100%;
  display: flex;
  align-content: center;
  justify-content: center;
  position: fixed;
  bottom: 0;
  height: 50px;
  background: #333;
  z-index: 10;
}

#nav div {
  align-self: center;
  font-size: 22px;
}

#progressSlider {
  width: 600px;
  margin-left: 16px;
  margin-right: 16px;
}

button {
  border-radius: 10px;
  background: #ffc34c;
  color: #444;
  font-size: 14px;
  margin: 10px;
  font-weight: 700;
  width: 5em;
}

#time {
  width: 80px;
}

svg {
  /* height: 900px; */
  width: 700px;
  width: 120% !important;
  height: 120% !important;
  display: none;
}

* {
  margin: 0;
  padding: 0;
}
/* Modal */
.modal-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.8);
  z-index: 10;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 2s linear;
}
.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background: steelblue;
  gap: 2rem;
  max-width: 600px;
  width: 100%;
  height: 600px;
  border-radius: 20px;
}
</style>
