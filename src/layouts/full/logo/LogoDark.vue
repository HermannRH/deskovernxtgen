<template>
  <div>
      <div class="logo" @click="dialog = true">
          <RouterLink to="/">
              <img class="logo-image" src="/logo.png" alt="Logo">
          </RouterLink>
      </div>

      <v-dialog v-model="dialog" max-width="500px">
          <v-card>
              <v-card-title class="text-h5">Deskover NextGeneration</v-card-title>
              <v-card-text>
                  <img class="logo-image" src="/logo.png" alt="Logo">
              </v-card-text>
          </v-card>
      </v-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { RouterLink } from 'vue-router';
const primary = ref('rgb(var(--v-theme-primary))');
const secondary = ref('rgb(var(--v-theme-secondary))');
const dialog = ref(false);
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
