<template>
    <div class="arcgis-map">
        <div ref="mapViewNode" class="map-view"></div>
    </div>
</template>
  
<script>
import { ref, onMounted } from 'vue';
import Map from '@arcgis/core/Map'
import MapView from '@arcgis/core/views/MapView'
import FeatureLayer from '@arcgis/core/layers/FeatureLayer'

export default {
    name: 'ArcGISMap',
    setup() {
        const mapViewNode = ref(null);

        onMounted(() => {
            const map = new Map({
                basemap: 'arcgis-topographic'
            });


            const view = new MapView({
                container: mapViewNode.value,
                map: map,
                center: [-102.28259, 21.88234],
                zoom: 10,
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

        return { mapViewNode };
    }
}
</script>
  
<style>
@import url("https://js.arcgis.com/4.27/");

.arcgis-map {
    width: 100%;
    height: 100%;
}

.map-view {
    width: 100%;
    height: 100%;
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