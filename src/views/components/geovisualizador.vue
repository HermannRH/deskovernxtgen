<template>
    <v-container>
        <h2 class="pb-5">Geovisualizador v0.000001</h2>
    </v-container>
    <v-container fluid>
        <v-card ref="fullscreenCard" class="pa-3">
            <v-btn @click="goFullscreen">Activar Mapa</v-btn>
            <div class="arcgis-map" ref="mapViewNode"></div>
        </v-card>
    </v-container>
</template>

<script>
import '@arcgis/core/assets/esri/themes/light/main.css';
import Map from '@arcgis/core/Map';
import MapView from '@arcgis/core/views/MapView';

export default {
    name: 'ArcGISMap',
    methods: {
        goFullscreen() {
            const card = this.$refs.fullscreenCard.$el;
            if (card.requestFullscreen) {
                card.requestFullscreen();
            } else if (card.msRequestFullscreen) {
                card.msRequestFullscreen();
            } else if (card.mozRequestFullScreen) { 
                card.mozRequestFullScreen();
            } else if (card.webkitRequestFullscreen) { 
                card.webkitRequestFullscreen();
            }
        },
        adjustHeight() {
            const card = this.$refs.fullscreenCard.$el;
            if (document.fullscreenElement) {
                card.querySelector('.arcgis-map').style.height = `${window.innerHeight * 0.9}px`;
            } else {
                card.querySelector('.arcgis-map').style.height = '100vh';
            }
        },
    },
    mounted() {
        const mapViewNode = this.$refs.mapViewNode;
        const map = new Map({
            basemap: 'streets-night-vector'
        });

        new MapView({
            container: mapViewNode,
            map: map,
            center: [-100.3161, 25.6866],
            zoom: 10,
        });

        document.addEventListener('fullscreenchange', this.adjustHeight);
    },
    beforeUnmount() {
        document.removeEventListener('fullscreenchange', this.adjustHeight);
    }
}
</script>

<style scoped>
.arcgis-map {
    width: 100%;
    overflow: hidden;
}
</style>



  

































<!-- 
<template>
    <div id="viewDiv"></div>
</template>
<script src="https://js.arcgis.com/4.27/"></script>
<style>
@import "https://js.arcgis.com/4.27/esri/themes/light/main.css";

html,
body,
#viewDiv {
    padding: 0;
    margin: 0;
    height: 100%;
    width: 100%;
}
</style>
<script>
    import ExternalScript from "https://js.arcgis.com/4.27/";
    require(["esri/config", "esri/Map", "esri/views/MapView", "esri/layers/FeatureLayer"], function (esriConfig, Map, MapView, FeatureLayer) {
        esriConfig.apiKey = "AAPK0a2a3f748281424c883403984dc273d7qvCeFpcsqEx0CqRL6W-w0I_t_bzqyhCaduUN3kakuxkMp0QpiV4hSW2S_ljRhcKH";

        const map = new Map({
            basemap: "arcgis-topographic"
        });
        const view = new MapView({
            map: map,
            center: [-102.28259, 21.88234],
            zoom: 10,
            container: "viewDiv"
        });
        const agsMun = new FeatureLayer({
            url: "https://services.arcgis.com/1Nu85FRaEkaZ6Fp7/arcgis/rest/services/01mun/FeatureServer/0",
            credential: { 
                username: 'soteliin',
                password: 'arcSOT0809'
            }
        });
        map.add(agsMun);
    });
</script> -->