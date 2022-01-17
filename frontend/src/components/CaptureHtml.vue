<template>
  <div>
    <!-- first section -->
    <div class="section-center first-test">
      <div class="box" id="first-img"></div>
      <div @click="handleFirstSection" class="btn first-btn">Get box</div>
      <!-- <div @click="getImges('first-img')" class="btn second-btn">item</div> -->
    </div>
    <!-- second section -->
    <div class="section-center second-test">
      <div class="boxes" id="second-img">
        <div class="box"></div>
        <div class="box"></div>
        <div class="box"></div>
        <div class="box"></div>
      </div>
      <div @click="handleSecondSection" class="btn second-btn">Get boxes</div>
    </div>
    <div @click="sendPicture" class="btn send-btn">send Img</div>
  </div>
</template>

<script>
// https://github.com/tsayen/dom-to-image

import domtoimage from 'dom-to-image';

// if save on computer
// https://github.com/eligrey/FileSaver.js
// npm install file-saver --save

import saveAs from 'file-saver'; // only need if save on computer
import axios from 'axios';

export default {
  components: {},
  data() {
    return {
      saveAs,
      img: '',
    };
  },
  methods: {
    // Can create on function and pass ID as param

    // getImges(item) {
    //   domtoimage.toBlob(document.getElementById(item)).then(function (blob) {
    //     console.log(blob);
    //     window.saveAs(blob, 'my-node.png');
    //   });
    // },

    //  create one function for each section
    handleFirstSection() {
      domtoimage.toBlob(document.getElementById('first-img')).then((blob) => {
        this.img = blob;
      });
    },
    handleSecondSection() {
      domtoimage
        .toBlob(document.getElementById('second-img'))
        .then(function (blob) {
          console.log(blob);
        });
    },

    async sendPicture() {
      // const data = {
      //   user_name: 'newMax',
      //   ID: '123B2C',
      // };

      const bodyFormData = new FormData();
      // append img file
      const blobFile = new File([this.img], 'your_file_name');
      bodyFormData.append('audio', blobFile);
      // bodyFormData.append('file', this.img, 'img1');

      // append extra data
      // bodyFormData.append('User_Details', JSON.stringify(data));
      // const formData = {
      //   img: this.img,
      // };
      try {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/api/v1/userDetails/',
          data: bodyFormData,
          // data: { img: bodyFormData },
          headers: { 'Content-Type': 'multipart/form-data' },
          processData: false,
          contentType: false,
        });
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style scoped>
.section-center {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  gap: 2rem;
  padding: 2rem;
}

.box {
  background: blue;
  height: 200px;
  width: 200px;
}
/* .first-btn {
} */

/* second section */
.second-test {
  background: cornsilk;
}
.boxes {
  display: grid;
  grid-template-columns: 1fr 1fr;
  place-content: center;
  gap: 2rem;
}
/* btn */
.btn {
  height: 50.12px;
  width: 200.91px;
  background: #f95c63;
  border-radius: 51px;
  font-style: normal;
  font-weight: bold;
  font-size: 20px;
  line-height: 150%;
  text-align: center;
  text-transform: capitalize;
  color: #ffffff;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.3 linear;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.4);
}
.btn:active {
  transform: translateY(3px);
  /* display: none; */
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
  color: #f95c63;
  background-color: white;
  border: 2px solid #f95c63;
  animation: shake 150ms 2 linear;
}
.isBtnActive {
  color: #f95c63;
  background-color: white;
  border: 2px solid #f95c63;
  animation: shake 150ms 2 linear;
}
@keyframes shake {
  0% {
    transform: translate(6px, 0);
  }
  50% {
    transform: translate(-6px, 0);
  }
  100% {
    transform: translate(0, 0);
  }
}
</style>
