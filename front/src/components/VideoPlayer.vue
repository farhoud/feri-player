<template>
  <v-container>
    <v-sheet>
      <div ref="videoContainer">
        <video ref="player" class="video-js">
          <source :src="videoSource" type="video/mp4" />
        </video>
        <subtitle :playing="playing" @clear="vjsRef.play()" @select="vjsRef.pause()" :text="text" class="overlay-text"></subtitle>
        <input
          ref="fileInput"
          type="file"
          id="fileInput"
          style="display: none"
          @change="loadSrt"
        />
      </div>
    </v-sheet>
  </v-container>
</template>

<script setup lang="ts">
import videojs from "video.js";
import "video.js/dist/video-js.css";
import { getCurrentInstance, onMounted } from "vue";
import { ref,watch } from "vue";
import toWebVTT from "srt-webvtt";
import Subtitle from "@/components/Subtitle.vue"

const props = defineProps({
  videoSource: {
    type: String,
    required: true,
  },
  subtitleSource: {
    type: String,
    default: "",
  },
});
const player = ref();
const playing = ref(false)
const isFullscreen = ref(false);
const videoContainer = ref();
const text = ref("");
const vjsRef = ref();
const fileInput = ref();
onMounted(() => {
  initVideoPlayer();
});
const initVideoPlayer = () => {
  const options = {
    controls: true,
    fill: false,
    controlBar: {
      fullscreenToggle: true,
      pictureInPictureToggle: false,
    },
    html5: {
      nativeTextTracks: false,
    },
  };

  const vjsplayer: videojs.Player = videojs(player.value, options);

  const fullscreenButton = vjsplayer
    .getChild("ControlBar")
    .getChild("FullscreenToggle")
    .el();

  // Add a click event listener to the fullscreen button
  var newf = fullscreenButton.cloneNode(true);
  fullscreenButton.parentNode.replaceChild(newf, fullscreenButton);
  newf.addEventListener("click", toggleFullscreen);

  // Add event listener for fullscreenchange event
  document.addEventListener("fullscreenchange", handleFullscreenChange);
  document.addEventListener("webkitfullscreenchange", handleFullscreenChange);
  document.addEventListener("mozfullscreenchange", handleFullscreenChange);
  document.addEventListener("MSFullscreenChange", handleFullscreenChange);

  const customButton = vjsplayer.controlBar.addChild("button", {
    text: "Custom Button",
    className: "vjs-icon-subtitles",
  });

  customButton.on("click", openSrt);
  //   customButton.setIcon('play')

  // Add Video.js event listener for fullscreenchange event
  vjsplayer.on("fullscreenchange", handleFullscreenChange);

  vjsplayer.on('play',()=>{
    playing.value = true
  })
  vjsplayer.on('pause',()=>{
    playing.value = false
  })
  vjsRef.value = vjsplayer;
};
const openSrt = () => {
  fileInput.value.click();
};
const loadSrt = async () => {
  const textTrackUrl = await toWebVTT(fileInput.value.files[0]);
  const trackEl = vjsRef.value.addRemoteTextTrack({ src: textTrackUrl, kind: "metadata", default: true, label: "English", language: "fa", mode:"hidden" }, false);
  trackEl.addEventListener("load", function () {
    const track = vjsRef.value.remoteTextTracks()[0];
    console.log(track)
    console.log(trackEl.track)
    trackEl.track.addEventListener("cuechange", () => {
      const activeCue = track.activeCues[0] || "";
      text.value = activeCue.text;
    });
  });
};
const toggleFullscreen = () => {
  if (!isFullscreen.value) {
    // Enter fullscreen
    if (videoContainer.value.requestFullscreen) {
      videoContainer.value.requestFullscreen();
    } else if (videoContainer.value.mozRequestFullScreen) {
      videoContainer.value.mozRequestFullScreen();
    } else if (videoContainer.value.webkitRequestFullscreen) {
      videoContainer.value.webkitRequestFullscreen();
    } else if (videoContainer.value.msRequestFullscreen) {
      videoContainer.value.msRequestFullscreen();
    }
  } else {
    // Exit fullscreen
    if (document.exitFullscreen) {
      document.exitFullscreen();
    } else if (document.mozCancelFullScreen) {
      document.mozCancelFullScreen();
    } else if (document.webkitExitFullscreen) {
      document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) {
      document.msExitFullscreen();
    }
  }
};
const handleFullscreenChange = () => {
  // Update the fullscreen state
  const _isFullscreen = !!(
    document.fullscreenElement ||
    document.webkitFullscreenElement ||
    document.mozFullScreenElement ||
    document.msFullscreenElement
  );
  isFullscreen.value = _isFullscreen;
  vjsRef.value.fill(_isFullscreen);
};

watch(()=>props.videoSource,(src)=>{vjsRef.value.src({ type: 'video/mp4', src })})
</script>
<style scoped>
.video-container {
  position: relative;
  height: 100%;
  width: 100%;
}

.overlay-text {
  position: absolute;
  top: 80%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 2147483647;
}
</style>
