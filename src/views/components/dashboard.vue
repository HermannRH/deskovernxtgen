<template>
    <v-container class="pt-0">
    <!-- Header and instructions -->
    <v-row>
        <v-col cols="12">
            <h1>Registro de Pacientes</h1>
            <p>Por favor, llena el siguiente formulario para registrarte y acceder a los beneficios que tenemos para ti.</p>
        </v-col>
    </v-row>
      <!-- Patient Registration Form -->
      <v-form ref="form" @submit.prevent="onSubmit">
  <v-container class="pa-0">
    <!-- Row 1: Name, Age, Blood Type -->
    <v-row >
      <v-col cols="8" class="pt-5  pb-0">
        <v-text-field v-model="patient.name" label="Nombre"></v-text-field>
      </v-col>
      <v-col cols="4" class="pt-5  pb-0">
        <v-text-field v-model="patient.age" label="Edad" type="number"></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      
       
        <v-col cols="6" class="py-0">
        <v-select v-model="patient.insurance_type" :items="insuranceTypes" class="truncate-select-option" label="Tipo de seguro"></v-select>
      </v-col>
       <v-col cols="6" class="py-0">
            <v-select  v-model="patient.insurer" :items="insurers" label="Aseguradora"  class="truncate-select-option"></v-select>
        </v-col>
        <v-col cols="6" class="py-0">
        <v-select v-model="patient.blood_type" :items="bloodTypes" label="Tipo de sangre"></v-select>
      </v-col>
        <v-col cols="6" class="py-0">
        <v-text-field v-model="patient.phone" label="Teléfono"></v-text-field>
        </v-col>
        <v-col>
            <v-text-field v-model="patient.address" label="Dirección"></v-text-field>
        </v-col>

    </v-row>++
    <v-row>
      <v-col cols="12" md="6">
        <v-file-input class="pb-10" v-model="patient.photo" label="Sube aquí tu fotografía" accept="image/jpeg, image/png"></v-file-input>
      </v-col>
      <v-col cols="12" md="6">
        <!-- Date Picker Component Here -->
      </v-col>
    </v-row>    
    <!-- Row 2: Address, Phone, Email -->
    <v-row class="pa-0">
      <v-col cols="12" md="4">
        
      </v-col>
      <v-col cols="12" md="4">
        
      </v-col>
      <v-col cols="12" md="4">
        <v-text-field v-model="patient.email" label="Correo electrónico"></v-text-field>
      </v-col>
    </v-row>


    <!-- Row 5: Submit Button -->
    <v-row justify="end">
      <v-col cols="12" md="3">
        <v-btn type="submit" color="primary">Registrar</v-btn>
      </v-col>
    </v-row>
  </v-container>
</v-form>

  
      <!-- Display Patient Information -->
      <v-row v-if="submitted">
        <v-col cols="12" md="6">
          <!-- Display image here -->
          <v-img :src="patient.photo" height="200"></v-img>
          <div>Nombre: {{ patient.name }}</div>
          <div>Edad: {{ patient.age }}</div>
          <div>Tipo de sangre: {{ patient.blood_type }}</div>
        </v-col>
        <v-col cols="12" md="6">
          <div>Dirección: {{ patient.address }}</div>
          <div>Teléfono: {{ patient.phone }}</div>
          <div>Correo electrónico: {{ patient.email }}</div>
          <div>Fecha de nacimiento: {{ patient.birth_date }}</div>
          <div>Aseguradora: {{ patient.insurer }}</div>
          <div>Tipo de seguro: {{ patient.insurance_type }}</div>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        patient: {
          photo: '',
          name: '',
          age: null,
          blood_type: '',
          address: '',
          phone: '',
          email: '',
          birth_date: '',
          insurer: '',
          insurance_type: ''
        },
        newInsurer: '',
        newInsuranceType: '',
        insurers: ['Aseguradora A', 'Aseguradora B'],
        insuranceTypes: ['Tipo de Seguro A', 'Tipo de Seguro B'],
        bloodTypes: ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'],
        menu: false,
        submitted: false
      };
    },
    methods: {
      onSubmit() {
        if (this.newInsurer && !this.insurers.includes(this.newInsurer)) {
          this.insurers.push(this.newInsurer);
        }
        if (this.newInsuranceType && !this.insuranceTypes.includes(this.newInsuranceType)) {
          this.insuranceTypes.push(this.newInsuranceType);
        }
        console.log(this.patient);
        this.submitted = true;
      }
    }
  };
  </script>
  
  <style>
  .truncate-select-option .v-select__selection {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
.button-text {
    display: inline-block; 
    max-width: 100%; 
    white-space: normal; 
    line-height: 1;
}

</style>
  

