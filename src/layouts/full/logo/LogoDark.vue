<template>
    <div class="logo">
        <RouterLink to="/">
            <img class="logo-image" src="/logo.png" alt="Logo">
        </RouterLink>
    </div>
</template>
<script setup lang="ts">
import { ref } from 'vue';
import { RouterLink } from 'vue-router';
const primary = ref('rgb(var(--v-theme-primary))');
const secondary = ref('rgb(var(--v-theme-secondary))');
</script>
<style scoped>
.logo {
  width: 100%;
  height: 100%;
}

.logo-image {
  width: 100%;
  height: 100%;
  object-fit: contain;
}
</style>
