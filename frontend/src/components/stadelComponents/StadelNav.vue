<template>
  <div class="nav" id="nav">
    <router-link to="/welcome">Home!</router-link> |
    <router-link to="/painting">Explore painting</router-link> |
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
#nav {
  padding: 0.5rem;
}
.nav {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
}
</style>
