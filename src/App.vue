<template>
  <div id="app">
    <RouterView></RouterView>
    <notifications position="bottom right" width="900" />
  </div>
</template>

<script setup lang="ts">
import { RouterView } from "vue-router";
</script>

<style>
#app {
  width: 100vw;
  height: 100vh;
  overflow: hidden;
}
</style>