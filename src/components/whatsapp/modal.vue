<template>
    <v-app>
      <v-container>
        <h1 class="pb-2">Enviar mensaje</h1>
  
        <span >
          Selecciona la(s) audiencia(s) a la(s) que deseas enviar el mensaje:
        </span>
        <v-row class="pt-4 pb-4">
          <v-col
            cols="4"
            v-for="(audience, index) in audiences"
            :key="index"
          >
            <v-checkbox
              :label="audience"
              v-model="selectedAudiences"
              :value="audience"
            ></v-checkbox>
          </v-col>
        </v-row>
  
        <v-text-field
          v-model.number="numberOfMessages"
          type="number"
          label="Número de Mensajes"
        ></v-text-field>
  
        <v-select
          :items="frequencies"
          label="Frecuencia del Mensaje"
          v-model="selectedFrequency"
        ></v-select>
        <span>Costo por mensaje: {{ costPerMessage }}</span>
        <v-container class="d-flex align-items-end justify-content-end">
          <v-card
            class="mx-auto"
            color="light-green lighten-4"
            dark
            max-width="400"
          >
            <v-card-title class="headline">
              Costo Total
            </v-card-title>
  
            <v-card-text class="display-1">
              ${{ totalCost.toFixed(2) }}
            </v-card-text>
          </v-card>
        </v-container>
  
        <v-btn
          color="primary"
          @click="sendMessage"
          :disabled="!isValid"
        >
          Send Message
        </v-btn>
      </v-container>
    </v-app>
  </template>
  
  <script>
  export default {
    data() {
      return {
        audiences: ["Empresarios y líderes de la industria", "Jóvenes votantes", "Comunidades minoritarias", "Trabajadores sindicalizados", "Madres y padres de familia", "Personas de la tercera edad", "Organizaciones benéficas y sin fines de lucro", "Estudiantes universitarios", "Agricultores y agricultoras"],
        selectedAudiences: [],
        numberOfMessages: 0,
        frequencies: ["Único", "Diario", "Semanal", "Mensual"],
        selectedFrequency: null,
        costPerMessage: 0.3,
      };
    },
    computed: {
      totalCost() {
        return this.numberOfMessages * this.costPerMessage;
      },
      isValid() {
        return (
          this.numberOfMessages > 0 &&
          this.selectedFrequency
        );
      },
    },
    methods: {
      sendMessage() {
        if (this.isValid) {
          alert(
            `Enviando la cantidad de ${this.numberOfMessages} mensajes a ${this.selectedAudiences.join(", ")} con una frecuencia ${this.selectedFrequency}. El costo total es: ${this.totalCost}.`
          );
        } else {
          alert("Porfavor complete todos los campos antes de enviar.");
        }
      },
    },
  };
  </script>
  