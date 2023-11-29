<template>
  <v-app>
    <v-main>
      <HelloWorld
        subtitle-source="/episode4.vtt"
        :video-source="url"
      />
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
import HelloWorld from "@/components/VideoPlayer.vue";
import { computed } from "vue";

const url = computed(()=> {
  // min and max included
  const min = 1, max = 8
  const eps = Math.floor(Math.random() * (max - min + 1) + min);
  return `https://dls5.top-film2serial.click/DonyayeSerial/series/Biohackers/Soft.Sub/S01/720p.Web-DL/Biohackers.S01E0${eps}.720p.WEB-DL.SoftSub.DonyayeSerial.mkv`
})
</script>
