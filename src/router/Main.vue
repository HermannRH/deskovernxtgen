<template>
    <v-container fluid class="app-bar">
        <v-row no-gutters align="center">
            <!-- Logos Section -->
            <v-col cols="auto">
                <v-img :src="logoHospital" max-height="100" max-width="100" />
                <v-img :src="logoCirculo" max-height="100" max-width="100" />
            </v-col>

            <!-- Spacer to push the navigation and session button to the right -->
            <v-spacer></v-spacer>

            <!-- Navigation Links -->
            <v-col cols="auto">
                <v-btn text>Sobre nosotros</v-btn>
                <v-btn text>Mi membresía</v-btn>
                <v-btn text>Sucursales</v-btn>
                <v-btn text>Avisos legales</v-btn>
            </v-col>

            <!-- Session Button -->
            <v-col cols="auto">
                <v-btn color="yellow darken-1" class="white--text">Cerrar sesión</v-btn>
            </v-col>
        </v-row>
    </v-container>
</template>

<style scoped>
.app-bar {
    background-color: white;
    height: 64px; /* Adjust as needed */
}
</style>
  
  <script>
  import LogoHospital from '@/assets/images/logohospital.png';
  import LogoCirculo from '@/assets/images/logocirculo.png';

  export default {
    name: 'HeaderComponent',
    data: () => ({
      drawer: false,
      logoHospital: LogoHospital,
    logoCirculo: LogoCirculo,
    }),
  };
  </script>
  
  <style>
  .empty-rectangle {
  width: 100px;  /* Adjust as needed */
  height: 100px; /* Adjust as needed */
  border: 1px solid white; /* Adjust as needed */
}

.custom-app-bar {
  height: 100px; /* Adjust as needed */
}
  </style>
  