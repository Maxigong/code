<template>
  <div class="parallax-container">
    <!-- background -->
    <div class="background">
      <div class="shootingStarContainer">
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
      </div>
      <div class="shootingStarContainer">
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
      </div>
      <div class="shootingStarContainer">
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
        <div class="shootingStar"></div>
      </div>

      <div class="stars"></div>
      <div class="twinkleMask"></div>
      <div class="twinkleMask2"></div>
      <div class="clouds"></div>

      <div class="fogContainer">
        <div class="fog"></div>
      </div>
    </div>
    <div class="card-container-2">
      <div
        v-for="card in cards"
        :key="card.id"
        class="parallax-card"
        :class="card.name"
      >
        <!-- :style="{ background: card.color, marginLeft: index * 20 + 'px' }" -->
        <h2>{{ card.text }}</h2>
        <SGVComponent :svgClass="card.class"
          ><div :class="card.class" v-html="card.svg"></div>
        </SGVComponent>
      </div>
    </div>
  </div>
</template>

<script>
import SGVComponent from './SVGComponent';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);
export default {
  components: { SGVComponent },
  data() {
    return {
      cards: [
        {
          id: 2,
          class: 'aries',
          name: 'card2',
          color: '#203B3F',
          svg: `<svg width="100%" height="475" viewBox="0 0 831 475" fill="none" xmlns="http://www.w3.org/2000/svg">
<path id="pointOnearies" d="M139.998 151.687C198.192 141.212 252.275 120.468 311.701 120.468" stroke="black" stroke-width="3" stroke-linecap="round"/>
<path id="patharies" d="M716.033 448.187C692.453 441.113 672.15 428.154 651.365 415.234C626.337 399.676 600.07 385.53 575.672 369.025C566.077 362.535 554.065 354.531 542.099 354.531C533.768 354.531 526.229 356.761 517.446 356.761C482.87 356.761 447.005 363.291 412.764 367.91C382.327 372.017 352.155 371.595 321.585 372.494C280.929 373.69 240.469 374.6 199.807 374.6C189.429 374.6 176.468 372.477 166.358 374.724C161.853 375.725 155.986 378.818 151.864 379.06C146.7 379.364 139.779 377.597 135.14 380.175C126.893 384.756 115.706 386.635 106.77 390.21C85.8308 398.585 65.0903 407.109 43.8368 414.739C35.9787 417.56 12.4896 425.197 7.41488 432.578C6.59353 433.773 -1.28963 445.71 3.57446 445.71C6.88753 445.71 9.24147 438.184 10.8836 436.542C13.7576 433.668 18.1592 432.952 21.4138 430.348C23.8639 428.388 25.6557 422.124 27.4841 419.198C30.3664 414.587 37.6337 414.812 40.3681 411.394C43.2209 407.828 65.2327 409.387 70.3481 407.925C77.8766 405.774 87.681 399.851 95.001 395.784C104.032 390.767 114.395 390.562 123.866 387.856C132.279 385.452 129.565 376.233 129.565 368.654C129.565 326.273 129.435 284.928 137.246 243.035C142.759 213.463 138.484 184.885 138.484 154.953C138.484 154.666 155.55 129.108 161.279 120.39C176.577 97.1096 198.953 78.4109 216.531 56.8371C229.392 41.0536 246.23 28.2531 260.634 13.8493C276.433 -1.94923 267.954 25.0005 270.545 35.6529C274.051 50.0654 283.5 65.0713 289.004 79.1363C292.649 88.4516 298.545 99.8269 305.728 107.01C309.268 110.55 319.838 121.419 324.682 122.496C335.309 124.857 346.187 121.44 357.016 124.85C376.125 130.865 396.109 132.654 414.87 139.22C423.118 142.107 434.909 143.615 441.753 149.379C446.925 153.734 458.603 154.658 465.167 157.183C475.749 161.253 486.476 165.973 497.501 168.952C513.986 173.408 529.902 180.166 546.063 185.553C561.259 190.618 576.989 195.317 591.157 202.401C599.331 206.488 613.69 216.276 622.376 216.276C628.681 216.276 628.597 202.873 630.181 198.437C633.638 188.756 639.789 185.483 646.905 178.368C659.879 165.394 674.845 154.911 690.265 145.043C695.353 141.786 705.5 134.126 711.573 133.769C718.165 133.381 722.421 168.859 727.678 176.138C746.91 202.768 769.238 229.985 785.16 258.645C791.656 270.338 802.604 281.539 811.423 290.359C814.166 293.101 816.693 296.358 819.724 298.783C824.94 302.956 823.069 307.239 823.069 294.323" stroke="white" stroke-width="3" stroke-linecap="round"/>
<ellipse id="pointTwoaries" cx="550" cy="354.5" rx="10" ry="8.5" fill="#D11C1C"/>
<ellipse id="pointThreearies" cx="140" cy="383.5" rx="10" ry="8.5" fill="#D11C1C"/>
<ellipse id="pointFouraries" cx="140" cy="151.5" rx="10" ry="8.5" fill="#D11C1C"/>
<ellipse id="pointFivearies" cx="268" cy="8.5" rx="10" ry="8.5" fill="#D11C1C"/>
<ellipse id="pointSixaries" cx="626" cy="213.5" rx="10" ry="8.5" fill="#D11C1C"/>
<ellipse cx="821" cy="301.5" rx="10" ry="8.5" fill="#D11C1C"/>
<path  d="M723.5 414L731.919 437.148H759.165L737.123 451.454L745.542 474.602L723.5 460.296L701.458 474.602L709.877 451.454L687.835 437.148H715.081L723.5 414Z" fill="#DAC719" id="stararies"/>
<path d="M626.119 214.124C672.622 214.124 711.109 232.048 754.339 246.458C768.062 251.032 782.763 258.033 792.867 268.138C794.63 269.901 797.537 276.508 797.823 278.792C798.249 282.2 802.886 283.874 804.513 286.721C807.296 291.591 812.419 293.692 815.662 297.746C820.92 304.319 821.193 302.972 820.122 294.401" stroke="black" stroke-width="3" stroke-linecap="round"/>
<path d="M626.119 214.124C672.622 214.124 711.109 232.048 754.339 246.458C768.062 251.032 782.763 258.033 792.867 268.138C794.63 269.901 797.537 276.508 797.823 278.792C798.249 282.2 802.886 283.874 804.513 286.721C807.296 291.591 812.419 293.692 815.662 297.746C820.92 304.319 821.193 302.972 820.122 294.401" stroke="white" stroke-width="3" stroke-linecap="round"/>
</svg>
`,
        },
        {
          id: 1,
          class: 'piscis',
          name: 'card3',
          color: '#203B3F',
          svg: `<svg
        width="100%" 
        height="475"
        viewBox="0 0 485 385"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
    
      >
        <path
          id="pathpiscis"
          d="M376.085 347.314C407.882 339.463 438.558 323.325 468.664 310.422C473.041 308.547 477.608 307.274 473.663 303.724C463.433 294.516 453.956 285.041 444.07 274.93C437.867 268.586 423.411 242.482 415.676 242.937C405.561 243.532 395.208 242.937 385.083 242.937C371.886 242.937 358.688 242.937 345.491 242.937C337.428 242.937 334.676 250.168 330.695 257.334C325.97 265.838 314.574 273.854 307.7 280.729C304.617 283.812 299.641 286.128 306.8 286.128C311.881 286.128 314.785 285.796 318.497 289.727C336.278 308.553 348.701 332.527 367.087 350.913C368.839 352.666 371.994 358.895 375.085 358.012C379.938 356.625 373.667 351.139 372.885 350.514C365.888 344.916 359.209 339.437 352.69 332.917C341.985 322.213 327.245 310.153 319.897 296.925C318.444 294.309 305.979 281.189 307.7 280.329C313.66 277.349 318.068 271.063 321.197 265.432C323.141 261.932 327.105 245.748 330.295 244.837C331.155 244.591 337.507 248.753 336.093 246.936C330.659 239.949 322.109 238.24 313.998 234.839C286.906 223.478 265.3 201.055 239.414 187.249C235.729 185.284 227.283 178.151 223.118 178.151C216.971 178.151 208.597 181.568 202.323 182.65C151.961 191.333 98.4347 188.962 49.456 199.846C46.7038 200.458 41.6059 204.345 46.7566 204.345C48.3805 204.345 48.5562 191.754 48.5562 190.748C48.5562 159.302 56.8449 125.561 62.1532 94.4695C64.4218 81.1821 69.852 67.0536 70.1515 53.5785C70.3888 42.9005 70.3597 33.0484 72.8509 22.5852C75.1032 13.1256 77.5936 23.2649 75.5503 23.3851C70.4923 23.6826 65.7423 23.151 60.7535 24.2849C48.6336 27.0394 33.7188 25.586 21.5621 23.785C19.9684 23.5489 6.10224 24.6134 5.46562 22.3853C2.9281 13.5039 13.1626 8.9882 20.6623 8.9882C35.8002 8.9882 50.0282 7.18859 65.6525 7.18859C69.1193 7.18859 88.9376 2.59935 83.5486 7.98842C80.003 11.5339 73.7507 18.0942 73.7507 23.3851"
          stroke="white"
          stroke-width="3"
          stroke-linecap="round"
        />
        <ellipse
          class="circle"
          id="pointFivepiscis"
          cx="72"
          cy="25.5"
          rx="10"
          ry="8.5"
          fill="#D11C1C"
        />
        <ellipse
          class="circle"
          id="pointSixpiscis"
          cx="10"
          cy="8.5"
          rx="10"
          ry="8.5"
          fill="#D11C1C"
        />
        <ellipse
          class="circle"
          id="pointThreepiscis"
          cx="222"
          cy="181.5"
          rx="10"
          ry="8.5"
          fill="#D11C1C"
        />
        <ellipse
          class="circle"
          id="pointTwopiscis"
          cx="414"
          cy="244.5"
          rx="10"
          ry="8.5"
          fill="#D11C1C"
        />
        <ellipse
          class="circle"
          id="pointOnepiscis"
          cx="475"
          cy="304.5"
          rx="10"
          ry="8.5"
          fill="#D11C1C"
        />
        <ellipse
          class="circle"
          id="pointpiscis"
          cx="47"
          cy="202.5"
          rx="10"
          ry="8.5"
          fill="#D11C1C"
        />
        <ellipse
          class="circle"
          id="pointFourpiscis"
          cx="47"
          cy="202.5"
          rx="10"
          ry="8.5"
          fill="#D11C1C"
        />
        <path
          d="M376.5 324L384.919 347.148H412.165L390.123 361.454L398.542 384.602L376.5 370.296L354.458 384.602L362.877 361.454L340.835 347.148H368.081L376.5 324Z"
          fill="#DAC719"
          id="starpiscis"
        />
      </svg>`,
        },
      ],
    };
  },
  mounted() {
    this.animations();
  },
  methods: {
    animations() {
      const slides = document.querySelectorAll('.parallax-card');
      slides.forEach(function (slide, index) {
        slide.style.left = `${index * 100}%`;
      });

      const singleCard = [];
      this.cards.map((card) => {
        if (card.name) {
          singleCard.push(card.name);
        }
      });

      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: '.parallax-container',
          start: 'top top',
          toggleActions: 'play none reverse pause',
          scrub: true,
          pinSpacing: true,
          pin: '.parallax-container',
          end: () =>
            '+=' + document.querySelector('.parallax-card').offsetWidth * 2,
        },
      });

      // const reverseCardsArray = singleCard.reverse();
      for (let i = 0; i < singleCard.length; i++) {
        tl.to(`.${singleCard[i]}`, {
          xPercent: -100,
          opacity: 1,
        });
      }
    },
  },
};
</script>

