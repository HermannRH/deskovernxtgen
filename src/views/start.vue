
<template>
    <div>
        <v-container fluid>
            <v-row class="header" align="center" no-gutters>
                <v-col cols="6" class="pl-7">
                    <v-img :src="logoCirculo" class="responsive-img"></v-img>
                </v-col>
                <v-col cols="6" class="pl-7" align="end">
                    <v-img :src="logoHospital" class="responsive-img"></v-img>
                </v-col>
                <v-col cols="1"></v-col>
            </v-row>
        </v-container>
    </div>
    <div class="black-band">
      <v-container>
        <v-row class="d-flex align-center text-center justify-center">
          <v-col class="white-text pb-0" cols="12">
            <span>Una membresía, </span>
            <span class="username">infinitas recompensas</span>
          </v-col>
          <v-col cols="12" class="d-flex justify-center pb-12">
            <v-card class="transparent-card text-center black-text">
              
              <span>¡Bienvenido, </span> 
            <span class="username">{{ username }}</span>
            <span>! </span> 
            </v-card>
          </v-col>

          <v-col cols="4"  class="white-text">
            <span>Mis Puntos:<br></span>
            <span class="username">6,789</span>
          </v-col>
          <v-col cols="4" class="white-text">
            <span>Nivel de membresía<br></span>
            <span class="username">ORO</span>
          </v-col>
          <v-col cols="4" class="white-text">
            <span>Beneficios próximos<br></span>
            <span class="username">Descuento Especial en tu Próximo Viaje</span>
          </v-col>
        </v-row>
      </v-container>
    </div>
    <v-container>
      <v-row>
        <v-col cols="4" class="align-center text-center big-black-text">
          <span>Conoce<br>tus<br></span>
          <span class="username">Beneficios</span>
        </v-col>
      </v-row>
    </v-container>
</template>

<style scoped>
.big-black-text {
    color: #000000;
    font-size: 70px;
    font-weight: bold;
}
.white-text {
    color: #ffffff;
    font-size: 30px;
    font-weight: bold;
}
.transparent-card {
    background-color: rgba(255, 255, 255, 0.8);
    border-radius: 15px;
    width: 80%;
    height: 10
}
.username {
    font-weight: bold;
    color: #b68d2c;
}
.black-band {
    background-color: #1b1a19;
    height: 600px;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    
}
.black-text {
    color: #000000;
    font-size: 70px;
    font-weight: bold;
}
.responsive-img {
  height: 100px; /* Default height for extra small screens */
}

@media (min-width: 600px) { /* Small screens and up */
  .responsive-img {
    height: 150px;
  }
}

@media (min-width: 960px) { /* Medium screens and up */
  .responsive-img {
    height: 200px;
  }
}
.responsive-btn {
  white-space: nowrap; /* Default for extra small screens */
}

@media (min-width: 600px) { /* Small screens and up */
  .responsive-btn {
    white-space: normal;
  }
}
</style>

<script>
import Rewards from '@/components/Rewards.vue';
import InputData from '@/components/InputData.vue';
import ImgCirculo from '@/assets/images/logocirculo.png';
import ImgHospital from '@/assets/images/logohospital.png';

export default {
    components: {
        Rewards,
        InputData,
    },
    data() {
        return {
            isLoggedIn: true, 
            logoCirculo: ImgCirculo,
            logoHospital: ImgHospital,
            username: 'Juan Perez',
        };
    },
    methods: {
        login() {
            // Implement your login logic here
        },
        logout() {
            // Implement your logout logic here
        },
    },
};
</script>