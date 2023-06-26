<template>
    <v-container fluid>
      <v-row>
        <v-col cols="6">
  <h2 class="pb-5">Comunicar vía Whatsapp</h2>
  <v-card flat v-for="item in messages" :key="item.text">
    <v-textarea readonly :value="item.text" outlined :rows="calculateRows(item.text)"></v-textarea>
    <v-row class="d-flex justify-center align-center pb-5">
        <v-col cols="6">
            <v-card-subtitle>Aprobación de META: {{ item.status }}</v-card-subtitle>
        </v-col>
        <v-col cols="6">
            <v-list-item-action>
                <v-btn v-if="item.status == 'pendiente'" color="primary" block>Editar</v-btn>
                <v-btn v-else-if="item.status == 'completado'" color="success" @click="dialog = true" block>Enviar</v-btn>
            </v-list-item-action>
        </v-col>
    </v-row>
  </v-card>
    </v-col>

        <v-col cols="6">
          <v-row class="fill-height">
            <v-col class="fill-height half">
              <h2 class="pb-5">Monitoreo en Tiempo Real</h2>
              <div>
                <v-btn v-if="!isClicked" color="primary" @click="startReceiving">Iniciar Monitoreo</v-btn>    <v-col class="fill-height half">
        <v-card
  v-for="(message, index) in messageswhatsapp"
  :key="index"
  class="mb-4"
  transition="fade-transition"
>
  <v-card-text v-if="message.isVisible">{{ message.text }}</v-card-text>
</v-card>


    </v-col>
  </div>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
      <v-dialog v-model="dialog" max-width="1500px">
      <v-card class="pa-5">
        <v-card-text>
          <ModalMessage/>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
  </template>
  
  <script>
  import ModalMessage from '@/components/whatsapp/modal.vue';
  export default {
    components: {
      ModalMessage
    },
    data() {
      return {
        messageswhatsapp: [
        { "text": "Felicitaciones por tu propuesta de educación inclusiva. ¡Eres un verdadero líder!", "isVisible": false },
  { "text": "Estoy orgulloso de apoyar tu campaña. Tus ideas son refrescantes y necesarias en estos tiempos difíciles.", "isVisible": false },
  { "text": "Hola, me preocupa tu postura sobre los impuestos. Creo que podrían afectar gravemente a la clase media", "isVisible": false },
  { "text": "No puedo creer que hayas mentido sobre tus antecedentes. No eres digno de confianza y no votaré por ti", "isVisible": false },
  { "text": "Tu compromiso con el medio ambiente es inspirador. Espero verte implementar políticas sostenibles en el gobierno", "isVisible": false },
  { "text": "No puedo apoyar a alguien que no muestra empatía hacia las minorías. Tu comportamiento es inaceptable", "isVisible": false }
],
        messages: [
          {
            text: '¡Un futuro brillante está a nuestro alcance! Juntos, podemos construir una comunidad más segura, equitativa y próspera. Vota por Ana López como tu alcaldesa y trabajemos juntos para lograrlo.',
            status: 'completado',
          },
          {
  text: '¡Es hora de cambiar el rumbo de nuestra ciudad! Con tu apoyo, podemos revitalizar la economía, mejorar los servicios públicos y garantizar una educación de calidad para nuestros hijos. Vota por Juan Torres como tu próximo alcalde.',
  status: 'completado'
},
{
  text: 'La honestidad y la transparencia son fundamentales en nuestra política. Como candidato, me comprometo a ser su voz en el Congreso y a luchar incansablemente por los derechos de todos los ciudadanos. Juntos, podemos marcar la diferencia. ¡Vota por Luisa Rodríguez!',
  status: 'completado'
},
{
  text: 'Queridos vecinos, nuestras voces importan y nuestras necesidades deben ser atendidas. Como concejal, me aseguraré de que cada una de sus preocupaciones sea escuchada y de que nuestras comunidades prosperen. ¡Vota por Miguel González!',
  status: 'pendiente'
},
{
  text: 'La juventud representa el futuro de nuestra sociedad y merece tener una voz fuerte en la toma de decisiones. Como representante estudiantil, trabajaré arduamente para garantizar una educación inclusiva y oportunidades equitativas para todos. ¡Vota por María Fernández!',
  status: 'pendiente'
},
{
  text: 'La protección de nuestro medio ambiente es una responsabilidad compartida. Como senador, promoveré políticas sostenibles y lucharé contra el cambio climático. Juntos, podemos preservar nuestro planeta para las futuras generaciones. Vota por Carlos Ramírez.',
  status: 'pendiente'
},
{
  text: 'La igualdad de género no es solo una aspiración, sino un derecho fundamental. Como diputada, defenderé los derechos de las mujeres y trabajaré por una sociedad más justa y equitativa para todos. ¡Vota por Laura Gómez!',
  status: 'pendiente'
},
{
  text: 'Nuestra comunidad necesita un líder que escuche y actúe. Como gobernador, me comprometo a trabajar incansablemente para impulsar el desarrollo económico, mejorar la educación y fortalecer nuestra seguridad. ¡Vota por Roberto Silva!',
  status: 'pendiente'
},
{
  text: 'La diversidad nos enriquece como sociedad. Como representante, trabajaré para promover la inclusión, el respeto y la igualdad de oportunidades para todos. Unidos, podemos construir un futuro más tolerante y acogedor. ¡Vota por Ana Cruz!',
  status: 'pendiente'
},
{
  text: 'La honestidad y la integridad son los pilares de mi campaña. Como candidato, me comprometo a servir con transparencia y a ser un defensor comprometido de los intereses de nuestra comunidad. ¡Vota por Pedro Pérez!',
  status: 'pendiente'
}
        ],
        timer: null,
      messageIndex: 0,
      isClicked: false,
      dialog: false,
      item: {
        status: 'completado'
        },
      };
    },
    methods: {
        calculateRows(text) {
      const charsPerLine = 50;
      return Math.ceil(text.length / charsPerLine);
    },
    startReceiving() {
        this.isClicked = true;
  console.log('startReceiving method called');
  this.timer = setInterval(() => {
    console.log('Inside interval, messageIndex is:', this.messageIndex);
    if (this.messageIndex < this.messageswhatsapp.length) {
      console.log('Setting isVisible for message at index:', this.messageIndex);
      this.messageswhatsapp[this.messageIndex].isVisible = true;
      this.messageIndex++;
    } else {
      console.log('All messages have been shown, clearing interval');
      clearInterval(this.timer);
    }
  }, 5000);
},

  beforeDestroy() {
    clearInterval(this.timer);
  },
    },
  };
  </script>
  
  <style scoped>
  .fade-transition {
    transition: opacity .3s ease;
  }
  
  .fade-enter, .fade-leave-to {
    opacity: 0;
  }
  .half {
    height: 50%;
  }
  </style>
  