<style scoped>
.parallax-container {
  height: 100vh;
  width: 100%;
  margin: 0 auto;
  background-color: cornsilk;
  font-weight: 700;
  overflow: hidden;
  position: relative;
}
.card-container-2 {
  height: 100%;
  /* position: relative; */
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
}

.card-container-2 {
  display: flex;
  flex-wrap: wrap;
}
.card-container-2 h2 {
  font-size: 32px;
  color: #ffffff;
  margin-bottom: 66px;
  width: 719px;
  margin-right: auto;
  margin-left: auto;
  display: inline-block;
}
.card-content {
  height: 100%;
  width: 100%;
}

/* test */
.parallax-card {
  transform: translateZ(300px);
}

.parallax-card {
  width: 100%;
  height: 100%;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
  margin: 0 auto;
  padding: 3rem;
  display: grid;
  justify-content: center;
  align-items: end;
  line-height: 4rem;
  position: absolute;
  top: 0;
  z-index: 100;
  /* top: 50%;
  left: 50%;
  transform: translate(-50%, -50%); */
}
/* Stars */

.background {
  /* position: relative; */
  /* height: 700px; */
  overflow: hidden;
}

.shootingStarContainer:nth-child(1) {
  position: absolute;
  width: 100%;
  height: 130%;
  transform: rotate(41deg);
  z-index: 10;
}
.shootingStarContainer:nth-child(2) {
  position: absolute;
  width: 100%;
  height: 130%;
  transform: rotate(42deg);
  z-index: 10;
}
.shootingStarContainer:nth-child(3) {
  position: absolute;
  width: 100%;
  height: 130%;
  transform: rotate(39deg);
  z-index: 10;
}

