<template>
  <div>
    <h2>Home</h2>
    <div class="links">
      <router-link :to="{ name: 'SVGPath' }">SVG</router-link>
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
