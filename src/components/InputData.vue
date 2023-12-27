<template>
  <form @submit="handleSubmit">
    <label for="name">Name:</label>
    <input type="text" id="name" v-model="name" required>

    <label for="email">Email:</label>
    <input type="email" id="email" v-model="email" required>

    <button type="submit">Submit</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      email: ''
    };
  },
  methods: {
    handleSubmit() {
      // Handle form submission logic here
      console.log('Form submitted');
      console.log('Name:', this.name);
      console.log('Email:', this.email);
    }
  }
};
</script>

<style scoped>
/* Add your custom styles here */
</style>
