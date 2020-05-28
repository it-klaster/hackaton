<template>
  <l-map
    ref="map"
    v-if="showMap"
    :zoom="zoom"
    :center="center"
    :options="mapOptions"
    
    @update:center="centerUpdate"
    @update:zoom="zoomUpdate"
  >
    <l-tile-layer
      :url="url"
      :attribution="attribution"
    />
  <l-marker :lat-lng="withTooltip">
      <l-tooltip :options="{ permanent: true, interactive: true }">
        <div @click="innerClick">
          I am clickable!!
          <p v-show="showParagraph">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque
            sed pretium nisl, ut sagittis sapien. Sed vel sollicitudin nisi.
            Donec finibus semper metus id malesuada.
          </p>
        </div>
      </l-tooltip>
    </l-marker>
  </l-map>
</template>

<script>
import { latLng } from "leaflet";
import { LMap, LTileLayer, LMarker, LPopup, LTooltip } from "vue2-leaflet";
import L from 'leaflet';

export default {
  name: "Example",
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LTooltip
  },
  data() {
    return {
      zoom: 13,
      center: latLng(56.106473, 94.582982),
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      withPopup: latLng(56.106473, 94.582982),
      withTooltip: latLng(56.106473, 94.582982),
      currentZoom: 11.5,
      currentCenter: latLng(56.106473, 94.582982),
      showParagraph: false,
      mapOptions: {
        zoomSnap: 0.5
      },
      showMap: true
    };
  },
  mounted() {
    const map = this.$refs.map.mapObject;
    map.addControl(L.Control.Fullscreen());
  },
  methods: {
    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
    },
    showLongText() {
      this.showParagraph = !this.showParagraph;
    },
    innerClick() {
      this.showLongText();
    }
  }
};
</script>