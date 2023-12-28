<template>
    <div>
        <v-container fluid>
            <v-row align="center" no-gutters>
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
    <v-container class="align-center text-center username pt-0 pb-5" style="font-size: 2em; padding-top: 80px; text-align: justify;">
        <span>¡Bienvenido al formulario de registro de pacientes del Hospital Andalucía!</span>
    </v-container>
    <div class="black-band">
      <v-container>
        <v-row class="d-flex text-center justify-center">
          <v-col class="white-text pb-0" cols="12">
            <span>Una membresía, </span>
            <span class="username">infinitas recompensas</span>
          </v-col>
          <v-col cols="12" class="d-flex justify-center pb-12">
            <v-card class="transparent-card text-center black-text">
              <span>¡Bienvenido, </span> 
            </v-card>
          </v-col>

          <v-col cols="4" class="white-text align-start text-center">
            <span>Mis Puntos:<br></span>
            <span class="username">9,876</span>
          </v-col>
          <v-col cols="4" class="white-text align-start text-center">
            <span>Nivel de membresía<br></span>
            <span class="username">ORO</span>
          </v-col>
          <v-col cols="4" class="white-text align-start text-center">
            <span>Miembro<br></span>
            <span class="username">10/09/2015</span>
          </v-col>
        </v-row>
      </v-container>
    </div>
    <v-container>
      <v-row>
        <v-col cols="3" class="align-center text-center big-black-text" v-for="i in 4" :key="i">
      <div class="window ">
        <span>Conoce<br>tus<br></span>
        <span class="username">Beneficios</span>
      </div>
    </v-col>
      </v-row>
    </v-container>
    <div class="grey-band">
      <v-container class="pa-10">
        <v-row>
          <v-col cols="5" class="align-center text-center">
            <div style="width: 100%; height: 200px; background-color: #cccccc;"></div>
          </v-col>
          <v-col cols="7" class="d-flex flex-column align-center justify-center">
            <span style="font-size: 2em" class="big-black-text">Precio Preferencial en Hotel Andalucía<br></span>
            <span style="font-size: 2em">Todo el año a solo $850 la noche</span>
          </v-col>
        </v-row>
      </v-container>
    </div>

<v-container fluid>
    <v-row justify="center">
      <v-col cols="12" class="text-center" >
        <v-btn variant="plain" class="username">Términos y condiciones</v-btn>
        <v-btn variant="plain" class="username">Preguntas frecuentes</v-btn>
        <v-btn variant="plain" class="username">Contáctanos</v-btn>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="12" class="text-center">
        <span class="caption">&copy; Todos los derechos reservados</span>
      </v-col>
    </v-row>
  </v-container>

</template>

<script lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';
import ImgCirculo from '@/assets/images/logocirculo.png';
import ImgHospital from '@/assets/images/logohospital.png';

export default {
    data() {
        return {
            logoCirculo: ImgCirculo,
            logoHospital: ImgHospital,
        };
    },
    setup() {
        const ngrok_email = ref('');

        onMounted(async () => {
            const response = await axios.get('api/info');
            ngrok_email.value = response.data.ngrok_email;
        });

        const submitForm = () => {
            // Handle form submission
        };

        return {
            ngrok_email,
            submitForm,
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
<style scoped>
.window {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
  overflow: auto;

}
.window span {
  font-size: calc(100% + 2vw); /* Adjust as needed */
}
.grey-band {
  background-color: #f2f2f2;
  height: 300px;
  width: 90%;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50px;
  margin: auto;
  overflow: auto;
}
.big-black-text {
    color: #000000;
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