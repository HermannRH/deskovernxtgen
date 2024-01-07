<template>
    <div>
        <v-container fluid>
            <v-row align="center" no-gutters>
                <v-col cols="6"  class="pl-7">
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
        <span>¡Bienvenid@ al formulario de registro de pacientes del Hospital Andalucía!</span>
    </v-container>
    <v-container class="align-center pt-0 pb-5" style="font-size: 2em; padding-top: 80px; text-align: justify;">
        <span style="font-size: 0.8em">Estamos comprometidos en brindarte una atención de calidad y personalizada. Para comenzar tu proceso de registro, por favor, completa el siguiente formulario con atención y precisión. Asegúrate de que todos los datos proporcionados sean correctos antes de enviarlos.</span>
    </v-container>
    <div class="gold-bandx">
        
        <v-container>
            <v-row class="pt-5 pb-10">
                <v-col cols="12" class="text-center" style="background-color: #f2f2f2; border-radius: 25px; padding: 10px;">
                    <span class="caption" style="font-weight: bold; font-size: 20px;">REGISTRO DE PACIENTE</span>
                </v-col>
            </v-row>
  <v-row align="end">
    <!-- Placeholder for the photograph, spanning vertically across 3 rows -->
    <v-col cols="5" class="mb-2">
    <v-row align="end">
        <v-col cols="12" class="mb-2">
      <!-- Display uploaded image or placeholder -->
    <v-img 
        :src="uploadedImage || logoUpload" 
        class="responsive-img" 
        @click="triggerFileInput"
        style="object-fit: contain; max-height: 250px; min-height: 250px;">
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
            <v-text-field v-model="name" label="Nombre completo"></v-text-field>
          </v-col>
          <v-col cols="4" class="pl-3">
            <v-text-field v-model="age" label="Edad" type="number"></v-text-field>
          </v-col>
          <v-col cols="4" class="pl-3">
            <v-select v-model="bloodType" label="Tipo de Sangre" :items="bloodTypes"></v-select>
          </v-col>
          <v-col cols="4" class="pl-3">
            <v-text-field v-model="birthDate" label="Fecha de nacimiento" type="date"></v-text-field>
          </v-col>
          <v-col cols="6" class="pl-3">
            <v-text-field v-model="email" label="Correo Electrónico"></v-text-field>
          </v-col>
          <v-col cols="6" class="pl-3">
            <v-text-field v-model="phone" label="Teléfono" type="number"></v-text-field>
          </v-col>
          <v-col class="pl-3">
            <v-text-field v-model="address" label="Dirección"></v-text-field>
          </v-col>
        </v-row>
    </v-col>
    </v-row>
  <v-row>
    <v-col cols="5">
            <v-select v-model="insuranceType" label="Tipo de seguro" :items="insuranceTypes"></v-select>
        </v-col>
        <v-col cols="7">
            <v-select v-model="insuranceCompany" label="Aseguradora" :items="insuranceCompanies"></v-select>
        </v-col>
        <v-col cols="12" class="pb-0">
          <v-text-field v-model="cardNumber" label="Agrega aquí el número de tu tarjeta"></v-text-field>
        </v-col>
        <v-col cols="12" class="pt-0">
          <v-checkbox v-model="termsAccepted" label="¿Aceptas los términos y condiciones?"></v-checkbox>
        </v-col>
  </v-row>
  <v-row class="pt-5 pb-5 text-center d-flex justify-center">
        <v-col cols="4" class="pa-5" style="background-color: #f2f2f2; border-radius: 25px; padding: 10px;" @click="submitForm">
            <span class="caption" style="font-weight: bold; font-size: 20px;">Guardar Información</span>
        </v-col>
    </v-row>
</v-container>
  </div>

  <v-container class="align-center pt-10 pb-5" style="font-size: 2em; padding-top: 80px; text-align: justify;">
        <span style="font-weight: bold;">¿Por Qué Recopilamos Esta Información?<br></span>
        <span style="font-size: 0.8em">La información que nos proporciones será utilizada exclusivamente para fines médicos y administrativos dentro del Hospital Andalucía. Esto nos permite ofrecerte una atención más eficiente y adecuada a tus necesidades de salud.</span>
    </v-container>
    <v-container class="align-center pt-10 pb-5" style="font-size: 2em; padding-top: 80px; text-align: justify;">
        <span style="font-weight: bold;">Confidencialidad y Seguridad<br></span>
        <span style="font-size: 0.8em">Tu privacidad es nuestra prioridad. Todos los datos recopilados en este formulario están protegidos y serán tratados con la máxima confidencialidad, de acuerdo con las leyes y normativas de protección de datos.</span>
    </v-container>

    <v-container class="align-center pt-10 pb-5" style="font-size: 2em; padding-top: 80px; text-align: justify;">
        <span style="font-weight: bold;">¿Tienes Dudas o Preguntas?<br></span>
        <span style="font-size: 0.8em">Si tienes alguna duda acerca del proceso de registro o necesitas asistencia adicional, no dudes en contactarnos. Puedes encontrar nuestros datos de contacto en la sección correspondiente de nuestra página web.</span>
    </v-container>
    <v-container class="align-center text-center pt-10 pb-5" style="font-size: 2em; padding-top: 80px; text-align: justify;">
        <span style="font-weight: bold;">¡Agradecemos tu confianza en el Hospital Andalucía!<br>Estamos aquí para apoyarte en tu camino hacia una mejor salud.</span>
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

