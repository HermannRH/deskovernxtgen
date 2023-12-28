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
    <v-container class="align-center pt-0 pb-5" style="font-size: 2em; padding-top: 80px; text-align: justify;">
        <span style="font-size: 0.8em">Estamos comprometidos en brindarte una atención de calidad y personalizada. Para comenzar tu proceso de registro, por favor, completa el siguiente formulario con atención y precisión. Asegúrate de que todos los datos proporcionados sean correctos antes de enviarlos.</span>
    </v-container>

    <div class="gold-band">
      <v-container class="pa-10">
        <v-row>
          <v-col cols="7" class="d-flex flex-column align-center justify-center">
            <span style="font-size: 2em" class="big-black-text">Registro de paciente<br></span>
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
.gold-band {
    background-color: #b68d2cb9;
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