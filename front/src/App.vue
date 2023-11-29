<template>
  <v-app>
    <v-main>
      <video-source @open="(link)=>{url=link}">

      </video-source>
      <HelloWorld
        v-if="url"
        subtitle-source="/episode4.vtt"
        :video-source="url"
      />
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
import HelloWorld from "@/components/VideoPlayer.vue";
import videoSource from "@/components/VideoSource.vue"
import { ref } from "vue";

const url = ref()
</script>
