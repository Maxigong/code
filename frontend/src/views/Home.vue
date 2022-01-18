<template>
  <div>
    <div id="nav">
      <router-link to="/">Home!!!</router-link> |
      <router-link to="/contact">Contact</router-link> |
      <router-link to="/welcome">Stadel</router-link> |
    </div>
    <h2>Home</h2>
    <div class="links">
      <router-link :to="{ name: 'SVGPath' }">SVG</router-link>
      <router-link :to="{ name: 'SVGPath2' }">SVG 2</router-link>
      <router-link :to="{ name: 'CaptureImg' }">Capture Img</router-link>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.links {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 1rem;
}
.links a {
  text-decoration: none;
  color: red;
}
</style>
