<!--
<template>
  <div id="map" style="width: 100%; height: 700px;"></div>
</template>

<script>
export default {
  mounted() {
    const mapDiv = document.getElementById('map');
    const iframe = document.createElement('iframe');
    iframe.style.width = '100%';
    iframe.style.height = '700px';
    iframe.style.border = '0';
    iframe.style.allowfullscreen = 'true';
    mapDiv.appendChild(iframe);

    const mapUrl = 'https://saoic51v4pnhz4yc.maps.arcgis.com/apps/instant/countdown/index.html?appid=103b0253b3704a499f0bcc4846448d67';
    const accessToken = 'AAPKf3dad29f663741ee851ea7bce532a040hd1tYsyABrG1ErF_YCgk0ifEZiSkTsus7rjzLDdToyiNc8MEq7iNlBghOv_OMDBE';

    // Set up the message event listener to receive the access token from the iframe
    window.addEventListener('message', event => {
      if (event.origin === 'https://saoic51v4pnhz4yc.maps.arcgis.com') {
        accessToken = event.data;
        loadMap();
      }
    });

    // Load the iframe with the map URL
    iframe.src = mapUrl;

    function loadMap() {
      // Create the map using the ArcGIS JavaScript API
      const map = new window.esri.Map({
        basemap: 'topo-vector'
      });

      // Add any additional layers or configurations as needed

      // Set the access token for authentication
      map.portalItem.setAuthentication({
        token: accessToken
      });

      // Display the map in the iframe
      const mapView = new window.esri.views.MapView({
        container: mapDiv,
        map: map
      });
    }
  }
};
</script>
-->



<template>
  <div id="map" style="width: 100%; height: 700px;">
    <iframe src="https://saoic51v4pnhz4yc.maps.arcgis.com/apps/instant/countdown/index.html?appid=103b0253b3704a499f0bcc4846448d67" width="100%" height="700px" frameborder="0" style="border:0" allowfullscreen>iFrames are not supported on this page.</iframe>
  </div>

</template>



<!--

<script>
import { loadModules } from 'esri-loader';

export default {
  mounted() {
    loadModules(['esri/Map', 'esri/views/MapView'], { css: true }).then(
      ([Map, MapView]) => {
        const map = new Map({
          basemap: 'streets' // Cambia esto según el tipo de mapa que desees
        });

        const view = new MapView({
          container: 'map',
          map: map,
          center: [-77.04, 38.907],
          zoom: 13
        });
      }
    );
  }
};
</script>

-->