<template>
  <RouterView></RouterView>
  <notifications position="bottom right" duration="9000" width="900" />
</template>

<script setup lang="ts">
import { RouterView } from "vue-router";
</script>

