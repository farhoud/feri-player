<template>
  <v-app>
    <v-main>
      <video-source @open="openHandler"/>
      <video-player
        v-if="url"
        :video-source="url"
        :ref="player"
      />
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
import VideoPlayer from "@/components/VideoPlayer.vue";
import videoSource from "@/components/VideoSource.vue"
import { ref } from "vue";

const url = ref()
const player = ref()
const openHandler = (link:string)=>{
  url.value=link
}
</script>
