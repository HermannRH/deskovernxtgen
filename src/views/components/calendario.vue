<template>
  <v-app>

    <v-container>
            <!-- Sección de Bienvenida al Cliente -->
            <v-row>
        <v-col cols="12">
          <v-card color="light-blue" class="white--text">
            <v-card-title>Bienvenido/a, [Nombre del Cliente]</v-card-title>
            <v-card-text>Explora tus beneficios exclusivos y ofertas.</v-card-text>
          </v-card>
        </v-col>
      </v-row>

      <!-- Panel de Información de Lealtad -->
      <v-row no-gutters>
  <v-col cols="12" md="4" >
    <v-card class="px-3 py-2" >
      <v-card-title class="justify-center">Puntos Acumulados</v-card-title>
      <v-card-text class="text-center">1,250 puntos</v-card-text>
    </v-card>
  </v-col>
  <v-col cols="12" md="4">
    <v-card class="px-3 py-2" >
      <v-card-title class="justify-center">Nivel de Membresía</v-card-title>
      <v-card-text class="text-center">Oro</v-card-text>
    </v-card>
  </v-col>
  <v-col cols="12" md="4">
    <v-card class="px-3 py-2">
      <v-card-title class="justify-center">Beneficios Próximos</v-card-title>
      <v-card-text class="text-center">Descuento especial en tu próximo viaje</v-card-text>
    </v-card>
  </v-col>
</v-row>

           <!-- Sección Principal -->
           <v-row>
    <v-col cols="12">
      <v-carousel height="200px" continuous="true" hide-delimiter-background="true" show-arrows="false">
        <v-carousel-item
          v-for="(item, i) in carouselItems"
          :key="i"
        >
          <div class="d-flex justify-center" style="height: 100%;">
            <v-img 
              :src="item.src"
            ></v-img>
          </div>
        </v-carousel-item>
      </v-carousel>
    </v-col>
  </v-row>
      <!-- Sección de Beneficios -->
      <v-row>
        <v-col
          cols="12"
          
          v-for="beneficio in beneficios"
          :key="beneficio.id"
        >
          <v-card>
            <v-img :src="beneficio.imagen" height="200px"></v-img>
            <v-card-title>{{ beneficio.titulo }}</v-card-title>
            <v-card-text>{{ beneficio.descripcion }}</v-card-text>
          </v-card>
        </v-col>
      </v-row>

      <!-- Beneficio del Mes -->
      <v-row>
        <v-col cols="12">
          <v-card color="secondary" dark>
            <v-card-title>Beneficio del Mes</v-card-title>
            <v-card-text>Detalles del beneficio del mes aquí.</v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import logo from '@/assets/images/logocirculo.png';
export default {
  data: () => ({
    carouselItems: [
      { src: logo },
      { src: logo },
      { src: logo },
      { src: logo },
      { src: logo },
    ],
    beneficios: [
      {
        id: 1,
        titulo: 'Precio Preferencial en Hotel Andalucía',
        descripcion: 'A sólo $850 la noche',
        imagen: logo,
      },
      {
        id: 2,
        titulo: 'Pizza al 2x1 en Los Sabores Andalucía',
        descripcion: 'Valor de $520 al mes',
        imagen: logo,
      },
      {
        id: 3,
        titulo: 'Tour guiado por la ciudad de Andalucía',
        descripcion: 'Descubre los encantos de la ciudad por solo $300 por persona',
        imagen: logo,
      },
      {
        id: 4,
        titulo: 'Descuento del 20% en el Spa del Hotel Andalucía',
        descripcion: 'Relájate y rejuvenece con un 20% de descuento en nuestros tratamientos de spa',
        imagen: logo,
      },
      {
        id: 5,
        titulo: 'Menú especial de la casa en el Restaurante Andalucía',
        descripcion: 'Prueba nuestro menú exclusivo por solo $250 por persona',
        imagen: logo,
      },
    ],
  }),
};
</script>

<style>
.v-app-bar {
  z-index: 4;
}
.text-truncate {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

</style>
  
  