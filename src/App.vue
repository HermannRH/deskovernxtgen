<template>
  <div id="app">
    <RouterView></RouterView>
    <notifications position="bottom right" width="70%" />
  </div>
</template>

<script setup lang="ts">
import { RouterView } from "vue-router";

</script>


<style>
html, body {
  font-family: 'Inter', sans-serif;
}

#app {
  width: 100vw;
  overflow: hidden;
}

@font-face {
  font-family: 'Inter';
  src: url('@/assets/Inter.ttf') format('truetype');
}
</style>