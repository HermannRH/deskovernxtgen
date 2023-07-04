<template>
    <v-container>
        <h2 class="pb-5">Geovisualizador v0.000001</h2>
    </v-container>
    <v-container fluid>
        <v-card ref="fullscreenCard" class="pa-3">
            <v-card elevation="2" class="pa-2">
                <v-row class="d-flex align-items-center justify-center">
                    <v-col cols="12" md="2">
                        <v-btn @click="goFullscreen">
                            <v-icon>mdi-map-marker</v-icon>
                            Activar Mapa
                        </v-btn>
                    </v-col>
                    <v-col cols="12" md="2">
                        <v-btn @click="addData">
                            <v-icon>mdi-plus</v-icon>
                            Agregar Datos
                        </v-btn>
                    </v-col>
                    <v-col cols="12" md="2">
                        <v-btn @click="changeTheme">
                            <v-icon>mdi-palette</v-icon>
                            Cambiar Tema
                        </v-btn>
                    </v-col>
                    <v-col cols="12" md="3">
                        <v-slider v-model="sliderValue"></v-slider>
                    </v-col>
                    <v-col cols="12" md="3">
                        <v-select v-model="selectValue" :items="['Mostrar Etiquetas', 'Ocultar Etiquetas']"
                            label="Etiquetas"></v-select>
                    </v-col>
                </v-row>
                <v-row class="d-flex align-items-center justify-center pb-5">
                    <h2> Esta es la Toolbar del Geovisualizador </h2>
                </v-row>

            </v-card>




            <div class="arcgis-map pt-3" id="mapViewNode"></div>
        </v-card>
    </v-container>
</template>

<script>
import '@arcgis/core/assets/esri/themes/light/main.css';
import esriConfig from '@arcgis/core/config';
import Map from '@arcgis/core/Map';
import MapView from '@arcgis/core/views/MapView';
import FeatureLayer from '@arcgis/core/layers/FeatureLayer';

export default {
    name: 'ArcGISMap',
    data() {
        return {
            sliderValue: 50,
            selectValue: 'Mostrar Etiquetas',
        };
    },
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
        esriConfig.apiKey = "AAPK0a2a3f748281424c883403984dc273d7qvCeFpcsqEx0CqRL6W-w0I_t_bzqyhCaduUN3kakuxkMp0QpiV4hSW2S_ljRhcKH";
        // const mapViewNode = this.$refs.mapViewNode;
        const map = new Map({
            // basemap: 'streets-night-vector'
            basemap: 'arcgis-topographic'
        });

        const view = new MapView({
            container: 'mapViewNode',
            map: map,
            // center: [-100.3161, 25.6866],
            center: [-99.2453, 19.463],
            // center: [-102.28259, 21.88234],
            zoom: 9,
            highlightOptions: {
                // color: 'green'
                color: 'yellow'
            }
        });

        const featLay = new FeatureLayer({
            // url: "https://services.arcgis.com/1Nu85FRaEkaZ6Fp7/arcgis/rest/services/01mun/FeatureServer/0",
            // url: "https://services.arcgis.com/1Nu85FRaEkaZ6Fp7/arcgis/rest/services/01man/FeatureServer/0",
            url: "https://services.arcgis.com/1Nu85FRaEkaZ6Fp7/arcgis/rest/services/edomexman/FeatureServer/0",
            credential: {
                username: 'soteliin',
                password: 'arcSOT0809'
            },
            renderer: {
                type: 'simple',
                symbol: {
                    type: 'simple-fill',
                    color: '#ff5432',
                    outline: {
                        color: '#aa0000',
                        width: 1
                    }
                }
            }
        });
        map.add(featLay);
        let highlight, highlightOld;
        view.when(async () => {
            let layerView = await view.whenLayerView(featLay);
            view.on('pointer-move', async (e) => {
                const { results } = await view.hitTest(e)
                const graphic = results[0].graphic;
                if (highlight) {
                    highlight?.remove();
                }
                highlight = layerView.highlight(graphic);
            })
        })
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