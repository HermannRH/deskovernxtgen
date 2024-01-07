
<template>
    <div>
        <v-container>
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
    <div class="black-band">
      <v-container>
        <v-row class="d-flex text-center justify-center">
          <v-col class="white-text pb-0" cols="12">
            <span>Una membresía, </span>
            <span class="username">infinitas recompensas</span>
          </v-col>
          <v-col cols="12" class="d-flex justify-center pb-12">
            <v-card class="transparent-card text-center black-text">
              <span v-if="username !== 'X'">¡Hola  </span> 
              <span class="username" v-if="username !== 'X'">{{ username.split(' ')[0] }}</span>
              <span v-if="username !== 'X'">! </span> 
              <span v-else>Usuario no Detectado</span>
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
    <div class="align-center text-center username pb-4" style="font-size: 2em; padding-top: 80px;">
      <span>¡Descubre el beneficio de este mes!</span>
    </div>
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
    <v-container class="align-left username pb-4" style="font-size: 2em; padding-top: 80px;">
      <span>Encuentra tu experiencia favorita</span>
    </v-container>
    <v-container>
      <v-row>
        <v-col cols="4" class="align-center text-center" v-for="i in 3" :key="i">
          <div style="width: 100%; height: 200px; background-color: #cccccc;"></div>
          <span style="font-size: 1.5em" class="big-black-text">Experiencia {{ i }}<br></span>
          <span style="font-size: 1.5em">Descripción</span>
        </v-col>
      </v-row>
    </v-container>
    <v-container class="pa-10">
  <v-row v-for="y in 4" :key="y">
    <v-col cols="5" class="align-center text-center">
      <!-- Image placeholder for each item -->
      <div style="width: 100%; height: 200px; background-color: #cccccc;"></div>
    </v-col>
    <v-col cols="7" class="d-flex flex-column align-center justify-center">
      <!-- Dynamic text content for each item -->
      <span style="font-size: 1.7em" class="big-black-text">Titulo de oferta {{ v }}<br></span>
      <span style="font-size: 1.7em">Descripción de la oferta {{ v }}</span>
    </v-col>
  </v-row>
</v-container>

<v-container fluid>
    <v-row justify="center">
      <v-col class="align-center text-center pt-10 pb-5" style="font-size: 1.3em; padding-top: 80px; text-align: justify;">
        <span>¡Síguenos en nuestras redes sociales!</span>
      </v-col>
      <v-col cols="12" class="text-center">
      <v-btn class="custom-button" size="x-large" variant="plain" href="https://fb.com/company123">
        <v-icon left>mdi-facebook</v-icon> Facebook
      </v-btn>
      <!-- Add Instagram Button -->
      <v-btn class="custom-button" size="x-large" variant="plain" href="https://instagram.com/company123">
        <v-icon left>mdi-instagram</v-icon> Instagram
      </v-btn>
    </v-col>
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

<script>
import Rewards from '@/components/Rewards.vue';
import InputData from '@/components/InputData.vue';
import ImgCirculo from '@/assets/images/logocirculo.png';
import ImgHospital from '@/assets/images/logohospital.png';
import { onBeforeMount, ref } from 'vue';
import axios from "axios";
import { useRouter } from 'vue-router';

export default {
  setup(_, { emit }) {
    // Declaring reactive data properties
    const isLoggedIn = ref(true);
    const router = useRouter();
    const logoCirculo = ref(ImgCirculo);
    const logoHospital = ref(ImgHospital);
    const formFirstName = ref('');
    const ngrokEmail = ref('');
    const username = ref('X');

    // Method to fetch data
    const fetchData = async () => {
      try {
        const response = await axios.get('api/info');
        if (response.data.new) {
          router.push('/login');
        } else {
          formFirstName.value = response.data.form_first_name;
          ngrokEmail.value = response.data.ngrok_email;

          if (formFirstName.value !== '') {
            username.value = formFirstName.value;
          } else {
            router.push('/login');
          }
        }
      } catch (error) {
        // router.push('/login');
      }
    };

    // Lifecycle hook
    onBeforeMount(() => {
      fetchData();
    });

    // Return all reactive data and methods
    return {
      isLoggedIn,
      logoCirculo,
      logoHospital,
      formFirstName,
      ngrokEmail,
      username,
      fetchData,
    };
  },
  components: {
    Rewards,
    InputData,
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