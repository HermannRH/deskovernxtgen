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
  <v-container class="align-center text-center username pt-0 pb-5" style="font-size: 1em; padding-top: 80px; text-align: justify;">
      <span>¡Bienvenid@ al formulario de registro de pacientes del Hospital Andalucía!</span>
  </v-container>
  <v-container class="align-center pt-0 pb-5" style="font-size: 1em; padding-top: 80px; text-align: justify;">
      <span style="font-size: 0.8em">Estamos comprometidos en brindarte una atención de calidad y personalizada. Para comenzar tu proceso de registro, por favor, completa el siguiente formulario con atención y precisión. Asegúrate de que todos los datos proporcionados sean correctos antes de enviarlos.</span>
  </v-container>
  <div class="gold-bandx">
      
      <v-container>
          <v-row class="pt-5 pb-5 pl-5 pr-5">
              <v-col cols="12" class="text-center" style="background-color: #f2f2f2; border-radius: 25px; padding: 10px;">
                  <span class="caption" style="font-weight: bold; font-size: 15px;">REGISTRO DE PACIENTE</span>
              </v-col>
          </v-row>
<v-row align="end" >
  <v-col cols="5" class="mb-0">
  <v-row align="end">
      <v-col cols="12" class="mb-0">
  <v-img 
      :src="uploadedImage || logoUpload" 
      class="responsive-img" 
      @click="triggerFileInput"
      style="object-fit: contain; max-height: 130px; min-height: 130px;">
  </v-img>
  </v-col>
  <v-col cols="12" class="pa-2" style="font-size: 0.3em;">
    <!-- File input for uploading image -->
    <v-file-input 
    v-if="!imageUploaded"
    ref="fileInput" 
    label="Fotografía" 
    prepend-icon="mdi-camera" 
    hide-details="auto" density="compact" variant="underlined"
    accept=".jpg, .jpeg, .png"
    @change="handleFileUpload"
    >
  </v-file-input>
  </v-col>
  </v-row>
  </v-col>

  <!-- Name field aligned next to the photograph -->
  <v-col cols="7" >
      <v-row>
        <v-col cols="12" class="pa-2">
          <v-text-field hide-details="auto" variant="underlined" v-model="name" label="Nombre completo"></v-text-field>
        </v-col>
        <v-col cols="12" class="pa-2">
          <v-select hide-details="auto" density="compact" variant="underlined" v-model="bloodType" label="Tipo de Sangre" :items="bloodTypes"></v-select>
        </v-col>
        <v-col cols="12" class="pa-2">
          <v-text-field hide-details="auto" density="compact" variant="underlined" v-model="birthDate" label="Fecha de nacimiento" type="date"></v-text-field>
        </v-col>
        <v-col cols="12" class="pa-2">
          <v-text-field hide-details="auto" density="compact" variant="underlined" v-model="email" label="Correo Electrónico"></v-text-field>
        </v-col>
      </v-row>
  </v-col>
  </v-row>
<v-row>
        <v-col cols="8" class="pa-2">
          <v-text-field hide-details="auto" density="compact" variant="underlined" v-model="address" label="Dirección"></v-text-field>
        </v-col>
        <v-col cols="4" class="pa-2">
          <v-text-field hide-details="auto" density="compact" variant="underlined" v-model="phone" label="Teléfono" type="number"></v-text-field>
        </v-col>
  <v-col cols="5" class="pa-2">
    <v-select v-model="insuranceType" hide-details="auto" density="compact" variant="underlined" label="Tipo de seguro" :items="insuranceTypes"></v-select>
  </v-col>
  <v-col cols="7" class="pa-2">
    <v-select v-model="insuranceCompany" hide-details="auto" density="compact" variant="underlined" label="Aseguradora" :items="insuranceCompanies"></v-select>
  </v-col>
      <v-col cols="12" class="pa-2" v-if="insuranceType === 'Otro'">
        <v-text-field hide-details="auto" density="compact" variant="underlined" v-model="otherInsuranceType" label="Indica cuál es el tipo de seguro que tienes"></v-text-field>
      </v-col>
      <v-col cols="12" class="pa-2" v-if="insuranceCompany === 'Otra'">
        <v-text-field hide-details="auto" density="compact" variant="underlined" v-model="otherInsuranceCompany" label="Indica cuál el nombre de tu aseguradora"></v-text-field>
      </v-col>

      <v-col cols="12" class="pa-2">
        <v-select v-model="centroTrabajo" hide-details="auto" density="compact" variant="underlined" label="Centro de Trabajo" :items="centrosTrabajo"></v-select>
      </v-col>
      <v-col cols="12" class="pa-2" v-if="centroTrabajo === 'Otro'">
        <v-text-field hide-details="auto" density="compact" variant="underlined" v-model="otherCentroTrabajo" label="Indica cuál el nombre de tu Centro de Trabajo"></v-text-field>
      </v-col>

      <v-col cols="12" class="pa-2">
        <v-text-field hide-details="auto" density="compact" variant="underlined" v-model="folioTarjeta" label="Agrega aquí el número de Folio de tu tarjeta" type="number"></v-text-field>
      </v-col>
      <v-col cols="12" class="pa-2">
        <v-checkbox v-model="termsAccepted" label="¿Aceptas los términos y condiciones?"></v-checkbox>
      </v-col>