.shootingStar {
  position: absolute;
  height: 1px;
  background: linear-gradient(-70deg, #ffebeb, black);
}
.shootingStarContainer:nth-child(1) .shootingStar:nth-child(1) {
  left: calc(25%);
  top: calc(95%);
  -webkit-animation: shootingFrames 2635ms ease-in-out 2789ms;
  animation: shootingFrames 2635ms ease-in-out 2789ms;
  opacity: 0.25;
}
.shootingStarContainer:nth-child(1) .shootingStar:nth-child(2) {
  left: calc(24%);
  top: calc(96%);
  -webkit-animation: shootingFrames 769ms ease-in-out 42875ms;
  animation: shootingFrames 769ms ease-in-out 42875ms;
  opacity: 0.26;
}
.shootingStarContainer:nth-child(1) .shootingStar:nth-child(3) {
  left: calc(50%);
  top: calc(36%);
  -webkit-animation: shootingFrames 2719ms ease-in-out 16457ms;
  animation: shootingFrames 2719ms ease-in-out 16457ms;
  opacity: 0.59;
}
.shootingStarContainer:nth-child(1) .shootingStar:nth-child(4) {
  left: calc(1%);
  top: calc(58%);
  -webkit-animation: shootingFrames 1008ms ease-in-out 8755ms;
  animation: shootingFrames 1008ms ease-in-out 8755ms;
  opacity: 0.73;
}
.shootingStarContainer:nth-child(1) .shootingStar:nth-child(5) {
  left: calc(4%);
  top: calc(68%);
  -webkit-animation: shootingFrames 1153ms ease-in-out 49278ms;
  animation: shootingFrames 1153ms ease-in-out 49278ms;
  opacity: 0.43;
}
.shootingStarContainer:nth-child(1) .shootingStar:nth-child(6) {
  left: calc(42%);
  top: calc(76%);
  -webkit-animation: shootingFrames 1600ms ease-in-out 27003ms;
  animation: shootingFrames 1600ms ease-in-out 27003ms;
  opacity: 0.77;
}
.shootingStarContainer:nth-child(1) .shootingStar:nth-child(7) {
  left: calc(15%);
  top: calc(60%);
  -webkit-animation: shootingFrames 2697ms ease-in-out 8359ms;
  animation: shootingFrames 2697ms ease-in-out 8359ms;
  opacity: 0.8;
}
.shootingStarContainer:nth-child(1) .shootingStar:nth-child(8) {
  left: calc(44%);
  top: calc(87%);
  -webkit-animation: shootingFrames 2534ms ease-in-out 27837ms;
  animation: shootingFrames 2534ms ease-in-out 27837ms;
  opacity: 0.18;
}
.shootingStarContainer:nth-child(1) .shootingStar:nth-child(9) {
  left: calc(46%);
  top: calc(3%);
  -webkit-animation: shootingFrames 1184ms ease-in-out 28841ms;
  animation: shootingFrames 1184ms ease-in-out 28841ms;
  opacity: 0.32;
}
.shootingStarContainer:nth-child(1) .shootingStar:nth-child(10) {
  left: calc(48%);
  top: calc(14%);
  -webkit-animation: shootingFrames 1793ms ease-in-out 21597ms;
  animation: shootingFrames 1793ms ease-in-out 21597ms;
  opacity: 0.46;
}
.shootingStarContainer:nth-child(2) .shootingStar:nth-child(1) {
  left: calc(23%);
  top: calc(50%);
  -webkit-animation: shootingFrames 2235ms ease-in-out 6979ms;
  animation: shootingFrames 2235ms ease-in-out 6979ms;
  opacity: 0.19;
}
.shootingStarContainer:nth-child(2) .shootingStar:nth-child(2) {
  left: calc(1%);
  top: calc(79%);
  -webkit-animation: shootingFrames 2251ms ease-in-out 26527ms;
  animation: shootingFrames 2251ms ease-in-out 26527ms;
  opacity: 0.63;
}
.shootingStarContainer:nth-child(2) .shootingStar:nth-child(3) {
  left: calc(39%);
  top: calc(90%);
  -webkit-animation: shootingFrames 1085ms ease-in-out 7954ms;
  animation: shootingFrames 1085ms ease-in-out 7954ms;
  opacity: 0.84;
}
.shootingStarContainer:nth-child(2) .shootingStar:nth-child(4) {
  left: calc(45%);
  top: calc(35%);
  -webkit-animation: shootingFrames 1638ms ease-in-out 57071ms;
  animation: shootingFrames 1638ms ease-in-out 57071ms;
  opacity: 0.63;
}
.shootingStarContainer:nth-child(2) .shootingStar:nth-child(5) {
  left: calc(31%);
  top: calc(44%);
  -webkit-animation: shootingFrames 2514ms ease-in-out 57386ms;
  animation: shootingFrames 2514ms ease-in-out 57386ms;
  opacity: 0.87;
}
.shootingStarContainer:nth-child(2) .shootingStar:nth-child(6) {
  left: calc(31%);
  top: calc(32%);
  -webkit-animation: shootingFrames 2547ms ease-in-out 50522ms;
  animation: shootingFrames 2547ms ease-in-out 50522ms;
  opacity: 0.46;
}
.shootingStarContainer:nth-child(2) .shootingStar:nth-child(7) {
  left: calc(18%);
  top: calc(33%);
  -webkit-animation: shootingFrames 838ms ease-in-out 49079ms;
  animation: shootingFrames 838ms ease-in-out 49079ms;
  opacity: 0.34;
}
.shootingStarContainer:nth-child(2) .shootingStar:nth-child(8) {
  left: calc(15%);
  top: calc(55%);
  -webkit-animation: shootingFrames 2165ms ease-in-out 4182ms;
  animation: shootingFrames 2165ms ease-in-out 4182ms;
  opacity: 0.45;
}
.shootingStarContainer:nth-child(2) .shootingStar:nth-child(9) {
  left: calc(39%);
  top: calc(16%);
  -webkit-animation: shootingFrames 2727ms ease-in-out 41845ms;
  animation: shootingFrames 2727ms ease-in-out 41845ms;
  opacity: 0.16;
}
.shootingStarContainer:nth-child(2) .shootingStar:nth-child(10) {
  left: calc(50%);
  top: calc(8%);
  -webkit-animation: shootingFrames 2575ms ease-in-out 12965ms;
  animation: shootingFrames 2575ms ease-in-out 12965ms;
  opacity: 0.74;
}
.shootingStarContainer:nth-child(3) .shootingStar:nth-child(1) {
  left: calc(27%);
  top: calc(75%);
  -webkit-animation: shootingFrames 1643ms ease-in-out 52790ms;
  animation: shootingFrames 1643ms ease-in-out 52790ms;
  opacity: 0.58;
}
.shootingStarContainer:nth-child(3) .shootingStar:nth-child(2) {
  left: calc(4%);
  top: calc(35%);
  -webkit-animation: shootingFrames 1671ms ease-in-out 40906ms;
  animation: shootingFrames 1671ms ease-in-out 40906ms;
  opacity: 0.82;
}
.shootingStarContainer:nth-child(3) .shootingStar:nth-child(3) {
  left: calc(19%);
  top: calc(13%);
  -webkit-animation: shootingFrames 2371ms ease-in-out 52140ms;
  animation: shootingFrames 2371ms ease-in-out 52140ms;
  opacity: 0.39;
}
.shootingStarContainer:nth-child(3) .shootingStar:nth-child(4) {
  left: calc(26%);
  top: calc(37%);
  -webkit-animation: shootingFrames 2422ms ease-in-out 28529ms;
  animation: shootingFrames 2422ms ease-in-out 28529ms;
  opacity: 0.29;
}
.shootingStarContainer:nth-child(3) .shootingStar:nth-child(5) {
  left: calc(28%);
  top: calc(23%);
  -webkit-animation: shootingFrames 872ms ease-in-out 46603ms;
  animation: shootingFrames 872ms ease-in-out 46603ms;
  opacity: 0.19;
}
.shootingStarContainer:nth-child(3) .shootingStar:nth-child(6) {
  left: calc(34%);
  top: calc(37%);
  -webkit-animation: shootingFrames 2111ms ease-in-out 25153ms;
  animation: shootingFrames 2111ms ease-in-out 25153ms;
  opacity: 0.78;
}
.shootingStarContainer:nth-child(3) .shootingStar:nth-child(7) {
  left: calc(4%);
  top: calc(10%);
  -webkit-animation: shootingFrames 2660ms ease-in-out 48705ms;
  animation: shootingFrames 2660ms ease-in-out 48705ms;
  opacity: 0.61;
}
.shootingStarContainer:nth-child(3) .shootingStar:nth-child(8) {
  left: calc(33%);
  top: calc(6%);
  -webkit-animation: shootingFrames 1718ms ease-in-out 1602ms;
  animation: shootingFrames 1718ms ease-in-out 1602ms;
  opacity: 0.44;
}
.shootingStarContainer:nth-child(3) .shootingStar:nth-child(9) {
  left: calc(47%);
  top: calc(92%);
  -webkit-animation: shootingFrames 930ms ease-in-out 29001ms;
  animation: shootingFrames 930ms ease-in-out 29001ms;
  opacity: 0.45;
}
.shootingStarContainer:nth-child(3) .shootingStar:nth-child(10) {
  left: calc(49%);
  top: calc(82%);
  -webkit-animation: shootingFrames 1454ms ease-in-out 56657ms;
  animation: shootingFrames 1454ms ease-in-out 56657ms;
  opacity: 0.42;
}

@-webkit-keyframes shootingFrames {
  0% {
    transform: translateX(0);
    width: 0;
  }
  30% {
    width: 200px;
  }
  100% {
    width: 0;
    transform: translateX(806px);
  }
}

@keyframes shootingFrames {
  0% {
    transform: translateX(0);
    width: 0;
  }
  30% {
    width: 200px;
  }
  100% {
    width: 0;
    transform: translateX(806px);
  }
}
.stars,
.twinkleMask,
.twinkleMask2,
.clouds {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  display: block;
}

.stars {
  background: #000 url('https://wolf.drjm.co.uk/nightsky/stars.jpg') repeat top
    center;
  z-index: 0;
}

.twinkleMask {
  background: transparent
    url('https://wolf.drjm.co.uk/nightsky/twinklemask.png') repeat top center;
  z-index: 1;
  -webkit-animation: twinkleFrames 700s linear infinite;
  animation: twinkleFrames 700s linear infinite;
}

.twinkleMask2 {
  background: transparent
    url('https://wolf.drjm.co.uk/nightsky/twinkleMask2.png') repeat top center;
  z-index: 2;
  height: 200%;
  -webkit-animation: twinkleFrames2 300s linear infinite;
  animation: twinkleFrames2 300s linear infinite;
}

.clouds {
  background: transparent url('https://wolf.drjm.co.uk/nightsky/clouds.png')
    repeat top center;
  z-index: 3;
  height: 150%;
  -webkit-animation: cloudsFrames 300s linear infinite;
  animation: cloudsFrames 300s linear infinite;
}

.fogContainer {
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  position: relative;
  z-index: 7;
}

.fog {
  position: absolute;
  left: -50%;
  top: -30%;
  width: 200%;
  height: 200%;
  -webkit-animation-name: fogFrames;
  animation-name: fogFrames;
  -webkit-animation-duration: 60s;
  animation-duration: 60s;
  -webkit-animation-timing-function: linear;
  animation-timing-function: linear;
  -webkit-animation-iteration-count: infinite;
  animation-iteration-count: infinite;
  -webkit-animation-direction: alternate;
  animation-direction: alternate;
  background: linear-gradient(
    -5deg,
    #00000000 0%,
    #ffffff15 40%,
    #74590121 45%,
    #8b845b21 55%,
    #00000000 70%
  );
}

@-webkit-keyframes fogFrames {
  0% {
    transform: none;
  }
  10% {
    transform: scaleY(0.75) translate(5%, -2%) rotate(15deg);
  }
  25% {
    transform: scaleY(1) translate(10%, 7%);
  }
  50% {
    transform: scaleY(0.5) rotate(-15deg);
  }
  75% {
    transform: scaleY(0.2) translate(7%, -2%);
  }
  100% {
    transform: none;
  }
}

@keyframes fogFrames {
  0% {
    transform: none;
  }
  10% {
    transform: scaleY(0.75) translate(5%, -2%) rotate(15deg);
  }
  25% {
    transform: scaleY(1) translate(10%, 7%);
  }
  50% {
    transform: scaleY(0.5) rotate(-15deg);
  }
  75% {
    transform: scaleY(0.2) translate(7%, -2%);
  }
  100% {
    transform: none;
  }
}
@-webkit-keyframes twinkleFrames {
  from {
    background-position: 0 0;
  }
  to {
    background-position: -10000px 5000px;
  }
}
@keyframes twinkleFrames {
  from {
    background-position: 0 0;
  }
  to {
    background-position: -10000px 5000px;
  }
}
@-webkit-keyframes twinkleFrames2 {
  from {
    background-position: 0 0;
  }
  to {
    background-position: 10000px 5000px;
  }
}
@keyframes twinkleFrames2 {
  from {
    background-position: 0 0;
  }
  to {
    background-position: 10000px 5000px;
  }
}
@-webkit-keyframes cloudsFrames {
  from {
    background-position: 0 0;
  }
  to {
    background-position: 10000px 0;
  }
}
@keyframes cloudsFrames {
  from {
    background-position: 0 0;
  }
  to {
    background-position: 10000px 0;
  }
}
</style>