<style scoped>
.gold-bandx .white-input input {
  background-color: white !important;
}
.gold-bandx {
    background-color:  #b68d2c5d;
    height: 950px;
    width: 90%;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50px;
    margin: auto;
    overflow: auto;
}
.username {
    font-weight: bold;
    color: #b68d2c;
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
</style>


<script lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';
import ImgCirculo from '@/assets/images/logocirculo.png';
import ImgHospital from '@/assets/images/logohospital.png';
import uploadlogo from '@/assets/images/uploadlogo.png'
import { useRouter } from 'vue-router';



export default {
    data() {
        return {
            logoCirculo: ImgCirculo,
            logoHospital: ImgHospital,
            logoUpload: uploadlogo,
            uploadedImage: null as string | null,
            bloodTypes: ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'],
            insuranceCompanies: ["AA", "BB", "CC", "DD", "EE", "FF", "GG", "HH", "II", "JJ", "KK"],
            insuranceTypes: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"],
            name: '',
            age: null as number | null,
            bloodType: '',
            birthDate: null,
            email: '',
            phone: "",
            address: '',
            insuranceType: '',
            insuranceCompany: '',
            termsAccepted: false,
            cardNumber: "",
            router : useRouter(),
        };
    },
    setup() {
        const ngrok_email = ref('');
        const fileInput = ref<HTMLInputElement|null>(null);

        onMounted(async () => {
            const response = await axios.get('api/info');
            ngrok_email.value = response.data.ngrok_email;
        });

        const triggerFileInput = () => {
            fileInput.value?.click();
        };

        return {
            ngrok_email,

        };
    },
    methods: {
      validateForm() {
        let errors = [];
        if (!this.name) {
          errors.push("El nombre es obligatorio.");
        }
        if (!this.age || this.age < 13 || this.age > 110) {
          errors.push("La edad debe estar entre 13 y 110 años.");
        }
        if (!this.bloodType) {
          errors.push("El tipo de sangre es obligatorio.");
        }
        if (!this.birthDate) {
          errors.push("La fecha de nacimiento es obligatoria.");
        }
        if (!this.email || !this.email.match(/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/)) {
          errors.push("El correo electrónico no es válido.");
        }
        if (!this.phone || !this.phone.match(/^\d{10}$/)) {
          errors.push("El teléfono debe tener 10 dígitos.");
        }
        if (!this.address) {
          errors.push("La dirección es obligatoria.");
        }
        if (!this.insuranceType) {
          errors.push("El tipo de seguro es obligatorio.");
        }
        if (!this.insuranceCompany) {
          errors.push("La compañía de seguros es obligatoria.");
        }

        if (!this.uploadedImage) {
          errors.push("La imagen es obligatoria.");
        }
        if (!this.termsAccepted) {
          errors.push("Debes aceptar los términos y condiciones.");
        }
        if (!this.cardNumber) {
          errors.push("El número de tarjeta es obligatorio");
        }
        return errors;
      },
        triggerFileInput() {
            const inputElement = this.$refs.fileInput as HTMLInputElement;
            inputElement.click();
        },
        submitForm() {
          const formErrors = this.validateForm();

      if (formErrors.length > 0) {
        formErrors.forEach(error => {
          this.$notify({ type: 'warn', title: 'Error de Validación', text: error });
        });
        return;
      }
        const formData = {
          name: this.name,
          age: this.age,
          bloodType: this.bloodType,
          birthDate: this.birthDate,
          email: this.email,
          phone: this.phone,
          address: this.address,
          insuranceType: this.insuranceType,
          insuranceCompany: this.insuranceCompany,
          image: this.uploadedImage,
        };
        console.log('Submitting form', formData);
        axios.post('api/form', formData)
            .then(response => {
              console.log('Form submitted successfully', response);
              this.$notify({ type: 'success', title: 'Éxito', text: 'Sus datos fueron registrados correctamente.' });
              setTimeout(() => {
                this.$router.push('/');
                window.scrollTo({ top: 0, behavior: 'smooth' });
              }, 3000);
                
            })
            .catch(error => {
                console.error('Error submitting form', error);
                this.$notify({ type: 'error', title: 'Error', text: 'Hubo un problema con sus datos, porfavor recarga la página y vuelva a intentar' });
            });
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