</v-row>
<v-row class="text-center d-flex justify-center pb-5">
      <v-col cols="6" class="pa-5" style="background-color: #f2f2f2; border-radius: 25px; padding: 10px;" @click="submitForm">
          <span class="caption" style="font-weight: bold; font-size: 1em;">Guardar Información</span>
      </v-col>
  </v-row>
</v-container>
</div>

<v-container class="align-center pt-10 pb-5" style="font-size: 1em;  text-align: justify;">
      <span style="font-weight: bold;">¿Por Qué Recopilamos Esta Información?<br></span>
      <span style="font-size: 0.8em">La información que nos proporciones será utilizada exclusivamente para fines médicos y administrativos dentro del Hospital Andalucía. Esto nos permite ofrecerte una atención más eficiente y adecuada a tus necesidades de salud.</span>
  </v-container>
  <v-container class="align-center pt-10 pb-5" style="font-size: 1em;  text-align: justify;">
      <span style="font-weight: bold;">Confidencialidad y Seguridad<br></span>
      <span style="font-size: 0.8em">Tu privacidad es nuestra prioridad. Todos los datos recopilados en este formulario están protegidos y serán tratados con la máxima confidencialidad, de acuerdo con las leyes y normativas de protección de datos.</span>
  </v-container>

  <v-container class="align-center pt-10 pb-5" style="font-size: 1em;  text-align: justify;">
      <span style="font-weight: bold;">¿Tienes Dudas o Preguntas?<br></span>
      <span style="font-size: 0.8em">Si tienes alguna duda acerca del proceso de registro o necesitas asistencia adicional, no dudes en contactarnos. Puedes encontrar nuestros datos de contacto en la sección correspondiente de nuestra página web.</span>
  </v-container>
  <v-container class="align-center text-center pt-10 pb-5" style="font-size: 1em;  text-align: justify;">
      <span style="font-weight: bold;">¡Agradecemos tu confianza en el Hospital Andalucía!<br>Estamos aquí para apoyarte en tu camino hacia una mejor salud.</span>
  </v-container>

<v-container fluid>
  <v-row justify="center">
    <v-col class="align-center text-center pt-10 pb-5" style="font-size: 1.3em; padding-top: 80px; text-align: justify;">
      <span>¡Síguenos en nuestras redes sociales!</span>
    </v-col>
    <v-col cols="12" class="text-center">
    <v-btn class="custom-button" size="x-large" variant="plain" href="https://www.facebook.com/HospitalAndaluciaMx">
      <v-icon left>mdi-facebook</v-icon> Facebook
    </v-btn>
    <!-- Add Instagram Button -->
    <v-btn class="custom-button" size="x-large" variant="plain" href="https://www.instagram.com/hospital_andalucia_mx/">
      <v-icon left>mdi-instagram</v-icon> Instagram
    </v-btn>
  </v-col><!--
    <v-col cols="12" class="text-center" >
      <v-btn variant="plain" class="username">Términos y condiciones</v-btn>
      <v-btn variant="plain" class="username">Preguntas frecuentes</v-btn>
      <v-btn variant="plain" class="username">Contáctanos</v-btn>
    </v-col> -->
  </v-row>
  <v-row justify="center">
    <v-col cols="12" class="text-center">
      <span class="caption">&copy; Todos los derechos reservados</span>
    </v-col>
  </v-row>
</v-container>

<v-dialog v-model="dialog" persistent width="90%">
    <v-card class="pa-5">
      <v-card-title class="headline">Acceso</v-card-title>
      <v-card-text v-if="!loading">
        Ingresa el Folio de tu Tarjeta para continuar.
        <v-text-field
          v-model="folioCheckInicial"
          label="Folio de Tarjeta"
          :rules="folioRules"
        ></v-text-field>
        <span v-if="validationError">{{ validationError }}</span>
      </v-card-text>
      <v-card-text v-else>
        Validando Folio... <br>
        <v-progress-circular indeterminate color="primary"></v-progress-circular>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="green darken-1" @click="validateFolio">Acceder</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

  <v-dialog v-model="dialogSuccess" persistent max-width="500px">
  <v-card class="pa-5">
    <v-container>
      <v-row>
        <v-col class="d-flex justify-center">
          <v-img :src="checkIcon"></v-img>
      </v-col>
      </v-row>
      <v-row>
        <v-col class="d-flex justify-center">
          <v-card-title class="headline text-center">¡Todo Listo!</v-card-title>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-card-text class="text-center">
            <span>¡Felicidades {{ name }}! <br>
            Tus datos fueron registrados correctamente. <br>
            ¡Pronto recibirás acceso a beneficios exclusivos! <br><br>
            Ya no es necesario hacer nada más. <br></span>
          </v-card-text>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="d-flex justify-center">
          <v-btn color="green darken-1" @click="redirectEnd">Cerrar</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</v-dialog>

