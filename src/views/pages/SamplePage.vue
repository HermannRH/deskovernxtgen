<template>
    <v-app>
      <v-main>
        <v-container>
          <h1>Reporte de Avances: Medio término</h1>
          <h2>Plataforma de Cuidado 2023</h2>
  
          <div v-if="!currentComponent">
            <!-- Place your introduction text here -->
            <p>INTRODUCCIÓN</p>
            <!-- Other content -->
  
            <v-btn
              v-for="(comp, index) in components"
              :key="index"
              color="primary"
              @click="loadComponent(comp)"
            >
              {{ comp.label }}
            </v-btn>
          </div>
  
          <component v-else :is="currentComponent" />
  
          <v-btn
            v-if="success"
            color="success"
          >
            Submit
          </v-btn>
        </v-container>
      </v-main>
    </v-app>
  </template>
  
  <script>
  import axios from 'axios';
  // Import other components here...
  
  export default {
    data() {
      return {
        currentComponent: '',
        success: false
      };
    },
    created() {
      axios.get('/public/status.json')
        .then((response) => {
          this.success = response.data.Success;
        });
    },
    methods: {
      loadComponent(comp) {
        this.currentComponent = comp.component;
      },
    },
    components: {
      ProjectDescription,
      ProjectImplementation,
      // Declare other components here...
    },
  };
  </script>
  