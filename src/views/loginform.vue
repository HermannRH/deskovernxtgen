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
    <div class="gold-bandx">
        <v-container>
  <v-row align="end">
    <!-- Placeholder for the photograph, spanning vertically across 3 rows -->
    <v-col cols="5" class="mb-2">
    <v-row align="end">
        <v-col cols="12" class="mb-2">
      <!-- Display uploaded image or placeholder -->
      <v-img 
        :src="uploadedImage || logoCirculo" 
        class="responsive-img" 
        @click="triggerFileInput">
      </v-img>
    </v-col>
    <v-col cols="12" class="pb-1">
      <!-- File input for uploading image -->
      <v-file-input 
        ref="fileInput" 
        label="Fotografía del paciente" 
        prepend-icon="mdi-camera" 
        accept=".jpg, .jpeg, .png"
        @change="handleFileUpload">
      </v-file-input>
    </v-col>
    </v-row>
    </v-col>

    <!-- Name field aligned next to the photograph -->
    <v-col cols="7">
        <v-row>
        <v-col cols="12" class="pl-3">
        <v-text-field label="Nombre completo"></v-text-field>
        </v-col>
        <v-col cols="4" class="pl-3">
            <v-text-field
                label="Edad"
                type="number"
                :rules="[v => (v >= 0 && v <= 110) || 'Edad debe ser entre 0 y 110']"
            ></v-text-field>
            </v-col>
        <v-col cols="4" class="pl-3">
        <v-select label="Tipo de Sangre" :items="bloodTypes"></v-select>
        </v-col>
        <v-col cols="4" class="pl-3">
        <v-text-field label="Fecha de nacimiento" v-model="date" type="date" :rules="[dateRule]"></v-text-field>
        </v-col>
        <v-col cols="6" class="pl-3">
            <v-text-field label="Correo Electrónico" :rules="[emailRule]"></v-text-field>
        </v-col>
        <v-col cols="6" class="pl-3">
            <v-text-field label="Teléfono" type="number" :rules="[phoneRule]"></v-text-field>
        </v-col>
        <v-col class="pl-3">
            <v-text-field label="Dirección"></v-text-field>
        </v-col>
        </v-row>
    </v-col>
    </v-row>


  <v-row>
    <!-- Address field spanning across most of the row -->

    <!-- Insurance fields occupying the remaining space in the same row -->

    <v-col cols="5">
      <v-select label="Tipo de seguro" :items="insuranceTypes"></v-select>
    </v-col>
    <v-col cols="7">
      <v-select label="Aseguradora" :items="insuranceCompanies"></v-select>
    </v-col>
  </v-row>
</v-container>
      <!-- Title -->

    <!-- Patient photo upload section -->
    
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
            menu: false,
            date: null,
            dateRule: (v: string) => {
        if (!v) return "Fecha de nacimiento es requerida";
        const selectedDate = new Date(v);
        const minDate = new Date('1900-01-01');
        const maxDate = new Date();
        if (selectedDate < minDate || selectedDate > maxDate) {
          return 'Fecha de nacimiento debe ser después de 1900 y antes de hoy';
        }
        return true;},
            logoCirculo: ImgCirculo,
            logoHospital: ImgHospital,
            uploadedImage: null as string | null,
            emailRule: (v: string) => /.+@.+\..+/.test(v) || 'Correo electrónico debe ser válido',
            phoneRule: v => (/^\d{10}$/.test(v) || 'Teléfono debe ser un número de 10 dígitos'),
            ages: [...Array(100).keys()].map((i) => i + 1),
            bloodTypes: ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'],
            insuranceCompanies: ["AA", "BB", "CC", "DD", "EE", "FF", "GG", "HH", "II", "JJ", "KK"],
            insuranceTypes: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

        };
    },
    setup() {
        const ngrok_email = ref('');
        const fileInput = ref<HTMLInputElement|null>(null);

        onMounted(async () => {
            const response = await axios.get('api/info');
            ngrok_email.value = response.data.ngrok_email;
        });

        const submitForm = () => {
            // Handle form submission
        };
        const triggerFileInput = () => {
            fileInput.value?.click();
        };

        return {
            ngrok_email,
            submitForm,
        };
    },
    methods: {
        triggerFileInput() {
            const inputElement = this.$refs.fileInput as HTMLInputElement;
            inputElement.click();
        },
    handleFileUpload(event: Event) {
        const file = (event.target as HTMLInputElement).files?.[0];
            if (file && file.type.startsWith('image/')) {
                const reader = new FileReader();
                reader.onload = e => {
                    this.uploadedImage = (e.target as FileReader).result as string;
                };
                reader.readAsDataURL(file);
            }
    }
  }
};
</script>

<style scoped>
.v-messages__message {
  color: #2210cc !important;
}
.gold-bandx .white-input input {
  background-color: white !important;
}
.gold-band {
  background-color: #D4AF37; /* Golden color */
}

.display-1 {
  font-size: 2em;
  color: #000; /* Black color for text */
}
.gold-bandx {
    background-color: #b68d2cba;
    height: 600px;
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
}.white-text {
    color: #ffffff;
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