<v-dialog v-model="dialogAdmin" persistent max-width="500px">
  <v-card class="pa-5">
    <v-container>
      <v-row>
        <v-col class="d-flex justify-center">
          <v-img :src="adminIcon"></v-img>
      </v-col>
      </v-row>
      <v-row>
        <v-col class="d-flex justify-center">
          <v-card-title class="headline text-center">Descarga de Información</v-card-title>
        </v-col>
        <v-col cols="12" class="pa-2">
          <v-text-field hide-details="auto" v-model="emailAdmin" label="Correo" type="email" required></v-text-field>
        </v-col>
        <v-col cols="12" class="pa-2">
          <v-text-field hide-details="auto" v-model="passwordAdmin" label="Credencial" type="password" required></v-text-field>
        </v-col>
        <v-col cols="12" class="pa-2">
          <v-checkbox  hide-details="auto" v-model="downloadUserData" label="Accept User Data"></v-checkbox>
        </v-col>
        <v-col cols="12" class="pa-2">
          <v-checkbox  hide-details="auto" v-model="downloadImages" label="Accept Images"></v-checkbox>
        </v-col>
        <v-col class="d-flex justify-center">
          <v-btn color="primary" @click="submitAdmin">
            Enviar Consulta
            <v-icon class="pl-3" left>mdi-send</v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</v-dialog>

</template>
<script lang="ts">
import axios from 'axios';
import ImgCirculo from '@/assets/images/logocirculo.png';
import ImgHospital from '@/assets/images/logohospital.png';
import uploadlogo from '@/assets/images/uploadlogo.png'
import checkIcon from '@/assets/images/check.png'
import { useRouter } from 'vue-router';
import adminIcon from '@/assets/images/admin-panel.png'



