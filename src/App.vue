<template>
  <div id="app">
    <RouterView></RouterView>
    <notifications position="bottom right" width="900" />
  </div>
</template>

<script setup lang="ts">
import { RouterView, useRouter } from "vue-router";
import axios from "axios";
import { ref, onMounted, provide } from 'vue';

const showModal = ref(false);
let form_first_name = '';
let form_first_surname = '';
let ngrok_email = '';

const router = useRouter();

onMounted(async () => {
  try {
    const response = await axios.get('api/info');
    if (response.data.new) {
      router.push('/login');
    } else {
      form_first_name = response.data.form_first_name;
      form_first_surname = response.data.form_first_surname;
      ngrok_email = response.data.ngrok_email;
      provide('form_first_name', form_first_name);
      provide('form_first_surname', form_first_surname);
      provide('ngrok_email', ngrok_email);
    }
  } catch (error) {
    router.push('/login');
  }
});
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