export default {
  data() {
      return {
          dialog: true,
          folioCheckInicial: null as number | null,
          loading: false,
          validationError: '',
          folioRules: [
            (v: any) => !!v || 'El Folio is required',
            (v: any) => (v === '#andalucia' || (v > 0 && v <= 10000)) || 'Este folio no funciona, contactános directamente'
          ],
          dialogSuccess: false,
          logoCirculo: ImgCirculo,
          logoHospital: ImgHospital,
          logoUpload: uploadlogo,
          checkIcon: checkIcon,
          dialogAdmin: false,
          adminIcon: adminIcon,
          imageLoaded: false,
          uploadedImage: null as string | null,
          imageUploaded: false,
          bloodTypes: ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-', 'Desconozco'],
          insuranceCompanies: [''],
          insuranceTypes: [''],
          centrosTrabajo: [''],
          name: '',
          age: null as number | null,
          bloodType: '',
          birthDate: null,
          email: '',
          phone: "",
          address: '',
          insuranceType: '',
          insuranceCompany: '',
          centroTrabajo: '',
          otherCentroTrabajo: '',
          otherInsuranceType: '',
          otherInsuranceCompany: '',
          termsAccepted: false,
          folioTarjeta: null as number | null,
          router : useRouter(),
          emailAdmin: '',
          passwordAdmin: '',
          downloadUserData: false,
          downloadImages: false,
      };
  },
  mounted() {
      this.preloadImage();
  },
  methods: {
    redirectEnd() {
      window.location.href = 'https://hospitalandalucia.com/';
    },
    validateForm() {
      let errors = [];
      if (!this.name) {
        errors.push("El nombre es obligatorio.");
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
      if (!this.insuranceType) {
        errors.push("El tipo de seguro es obligatorio.");
      }
      if (this.insuranceType === 'Otro' && !this.otherInsuranceType) {
        errors.push("Debes indicar el tipo de seguro o indicar que no aplica");
      }
      if (this.insuranceType === 'Otro') {
        this.insuranceType = this.otherInsuranceType;
      }
      if (!this.insuranceCompany) {
        errors.push("La compañía de seguros es obligatoria, puedes mencionar que no tienes si no aplica.");
      }
      if (this.insuranceCompany === 'Otra' && !this.otherInsuranceCompany) {
        errors.push("Debes indicar la compañía de seguros.");
      }
      if (this.insuranceCompany === 'Otra') {
        this.insuranceCompany = this.otherInsuranceCompany;
      }
      if (!this.centroTrabajo) {
        errors.push("El centro de trabajo es obligatorio, puedes mencionar que no tienes si no aplica.");
      }
      if (this.centroTrabajo === 'Otro' && !this.otherCentroTrabajo) {
        errors.push("Debes indicar el centro de trabajo.");
      }
      if (this.centroTrabajo === 'Otro') {
        this.centroTrabajo = this.otherCentroTrabajo;
      }
      if (!this.termsAccepted) {
        errors.push("Debes aceptar los términos y condiciones.");
      }
      if (this.folioCheckInicial !== Number(this.folioTarjeta)) {
        errors.push("El número de tarjeta no coincide, por favor, verifica que sea correcto y recarga la página.");
      }
      return errors;
    },
      triggerFileInput() {
        this.imageUploaded = false;
          const inputElement = this.$refs.fileInput as HTMLInputElement;
          inputElement.click();
      },
      preloadImage() {
      const image = new Image();
      image.onload = () => {
        this.imageLoaded = true; // Set to true once the image is loaded
      };
      image.src = this.checkIcon;
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
        centroTrabajo: this.centroTrabajo,
        bloodType: this.bloodType,
        birthDate: this.birthDate,
        email: this.email,
        phone: this.phone,
        address: this.address,
        insuranceType: this.insuranceType,
        insuranceCompany: this.insuranceCompany,
        image: this.uploadedImage,
        folioTarjeta: this.folioTarjeta,
        folioCheckInicial: this.folioCheckInicial,
      };
      console.log('Submitting form', formData);
      axios.post('api/form', formData)
          .then(response => {
            console.log('Form submitted successfully', response);
            this.$notify({ type: 'success', title: 'Éxito', text: 'Sus datos fueron registrados correctamente.' });
            this.dialogSuccess = true;
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
    this.imageUploaded = true;
      const file = (event.target as HTMLInputElement).files?.[0];
          if (file && file.type.startsWith('image/')) {
              const reader = new FileReader();
              reader.onload = e => {
                  this.uploadedImage = (e.target as FileReader).result as string;
              };
              reader.readAsDataURL(file);
          }
  },
  async getInfo() {
    try {
      const response = await axios.get('api/info', { params: { folioCheckInicial: this.folioCheckInicial } });
      console.log('Response from getInfo', response);
      this.insuranceTypes = response.data.unique_Tipo_Seguro.filter(Boolean);
      this.insuranceCompanies = response.data.unique_Nombre_Aseguradora.filter(Boolean);
      this.centrosTrabajo = response.data.unique_Centro_Trabajo.filter(Boolean);
      this.insuranceTypes.push('Otro');
      this.insuranceCompanies.push('Otra');
      this.centrosTrabajo.push('Otro');
    } catch (error) {
      console.error('Error in getInfo', error);
    } finally {
      this.checkUpdated();
    }
  },
  validateFolio() {
    if (this.folioCheckInicial?.toString() === '#andalucia') {
      this.dialogAdmin = true;
      this.dialog = false;
      return;
    }

    this.validationError = '';
    const isValid = this.folioRules.every(rule => rule(this.folioCheckInicial ?? 0) === true);

    if (isValid) {
      this.loading = true;
      this.folioCheckInicial = Number(this.folioCheckInicial);
      this.getInfo();
    } else {
      this.validationError = 'Este folio no funciona, contactános directamente';
    }
  },
    checkUpdated() {
      if (this.insuranceTypes.length > 1 && this.insuranceCompanies.length > 1) {
        console.log(this.insuranceTypes.length);
        this.loading = false;
        this.dialog = false;
      } else {
        this.loading = false;
        // Show error and reload
        this.$notify({ type: 'error', title: 'Error', text: 'Hubo un problema con el folio, porfavor recarga la página y vuelva a intentar' });
      }
    },
    async submitAdmin() {
  try {
    const response = await axios.get('api/pullmoll', {
      params: {
        email: this.emailAdmin, 
        password: this.passwordAdmin, 
        downloadUserData: this.downloadUserData, 
        downloadImages: this.downloadImages
      },
      responseType: 'blob' // This is important for handling binary data
    });
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', `Informacion-${Date.now()}.zip`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link); // Clean up
  } catch (error) {
    console.error('Error in getInfo', error);
  } finally {
    this.dialogAdmin = false;
  }
}

  },
 };
</script>

<style scoped>
:deep().font-small {
font-size: 1em !important;
}
.gold-bandx .white-input input {
background-color: white !important;
}
.gold-bandx {
  background-color:  #b68d2c5d;

  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;

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